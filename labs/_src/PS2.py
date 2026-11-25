# %% [markdown]
# # Problem set 2 · Truth tables, arguments and encodings
#
# Week 2 · 60 minutes · **AI off for the first attempt**: no assistant, no search for the answer.
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
# ## 1 [written] · Translate three rules
#
# Translate each rule of a sports club into a propositional formula. Name your variables first
# (for example m = "is a member"), then write the formula with and, or, not and →.
#
# 1. A guest may use the pool only if a member signs them in.
# 2. Lockers are free for members, and for guests on their first visit.
# 3. Staff may open any locker, but members only their own.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 2 [code] · Tautologies
#
# Write `is_tautology(f, n)`: True when the Python function `f` of n booleans is true on every
# row of its truth table.

# %%
def is_tautology(f, n):
    # ✏️ your code
    raise NotImplementedError

# %% [markdown]
# ## 3 [written] · Valid or invalid
#
# For each argument say whether it is valid. For an invalid one give the row that is a
# counterexample; for a valid one say why no such row exists.
#
# 1. If the report is late, the manager is told. The manager was not told. So the report is not late.
# 2. If it rains, the match is moved. The match was moved. So it rained.
# 3. Either the badge or the code is wrong. The badge is right. So the code is wrong.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 4 [code] · Counting rows
#
# Write `count_models(f, n)`: the number of rows of the truth table on which `f` is true.

# %%
def count_models(f, n):
    # ✏️ your code
    raise NotImplementedError

# %% [markdown]
# ## 5 [written] · An encoding in words
#
# Three volunteers a, b and c. Write the clauses that say "at most one of a, b, c works the
# evening shift" and the clause that says "at least one does". How many clauses does "at most one of
# n" need with the pairwise method? Give the formula and the reason.

# %% [markdown]
# *Your answer:*

# %%
import pscheck
pscheck.check(2, globals())
