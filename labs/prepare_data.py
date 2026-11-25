"""Write the synthetic data of the community volunteer centre (FND-MTH-105) into labs/data/.

    uv run python prepare_data.py

Standard library only, seed 105: every run writes the same files. Nothing here is real. The
centre, its city and its people have no names: volunteers are coded V-00001 to V-04000, postal
districts PD-01 to PD-12, events EV-01 to EV-30, shifts SH-001 onwards, team leads TL-01 to TL-12,
training modules T1 to T8, software modules M1 to M9, pipeline jobs J01 to J30. No person name,
phone number or national identifier is generated.

What is planted, and which lab finds it, is listed in solutions/answer_key.md.
"""
from __future__ import annotations

import csv
import datetime as dt
import json
import random
from pathlib import Path

SEED = 105
DATA = Path(__file__).resolve().parent / "data"

DISTRICTS = [f"PD-{i:02d}" for i in range(1, 13)]
# uneven district sizes: central districts are larger
DISTRICT_WEIGHTS = [14, 12, 11, 10, 9, 9, 8, 7, 6, 6, 5, 3]
SKILLS = ["first aid", "driving", "lifting", "translation", "sign language", "cooking", "tutoring", "logistics"]
EVENT_KINDS = ["food parcels", "park clean-up", "reading hour", "home visits", "school supplies", "tree planting"]
REF_DATE = dt.date(2026, 9, 1)


def write_csv(name: str, header: list[str], rows: list[list]) -> None:
    with (DATA / name).open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)


def age_on(birth: dt.date, day: dt.date) -> int:
    return day.year - birth.year - ((day.month, day.day) < (birth.month, birth.day))


def register(rng: random.Random) -> list[dict]:
    """4,000 volunteers. Birth dates from 1956 to 2010, more of them young."""
    people = []
    start = dt.date(1956, 1, 1)
    span = (dt.date(2010, 8, 31) - start).days
    for i in range(1, 4001):
        # a triangular draw leaning to younger volunteers
        offset = int(rng.triangular(0, span, span * 0.78))
        birth = start + dt.timedelta(days=offset)
        sex = rng.choice("FM")
        district = rng.choices(DISTRICTS, weights=DISTRICT_WEIGHTS)[0]
        joined = dt.date(2019, 1, 1) + dt.timedelta(days=rng.randrange(0, (REF_DATE - dt.date(2019, 1, 1)).days))
        k = rng.choice([1, 1, 2, 2, 2, 3])
        skills = sorted(rng.sample(SKILLS, k), key=SKILLS.index)
        minor = age_on(birth, REF_DATE) < 18
        guardian = "Y" if minor else "-"
        people.append({"vol_code": f"V-{i:05d}", "birth_date": birth.isoformat(), "sex": sex, "district": district,
                       "joined": joined.isoformat(), "skills": ";".join(skills), "guardian_consent": guardian,
                       "share_consent": rng.choice("YYYN")})
    # planted: three minors without guardian consent (a data-quality rule, week 3 and PS3)
    minors = [p for p in people if p["guardian_consent"] == "Y"]
    for p in rng.sample(minors, 3):
        p["guardian_consent"] = "N"
    return people


def badges(rng: random.Random, people: list[dict]) -> list[list]:
    """Check-in badge numbers BD-0001 onwards for the first 300 volunteers.
    Planted (lab 1.1): two volunteers have no badge (the map is not total) and three badge numbers
    were issued twice (the map is not injective)."""
    first = [p["vol_code"] for p in people[:300]]
    nums = rng.sample(range(1, 1000), 300)
    rows = [[v, f"BD-{n:04d}"] for v, n in zip(first, nums)]
    rows = [r for r in rows if r[0] not in ("V-00117", "V-00242")]
    for a, b in [(10, 200), (55, 260), (131, 287)]:
        rows[b][1] = rows[a][1]
    rows.sort()
    return rows


def events_and_shifts(rng: random.Random):
    events, shifts = [], []
    day0 = dt.date(2026, 9, 5)
    for e in range(1, 31):
        district = rng.choices(DISTRICTS, weights=DISTRICT_WEIGHTS)[0]
        kind = EVENT_KINDS[(e - 1) % len(EVENT_KINDS)]
        day = day0 + dt.timedelta(days=(e - 1) * 2)
        events.append([f"EV-{e:02d}", kind, district, day.isoformat()])
        for part in ("early", "middle", "late"):
            s = len(shifts) + 1
            shifts.append([f"SH-{s:03d}", f"EV-{e:02d}", part, f"TL-{rng.randrange(1, 13):02d}"])
    return events, shifts


def assignments(rng: random.Random, people: list[dict], shifts: list[list]) -> list[list]:
    """About 600 (volunteer, shift) pairs over the first 300 volunteers.
    Planted (lab 1.1): some volunteers work two shifts of the same event, so a join of
    assignments with shifts repeats the (volunteer, event) pair; composition does not."""
    vols = [p["vol_code"] for p in people[:300]]
    pairs = set()
    while len(pairs) < 600:
        pairs.add((rng.choice(vols), rng.choice(shifts)[0]))
    return sorted([list(p) for p in pairs])


def schedule_puzzle(rng: random.Random) -> dict:
    """Lab 2.1: ten volunteers, five shifts. Availability, first aid and two conflicts."""
    vols = [f"V-{i:05d}" for i in (12, 27, 31, 48, 56, 63, 71, 84, 90, 99)]
    shifts = ["SH-A", "SH-B", "SH-C", "SH-D", "SH-E"]
    first_aid = ["V-00012", "V-00048", "V-00071", "V-00090", "V-00099"]
    avail = {
        "V-00012": ["SH-A", "SH-B", "SH-E"], "V-00027": ["SH-A", "SH-C"], "V-00031": ["SH-B", "SH-C", "SH-D"],
        "V-00048": ["SH-C", "SH-D"], "V-00056": ["SH-A", "SH-D", "SH-E"], "V-00063": ["SH-B", "SH-E"],
        "V-00071": ["SH-A", "SH-B"], "V-00084": ["SH-C", "SH-D", "SH-E"], "V-00090": ["SH-D", "SH-E"],
        "V-00099": ["SH-B", "SH-C", "SH-E"],
    }
    return {
        "volunteers": vols, "shifts": shifts, "first_aid": first_aid, "available": avail,
        "per_shift": 2,
        "rules": [
            "every volunteer works exactly one shift",
            "every shift has exactly two volunteers",
            "a volunteer works only a shift they are available for",
            "every shift has at least one volunteer trained in first aid",
            "V-00027 and V-00063 do not work the same shift (one checks the other's hours)",
            "V-00056 and V-00084 do not work the same shift (same household)",
        ],
        "conflicts": [["V-00027", "V-00063"], ["V-00056", "V-00084"]],
        # the coordinator's late change, which makes the puzzle infeasible
        "late_change": {"V-00090": ["SH-E"], "V-00099": ["SH-E"]},
    }


def relations(rng: random.Random, people: list[dict]) -> None:
    """Lab 3.1 files."""
    # training prerequisites: a DAG on T1..T8, not closed under transitivity
    write_csv("training_prereq.csv", ["module", "requires"],
              [["T2", "T1"], ["T3", "T1"], ["T4", "T2"], ["T5", "T2"], ["T5", "T3"], ["T6", "T4"], ["T7", "T5"], ["T8", "T6"], ["T8", "T7"]])
    # team leads who can cover for each other; meant to be symmetric; planted: TL-04 covers TL-09 but not back
    leads = [f"TL-{i:02d}" for i in range(1, 13)]
    cover = set()
    for a in leads:
        for b in leads:
            if a < b and rng.random() < 0.3:
                cover.add((a, b))
                cover.add((b, a))
    cover.discard(("TL-09", "TL-04"))
    cover.add(("TL-04", "TL-09"))
    write_csv("can_cover.csv", ["lead", "covers_for"], sorted([list(p) for p in cover]))
    # software: which module of the scheduling software imports which
    write_csv("module_imports.csv", ["module", "imports"],
              [["M1", "M2"], ["M1", "M3"], ["M2", "M4"], ["M3", "M4"], ["M4", "M5"], ["M6", "M5"], ["M7", "M1"], ["M7", "M6"], ["M8", "M7"], ["M9", "M5"]])
    # releases of the scheduling software; text order and version order differ
    write_csv("releases.csv", ["tag"], [[t] for t in ["2.1.0", "2.9.3", "2.10.0", "2.10.1", "2.2.5", "3.0.0", "2.11.0", "10.0.0", "9.4.1"]])
    # a sample of 40 volunteers for the skills relations
    sample = people[300:340]
    write_csv("skills_sample.csv", ["vol_code", "birth_date", "district", "skills"],
              [[p["vol_code"], p["birth_date"], p["district"], p["skills"]] for p in sample])


def teams(rng: random.Random) -> dict:
    """Lab 4.1: the centre's team tree, zones, then teams, then sub-teams; leaves are teams."""
    counter = [0]

    def node(depth: int) -> dict:
        counter[0] += 1
        code = f"N{counter[0]:03d}"
        if depth == 0:
            kids = 4
        elif depth >= 3:
            kids = 0
        else:
            kids = rng.choice([0, 2, 3]) if depth >= 2 else rng.choice([2, 3])
        return {"code": code, "children": [node(depth + 1) for _ in range(kids)]}

    return node(0)


def signin_sheet(rng: random.Random, people: list[dict]) -> list[list]:
    """Lab 6.1: a sign-in sheet of one event, published with the volunteer code removed.
    It keeps birth date, sex and postal district, and the shift each person worked."""
    chosen = rng.sample(people, 60)
    rows = [[p["birth_date"], p["sex"], p["district"], rng.choice(["early", "middle", "late"])] for p in chosen]
    rows.sort()
    return rows


def pipeline(rng: random.Random):
    """Lab 7.1: thirty nightly jobs. Planted: a cycle J12 -> J19 -> J23 -> J12."""
    names = {
        "J01": "copy the register extract", "J02": "copy the shift table", "J03": "copy the assignments",
        "J04": "copy the event list", "J05": "copy the training records", "J06": "check register dates",
        "J07": "check district codes", "J08": "check shift codes", "J09": "deduplicate assignments",
        "J10": "join assignments to shifts", "J11": "join shifts to events", "J12": "compute volunteer hours",
        "J13": "compute training status", "J14": "flag expired training", "J15": "build the district summary",
        "J16": "build the event summary", "J17": "suppress small counts", "J18": "build the coordinator report",
        "J19": "compute hours by district", "J20": "build check-in codes", "J21": "check code collisions",
        "J22": "build the badge file", "J23": "refresh the hours baseline", "J24": "build the weekly digest",
        "J25": "archive yesterday's files", "J26": "write the audit record", "J27": "publish the open summary",
        "J28": "notify the coordinators", "J29": "compute the quality score", "J30": "close the run",
    }
    edges = [
        ("J01", "J06"), ("J01", "J07"), ("J02", "J08"), ("J03", "J09"), ("J06", "J12"), ("J07", "J15"),
        ("J08", "J10"), ("J09", "J10"), ("J10", "J11"), ("J04", "J11"), ("J11", "J12"), ("J05", "J13"),
        ("J13", "J14"), ("J12", "J19"), ("J19", "J23"), ("J23", "J12"), ("J19", "J15"), ("J11", "J16"),
        ("J15", "J17"), ("J16", "J17"), ("J17", "J27"), ("J14", "J18"), ("J12", "J18"), ("J01", "J20"),
        ("J20", "J21"), ("J21", "J22"), ("J18", "J24"), ("J17", "J24"), ("J24", "J28"), ("J22", "J28"),
        ("J06", "J29"), ("J07", "J29"), ("J08", "J29"), ("J29", "J24"), ("J27", "J26"), ("J28", "J26"),
        ("J26", "J30"), ("J25", "J30"), ("J01", "J25"), ("J02", "J25"), ("J03", "J25"), ("J04", "J25"),
    ]
    jobs = [[j, names[j]] for j in sorted(names)]
    return jobs, sorted([list(e) for e in edges])


def main() -> None:
    rng = random.Random(SEED)
    DATA.mkdir(exist_ok=True)
    people = register(rng)
    cols = ["vol_code", "birth_date", "sex", "district", "joined", "skills", "guardian_consent", "share_consent"]
    write_csv("register.csv", cols, [[p[c] for c in cols] for p in people])
    write_csv("badges.csv", ["vol_code", "badge"], badges(rng, people))
    events, shifts = events_and_shifts(rng)
    write_csv("events.csv", ["event", "kind", "district", "day"], events)
    write_csv("shifts.csv", ["shift", "event", "part", "lead"], shifts)
    write_csv("assignments.csv", ["vol_code", "shift"], assignments(rng, people, shifts))
    (DATA / "schedule_puzzle.json").write_text(json.dumps(schedule_puzzle(rng), indent=1) + "\n", encoding="utf-8", newline="\n")
    relations(rng, people)
    (DATA / "teams.json").write_text(json.dumps(teams(rng), indent=1) + "\n", encoding="utf-8", newline="\n")
    write_csv("signin_sheet.csv", ["birth_date", "sex", "district", "part"], signin_sheet(rng, people))
    jobs, edges = pipeline(rng)
    write_csv("pipeline_jobs.csv", ["job", "task"], jobs)
    write_csv("pipeline_edges.csv", ["upstream", "downstream"], edges)
    print("wrote", ", ".join(sorted(p.name for p in DATA.iterdir() if p.is_file())))


if __name__ == "__main__":
    main()
