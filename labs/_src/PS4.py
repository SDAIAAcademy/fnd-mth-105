# %% [markdown]
# # Problem set 4 · Induction and invariants
#
# Week 4 · 60 minutes · **AI off for the first attempt**: no assistant, no search for the answer.
# After you submit, you may use the hint-only tutor to understand what you missed.
#
# Items marked **[code]** are checked by the last cell, which runs your functions on generated
# cases and stores no answers. Items marked **[written]** are marked by the trainer: write your
# answer in the cell below each one, in full sentences.

# %%
import os, sys, subprocess
from pathlib import Path
if "google.colab" in sys.modules:
    if not Path("/content/fnd-mth-105").exists():
        subprocess.run(["git", "clone", "-q", "https://github.com/SDAIAAcademy/fnd-mth-105.git", "/content/fnd-mth-105"], check=True)
    os.chdir("/content/fnd-mth-105/labs/problem-sets")
while not Path("pscheck.py").exists() and Path.cwd() != Path.cwd().parent:
    os.chdir("problem-sets" if Path("problem-sets").exists() else "..")
sys.path.insert(0, os.getcwd())

# %% [markdown]
# ## 1 [written] · An induction proof with its test
#
# Claim: for every integer n ≥ 1, 1 + 2 + 4 + … + 2ⁿ⁻¹ = 2ⁿ − 1. First test it in code for
# n from 1 to 60 and paste the test. Then prove it by induction: state the base case, the hypothesis
# and the step, and say where the step uses the hypothesis.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 2 [code] · A function with an invariant
#
# Write `running_max(xs)` that returns the largest element of a non-empty list with a single
# loop, and inside the loop `assert` the invariant "best is the largest of the elements seen so far".

# %%
def running_max(xs):
    # ✏️ your code
    raise NotImplementedError

# %% [markdown]
# ## 3 [written] · A loop invariant
#
# For your `running_max`, write the invariant, and prove initialisation, maintenance and
# termination. Say what the invariant gives you when the loop ends.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 4 [written] · The gap in a proof
#
# Find the error in this argument and say which step fails for which n.
#
# *Claim:* in any group of n ≥ 1 volunteers, all are in the same district. *Base:* one volunteer is
# in one district. *Step:* take n + 1 volunteers. Remove the first: the other n share a district by
# the hypothesis. Remove the last: the first n share a district. The two groups overlap, so all n + 1
# share a district.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 5 [code] · The height of a tree
#
# A tree is a dictionary `{"code": ..., "children": [...]}`. Write `height(t)` recursively:
# a node with no children has height 0, any other node one more than its tallest child.

# %%
def height(t):
    # ✏️ your code
    raise NotImplementedError

# %%
import pscheck
pscheck.check(4, globals())
