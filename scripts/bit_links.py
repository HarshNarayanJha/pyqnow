import glob
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

extra_links = {
    "Data Structures": [
        {"name": "Infix to Prefix Conversion (Find others on the sidebar)", "url": "https://www.calcont.in/Conversion/infix_to_prefix"},
        {"name": "Stack Visualizer", "url": "https://www.cs.usfca.edu/~galles/visualization/StackArray.html"},
        {"name": "Queue Visualizer", "url": "https://www.cs.usfca.edu/~galles/visualization/QueueArray.html"},
        {"name": "Binary Search", "url": "https://www.cs.usfca.edu/~galles/visualization/Search.html"},
        {"name": "Binary Search Tree", "url": "https://www.cs.usfca.edu/~galles/visualization/BST.html"},
        {"name": "AVL Tree Visualizer", "url": "https://www.cs.usfca.edu/~galles/visualization/AVLtree.html"},
        {"name": "More Visualizers", "url": "https://www.cs.usfca.edu/~galles/visualization/Algorithms.html"},
    ],
    "Computer Organization and Architecture": [
        {"name": "Booth's Algorithm Calculator", "url": "https://www.grahn.us/projects/booths-algorithm/"}
    ],
}
cse_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/446"
chem_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/379"
env_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/445"
eee_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/448"
ece_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/449"
math_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/451"
mech_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/452"
phy_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/453"
bio_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/375"

remote_urls: tuple[str, ...] = (cse_url, chem_url, env_url, eee_url, ece_url, math_url, mech_url, phy_url, bio_url)

local_source = glob.glob("pyqs/*/*")
local_url_base = "https://raw.githubusercontent.com/HarshNarayanJha/pyqnow/refs/heads/main/"
local_file_urls = [local_url_base + lf for lf in local_source]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

pdf_base_url = "https://www.bitmesra.ac.in"
pdfs_1st: dict[str, set[str]] = {key: set() for key in subjects_1st}
pdfs_2nd: dict[str, set[str]] = {key: set() for key in subjects_2nd}

for url in remote_urls:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    link_elements = soup.select("td a")
    links = [link.get("href") for link in link_elements]

    for href in links + local_file_urls:
        assert isinstance(href, str)

        for sub in subjects_1st:
            if f"/{sub}" in href:
                pdfs_1st[sub].add(pdf_base_url + href if "https://" not in href else href)

        for sub in subjects_2nd:
            if f"/{sub}" in href:
                pdfs_2nd[sub].add(pdf_base_url + href if "https://" not in href else href)

# pprint(pdfs_1st)
# pprint(pdfs_2nd)

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
            "quiz1": [],
            "mid": [],
            "quiz2": [],
            "end": [],
        }

    for u in _urls:
        m = re.search(re.compile(r"(SP|MO)(\d{4})"), u)
        if m is None:
            continue

        year: str = m.group(2)
        if "MID" in u:
            papers[year]["mid"].append(u)
        elif "END" in u:
            papers[year]["end"].append(u)
        elif "QUIZ 1" in u:
            papers[year]["quiz1"].append(u)
        elif "QUIZ 2" in u:
            papers[year]["quiz2"].append(u)
        else:
            papers[year]["mid"].append(u)

    papers = {k: papers[k] for k in sorted(papers.keys())}

    data = {"code": p, "display": subjects_1st[p], "papers": papers}

    if subjects_1st[p] in extra_links:
        data["links"] = extra_links[subjects_1st[p]]

    writable_file["1"].append(data)

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
            "quiz1": [],
            "mid": [],
            "quiz2": [],
            "end": [],
        }

    for u in _urls:
        m = re.search(re.compile(r"(SP|MO)(\d{4})"), u)
        if m is None:
            continue
        year: str = m.group(2)
        if "MID" in u:
            papers[year]["mid"].append(u)
        elif "END" in u:
            papers[year]["end"].append(u)
        elif "QUIZ 1" in u:
            papers[year]["quiz1"].append(u)
        elif "QUIZ 2" in u:
            papers[year]["quiz2"].append(u)
        else:
            papers[year]["mid"].append(u)

    papers = {k: papers[k] for k in sorted(papers.keys())}

    data = {"code": p, "display": subjects_2nd[p], "papers": papers}

    if subjects_2nd[p] in extra_links:
        data["links"] = extra_links[subjects_2nd[p]]

    writable_file["2"].append(data)

# pprint(writable_file)

with open("hosted/subjects.json", "w") as fp:
    json.dump(writable_file, fp, indent=2, separators=(",", ": "))

# with open("1st_links.json", "w") as fp:
# json.dump(pdfs_1st, fp, indent=4, separators=(",", ": "))

# with open("2nd_links.json", "w") as fp:
# json.dump(pdfs_2nd, fp, indent=4, separators=(",", ": "))
