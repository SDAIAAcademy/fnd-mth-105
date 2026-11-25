# %% [markdown]
# # Problem set 3 · Quantifiers, relations and first proofs
#
# Week 3 · 60 minutes · **AI off for the first attempt**: no assistant, no search for the answer.
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
# ## 1 [written] · Quantifiers and negation
#
# Let the domain be the volunteers of a centre, A(v) "v is active" and S(v, e) "v works a shift
# at event e". Write in symbols, then negate and simplify so that no "not" stands before a quantifier:
#
# 1. Every active volunteer works at some event.
# 2. Some event has no volunteer.
# 3. No inactive volunteer works any shift.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 2 [code] · The symmetric closure
#
# Write `symmetric_closure(R)`: the smallest symmetric relation that contains the relation R
# (a set of pairs).

# %%
def symmetric_closure(R):
    # ✏️ your code
    raise NotImplementedError

# %% [markdown]
# ## 3 [written] · A direct proof
#
# Prove directly: if a and b are integers and both are odd, then a·b is odd. Test the claim in
# code on a range of integers first and paste the test under your proof.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 4 [written] · A proof by contradiction
#
# Prove by contradiction: there is no largest even integer. Then say in one sentence which
# statement you assumed, and which contradiction you reached.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 5 [code] · A witness against transitivity
#
# Write `transitivity_witness(R)`: a triple (x, y, z) with (x, y) and (y, z) in R and (x, z)
# not in R, or None when R is transitive.

# %%
def transitivity_witness(R):
    # ✏️ your code
    raise NotImplementedError

# %%
import pscheck
pscheck.check(3, globals())
