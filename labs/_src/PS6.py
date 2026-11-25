# %% [markdown]
# # Problem set 6 · Inclusion-exclusion and linkage
#
# Week 6 · 60 minutes · **AI off for the first attempt**: no assistant, no search for the answer.
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
# ## 1 [written] · Inclusion-exclusion by hand
#
# In a club of 200 members, 90 swim, 70 run and 50 cycle; 30 swim and run, 20 swim and cycle,
# 25 run and cycle, and 10 do all three. How many do at least one? How many do none? Show the
# formula you used.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 2 [code] · Union by inclusion-exclusion
#
# Write `union_size(sets)`: the size of the union of a list of sets, computed **only** from
# the sizes of intersections, by inclusion-exclusion over every non-empty sub-collection.

# %%
def union_size(sets):
    # ✏️ your code
    raise NotImplementedError

# %% [markdown]
# ## 3 [written] · A linkage count
#
# A published table lists people by birth year, sex and one of 8 districts. Years run over
# 50 values. If 1,000 people were spread evenly over the combinations, how many combinations are
# there, and about how many people would share each? Then explain why real registers are not spread
# evenly, and what that does to the number of people who stand alone.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 4 [written] · A note on anonymisation
#
# In five sentences for a non-specialist: why does removing the column of codes from a
# register not make it anonymous, and what does generalising a column (for example birth date to
# birth year) change? Use a count to make the point.

# %% [markdown]
# *Your answer:*

# %% [markdown]
# ## 5 [code] · Divisible by at least one
#
# Write `count_divisible(n, divisors)`: how many of the integers 1 to n are divisible by at
# least one of the numbers in `divisors`, by inclusion-exclusion over the sub-collections of the
# divisors (`math.lcm` gives the numbers divisible by all of a sub-collection), not by looping
# over 1 to n, so that n = 10¹² returns at once.

# %%
def count_divisible(n, divisors):
    # ✏️ your code
    raise NotImplementedError

# %%
import pscheck
pscheck.check(6, globals())
