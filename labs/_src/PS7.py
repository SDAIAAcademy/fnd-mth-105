# %% [markdown]
# # Problem set 7 · Recurrences, graphs and growth
#
# Week 7 · 60 minutes · **AI off for the first attempt**: no assistant, no search for the answer.
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
# ## 1 [written] · A recurrence solved and proved
#
# A staircase of n steps is climbed one or two steps at a time. Let W(n) be the number of
# ways. Write the recurrence with its first values, compute W(10), and prove by strong induction that
# W(n) ≤ 2ⁿ for every n ≥ 1. Test the bound in code first.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 2 [code] · Counting orders by enumeration
#
# Write `count_orders(nodes, edges)`: the number of orderings of all the nodes in which every
# edge (u, v) has u before v, by trying every permutation.

# %%
def count_orders(nodes, edges):
    # ✏️ your code
    raise NotImplementedError

# %% [markdown]
# ## 3 [written] · A topological order by hand
#
# Tasks: wash (W), cut (C), cook (K), set the table (T), serve (S). C after W; K after C;
# S after K and after T. Give two different valid orders and say how many there are in all, with the
# reason.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 4 [written] · Growth compared
#
# Order these by growth for large n, and justify each step with a ratio or a limit:
# n², 2ⁿ, n log₂ n, n!, 100n.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 5 [code] · The staircase by recurrence
#
# Write `stair_ways(n)` from item 1's recurrence, storing the values already computed so that
# `stair_ways(80)` returns at once.

# %%
def stair_ways(n):
    # ✏️ your code
    raise NotImplementedError

# %%
import pscheck
pscheck.check(7, globals())
