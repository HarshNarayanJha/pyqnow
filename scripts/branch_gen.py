import json
import logging
from typing import Required, TypedDict

logging.basicConfig(
    level=logging.INFO, format="\033[36m%(asctime)s\033[0m - \033[32m%(levelname)s\033[0m - \033[35m%(message)s\033[0m"
)


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
    "CS240": ["cse"],
    "CS206": ["cse"],
    "CS241": ["cse"],
    "CS6101": ["cse"],
    "MT131": ["cse", "ece"],
    # cse/3rd year
    "CS341": ["cse"],
    "IT6027": ["cse"],
    "CS310": ["cse"],
    "CS331": ["cse"],
    "CS5101": ["cse"],
    "CS332": ["cse"],
    "CS343": ["cse"],
    "CS6103": ["cse"],
    "CS321": ["cse"],
    "CS347": ["cse"],
    # "CS5015": ["cse"],
    "IT301": ["cse"],
    "IT333": ["cse"],
    "IT334": ["cse"],
    "IT335": ["cse"],
    "IT426": ["cse"],
    "IT7021": ["cse"],
    "IT336": ["cse"],
    "IT305": ["cse"],
    "IT337": ["cse"],
    "CS6109": ["cse"],
    "IT338": ["cse"],
    "CS333": ["cse"],
    "CS335": ["cse"],
    "MT204": ["cse"],
    "CS334": ["cse"],
    "CS336": ["cse"],
    "CS338": ["cse"],
    "MT133": ["cse"],
    "IT349": ["cse"],
    "CS351": ["cse"],
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
    "EC301": ["ece"],
    "EC302": ["ece"],
    "EC303": ["ece"],
    "EC305": ["ece"],
    "EC306": ["ece"],
    "EC307": ["ece"],
    "EC319": ["ece"],
    "EC320": ["ece"],
}

logging.info("Setting 2nd year branches")
for sub in data["2"]:
    sub["branch"] = branches[sub["code"]]

logging.info("Setting 3rd year branches")
for sub in data["3"]:
    sub["branch"] = branches[sub["code"]]

logging.info("Writing back to hosted/subjects.json")
with open("hosted/subjects.json", "w") as fp:
    json.dump(data, fp, indent=2, separators=(",", ": "))
