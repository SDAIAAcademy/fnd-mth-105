---
course: "Discrete Mathematics and Logic for Computing"
code: "FND-MTH-105"
version: "2027.1.0"
deck: "week7"
day: 7
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-mth-105/slides/week7.html"
---

# Discrete Mathematics and Logic for Computing

## Week 7: Graphs, topological order and growth

Dependencies as a directed graph, the cycle that blocks a run, and how counts grow

#### [week7#title] Graphs, topological order and growth

*SDAIA Academy · Discrete Mathematics and Logic for Computing*

Week 7: Dependencies as a directed graph, the cycle that blocks a run, and how counts grow

Data & AI Foundations Track · 7 weeks + capstone · 1 session · 1 lab · FND-MTH-105

#### [week7#agenda] Graphs, topological order and growth

*This week*

- **Session 1 · Graphs, cycles, orders and recurrences**: Graphs, trees and directed acyclic graphs, paths and cycles, topological order, and recurrences and the growth of functions

#### [week7#review-week6] How many people can be found?

*Review · week 6*

**Question:** Two tables are released. 32 people are alone in their combination in the first, 18 in the second, and 7 of them are alone in both. How many people are alone in at least one table?

- A. 43
- B. 50
- C. 32
- D. 36

### Session 1: Graphs, cycles, orders and recurrences

#### [week7#s1] Graphs, cycles, orders and recurrences

*Session 1*

- Model dependencies as a directed graph and decide whether it has a cycle
- Compute a topological order and check that every edge points forward
- Set up a recurrence for a count, solve it, and compare how fast functions grow

#### [week7#graphs] A directed graph is a set of nodes and a relation on them

*Block A · graphs*

- An **edge** (u, v) is a pair in the relation: here "u must finish before v starts"
- **In-degree**: edges arriving; **out-degree**: edges leaving
- A **source** has in-degree 0; a **sink** has out-degree 0
- A **path** follows edges forward; a **cycle** is a path that returns to its start
- A **DAG** is a directed graph with no cycle; a **tree** has no cycle even with edges read both ways

- **A morning of five tasks.** A and B feed C; C feeds D and E. Sources A, B; sinks D, E. The in-degrees add up to 4, the number of edges.

#### [week7#cycle-blocks] A cycle of dependencies means no job on it can ever start

*Why cycles matter*

1. **1 · Start what is ready** Every job whose dependencies have all finished
2. **2 · Peel it off** Remove it; its successors lose one unfinished dependency
3. **3 · Repeat or stop** All gone: no cycle. Some left, none ready: a cycle among them

> **Takeaway.** In a graph with no cycle there is always a job with nothing unfinished before it, so peeling only stops early when a cycle exists.

#### [week7#check-cycle] Which jobs are never ready?

*Checkpoint*

**Question:** Edges: A → B, B → C, C → D, D → B, A → E. Peeling starts with every job that has no dependency. Which jobs are never ready?

- A. B, C and D
- B. D only
- C. B, C, D and E
- D. none, since A has no dependency

#### [week7#topo-order] A topological order puts every edge forward

*Block B · topological order*

The jobs in the order they are peeled form a **topological order**: for every edge (u, v), u comes before v.

The morning of five tasks has 4 of them: ABCDE, ABCED, BACDE, BACED. An order is rarely unique.

| Order A C B D E: edge | Positions | Forward? |
| --- | --- | --- |
| A → C | 1, 2 | yes |
| B → C | 3, 2 | no |
| C → D | 2, 4 | yes |
| C → E | 2, 5 | yes |

> **Check, do not trust.** The definition is edge by edge: one backward edge makes an order invalid, and no backward edge, with every node once, makes it valid.

#### [week7#invariant] A loop invariant proves the peeled order is topological

*Why peeling is correct*

| Part | For the invariant "every job in the list has all its predecessors earlier in the list" |
| --- | --- |
| Initialisation | The list is empty: nothing to check |
| Maintenance | A job is added only when all its predecessors are already in the list |
| Termination | If every job is peeled, the invariant covers every edge: the list is a topological order |

#### [week7#check-topo] Which order is valid?

*Checkpoint*

**Question:** Edges: P → R, Q → R, R → S, Q → S. Which running order respects every edge?

- A. P R Q S
- B. Q P S R
- C. Q P R S
- D. R Q P S

#### [week7#recurrence-paths] Count paths into a node from the counts into its predecessors

*Block C · recurrences*

In a grid walked right or down, the paths into a point are the paths into the point above plus the paths into the point on the left: **P(i, j) = P(i − 1, j) + P(i, j − 1)**, with 1 along the edges.

| 1 | 1 | 1 |
| --- | --- | --- |
| 1 | 2 | 3 |
| 1 | 3 | 6 |

- **Why it works.** Every path into a point arrives by exactly one last edge, so the paths split into disjoint groups, one per predecessor: the sum rule of week 5. Walk the points in a topological order so each sum uses finished counts.

#### [week7#growth] Counts that look small at n = 10 are out of reach at n = 30

*Growth*

| n | n² | 2ⁿ | n! |
| --- | --- | --- | --- |
| 10 | 100 | 1,024 | 3.6 × 10⁶ |
| 20 | 400 | 1,048,576 | 2.4 × 10¹⁸ |
| 30 | 900 | 1,073,741,824 | 2.7 × 10³² |

- Paths across an n by n grid: 252 at n = 5, 184,756 at n = 10, about 1.2 × 10¹⁷ at n = 30
- Listing every path or order is fine for a toy and hopeless at scale
- A recurrence does one step per node: count without listing

#### [week7#solve-recurrence] Guess a closed form from the first values, then prove it by induction

*Solve, then prove*

1. **1 · Recurrence** Links among n people: H(1) = 0, H(n) = H(n − 1) + (n − 1)
2. **2 · Guess** 0, 1, 3, 6, 10: H(n) = n(n − 1)/2
3. **3 · Prove** H(n − 1) + (n − 1) = (n − 1)(n − 2)/2 + (n − 1) = n(n − 1)/2

> **Takeaway.** The step uses the hypothesis for n − 1: that is the induction. Test the guess in code first, as the capstone asks.

#### [week7#check-recurrence] What does the recurrence give?

*Checkpoint*

**Question:** H(1) = 0 and H(n) = H(n − 1) + (n − 1). What is H(6)?

- A. 21
- B. 30
- C. 36
- D. 15

#### [week7#beyond] This course stops at cycles, orders and counts

*Where this goes next*

- **Here.** Graphs as relations, degrees, cycles, topological order, path counts by recurrence, and growth.
- **FND-PRG-103.** Graph algorithms: breadth-first and depth-first search and shortest paths, with their running times.

#### [week7#lab-7-1] Cycle detection and topological order in a pipeline graph

Lab 7.1 · 105 min

Find and name the cycle in the centre's thirty nightly jobs, remove the wrong edge, check an order edge by edge, and count paths two ways.

[W7_1.ipynb](https://sdaiaacademy.github.io/fnd-mth-105/labs/W7_1.ipynb)

- [ ] A small graph by hand; load the pipeline (10 min)
- [ ] Degrees, sources and sinks (10 min)
- [ ] Find a cycle: library and peeling (20 min)
- [ ] Name the cycle and remove the wrong edge (10 min)
- [ ] A topological order, checked edge by edge (15 min)
- [ ] Count paths: recurrence and listing (20 min)
- [ ] How path counts grow (10 min)
- [ ] Record for the operations lead (10 min)
- [ ] ✱ Stretch: Earliest round of each job when every ready job runs at once

#### [week7#debrief-pipeline] Three jobs waiting on each other stopped eleven

*Debrief · lab 7.1*

| Measure | Value |
| --- | --- |
| Jobs, dependencies | 30, 42 |
| Peeled before the run blocked | 19 |
| Cycle: J12 → J19 → J23 → J12 | 3 jobs |
| Paths from a source to J30 | 29 |
| Rounds if ready jobs run at once | 12 |

- Removing J23 → J12 leaves no cycle; peeled, library and checked orders all pass
- The alphabetical order breaks an edge
- Chained diamonds: 2ᵏ paths through 3k + 1 jobs

#### [week7#wrap-up] Three things to keep

*Week 7 · wrap-up*

- **Peel to find cycles.** If jobs remain and none is ready, a cycle holds them.
- **Check every edge.** An order is valid when every edge points forward: a finite check.
- **Count by recurrence.** Sum over predecessors, then prove the closed form by induction.

#### [week7#next] Capstone: Portfolio oral defences

*Next*

Problem set 7, then the second test. Your portfolio: three proofs from the claim list, each with its test code first, in a public GitHub repository.
