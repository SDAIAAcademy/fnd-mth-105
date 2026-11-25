# %% [markdown]
# # Problem set 5 · Counting and collisions
#
# Week 5 · 60 minutes · **AI off for the first attempt**: no assistant, no search for the answer.
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
# ## 1 [written] · Counting codes
#
# A locker code is two capital letters (26 choices each) followed by three digits.
# 1. How many codes are there?
# 2. How many have no repeated letter and no repeated digit?
# 3. How many contain at least one 7? (Count the complement.)
# Give each count with the rule you used.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 2 [code] · Arrangements and selections
#
# Write `perm(n, k)` (ordered selections of k from n, no repeats) and `comb(n, k)`
# (unordered), with loops or the formulas, without importing a counting function.

# %%
def perm(n, k):
    # ✏️ your code
    raise NotImplementedError

def comb(n, k):
    # ✏️ your code
    raise NotImplementedError

# %% [markdown]
# ## 3 [written] · A pigeonhole argument
#
# A centre gives 730 volunteers a birthday card on their birthday (month and day). Show that
# some day has at least two cards to send, and find the largest number of cards that the pigeonhole
# principle guarantees on one day.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 4 [written] · A collision formula explained
#
# n codes are drawn uniformly from N possible codes. Explain, counting arrangements, why the
# chance that all n are different is N·(N − 1)·…·(N − n + 1) / Nⁿ. Then check it by listing all cases
# for N = 4 and n = 3, by hand or in code.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 5 [code] · Onto maps by enumeration
#
# Write `count_onto(n, k)`: the number of functions from an n-element set onto a k-element
# set (every element of the second set is reached), counted by enumerating every function.

# %%
def count_onto(n, k):
    # ✏️ your code
    raise NotImplementedError

# %%
import pscheck
pscheck.check(5, globals())
