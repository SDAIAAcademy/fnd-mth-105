# Discrete Mathematics and Logic for Computing: labs

## Quick start

- Google Colab: open a notebook from the course page; its first cell clones this repository and installs `requirements-colab.txt` (the SAT solver library, about 2 MB).
- Locally: clone the repository and, from `labs/`, open the notebooks with `uv run --with jupyterlab jupyter lab` (the dependencies are in `pyproject.toml`, the versions in `uv.lock`). The data in `data/` is already there; `uv run python prepare_data.py` writes it again, identically.

| Unit | Session | Lab | Notebook |
|---|---|---|---|
| Week 1 | Sets, functions and relations | Sets, functions and joins in code (an addition) | [`W1_1.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fnd-mth-105/blob/main/labs/W1_1.ipynb) |
| Week 2 | Propositional logic, normal forms and SAT | Truth tables in code, and a scheduling puzzle solved with a SAT solver | [`W2_1.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fnd-mth-105/blob/main/labs/W2_1.ipynb) |
| Week 3 | Quantifiers, relations and first proofs | Relation properties checked in code | [`W3_1.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fnd-mth-105/blob/main/labs/W3_1.ipynb) |
| Week 4 | Induction, invariants, testing and proof | Claims tested in code, then proved (an addition) | [`W4_1.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fnd-mth-105/blob/main/labs/W4_1.ipynb) |
| Week 5 | Counting arrangements and collisions | Hash collisions and the birthday problem, by formula and by brute force | [`W5_1.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fnd-mth-105/blob/main/labs/W5_1.ipynb) |
| Week 6 | Inclusion-exclusion and linkage risk | Re-identification risk counted from birth date, sex and postal district in a synthetic register | [`W6_1.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fnd-mth-105/blob/main/labs/W6_1.ipynb) |
| Week 7 | Graphs, cycles, orders and recurrences | Cycle detection and topological order in a pipeline graph | [`W7_1.ipynb`](https://colab.research.google.com/github/SDAIAAcademy/fnd-mth-105/blob/main/labs/W7_1.ipynb) |

Labs 2.1, 3.1, 5.1, 6.1 and 7.1 are the catalog entry's five lab lines, in its order and wording. Labs 1.1 and 4.1 are additions, so that each of the seven weekly sessions has a lab: they practise the entry's topics of sets, functions and joins as relation composition, and of induction, loop invariants and testing a claim versus proving it.

Every lab tests a claim in code before anything is proved: on every case when there are few, on generated cases when there are many. An exercise left undone raises `NotImplementedError`; the notebook then falls back on a reference value in `data/reference/` so that every later step still runs. The worked versions, with model proofs of the lab's own claims, are in [`solutions/`](solutions/); what each lab should show is in [`solutions/answer_key.md`](solutions/answer_key.md).

## Problem sets

[`problem-sets/PS1.ipynb`](problem-sets/) to `PS7.ipynb`, one a week, 60 minutes each, AI off for the first attempt. Each has code items and written items (proofs, translations, counts with reasons). The last cell calls [`pscheck.py`](problem-sets/pscheck.py), which runs your functions on generated cases whose right result is known by construction, prints one line per code item and lists the written items. It stores no answers. The trainer marks the written items; the worked answers are kept by the trainer, outside this repository.

## Data

`prepare_data.py` writes the volunteer centre's synthetic data into `data/` with seed 105: the register of 4,000 volunteers (coded V-00001 to V-04000, with birth date, sex, postal district, join date and skills), check-in badges, events, shifts and assignments, the shift puzzle, the relations of lab 3.1, the team tree, a sign-in sheet published without volunteer codes, and the nightly pipeline's jobs and dependencies. No person names, phone numbers or identifiers of any real kind are generated, and nothing is downloaded: the labs need only the Python packages in `pyproject.toml`.

## Settings

| Variable | Effect |
|---|---|
| `DM_QUICK=1` | Smaller enumerations, for a fast run-through |

## Tutor

[`tutor/TUTOR.md`](tutor/TUTOR.md) is the instruction for the hint-only tutor allowed in labs: it points at gaps and never writes the proof.

## For maintainers

The notebooks are generated from the percent-format sources in `labs/_src/` by `labs/_tools/py2nb.py` (`uv run python _tools/py2nb.py` from `labs/`), which also writes the solutions to `labs/solutions/` and the problem sets to `labs/problem-sets/` (problem sets have no solution notebook). Edit the sources, not the notebooks. `labs/_tools/slide_numbers.py` recomputes the numbers quoted on the slides from the parallel examples.
