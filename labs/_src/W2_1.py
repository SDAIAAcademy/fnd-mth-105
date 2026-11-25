# /// script
# requires-python = ">=3.11"
# dependencies = ["python-sat>=1.8.dev0"]
# ///
# %% [markdown]
# # Lab 2.1 · Truth tables in code, and a scheduling puzzle solved with a SAT solver
#
# Week 2 · Session 1 (Propositional logic, normal forms and SAT) · 105 min.
#
# The volunteer centre writes its rules in words. You turn them into formulas, check laws and
# arguments by truth table, find the one situation where two phrasings of an access rule disagree,
# and then let a SAT solver place ten volunteers on five shifts, check its answer against every
# rule, and explain why the coordinator's late change has no solution.
#
# **AI policy.** AI-tutor: it may point at a gap, never write the answer (`labs/tutor/TUTOR.md`).
#
# **Tasks**
# - [ ] 1 · Set up; a truth table by hand and in code (15 min)
# - [ ] 2 · Equivalent or not: laws by truth table (15 min)
# - [ ] 3 · Valid and invalid arguments (15 min)
# - [ ] 4 · Two phrasings of an access rule (15 min)
# - [ ] 5 · Encode the shift puzzle in CNF (20 min)
# - [ ] 6 · Solve, then check against every rule (10 min)
# - [ ] 7 · The late change: unsatisfiable, and why (10 min)
# - [ ] 8 · Small variant: brute force against solver (5 min)
# - [ ] ✱ Stretch · Count every schedule of the full puzzle by blocking each one found

# %%
import os, sys, subprocess
from pathlib import Path

IN_COLAB = "google.colab" in sys.modules
if IN_COLAB:
    REPO_URL = "https://github.com/SDAIAAcademy/fnd-mth-105.git"
    if not Path("/content/fnd-mth-105").exists():
        subprocess.run(["git", "clone", "-q", REPO_URL, "/content/fnd-mth-105"], check=True)
    os.chdir("/content/fnd-mth-105/labs")
    subprocess.run([sys.executable, "-m", "pip", "install", "-q", "-r", "requirements-colab.txt"], check=True)
else:
    while not Path("_tools").exists() and Path.cwd() != Path.cwd().parent:
        os.chdir("..")  # solutions/ notebooks run from labs/
sys.path.insert(0, os.getcwd())

import itertools
from pysat.solvers import Solver
import dm as U

def implies(a, b):
    return (not a) or b

# %% [markdown]
# ## 1 · A truth table
#
# **By hand first.** Fill in the column of `p → q` (if p then q) for the four rows
# (p, q) = (F, F), (F, T), (T, F), (T, T), as a list of four booleans in `hand_implies`.
#
# Then write `truth_table(f, n)`: every row of n truth values, in the order of
# `itertools.product([False, True], repeat=n)`, with the value of `f` on it.

# %%
hand_implies = None   # ✏️ four booleans

def truth_table(f, n):
    """A list of (row, value) pairs; row is a tuple of n booleans."""
    # BEGIN SOLUTION
    return [(row, bool(f(*row))) for row in itertools.product([False, True], repeat=n)]
    # END SOLUTION

def show(f, n, names):
    try:
        rows = truth_table(f, n)
    except NotImplementedError:
        rows = [(r, bool(f(*r))) for r in itertools.product([False, True], repeat=n)]
    U.table([["T" if x else "F" for x in r] + ["T" if v else "F"] for r, v in rows], names + ["value"])
    return rows

# %%
rows = show(implies, 2, ["p", "q"])
U.check([v for _, v in rows] == [True, True, False, True], "p → q is false only when p is true and q false")
if hand_implies is not None:
    U.check(list(hand_implies) == [v for _, v in rows], "hand and code agree")

# %% [markdown]
# ## 2 · Equivalent or not
#
# Two formulas are **equivalent** when they agree on every row. Write `equivalent(f, g, n)` and
# use it on four claims. Predict each answer before you run the cell.

# %%
def equivalent(f, g, n):
    # BEGIN SOLUTION
    return all(bool(f(*r)) == bool(g(*r)) for r in itertools.product([False, True], repeat=n))
    # END SOLUTION

# %%
claims = {
    "not (p and q)  ==  (not p) or (not q)": (lambda p, q: not (p and q), lambda p, q: (not p) or (not q), 2),
    "p → q  ==  not q → not p (contrapositive)": (lambda p, q: implies(p, q), lambda p, q: implies(not q, not p), 2),
    "p → q  ==  q → p (converse)": (lambda p, q: implies(p, q), lambda p, q: implies(q, p), 2),
    "p and (q or r)  ==  (p and q) or (p and r)": (lambda p, q, r: p and (q or r), lambda p, q, r: (p and q) or (p and r), 3),
}
try:
    verdicts = {k: equivalent(f, g, n) for k, (f, g, n) in claims.items()}
except NotImplementedError:
    verdicts = dict(zip(claims, [True, True, False, True]))
for k, v in verdicts.items():
    print(("equivalent    " if v else "NOT equivalent"), k)
U.check(list(verdicts.values()) == [True, True, False, True], "three laws hold; the converse is not the rule")

# %% [markdown]
# ## 3 · Valid and invalid arguments
#
# An argument is **valid** when no row makes every premise true and the conclusion false. Write
# `counterexamples(premises, conclusion, n)` returning those rows (an empty list means valid).
# The variables: m = "the volunteer is a minor", g = "guardian consent is on file".

# %%
def counterexamples(premises, conclusion, n):
    # BEGIN SOLUTION
    return [r for r in itertools.product([False, True], repeat=n)
            if all(P(*r) for P in premises) and not conclusion(*r)]
    # END SOLUTION

# %%
rule = lambda m, g: implies(m, g)            # the centre's rule: a minor has guardian consent on file
arguments = {
    "m → g; m; so g (modus ponens)": ([rule, lambda m, g: m], lambda m, g: g),
    "m → g; g; so m (affirming the consequent)": ([rule, lambda m, g: g], lambda m, g: m),
    "m → g; not g; so not m (modus tollens)": ([rule, lambda m, g: not g], lambda m, g: not m),
    "m → g; not m; so not g (denying the antecedent)": ([rule, lambda m, g: not m], lambda m, g: not g),
}
try:
    found = {k: counterexamples(P, c, 2) for k, (P, c) in arguments.items()}
except NotImplementedError:
    found = {k: [r for r in itertools.product([False, True], repeat=2) if all(p(*r) for p in P) and not c(*r)]
             for k, (P, c) in arguments.items()}
for k, rows_ in found.items():
    print("valid  " if not rows_ else f"INVALID, counterexample (m, g) = {rows_}", "|", k)
U.check([len(v) == 0 for v in found.values()] == [True, False, True, False], "two valid forms, two fallacies")

# %% [markdown]
# **Look at** the counterexample of the second argument: an adult whose guardian consent is on
# file anyway. Nothing in the rule forbids it, so consent on file does not tell you the volunteer
# is a minor.

# %% [markdown]
# ## 4 · Two phrasings of one access rule
#
# Who may see a volunteer's contact details? Variables: o = the requester is the data protection
# officer, c = the requester is a coordinator, d = the volunteer is in the requester's district,
# s = the volunteer consented to share.
#
# - The data protection officer's rule: "The data protection officer may see all contact details.
#   A coordinator may see those of volunteers in their district, and of volunteers who consented."
# - The handbook's sentence: "Contact details are visible to the data protection officer, to
#   coordinators for their own district, and for volunteers who consented to share."
#
# Write both as Python functions of (o, c, d, s), then list the rows where they differ.

# %%
def officer_rule(o, c, d, s):
    # BEGIN SOLUTION
    return o or (c and (d or s))
    # END SOLUTION

def handbook_rule(o, c, d, s):
    # BEGIN SOLUTION
    return o or (c and d) or s
    # END SOLUTION

# %%
try:
    diff = [r for r in itertools.product([False, True], repeat=4) if officer_rule(*r) != handbook_rule(*r)]
except NotImplementedError:
    diff = [tuple(r) for r in U.reference("w2_rule_diff")]
diff = U.keep("w2_rule_diff", diff)
U.table([["T" if x else "F" for x in r] for r in diff], ["o", "c", "d", "s"])
U.check(len(diff) == 2 and all(r[0] is False and r[1] is False and r[3] is True for r in diff),
        "they differ only when a requester who is neither officer nor coordinator asks about a consenting volunteer")

# %% [markdown]
# **Look at** who the handbook lets in: anyone at all, for a volunteer who consented. "Consented
# to share" was meant as consent to share with coordinators. The sentence needs brackets.

# %% [markdown]
# ## 5 · The shift puzzle in conjunctive normal form
#
# `data/schedule_puzzle.json` holds ten volunteers, five shifts, who is available when, who has
# first aid, and two pairs who must not share a shift. One boolean variable per (volunteer, shift)
# pair: true means "works that shift". A SAT solver wants **clauses**: lists of literals, at least
# one of which must be true; literal `k` is variable k, `-k` its negation.
#
# Write `encode(puzzle)` returning the list of clauses for the six rules printed below. Hints:
# "exactly one shift" is "at least one" (one clause) plus "not two" (a clause for each pair); "at
# most two on a shift" is "not three" (a clause for each triple); "at least two on a shift" is "for
# each volunteer v, someone other than v is on it".

# %%
puzzle = U.load_json("schedule_puzzle.json")
VOLS, SHIFTS = puzzle["volunteers"], puzzle["shifts"]
var = {(v, s): 1 + i * len(SHIFTS) + j for i, v in enumerate(VOLS) for j, s in enumerate(SHIFTS)}
name = {k: vs for vs, k in var.items()}
for r in puzzle["rules"]:
    print("-", r)

def encode(pz, available=None):
    available = available or pz["available"]
    cl = []
    # BEGIN SOLUTION
    V, S = pz["volunteers"], pz["shifts"]
    for v in V:
        cl.append([var[v, s] for s in S])                                   # at least one shift
        cl += [[-var[v, a], -var[v, b]] for a, b in itertools.combinations(S, 2)]   # not two
        cl += [[-var[v, s]] for s in S if s not in available[v]]            # availability
    for s in S:
        cl += [[-var[a, s], -var[b, s], -var[c, s]] for a, b, c in itertools.combinations(V, 3)]  # not three
        cl += [[var[u, s] for u in V if u != v] for v in V]                 # at least two
        cl.append([var[v, s] for v in pz["first_aid"]])                     # first aid on every shift
        cl += [[-var[a, s], -var[b, s]] for a, b in pz["conflicts"]]        # conflicts
    # END SOLUTION
    return cl

# %%
try:
    clauses = encode(puzzle)
except NotImplementedError:
    clauses = [list(c) for c in U.reference("w2_clauses")]
clauses = U.keep("w2_clauses", clauses)
print(len(var), "variables,", len(clauses), "clauses")

# %% [markdown]
# ## 6 · Solve, then check
#
# The solver returns a model: a sign for every variable. Turn it into a schedule, then check the
# schedule against every rule **in plain Python**, without the clauses: a check that reuses your
# encoding would repeat any mistake in it.

# %%
def solve(cl):
    with Solver(name="g4", bootstrap_with=cl) as sat:
        return sat.get_model() if sat.solve() else None

def schedule_from(model):
    return {name[k][0]: name[k][1] for k in model if k > 0}

def check_schedule(sched, pz, available=None):
    available = available or pz["available"]
    # BEGIN SOLUTION
    S = pz["shifts"]
    on = {s: [v for v in sched if sched[v] == s] for s in S}
    return {
        "every volunteer works exactly one shift": set(sched) == set(pz["volunteers"]),
        "every shift has exactly two volunteers": all(len(on[s]) == pz["per_shift"] for s in S),
        "available for the shift worked": all(sched[v] in available[v] for v in sched),
        "first aid on every shift": all(any(v in pz["first_aid"] for v in on[s]) for s in S),
        "no conflicting pair on one shift": all(sched[a] != sched[b] for a, b in pz["conflicts"]),
    }
    # END SOLUTION

# %%
model = solve(clauses)
U.check(model is not None, "the puzzle has a schedule")
sched = schedule_from(model)
for s in SHIFTS:
    print(s, sorted(v for v in sched if sched[v] == s))
try:
    report = check_schedule(sched, puzzle)
except NotImplementedError:
    report = {"(check_schedule not written yet)": True}
for k, ok in report.items():
    print("[ok]" if ok else "[FAIL]", k)
U.check(all(report.values()), "the solver's schedule meets every rule")

# %% [markdown]
# ## 7 · The late change
#
# The coordinator writes: V-00090 and V-00099 can now only work SH-E. Encode again with the new
# availability and solve. Then find **why** there is no schedule: give each rule group a switch
# (an extra variable that turns the group on) and ask the solver for a small set of switches that
# already conflict (its "core").

# %%
late = dict(puzzle["available"]) | puzzle["late_change"]
try:
    model2 = solve(encode(puzzle, late))
except NotImplementedError:
    model2 = None
print("schedule after the late change:", "none" if model2 is None else "found")
U.check(model2 is None, "the late change makes the puzzle unsatisfiable")

def grouped_clauses(pz, available):
    """The same rules, as named groups of clauses (written for you)."""
    V, S, g = pz["volunteers"], pz["shifts"], {}
    g["one shift each"] = [[var[v, s] for s in S] for v in V] + [[-var[v, a], -var[v, b]] for v in V for a, b in itertools.combinations(S, 2)]
    g["two per shift"] = [[-var[a, s], -var[b, s], -var[c, s]] for s in S for a, b, c in itertools.combinations(V, 3)] + [[var[u, s] for u in V if u != v] for s in S for v in V]
    g["availability"] = [[-var[v, s]] for v in V for s in S if s not in available[v]]
    for s in S:
        g[f"first aid on {s}"] = [[var[v, s] for v in pz["first_aid"]]]
    g["conflicts"] = [[-var[a, s], -var[b, s]] for s in S for a, b in pz["conflicts"]]
    return g

groups = grouped_clauses(puzzle, late)
switch = {gname: 1000 + i for i, gname in enumerate(groups)}
with Solver(name="g4") as sat:
    for gname, cls in groups.items():
        for c in cls:
            sat.add_clause(c + [-switch[gname]])     # the group holds when its switch is on
    sat.solve(assumptions=list(switch.values()))
    core = sorted(gname for gname, k in switch.items() if k in (sat.get_core() or []))
print("rule groups in the conflict:", core)
fa = puzzle["first_aid"]
print("first-aiders available for SH-C or SH-D after the change:", sorted(v for v in fa if set(late[v]) & {"SH-C", "SH-D"}))

# %% [markdown]
# **Look at** the core and the last line: after the change, one first-aider is left who can work
# SH-C or SH-D, and both shifts need one. Two shifts, one person, one shift each: the pigeonhole
# principle of week 5, found by the solver without being told. Relaxing first aid on one of the
# two shifts, or keeping V-00090 available for SH-D, restores a schedule. Which relaxation to take
# is for someone other than the person who entered the change: dropping a first-aid rule needs a
# second sign-off.

# %% [markdown]
# ## 8 · Brute force against the solver, on a small variant
#
# A small variant: 6 volunteers, 3 shifts, everyone available, three of them first-aiders. There
# are 3⁶ = 729 ways to give each volunteer one shift: few enough to try them all. Count the
# schedules that meet the rules by brute force, then count them with the solver by adding, after
# each solution, a clause that forbids exactly that solution. **Before you run it**, count them by
# hand with the product rule: one first-aider per shift, then the other three, one per shift.

# %%
small = {"volunteers": VOLS[:6], "shifts": SHIFTS[:3], "first_aid": ["V-00012", "V-00031", "V-00048"],
         "available": {v: SHIFTS[:3] for v in VOLS[:6]}, "per_shift": 2, "conflicts": [["V-00027", "V-00063"]]}
print("small variant: 6 volunteers, 3 shifts, everyone available, first-aiders", small["first_aid"])

def brute_count(pz):
    n = 0
    for choice in itertools.product(pz["shifts"], repeat=len(pz["volunteers"])):
        sched_ = dict(zip(pz["volunteers"], choice))
        if all(check_schedule(sched_, pz).values()):
            n += 1
    return n

def solver_count(pz, limit=10000):
    n = 0
    with Solver(name="g4", bootstrap_with=encode(pz)) as sat:
        while n < limit and sat.solve():
            m = sat.get_model()
            sat.add_clause([-k for k in m if k > 0 and name[k][0] in pz["volunteers"] and name[k][1] in pz["shifts"]])
            n += 1
    return n

# %%
try:
    counts = (brute_count(small), solver_count(small))
except NotImplementedError:
    counts = tuple(U.reference("w2_small_counts"))
counts = U.keep("w2_small_counts", counts)
print("schedules of the small variant: brute force", counts[0], "| solver", counts[1])
U.check(counts[0] == counts[1] == 36, "brute force, the solver and the product rule (3! · 3! = 36) agree")

# %% [markdown]
# ## ✱ Stretch
#
# Use `solver_count(puzzle)` on the full puzzle. Why can brute force not check that number
# here? (Count the assignments it would have to try.)

# %% [markdown]
# ## Check yourself
#
# <details><summary>1. A rule is written "if the volunteer is a minor, consent is on file". A colleague concludes from "consent is on file" that the volunteer is a minor. What is wrong?</summary>
# Affirming the consequent: the row (minor false, consent true) makes the premises true and the
# conclusion false, so the argument is invalid.</details>
#
# <details><summary>2. Why check the solver's schedule with separate code?</summary>
# The solver only satisfies the clauses you gave it. If a clause is wrong, the schedule is wrong in
# the same way; a check written from the rules in words catches that.</details>
#
# <details><summary>3. The solver says "unsatisfiable". What does that prove, and what does it not?</summary>
# That no assignment meets the clauses: a proof by exhausting every case, done cleverly. It says
# nothing about whether the clauses say what the coordinator meant.</details>
#
# ## Carry forward
#
# Nothing to save. Week 3 adds quantifiers ("for every volunteer", "some shift") to these formulas.
