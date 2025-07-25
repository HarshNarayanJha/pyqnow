import json
import logging
from pathlib import Path

import pydantic

logging.basicConfig(
    level=logging.INFO, format="\033[36m%(asctime)s\033[0m - \033[32m%(levelname)s\033[0m - \033[35m%(message)s\033[0m"
)


class ModuleEntry(pydantic.BaseModel):
    topics: list[str]
    important_topics: list[int]


class SyllabusEntry(pydantic.BaseModel):
    code: str
    display: str
    modules: dict[str, dict[str, ModuleEntry]]


DEST_DIR = Path("server/data/syllabus")

if not DEST_DIR.exists():
    DEST_DIR.mkdir(parents=True)

subjects: dict[str, list[SyllabusEntry]] = {}
index: dict[str, str] = {}

year = input("Year: ").strip()
code = input("Subject Code: ").strip()
name = input("Subject Display Name: ").strip()

if not (DEST_DIR / year).exists():
    logging.info(f"Creating directory {DEST_DIR / year}")
    (DEST_DIR / year).mkdir(parents=True)

sub = SyllabusEntry(
    code=code, display=name, modules={"1": {"Intro": ModuleEntry(topics=["A", "B"], important_topics=[1])}}
)

with open(DEST_DIR / year / f"{code}.json", "w") as fp:
    logging.info(f"Writing syllabus entry to {DEST_DIR / year / f'{code}.json'}")
    json.dump(sub.model_dump(exclude_none=True), fp, indent=2)

index[sub.code] = f"./{year}/{sub.code}.json"

index_file_path = DEST_DIR / "index.json"
if index_file_path.exists():
    logging.info(f"Updating index file at {index_file_path}")
    with open(index_file_path, "r") as fp:
        read_index: dict[str, str] = json.load(fp)
    read_index.update(index)
else:
    read_index = index

with open(index_file_path, "w") as fp:
    logging.info(f"Writing index file to {index_file_path}")
    json.dump(read_index, fp)
