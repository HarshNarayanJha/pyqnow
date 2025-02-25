import json
from typing import Required, TypedDict


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


with open("hosted/subjects.json", "r") as fp:
    data: dict[str, list[BranchSubject]] = json.load(fp)

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

for sub in data["2"]:
    sub["branch"] = branches[sub["code"]]

with open("hosted/subjects.json", "w") as fp:
    json.dump(data, fp, indent=2, separators=(",", ": "))
