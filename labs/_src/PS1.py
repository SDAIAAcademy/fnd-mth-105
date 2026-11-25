# %% [markdown]
# # Problem set 1 · Sets, functions and composition
#
# Week 1 · 60 minutes · **AI off for the first attempt**: no assistant, no search for the answer.
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
# ## 1 [written] · A set identity
#
# Prove, or refute with a counterexample: for all sets A and B, (A ∪ B) − B = A.
# If it is false, state the extra condition under which it becomes true, and prove that version.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 2 [code] · All subsets
#
# Write `power_set(S)` that returns a list of every subset of the set S, each as a `frozenset`.

# %%
def power_set(S):
    # ✏️ your code
    raise NotImplementedError

# %% [markdown]
# ## 3 [code] · Composition of maps
#
# A function is given as a Python dictionary. Write `compose_maps(f, g)` that returns the
# dictionary of "f, then g": x goes to g[f[x]]. Every value of f is a key of g.

# %%
def compose_maps(f, g):
    # ✏️ your code
    raise NotImplementedError

# %% [markdown]
# ## 4 [written] · Which kind of function?
#
# For each map, say whether it is a function on the stated domain and, if so, whether it is
# injective, surjective onto the stated codomain, or bijective. Give a reason or a counterexample
# for each answer.
#
# 1. Each volunteer code V-00001 to V-04000 to its year of birth; codomain the years 1956 to 2010.
# 2. Each shift to its event; codomain the 30 events; every event has three shifts.
# 3. Each integer n to 2n + 1, from the integers to the integers.
# 4. Each integer n to n + 1, from the integers to the integers.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 5 [written] · Inverse of a composition
#
# f: X → Y and g: Y → Z are bijections. Show that "f, then g" is a bijection and that its inverse
# is "the inverse of g, then the inverse of f". Test the claim first with `compose_maps` on a small
# case of your own, and paste the test below your argument.

# %% [markdown]
# *Your answer:*

# %%
import pscheck
pscheck.check(1, globals())
