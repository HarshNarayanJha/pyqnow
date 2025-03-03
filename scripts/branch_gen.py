import json
import logging
from typing import Required, TypedDict

logging.basicConfig(level=logging.INFO, format="\033[36m%(asctime)s\033[0m - \033[32m%(levelname)s\033[0m - \033[35m%(message)s\033[0m")


class ExtraLink(TypedDict):
    name: str
    url: str


class Paper(TypedDict):
    display: str
    quiz1: list[str]
    mid: list[str]
    quiz2: list[str]
    end: list[str]


class BranchSubject(TypedDict, total=False):
    code: Required[str]
    display: str
    papers: dict[str, Paper]
    links: list[ExtraLink]
    branch: list[str]


logging.info("\n\n------------\nBranch Gen Script...")
logging.info("Reading hosted/subjects.json")

with open("hosted/subjects.json", "r") as fp:
    data: dict[str, list[BranchSubject]] = json.load(fp)


logging.info("Setting all branches to all 1st year subjects")
for sub in data["1"]:
    sub["branch"] = ["cse", "ece", "eee"]

branches = {
    # cse/ece
    "MA205": ["cse"],
    "EC203": ["cse", "ece"],
    "CS201": ["cse"],
    "CS231": ["cse"],
    "CS204": ["cse"],
    "CS233": ["cse"],
    "CS203": ["cse"],
    "CS235": ["cse"],
    "MA203": ["cse", "ece"],
    "CS301": ["cse"],
    "CS237": ["cse"],
    "CS247": ["cse"],
    "CS211": ["cse"],
    "CS239": ["cse"],
    "CS303": ["cse"],
    "CS206": ["cse"],
    "CS241": ["cse"],
    "CS6101": ["cse"],
    "MT131": ["cse", "ece"],
    # ece
    "EE205": ["ece"],
    "EC201": ["ece"],
    "EC205": ["ece"],
    "EC251": ["ece"],
    "EC253": ["ece"],
    "EC255": ["ece"],
    "EC257": ["ece"],
    "EC207": ["ece"],
    "EC209": ["ece"],
    "EE251": ["ece"],
    "EE305": ["ece"],
}

logging.info("Setting 2nd year branches")
for sub in data["2"]:
    sub["branch"] = branches[sub["code"]]

logging.info("Writing back to hosted/subjects.json")
with open("hosted/subjects.json", "w") as fp:
    json.dump(data, fp, indent=2, separators=(",", ": "))
