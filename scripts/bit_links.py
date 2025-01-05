import json
import re
from pprint import pprint

import requests
from bs4 import BeautifulSoup

subjects_1st = {
    "MA103": "Mathematics I",
    "CH101": "Chemistry",
    "EC101": "Basics of Electronics and Communicaion Engineering",
    "ME101": "Basics of Mechanical Engineering",
    "MA107": "Mathematics II",
    "PH113": "Physics",
    "CE101": "Environmental Science",
    "CS101": "Programming for Problem Solving",
    "EE101": "Basics of Electrical Engineering",
    "BE101": "Biological Science for Engineers",
}

subjects_2nd = {
    "MA205": "Discrete Mathematics",
    "EC203": "Digital System Design",
    "CS201": "Data Structures",
    "CS231": "Data Structures",
    "CS204": "Object Oriented Programming and Design Patterns",
    "CS233": "Object Oriented Programming and Deisgn Patterns",
    "CS203": "Computer Organization and Architecture",
    "CS235": "Computer Organization and Architecture",
    "MA203": "Numerical Methods",
    "CS301": "Database Management System",
    "CS237": "Database Management System",
    "CS247": "Database Management System",
    "CS211": "Operating System",
    "CS239": "Operating System",
    "CS303": "Operating System",
    "CS240": "Shell and Kernel Programming",
    "CS206": "Design and Analysis of Algorithm",
    "CS241": "Design and Analysis of Algorithm",
    "IT310": "Shell and Kernel Programming",
    "MT131": "UHV2: Understanding Harmony",
}

cse_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/446"
# cse_url = "https://archive.bitmesra.ac.in/Visit_Other_Department_9910?cid=1&deptid=258&pid=446"
chem_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/379"
# chem_url = "https://archive.bitmesra.ac.in/Visit_Other_Department_9910?cid=1&deptid=258&pid=379"
env_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/445"
# env_url = "https://archive.bitmesra.ac.in/Visit_Other_Department_9910?cid=1&deptid=258&pid=445"
eee_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/448"
# eee_url = "https://archive.bitmesra.ac.in/Visit_Other_Department_9910?cid=1&deptid=258&pid=448"
ece_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/449"
# ece_url = "https://archive.bitmesra.ac.in/Visit_Other_Department_9910?cid=1&deptid=258&pid=449"
math_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/451"
# math_url = "https://archive.bitmesra.ac.in/Visit_Other_Department_9910?cid=1&deptid=258&pid=451"
mech_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/452"
# mech_url = "https://archive.bitmesra.ac.in/Visit_Other_Department_9910?cid=1&deptid=258&pid=452"
phy_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/453"
# phy_url = "https://archive.bitmesra.ac.in/Visit_Other_Department_9910?cid=1&deptid=258&pid=453"
bio_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/375"
# bio_url = "https://archive.bitmesra.ac.in/Visit_Other_Department_9910?cid=1&deptid=258&pid=375"

urls: tuple[str, ...] = (cse_url, chem_url, env_url, eee_url, ece_url, math_url, mech_url, phy_url, bio_url)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

pdf_base_url = "https://www.bitmesra.ac.in"
pdfs_1st: dict[str, list[str]] = {key: [] for key in subjects_1st}
pdfs_2nd: dict[str, list[str]] = {key: [] for key in subjects_2nd}

for url in urls:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.select("td a")

    for link in links:
        href = link.get("href")

        assert isinstance(href, str)

        for sub in subjects_1st:
            if f"/{sub}" in href:
                pdfs_1st[sub].append(pdf_base_url + href)

        for sub in subjects_2nd:
            if f"/{sub}" in href:
                pdfs_2nd[sub].append(pdf_base_url + href)

pprint(pdfs_1st)
pprint(pdfs_2nd)

writable_file: dict[str, list[dict[str, str | dict[str, str | dict[str, str | list[str]]]]]] = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
}

for p in pdfs_1st:
    _urls = pdfs_1st[p]
    papers = {}
    for u in _urls:
        m = re.search(re.compile(r"(SP|MO)(\d{4})"), u)
        if m is None:
            continue

        year: str = m.group(2)
        papers[year] = {
            "display": year,
            "mid": [],
            "end": [],
        }

    for u in _urls:
        m = re.search(re.compile(r"(SP|MO)(\d{4})"), u)
        if m is None:
            continue
        year: str = m.group(2)
        if "MID_" in u:
            papers[year]["mid"].append(u)
        elif "END_" in u:
            papers[year]["end"].append(u)
        else:
            papers[year]["mid"].append(u)

    papers = {k: papers[k] for k in sorted(papers.keys())}

    writable_file["1"].append({"code": p, "display": subjects_1st[p], "papers": papers})

for p in pdfs_2nd:
    _urls = pdfs_2nd[p]
    papers = {}
    for u in _urls:
        m = re.search(re.compile(r"(SP|MO)(\d{4})"), u)
        if m is None:
            continue

        year: str = m.group(2)
        papers[year] = {
            "display": year,
            "mid": [],
            "end": [],
        }

    for u in _urls:
        m = re.search(re.compile(r"(SP|MO)(\d{4})"), u)
        if m is None:
            continue
        year: str = m.group(2)
        if "MID_" in u:
            papers[year]["mid"].append(u)
        elif "END_" in u:
            papers[year]["end"].append(u)
        else:
            papers[year]["mid"].append(u)

    papers = {k: papers[k] for k in sorted(papers.keys())}

    writable_file["2"].append({"code": p, "display": subjects_2nd[p], "papers": papers})

pprint(writable_file)

with open("public/subjects.json", "w") as fp:
    json.dump(writable_file, fp, indent=2, separators=(",", ": "))

# with open("1st_links.json", "w") as fp:
# json.dump(pdfs_1st, fp, indent=4, separators=(",", ": "))

# with open("2nd_links.json", "w") as fp:
# json.dump(pdfs_2nd, fp, indent=4, separators=(",", ": "))