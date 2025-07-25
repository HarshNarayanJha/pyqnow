# run from workspace root. MIGRATED. No longer needed

print("Syllabus migration was done. Create and edit files in server/data/syllabus")
exit()

import json
from pathlib import Path
from typing import Any

import pydantic


class ModuleEntry(pydantic.BaseModel):
    topics: list[str]
    important_topics: list[int]


class SyllabusEntry(pydantic.BaseModel):
    code: str
    display: str
    modules: dict[str, dict[str, ModuleEntry]]


SOURCE_FILE = "hosted/syllabus.json"
DEST_DIR = Path("server/data/syllabus")

if not DEST_DIR.exists():
    DEST_DIR.mkdir(parents=True)

with open(SOURCE_FILE, "r") as fp:
    data: dict[str, Any] = json.load(fp)
    subjects: dict[str, list[SyllabusEntry]] = {}
    index: dict[str, str] = {}

    for year in data:
        subjects[year] = []
        for e in data[year]:
            subjects[year].append(SyllabusEntry(**e))

    for year in subjects:
        for sub in subjects[year]:
            if not (DEST_DIR / year).exists():
                (DEST_DIR / year).mkdir(parents=True)

            with open(DEST_DIR / year / f"{sub.code}.json", "w") as fp:
                json.dump(sub.model_dump(exclude_none=True), fp, indent=2)
                index[sub.code] = f"./{year}/{sub.code}.json"

    with open(DEST_DIR / "index.json", "w") as fp:
        json.dump(index, fp)
