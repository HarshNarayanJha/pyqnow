# run from workspace root

import json
import logging
from pathlib import Path
from typing import Any

import pydantic

logging.basicConfig(
    level=logging.INFO, format="\033[36m%(asctime)s\033[0m - \033[32m%(levelname)s\033[0m - \033[35m%(message)s\033[0m"
)


class LinkEntry(pydantic.BaseModel):
    name: str
    url: str


class PaperEntry(pydantic.BaseModel):
    display: str
    quiz1: list[str]
    mid: list[str]
    quiz2: list[str]
    end: list[str]


class SubjectEntry(pydantic.BaseModel):
    code: str
    display: str
    papers: dict[str, PaperEntry]
    links: list[LinkEntry] | None = pydantic.Field(None)
    branch: list[str]


logging.info("\n\n------------\nSplit Subjects Script...")


SOURCE_FILE = "hosted/subjects.json"
DEST_DIR = Path("server/data/subjects")

if not DEST_DIR.exists():
    logging.info(f"Creating {DEST_DIR}")
    DEST_DIR.mkdir(parents=True)

logging.info(f"Reading {SOURCE_FILE}")

with open(SOURCE_FILE, "r") as fp:
    data: dict[str, Any] = json.load(fp)
    subjects: dict[str, list[SubjectEntry]] = {}
    index: dict[str, str] = {}

    scount = 0

    for year in data:
        subjects[year] = []
        for e in data[year]:
            subjects[year].append(SubjectEntry(**e))
            scount += 1

    logging.info(f"Splitting {scount} subjects")

    for year in subjects:
        for sub in subjects[year]:
            if not (DEST_DIR / year).exists():
                logging.info(f"Creating {DEST_DIR / year}")
                (DEST_DIR / year).mkdir(parents=True)

            with open(DEST_DIR / year / f"{sub.code}.json", "w") as fp:
                logging.info(f"Writing {DEST_DIR / year / f'{sub.code}.json'}")
                json.dump(sub.model_dump(exclude_none=True), fp, indent=2)
                index[sub.code] = f"./{year}/{sub.code}.json"

    with open(DEST_DIR / "index.json", "w") as fp:
        logging.info(f"Writing {DEST_DIR / 'index.json'}")
        json.dump(index, fp)
