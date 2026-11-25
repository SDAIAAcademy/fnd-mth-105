# /// script
# requires-python = ">=3.11"
# dependencies = ["networkx>=3.3"]
# ///
# %% [markdown]
# # Lab 7.1 · Cycle detection and topological order in a pipeline graph
#
# Week 7 · Session 1 (Graphs, cycles, orders and recurrences) · 105 min.
#
# Every night the volunteer centre runs thirty jobs, J01 to J30: copies, checks, joins, summaries,
# reports. A job may start only when every job it depends on has finished. Last night the run
# stopped half way: nothing was ready to start. You model the jobs as a directed graph, find and
# name the cycle that blocked the run, remove the edge the operations lead marks as wrong, check a
# running order edge by edge, and count the paths through the pipeline by a recurrence.
#
# **AI policy.** AI-tutor: it may point at a gap, never write the answer (`labs/tutor/TUTOR.md`).
#
# **Tasks**
# - [ ] 1 · A small graph by hand; load the pipeline (10 min)
# - [ ] 2 · Degrees, sources and sinks (10 min)
# - [ ] 3 · Find a cycle: library and peeling (20 min)
# - [ ] 4 · Name the cycle and remove the wrong edge (10 min)
# - [ ] 5 · A topological order, checked edge by edge (15 min)
# - [ ] 6 · Count paths: recurrence and listing (20 min)
# - [ ] 7 · How path counts grow (10 min)
# - [ ] 8 · Record for the operations lead (10 min)
# - [ ] ✱ Stretch · Earliest round of each job when every ready job runs at once

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
import networkx as nx
import dm as U

# %% [markdown]
# ## 1 · A small graph, then the pipeline
#
# **By hand first.** Four jobs: P → Q, P → R, Q → S, R → S (an arrow means "must finish before").
# Write the in-degree of each job (how many arrows arrive) in `hand_in`, and list every order in
# which the four jobs can run in `hand_orders`. Then load the pipeline: an edge (u, v) means "u
# must finish before v starts".

# %%
hand_in = None        # ✏️ a dictionary such as {"P": 0, ...}
hand_orders = None    # ✏️ a list of strings such as ["PQRS", ...]

small = nx.DiGraph([("P", "Q"), ("P", "R"), ("Q", "S"), ("R", "S")])
print("in-degrees:", dict(small.in_degree()))
orders = ["".join(p) for p in itertools.permutations("PQRS") if all(p.index(u) < p.index(v) for u, v in small.edges)]
print("valid orders:", orders)
if hand_in is not None:
    U.check(hand_in == dict(small.in_degree()), "hand and code agree on the in-degrees")
if hand_orders is not None:
    U.check(sorted(hand_orders) == sorted(orders), "hand and code agree on the orders")

jobs = {r["job"]: r["task"] for r in U.load_csv("pipeline_jobs.csv")}
G = nx.DiGraph()
G.add_nodes_from(jobs)
G.add_edges_from((r["upstream"], r["downstream"]) for r in U.load_csv("pipeline_edges.csv"))
print(G.number_of_nodes(), "jobs,", G.number_of_edges(), "dependencies")

# %% [markdown]
# ## 2 · Degrees, sources and sinks
#
# A **source** has no incoming edge (it can start at once); a **sink** has no outgoing edge
# (nothing waits for it). Write `sources(G)` and `sinks(G)`.

# %%
def sources(G):
    # BEGIN SOLUTION
    return sorted(v for v in G if G.in_degree(v) == 0)
    # END SOLUTION

def sinks(G):
    # BEGIN SOLUTION
    return sorted(v for v in G if G.out_degree(v) == 0)
    # END SOLUTION

# %%
try:
    src, snk = sources(G), sinks(G)
except NotImplementedError:
    src, snk = U.reference("w7_ends")
src, snk = U.keep("w7_ends", [src, snk])
print("sources:", src)
print("sinks:  ", snk)
print("most depended on:", sorted(G.out_degree, key=lambda x: -x[1])[:3])
U.check(sum(d for _, d in G.in_degree()) == G.number_of_edges(), "the in-degrees add up to the number of edges")

# %% [markdown]
# **On paper:** why must the in-degrees of any directed graph add up to its number of edges?

# %% [markdown]
# BEGIN SOLUTION
# Each edge arrives at exactly one job, so it adds exactly one to exactly one in-degree. Summing
# the in-degrees counts every edge once.
# END SOLUTION

# %% [markdown]
# ## 3 · Find a cycle
#
# The run works by **peeling**: start every job with no unfinished dependency; when it finishes,
# remove it; repeat. Write `peel(G)` returning (order, stuck): the jobs in the order they were
# peeled, and the set of jobs never reached. If `stuck` is not empty, the graph has a cycle. Then
# ask the library for one cycle.

# %%
def peel(G):
    # BEGIN SOLUTION
    indeg = dict(G.in_degree())
    ready = sorted(v for v in G if indeg[v] == 0)
    order = []
    while ready:
        v = ready.pop(0)
        order.append(v)
        for w in sorted(G.successors(v)):
            indeg[w] -= 1
            if indeg[w] == 0:
                ready.append(w)
        ready.sort()
    return order, set(G) - set(order)
    # END SOLUTION

# %%
try:
    order, stuck = peel(G)
except NotImplementedError:
    order, stuck = U.reference("w7_peel")
    stuck = set(stuck)
order, stuck_list = U.keep("w7_peel", [order, sorted(stuck)])
print("peeled:", len(order), "jobs | never ready:", sorted(stuck))
cycle = nx.find_cycle(G)
print("a cycle found by the library:", cycle)
U.check(len(stuck) > 0 and not nx.is_directed_acyclic_graph(G), "the run blocks: the graph has a cycle")

# %% [markdown]
# **Look at** the stuck jobs: more than the cycle itself. Every job downstream of the cycle waits
# for it too, which is why the whole second half of the run stopped.

# %% [markdown]
# ## 4 · Name the cycle and remove the wrong edge
#
# Print the cycle with each job's task. The operations lead explains: J23 (refresh the hours
# baseline) is meant to feed **tomorrow's** J12, not tonight's, so the edge J23 → J12 is wrong.
# Remove it and check that no cycle is left.

# %%
for u, v in cycle:
    print(f"{u} ({jobs[u]})  ->  {v} ({jobs[v]})")
H = G.copy()
H.remove_edge("J23", "J12")
print("after removing J23 -> J12: acyclic", nx.is_directed_acyclic_graph(H))
U.check(sorted({u for u, _ in cycle}) == ["J12", "J19", "J23"] and nx.is_directed_acyclic_graph(H), "the cycle J12, J19, J23 is gone")

# %% [markdown]
# ## 5 · A topological order, checked edge by edge
#
# A **topological order** lists every job so that every edge points forward. Peel H to get one.
# Then write `is_topological(order, G)`: True when the order has every job exactly once and every
# edge (u, v) has u before v. Check your order, the library's order, and a wrong order.

# %%
def is_topological(order, G):
    # BEGIN SOLUTION
    pos = {v: i for i, v in enumerate(order)}
    return len(pos) == len(order) == G.number_of_nodes() and set(pos) == set(G) and all(pos[u] < pos[v] for u, v in G.edges)
    # END SOLUTION

# %%
try:
    run, left = peel(H)
except NotImplementedError:
    run, left = list(nx.lexicographical_topological_sort(H)), set()
run = U.keep("w7_order", run)
lib = list(nx.topological_sort(H))
try:
    verdicts = (is_topological(run, H), is_topological(lib, H), is_topological(sorted(H), H))
except NotImplementedError:
    verdicts = (True, True, False)
print("your order:", " ".join(run))
print("valid: yours", verdicts[0], "| library's", verdicts[1], "| alphabetical", verdicts[2])
U.check(not left and verdicts == (True, True, False), "a valid order; the alphabetical order breaks an edge")

# %% [markdown]
# **Look at** two valid orders that differ: a topological order is rarely unique. Any order that
# passes the edge check is a correct running order.

# %% [markdown]
# ## 6 · Count paths by a recurrence
#
# How many different chains of dependencies lead from the sources to J30 (close the run)? In a
# graph without cycles, the number of paths into v is the sum of the paths into each predecessor of
# v, with 1 for each source. Write `count_paths_to(H, order, target)` with that recurrence, walking
# the topological order, then check it by listing every path with `nx.all_simple_paths`.

# %%
def count_paths_to(H, order, target):
    # BEGIN SOLUTION
    paths = {}
    for v in order:
        preds = list(H.predecessors(v))
        paths[v] = 1 if not preds else sum(paths[u] for u in preds)
    return paths[target]
    # END SOLUTION

# %%
try:
    by_recurrence = count_paths_to(H, run, "J30")
except NotImplementedError:
    by_recurrence = U.reference("w7_paths")
by_recurrence = U.keep("w7_paths", by_recurrence)
by_listing = sum(sum(1 for _ in nx.all_simple_paths(H, s, "J30")) for s in [v for v in H if H.in_degree(v) == 0])
print("paths from a source to J30: recurrence", by_recurrence, "| listing", by_listing)
U.check(by_recurrence == by_listing, "the recurrence and the listing agree")

# %% [markdown]
# ## 7 · Growth
#
# Chain k "diamonds" (each like the small graph of task 1) one after another. The number of paths
# from start to end obeys D(k) = 2 · D(k − 1), D(0) = 1, so D(k) = 2ᵏ, while the number of jobs is
# only 3k + 1. Check the recurrence with your counter for k = 1 to 12, and compare how 3k + 1, k²
# and 2ᵏ grow.

# %%
def diamonds(k):
    D = nx.DiGraph()
    D.add_node("d0")
    for i in range(k):
        a, b, c, d = f"d{i}", f"u{i}", f"w{i}", f"d{i + 1}"
        D.add_edges_from([(a, b), (a, c), (b, d), (c, d)])
    return D

rows = []
for k in range(1, U.pick(13, 9)):
    D = diamonds(k)
    try:
        n_paths = count_paths_to(D, list(nx.topological_sort(D)), f"d{k}")
    except NotImplementedError:
        n_paths = 2 ** k
    rows.append([k, D.number_of_nodes(), k * k, n_paths])
U.table(rows, ["k", "jobs (3k + 1)", "k squared", "paths"])
U.check(all(r[3] == 2 ** r[0] for r in rows), "paths double with every diamond: D(k) = 2^k")

# %% [markdown]
# *Prove D(k) = 2ᵏ by induction on k, from the recurrence.*

# %% [markdown]
# BEGIN SOLUTION
# **Base.** k = 0: one node, one path, 2⁰ = 1.
#
# **Step.** Assume D(k) = 2ᵏ paths from d0 to dk. A path to d(k+1) is a path to dk followed by one
# of the two routes through the next diamond (via u_k or via w_k), and every such pair gives a
# different path. So D(k + 1) = 2 · D(k) = 2 · 2ᵏ = 2ᵏ⁺¹, using the hypothesis.
# END SOLUTION

# %% [markdown]
# **Look at** the last column against the second: listing every path is fine for the centre's
# thirty jobs and hopeless for a pipeline of a few hundred. The recurrence needs one pass.

# %% [markdown]
# ## 8 · Record
#
# Write three or four sentences for the operations lead: which jobs formed the cycle, which edge
# was removed and why, a valid running order (or where to find it), and how the order was checked.
# (No code.)

# %% [markdown]
# BEGIN SOLUTION
# The run stopped because J12 (compute volunteer hours), J19 (compute hours by district) and J23
# (refresh the hours baseline) wait on each other: J12 → J19 → J23 → J12. Peeling stopped after 19
# of the 30 jobs; the other 11 are the cycle and every job downstream of it. On the operations
# lead's word the edge J23 → J12 was removed, since the baseline feeds tomorrow's run, not
# tonight's; the graph then has no cycle. The running order printed in task 5 puts the upstream job
# first in each of the 41 remaining dependencies, checked edge by edge by code, and the library's order
# passes the same check. Who changes the pipeline file and who approves the change should be two
# different people, so that a wrong edge is caught before the night run rather than during it.
# END SOLUTION

# %% [markdown]
# ## ✱ Stretch
#
# If every ready job runs at once, a job's earliest round is one more than the latest round of its
# dependencies (round 1 for a source). Compute every job's round with a recurrence over your order.
# How many rounds does the night need, and which chain of jobs decides it?

# %% [markdown]
# ## Check yourself
#
# <details><summary>1. The peeling stops with jobs left over. What does that prove?</summary>
# That the graph has a cycle: in a graph without cycles there is always a job with no unfinished
# dependency, so peeling would continue until every job is gone.</details>
#
# <details><summary>2. Why is checking every edge enough to prove an order is topological?</summary>
# Because "topological" is defined edge by edge: every edge (u, v) has u before v. A finite check of
# all edges is the whole definition.</details>
#
# <details><summary>3. Why count paths with a recurrence rather than by listing them?</summary>
# The number of paths can grow like 2ᵏ while the graph grows like k; the recurrence does one sum per
# job.</details>
#
# ## Carry forward
#
# Nothing to save. Graph algorithms beyond cycles and topological order, such as breadth-first
# and depth-first search and shortest paths, follow in FND-PRG-103.
