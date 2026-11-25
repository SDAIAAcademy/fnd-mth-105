# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
# %% [markdown]
# # Lab 3.1 · Relation properties checked in code
#
# Week 3 · Session 1 (Quantifiers, relation properties and first proofs) · 105 min.
#
# Each property of a relation is a quantified statement: "for every x, x R x" is reflexivity. On a
# finite set your code can check every case, which for that set is a proof. You write the four
# checkers, classify nine relations from the volunteer centre's data and its scheduling software,
# find the two planted faults, build a partition and a closure, and then meet a claim over all the
# integers, where checking cases is no longer enough.
#
# **AI policy.** AI-tutor: it may point at a gap, never write the answer (`labs/tutor/TUTOR.md`).
#
# **Tasks**
# - [ ] 1 · Set up; properties as quantified statements (10 min)
# - [ ] 2 · Write the property checkers (20 min)
# - [ ] 3 · Classify nine relations (20 min)
# - [ ] 4 · Counterexamples: the planted faults (15 min)
# - [ ] 5 · Equivalence classes and the partition (10 min)
# - [ ] 6 · Transitive closure of the training prerequisites (15 min)
# - [ ] 7 · A claim over all integers: test, then prove (10 min)
# - [ ] 8 · Record what the checks prove and what they only test (5 min)
# - [ ] ✱ Stretch · Count, among the 512 relations on a three-element set, how many are equivalence relations

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

import datetime as dt
import itertools
import random
import dm as U

# %% [markdown]
# ## 1 · Properties as quantified statements
#
# For a relation R on a set X (a set of pairs of elements of X):
#
# | Property | Statement |
# |---|---|
# | reflexive | for every x in X: (x, x) in R |
# | symmetric | for every x, y: if (x, y) in R then (y, x) in R |
# | antisymmetric | for every x, y: if (x, y) and (y, x) in R then x = y |
# | transitive | for every x, y, z: if (x, y) and (y, z) in R then (x, z) in R |
#
# **On paper:** write the negation of "transitive" so that no "not" stands in front of a
# quantifier. It tells you what a counterexample looks like. Then load the relations.

# %%
sample = U.load_csv("skills_sample.csv")                      # 40 volunteers
P = [r["vol_code"] for r in sample]
born = {r["vol_code"]: dt.date.fromisoformat(r["birth_date"]) for r in sample}
district = {r["vol_code"]: r["district"] for r in sample}
skills = {r["vol_code"]: frozenset(r["skills"].split(";")) for r in sample}
T = [f"T{i}" for i in range(1, 9)]
LEADS = [f"TL-{i:02d}" for i in range(1, 13)]
MODS = [f"M{i}" for i in range(1, 10)]
TAGS = [r["tag"] for r in U.load_csv("releases.csv")]

def version(tag):
    return tuple(int(x) for x in tag.split("."))

RELATIONS = {
    "same district": (P, {(a, b) for a in P for b in P if district[a] == district[b]}),
    "born within a year of": (P, {(a, b) for a in P for b in P if abs((born[a] - born[b]).days) <= 365}),
    "strictly older than": (P, {(a, b) for a in P for b in P if born[a] < born[b]}),
    "has at least the skills of": (P, {(a, b) for a in P for b in P if skills[a] >= skills[b]}),
    "module requires module": (T, U.pairs("training_prereq.csv", "module", "requires")),
    "lead can cover for lead": (LEADS, U.pairs("can_cover.csv", "lead", "covers_for")),
    "software module imports": (MODS, U.pairs("module_imports.csv", "module", "imports")),
    "release version at most": (TAGS, {(a, b) for a in TAGS for b in TAGS if version(a) <= version(b)}),
    "release text at most": (TAGS, {(a, b) for a in TAGS for b in TAGS if a <= b}),
}
for k, (X, R) in RELATIONS.items():
    print(f"{k:28s} on {len(X):2d} elements: {len(R):4d} pairs")

# %% [markdown]
# BEGIN SOLUTION
# There exist x, y, z with (x, y) in R and (y, z) in R and (x, z) not in R. A counterexample is
# such a triple.
# END SOLUTION

# %% [markdown]
# ## 2 · The property checkers
#
# Write the four functions, each a direct translation of its statement: "for every" is `all`,
# "there exists" is `any`. They return True or False.

# %%
def reflexive(R, X):
    # BEGIN SOLUTION
    return all((x, x) in R for x in X)
    # END SOLUTION

def symmetric(R):
    # BEGIN SOLUTION
    return all((y, x) in R for x, y in R)
    # END SOLUTION

def antisymmetric(R):
    # BEGIN SOLUTION
    return all(x == y for x, y in R if (y, x) in R)
    # END SOLUTION

def transitive(R):
    # BEGIN SOLUTION
    after = {}
    for y, z in R:
        after.setdefault(y, set()).add(z)
    return all((x, z) in R for x, y in R for z in after.get(y, ()))
    # END SOLUTION

# %%
X3 = [1, 2, 3]
le3 = {(a, b) for a in X3 for b in X3 if a <= b}
try:
    small = (reflexive(le3, X3), symmetric(le3), antisymmetric(le3), transitive(le3))
except NotImplementedError:
    small = (True, False, True, True)
print("<= on {1, 2, 3}: reflexive, symmetric, antisymmetric, transitive =", small)
U.check(small == (True, False, True, True), "<= is reflexive, antisymmetric and transitive, not symmetric")

# %% [markdown]
# ## 3 · Classify nine relations
#
# For each relation, print the four properties and a verdict: **equivalence** (reflexive,
# symmetric, transitive), **partial order** (reflexive, antisymmetric, transitive), **strict
# order** (not reflexive on any element, transitive, antisymmetric), **preorder** (reflexive and
# transitive only), or **none of these**. Write `verdict(R, X)`.
#
# Predict each verdict before you run the cell.

# %%
def props(R, X):
    try:
        return {"refl": reflexive(R, X), "sym": symmetric(R), "anti": antisymmetric(R), "trans": transitive(R)}
    except NotImplementedError:
        return None

def verdict(R, X):
    p = props(R, X)
    # BEGIN SOLUTION
    irreflexive = all((x, x) not in R for x in X)
    if p["refl"] and p["sym"] and p["trans"]:
        return "equivalence"
    if p["refl"] and p["anti"] and p["trans"]:
        return "partial order"
    if irreflexive and p["anti"] and p["trans"]:
        return "strict order"
    if p["refl"] and p["trans"]:
        return "preorder"
    return "none of these"
    # END SOLUTION

# %%
rows, verdicts = [], {}
for k, (X, R) in RELATIONS.items():
    p = props(R, X)
    try:
        v = verdict(R, X)
    except (NotImplementedError, TypeError):
        v = U.reference("w3_verdicts")[k]
    verdicts[k] = v
    rows.append([k] + (["yes" if p[c] else "no" for c in ("refl", "sym", "anti", "trans")] if p else ["?"] * 4) + [v])
verdicts = U.keep("w3_verdicts", verdicts)
U.table(rows, ["relation", "refl", "sym", "anti", "trans", "verdict"])
U.check(verdicts["same district"] == "equivalence" and verdicts["strictly older than"] == "strict order"
        and verdicts["has at least the skills of"] == "preorder", "three of the verdicts")

# %% [markdown]
# **Look at** the two release relations. Both are orders, and every two tags are comparable in
# both. Only one of them is the order people mean: the properties cannot tell you which.

# %%
print("by version:", sorted(TAGS, key=version))
print("by text:   ", sorted(TAGS))

# %% [markdown]
# ## 4 · Counterexamples
#
# A "no" in the table is a claim that a counterexample exists. Write `transitivity_counterexample(R)`
# returning one triple (x, y, z) with (x, y), (y, z) in R and (x, z) not in R, or None; and find the
# pair that breaks symmetry of "can cover for". Both faults were planted: one is in the data, one is
# in the meaning of a relation.

# %%
def transitivity_counterexample(R):
    # BEGIN SOLUTION
    after = {}
    for y, z in R:
        after.setdefault(y, set()).add(z)
    for x, y in sorted(R):
        for z in sorted(after.get(y, ())):
            if (x, z) not in R:
                return (x, y, z)
    return None
    # END SOLUTION

# %%
_, near = RELATIONS["born within a year of"]
try:
    cx = transitivity_counterexample(near)
except NotImplementedError:
    cx = tuple(U.reference("w3_counterexample"))
cx = U.keep("w3_counterexample", cx)
x, y, z = cx
print("born within a year:", x, born[x], "|", y, born[y], "|", z, born[z])
print("days apart:", abs((born[x] - born[y]).days), abs((born[y] - born[z]).days), "but", abs((born[x] - born[z]).days))
U.check((x, y) in near and (y, z) in near and (x, z) not in near, "a real counterexample to transitivity")
_, cover = RELATIONS["lead can cover for lead"]
one_way = sorted((a, b) for a, b in cover if (b, a) not in cover)
print("can cover, but not covered back:", one_way)
U.check(one_way == [("TL-04", "TL-09")], "one pair breaks symmetry")

# %% [markdown]
# **Look at** the two kinds of fault. "Within a year" is not transitive by its meaning: nobody can
# fix that in the data, so it must never be used to form groups. The cover table is meant to be
# symmetric and is not: that is a data-quality error for the coordinator.

# %% [markdown]
# ## 5 · Equivalence classes
#
# An equivalence relation splits its set into classes: x's class is every y with x R y. Write
# `classes(R, X)` returning a list of frozensets, then check the two defining facts of a
# **partition**: the classes cover X, and two different classes share nothing.

# %%
def classes(R, X):
    # BEGIN SOLUTION
    out = []
    for x in X:
        c = frozenset(y for y in X if (x, y) in R)
        if c not in out:
            out.append(c)
    return out
    # END SOLUTION

# %%
X, R = RELATIONS["same district"]
try:
    parts = classes(R, X)
except NotImplementedError:
    parts = [frozenset(c) for c in U.reference("w3_classes")]
parts = U.keep("w3_classes", parts)
print(len(parts), "classes, sizes", sorted((len(c) for c in parts), reverse=True))
U.check(set().union(*parts) == set(X), "the classes cover the 40 volunteers")
U.check(all(not (a & b) for a, b in itertools.combinations(parts, 2)), "different classes are disjoint")

# %% [markdown]
# ## 6 · Transitive closure of the prerequisites
#
# `module requires module` lists only direct prerequisites. The **transitive closure** adds (a, c)
# whenever (a, b) and (b, c) are there, until nothing changes. Write `closure(R)`. Then add the
# pairs (t, t) and check that the result is a partial order: "requires, directly or not, or is".

# %%
def closure(R):
    # BEGIN SOLUTION
    C = set(R)
    while True:
        new = {(a, d) for a, b in C for c, d in C if b == c} - C
        if not new:
            return C
        C |= new
    # END SOLUTION

# %%
X, R = RELATIONS["module requires module"]
try:
    Rc = closure(R)
except NotImplementedError:
    Rc = {tuple(p) for p in U.reference("w3_closure")}
Rc = U.keep("w3_closure", Rc)
order = Rc | {(t, t) for t in X}
print("direct pairs:", len(R), "| after closure:", len(Rc))
print("everything T8 needs:", sorted(b for a, b in Rc if a == "T8"))
p = props(order, X)
print("closure plus (t, t):", p)
U.check(p is None or (p["refl"] and p["anti"] and p["trans"]), "the reflexive-transitive closure is a partial order")

# %% [markdown]
# ## 7 · A claim over all integers
#
# Claim: "divides" is transitive on the positive integers: if a divides b and b divides c, then a
# divides c. Your checker can test it on 1 to 60, every triple. That is 216,000 cases, and it says
# nothing about 61. Test it, then write the proof below.

# %%
N = U.pick(60, 25)
D = {(a, b) for a in range(1, N + 1) for b in range(1, N + 1) if b % a == 0}
try:
    print("divides on 1 to", N, ": transitive", transitive(D), "| symmetric", symmetric(D), "| antisymmetric", antisymmetric(D))
except NotImplementedError:
    pass

# %% [markdown]
# *Your proof that "divides" is transitive on all positive integers, and a counterexample that
# shows it is not symmetric:*

# %% [markdown]
# BEGIN SOLUTION
# **Proof (direct).** Let a, b, c be positive integers with a | b and b | c. By definition there are
# integers k and l with b = k·a and c = l·b. Substituting, c = l·(k·a) = (l·k)·a, and l·k is an
# integer, so a | c. Nothing in the argument depends on the size of a, b or c, so it covers every
# case, including those beyond 60.
#
# **Not symmetric.** 2 | 4 but 4 does not divide 2. One counterexample is enough to refute a
# "for every" claim.
# END SOLUTION

# %% [markdown]
# ## 8 · Record
#
# Write three sentences: which of today's results are proofs (every case of a finite relation was
# checked), which are tests of a claim with infinitely many cases, and which two faults the
# coordinator should hear about. (No code.)

# %% [markdown]
# *Your note:*

# %% [markdown]
# ## ✱ Stretch
#
# On X = {1, 2, 3} there are 3 · 3 = 9 possible pairs and 2⁹ = 512 relations. Enumerate them all
# with your checkers and count the equivalence relations. Compare with the number of ways to split
# a three-element set into groups.

# %% [markdown]
# ## Check yourself
#
# <details><summary>1. Your code checks transitivity on all 40 volunteers and finds no counterexample. Is that a proof?</summary>
# For that relation on those 40 volunteers, yes: every case was checked. It is not a proof for the
# next volunteer who joins, unless the relation's definition guarantees it.</details>
#
# <details><summary>2. Why is "has at least the skills of" not a partial order?</summary>
# It is not antisymmetric: two different volunteers with the same skills each have at least the
# skills of the other.</details>
#
# <details><summary>3. What does one counterexample to "for every x" show?</summary>
# That the claim is false. The negation of "for every x, P(x)" is "there exists x with not P(x)",
# and one such x is a witness.</details>
#
# ## Carry forward
#
# Nothing to save. Week 4 proves claims about every integer by induction, where week 3's direct
# proof is not enough.
