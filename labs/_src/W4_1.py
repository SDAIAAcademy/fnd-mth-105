# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
# %% [markdown]
# # Lab 4.1 · Claims tested in code, then proved
#
# Week 4 · Session 1 (Induction, invariants, testing and proof) · 105 min.
#
# *An added lab, beyond the catalog entry's five lab lines.*
#
# Every claim today goes through the same two gates: a test in code on many generated cases, then
# a proof that covers the cases no test reached. You will meet a claim that passes its first forty
# tests and fails on the next, prove a fact about the volunteer centre's team tree by structural
# induction, put invariants inside loops as assertions, and find the gap in a proof that looks
# complete.
#
# **AI policy.** AI-tutor: it may point at a gap, never write the proof (`labs/tutor/TUTOR.md`).
# Proofs are AI-off for the first attempt.
#
# **Tasks**
# - [ ] 1 · Set up; test a sum formula on many cases (10 min)
# - [ ] 2 · Prove it by induction (15 min)
# - [ ] 3 · True for forty cases, false on the next (10 min)
# - [ ] 4 · Structural induction on the team tree (20 min)
# - [ ] 5 · Loop invariants asserted in code (20 min)
# - [ ] 6 · Find the gap in a flawed proof (15 min)
# - [ ] 7 · Record which claims are proved (15 min)
# - [ ] ✱ Stretch · Prove an invariant for binary search over the volunteer codes

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

import random
import dm as U

rng = random.Random(4)

# %% [markdown]
# ## 1 · Test a claim
#
# Write `first_counterexample(claim, cases)`: the first case for which `claim(case)` is False, or
# None when every case passes. You will reuse it all lab.
#
# Claim A: for every n ≥ 1, the sum of the first n odd numbers, 1 + 3 + … + (2n − 1), equals n².

# %%
def first_counterexample(claim, cases):
    # BEGIN SOLUTION
    for c in cases:
        if not claim(c):
            return c
    return None
    # END SOLUTION

def claim_A(n):
    return sum(2 * k - 1 for k in range(1, n + 1)) == n * n

# %%
N = U.pick(1000, 200)
try:
    cx = first_counterexample(claim_A, range(1, N + 1))
except NotImplementedError:
    cx = next((n for n in range(1, N + 1) if not claim_A(n)), None)
print(f"claim A on n = 1 to {N}: counterexample", cx)
U.check(cx is None, "no counterexample in the tested range")

# %% [markdown]
# **Look at** what the test says: nothing about n = 1,001. That is the gap the proof closes.

# %% [markdown]
# ## 2 · Prove claim A by induction
#
# Write the proof in the cell below: the **base case** (n = 1), the **induction hypothesis**
# (assume it for some k ≥ 1), and the **step** (show it for k + 1, saying where you use the
# hypothesis).

# %% [markdown]
# BEGIN SOLUTION
# **Base case.** For n = 1 the sum is 1 and 1² = 1.
#
# **Hypothesis.** For some k ≥ 1, 1 + 3 + … + (2k − 1) = k².
#
# **Step.** The sum of the first k + 1 odd numbers is (1 + 3 + … + (2k − 1)) + (2k + 1). By the
# hypothesis the bracket is k², so the sum is k² + 2k + 1 = (k + 1)². The claim holds for k + 1.
#
# By induction it holds for every n ≥ 1, including every n the test never reached.
# END SOLUTION

# %% [markdown]
# ## 3 · Forty passes, then a failure
#
# Claim B: for every n ≥ 0, n² + n + 41 is prime. Write `is_prime(m)` by trial division, then test
# claim B on n = 0 to 39, and then on n = 0 to 100.

# %%
def is_prime(m):
    # BEGIN SOLUTION
    if m < 2:
        return False
    d = 2
    while d * d <= m:
        if m % d == 0:
            return False
        d += 1
    return True
    # END SOLUTION

# %%
def claim_B(n):
    return is_prime(n * n + n + 41)

try:
    first40 = first_counterexample(claim_B, range(0, 40))
    first101 = first_counterexample(claim_B, range(0, 101))
except NotImplementedError:
    first40, first101 = None, 40
print("n = 0 to 39: counterexample", first40, "| n = 0 to 100: counterexample", first101)
U.check(first40 is None and first101 == 40, "forty passes, then a failure at n = 40")
print("at n = 40:", 40 * 40 + 40 + 41, "=", 41, "x", 41)

# %% [markdown]
# **Look at** why n = 40 had to fail: 40² + 40 + 41 = 40 · 41 + 41 = 41 · 41. Forty passing cases
# were never evidence of a pattern that must continue.

# %% [markdown]
# ## 4 · Structural induction on the team tree
#
# `data/teams.json` is the centre's team tree: the centre, its zones, their teams and sub-teams.
# A tree is either a single node, or a node with a list of subtrees. Write `count_nodes(t)` and
# `count_edges(t)` recursively (an edge joins a node to one of its children). Test the claim
# "edges = nodes − 1" on the team tree and on 500 generated trees, then prove it by **structural
# induction**: assume it for every subtree, show it for the tree.

# %%
def count_nodes(t):
    # BEGIN SOLUTION
    return 1 + sum(count_nodes(c) for c in t["children"])
    # END SOLUTION

def count_edges(t):
    # BEGIN SOLUTION
    return sum(1 + count_edges(c) for c in t["children"])
    # END SOLUTION

def random_tree(depth=0):
    kids = rng.randrange(0, 4) if depth < 5 else 0
    return {"code": "n", "children": [random_tree(depth + 1) for _ in range(kids)]}

# %%
tree = U.load_json("teams.json")
try:
    nodes, edges = count_nodes(tree), count_edges(tree)
except NotImplementedError:
    nodes, edges = U.reference("w4_tree")
nodes, edges = U.keep("w4_tree", [nodes, edges])
print("team tree:", nodes, "nodes,", edges, "edges")
trees = [random_tree() for _ in range(U.pick(500, 100))]
try:
    bad = first_counterexample(lambda t: count_edges(t) == count_nodes(t) - 1, trees)
except NotImplementedError:
    bad = None
U.check(edges == nodes - 1 and bad is None, "edges = nodes - 1 on the team tree and on every generated tree")

# %% [markdown]
# *Your proof by structural induction:*

# %% [markdown]
# BEGIN SOLUTION
# Let E(t) and N(t) be the edges and nodes of a tree t. **Claim:** E(t) = N(t) − 1.
#
# **Base.** A single node has N = 1 and E = 0 = 1 − 1.
#
# **Step.** Let t be a root with subtrees t₁, …, t_m (m ≥ 1), and assume the claim for each subtree:
# E(tᵢ) = N(tᵢ) − 1. The nodes of t are the root and the nodes of the subtrees:
# N(t) = 1 + Σ N(tᵢ). The edges of t are the m edges from the root to the subtrees, plus their
# edges: E(t) = m + Σ E(tᵢ) = m + Σ (N(tᵢ) − 1) = Σ N(tᵢ) = N(t) − 1.
#
# Every tree is built from single nodes by this one construction, so the claim holds for every
# tree. The structure of the proof follows the structure of `count_edges`.
# END SOLUTION

# %% [markdown]
# ## 5 · Loop invariants
#
# An **invariant** is a statement that is true before the loop and after every pass. Write
# `divide(a, b)` for a ≥ 0 and b > 0 by repeated subtraction, returning (q, r), and `assert` the
# invariant `a == q * b + r and r >= 0` before the loop and at the end of every pass. Test on
# 2,000 generated pairs against `divmod`.

# %%
def divide(a, b):
    # BEGIN SOLUTION
    q, r = 0, a
    assert a == q * b + r and r >= 0
    while r >= b:
        q, r = q + 1, r - b
        assert a == q * b + r and r >= 0
    return q, r
    # END SOLUTION

# %%
pairs = [(rng.randrange(0, 500), rng.randrange(1, 40)) for _ in range(U.pick(2000, 300))]
try:
    bad = first_counterexample(lambda p: divide(*p) == divmod(*p), pairs)
except NotImplementedError:
    bad = None
print("divide against divmod on", len(pairs), "pairs: counterexample", bad)
U.check(bad is None, "divide agrees with divmod and the invariant held at every pass")

# %% [markdown]
# *Prove `divide` correct from its invariant: initialisation, maintenance, termination, and what
# the invariant and the exit condition give together.*

# %% [markdown]
# BEGIN SOLUTION
# **Invariant.** a = q·b + r and r ≥ 0.
#
# **Initialisation.** q = 0, r = a: a = 0·b + a, and r = a ≥ 0.
#
# **Maintenance.** A pass runs only when r ≥ b. It sets q′ = q + 1 and r′ = r − b. Then
# q′·b + r′ = q·b + b + r − b = q·b + r = a, and r′ = r − b ≥ 0 because r ≥ b.
#
# **Termination.** Each pass lowers r by b ≥ 1 and r stays ≥ 0, so the loop stops after at most a
# passes.
#
# **At exit** the invariant holds and the loop condition is false: a = q·b + r with 0 ≤ r < b, which
# is exactly what quotient and remainder mean.
# END SOLUTION

# %% [markdown]
# ## 6 · The gap in a proof
#
# A colleague hands in this proof. Test the claim first, then find the step that does not follow.
#
# > **Claim.** For every n ≥ 1, 2ⁿ ≥ n².
# >
# > **Base.** n = 1: 2 ≥ 1.
# >
# > **Step.** Assume 2ᵏ ≥ k². Then 2ᵏ⁺¹ = 2 · 2ᵏ ≥ 2k² = k² + k² ≥ k² + 2k + 1 = (k + 1)².
# > So the claim holds for k + 1.

# %%
try:
    gap = first_counterexample(lambda n: 2 ** n >= n * n, range(1, 50))
except NotImplementedError:
    gap = 3
print("first n with 2^n < n^2:", gap, "|", 2 ** gap, "<", gap * gap)
print("where k^2 >= 2k + 1 fails:", [k for k in range(1, 10) if not k * k >= 2 * k + 1])
U.check(gap == 3, "the claim fails at n = 3")

# %% [markdown]
# *Which step fails, for which k, and how would you repair the claim and its proof?*

# %% [markdown]
# BEGIN SOLUTION
# The step uses k² ≥ 2k + 1, which is false for k = 1 and k = 2. So the step from n = 2 to n = 3
# is not justified, and indeed 2³ = 8 < 9 = 3². The base case and the algebra are fine; the gap is
# a hidden assumption about k.
#
# **Repair.** Claim: for every n ≥ 4, 2ⁿ ≥ n². Base n = 4: 16 ≥ 16. Step for k ≥ 4: k² ≥ 2k + 1
# holds because k² − 2k − 1 = (k − 1)² − 2 ≥ 7. The rest of the step is unchanged. (The claim also
# happens to hold at n = 1 and n = 2, but not at n = 3.)
# END SOLUTION

# %% [markdown]
# ## 7 · Record
#
# Fill in the status of each of today's claims: proved, tested only, or refuted. The cell prints
# the table you fill.

# %%
status = {
    "A: sum of the first n odd numbers is n squared": None,   # ✏️ "proved", "tested only" or "refuted"
    "B: n^2 + n + 41 is prime for every n >= 0": None,
    "edges = nodes - 1 in every tree": None,
    "divide returns the quotient and remainder": None,
    "2^n >= n^2 for every n >= 1": None,
}
U.table([[k, v or "(fill in)"] for k, v in status.items()], ["claim", "status"])

# %% [markdown]
# *One sentence on why "tested only" is not the same as "true":*

# %% [markdown]
# BEGIN SOLUTION
# A proved; B refuted (n = 40); edges = nodes − 1 proved by structural induction; divide proved
# from its invariant and termination; 2ⁿ ≥ n² refuted at n = 3, and proved for n ≥ 4 after the
# repair. "Tested only" means no counterexample was found in the range tried: claim B was "tested
# only" for n up to 39, and false.
# END SOLUTION

# %% [markdown]
# ## ✱ Stretch
#
# Binary search over the sorted volunteer codes keeps two indices lo and hi. Write it with the
# invariant "if the code is in the list, its index is in [lo, hi)" asserted on every pass (by a
# slow check), test it on 1,000 searches, and prove termination.

# %% [markdown]
# ## Check yourself
#
# <details><summary>1. What does the induction hypothesis assume, and what does it not?</summary>
# It assumes the claim for one k (or for every value up to k, in strong induction) in order to show
# it for k + 1. It never assumes the claim for all n, which would be circular.</details>
#
# <details><summary>2. A loop's invariant holds before and after every pass. Why is that not yet a proof that the loop is correct?</summary>
# You also need termination, and the invariant together with the exit condition must give the
# result you want. An invariant such as "r ≥ 0" alone holds and proves little.</details>
#
# <details><summary>3. A claim passes 10,000 generated tests. What should the record say?</summary>
# "Tested on 10,000 cases, no counterexample", with the range, until a proof exists. Claim B passed
# forty.</details>
#
# ## Carry forward
#
# Nothing to save. Bring your record of claims: the portfolio asks for the same two gates, test
# then proof, for three claims the assessor issues.
