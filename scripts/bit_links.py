import glob
import json
import logging
import re
import urllib.parse
from typing import Required, TypedDict

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO, format="\033[36m%(asctime)s\033[0m - \033[32m%(levelname)s\033[0m - \033[35m%(message)s\033[0m")

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
    # cse/ece
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
    "CS206": "Design and Analysis of Algorithm",
    "CS241": "Design and Analysis of Algorithm",
    "CS6101": "Design and Analysis of Algorithm",
    "MT131": "UHV2: Understanding Harmony",
    # ece
    "EE205": "Circuit Theory",
    "EC201": "Electronic Devices",
    "EC205": "Signals and Systems",
    "EC207": "Electronic Measurements",
    "EC209": "Network Theory",
    "EC251": "Probability and Random Processes",
    "EC253": "Analog Circuits",
    "EC255": "Analog Communication",
    "EC257": "Electromagnetic Fields and Waves",
    "EE305": "Digital Signal Processing",
    "EE251": "DC Machines and Transformer",
}

logging.info(f"Working with {len(subjects_1st)} 1st year subjects and {len(subjects_2nd)} 2nd year subjects")


class ExtraLink(TypedDict):
    name: str
    url: str


class Paper(TypedDict):
    display: str
    quiz1: list[str]
    mid: list[str]
    quiz2: list[str]
    end: list[str]


class Subject(TypedDict, total=False):
    code: Required[str]
    display: str
    papers: dict[str, Paper]
    links: list[ExtraLink]


extra_links: dict[str, list[ExtraLink]] = {
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
    "Operating System": [
        {"name": "Process Scheduling Solver", "url": "https://process-scheduling-solver.boonsuen.com/"},
        {"name": "Process Scheduling Calculator", "url": "https://aadhil2k4.github.io/Process_Scheduling_Calculator/#/"},
        {"name": "Process Scheduling", "url": "https://www.algorithmroom.com/calculator/process-scheduling"},
        {"name": "CPU Scheduling Simulator", "url": "https://da111003.github.io/CPU_Scheduler/backend/ganttcharts.html"},
    ],
    "Numerical Methods": [
        {"name": "Bisection Method Calculator", "url": "https://www.codesansar.com/numerical-methods/bisection-method-online-calculator.htm"},
        {"name": "Secant Method Calculator", "url": "https://www.codesansar.com/numerical-methods/secant-method-online-calculator.htm"},
    ],
    "Design and Analysis of Algorithms": [
        {"name": "Master's Theorem Solver", "url": "https://onlinetoolkit.co/master-theorem-calculator/"},
        {"name": "Huffman Tree Generator", "url": "https://planetcalc.com/2481/"},
        {"name": "Knapsack Calculator", "url": "https://augustineaykara.github.io/Knapsack-Calculator/"},
    ],
}

logging.info(f"Working with {len(extra_links)} subjects with extra links")

cse_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/446"
chem_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/379"
env_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/445"
eee_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/448"
ece_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/449"
math_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/451"
mech_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/452"
phy_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/453"
bio_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/375"
mgmt_url = "https://www.bitmesra.ac.in/Other-Department-Pages/content/1/258/439"

remote_urls: tuple[str, ...] = (cse_url, chem_url, env_url, eee_url, ece_url, math_url, mech_url, phy_url, bio_url, mgmt_url)

local_source = glob.glob("pyqs/*/*")
local_url_base = "https://raw.githubusercontent.com/HarshNarayanJha/pyqnow/refs/heads/main/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
}

pdf_base_url = "https://www.bitmesra.ac.in"
pdfs_1st: dict[str, set[str]] = {key: set() for key in subjects_1st}
pdfs_2nd: dict[str, set[str]] = {key: set() for key in subjects_2nd}

blacklisted_403_urls = {
    "https://www.bitmesra.ac.in/UploadedDocuments/adminexam/files/MO2022%20QP/CS301%20DATABASE%20MANAGEMENT%20SYSTEM%20(MID_MO22).pdf",
    "https://www.bitmesra.ac.in/UploadedDocuments/adminexam/files/MO2022%20QP/CS301%20DATABASE%20MANAGEMENT%20SYSTEM%20(END_MO22).pdf",
    "https://www.bitmesra.ac.in/UploadedDocuments/adminexam/files/SP2022%20QP/CS301%20DATABASE%20MANAGEMENT%20SYSTEM%20(MINOR)%20(END_SP22).pdf",
    "https://www.bitmesra.ac.in/UploadedDocuments/adminexam/files/SP2023%20QP/CS301%20DATABASE%20MANAGEMENT%20SYSTEM%20(MID_SP23).pdf",
    #
    "https://www.bitmesra.ac.in/UploadedDocuments/adminexam/files/SP2023%20QP/CS237%20DATABASE%20MANAGEMENT%20SYSTEM%20(MID-SP23).pdf",
    "https://www.bitmesra.ac.in/UploadedDocuments/adminexam/files/SP2023%20QP/CS237%20DATABASE%20MANAGEMENT%20SYSTEM%20(END_SP23).pdf",
    #
    "https://www.bitmesra.ac.in/UploadedDocuments/adminexam/files/SP2023%20QP/CS247%20DATABASE%20MANAGEMENT%20SYSTEM%20(MID_SP23).pdf",
    "https://www.bitmesra.ac.in/UploadedDocuments/adminexam/files/SP2023%20QP/CS247%20DATABASE%20MANAGEMENT%20SYSTEM%20(END_SP23).pdf",
}

for url in remote_urls:
    response = requests.get(url, headers=headers)
    logging.info(f"Requesting {url}")

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    link_elements = soup.select("td a")
    links = [link.get("href") for link in link_elements]

    for href in links:
        assert isinstance(href, str)

        for sub in subjects_1st:
            if f"/{sub}" in href:
                # logging.info(f"Found Subject {sub}")

                if pdf_base_url + href in blacklisted_403_urls:
                    logging.warning(f"Blacklisted 403 URL {pdf_base_url + href}")
                    continue

                pdfs_1st[sub].add(pdf_base_url + href)

        for sub in subjects_2nd:
            if f"/{sub}" in href:
                # logging.info(f"Found Subject {sub}")

                if pdf_base_url + href in blacklisted_403_urls:
                    logging.warning(f"Blacklisted 403 URL {pdf_base_url + href}")
                    continue

                pdfs_2nd[sub].add(pdf_base_url + href)

for href in local_source:
    logging.info(f"Reading Local File {href}")

    for sub in subjects_1st:
        if f"/{sub}" in href:
            logging.info(f"Found Local Paper for {sub}")
            pdfs_1st[sub].add(local_url_base + urllib.parse.quote(href, safe="/()"))
    for sub in subjects_2nd:
        if f"/{sub}" in href:
            logging.info(f"Found Local Paper for {sub}")
            pdfs_2nd[sub].add(local_url_base + urllib.parse.quote(href, safe="/()"))

writable_file: dict[str, list[Subject]] = {
    "1": [],
    "2": [],
    "3": [],
    "4": [],
}

logging.info("Creating subjects JSON structure for 1st year")

for p in pdfs_1st:
    _urls = pdfs_1st[p]
    papers: dict[str, Paper] = {}

    for u in _urls:
        m = re.search(re.compile(r"(SP|MO)(\d{4})"), u)
        if m is None:
            continue

        year = m.group(2)
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

        year = m.group(2)
        if "MID" in u:
            papers[year]["mid"].append(u)
        elif "END" in u:
            papers[year]["end"].append(u)
        elif "QUIZ%201" in u:
            papers[year]["quiz1"].append(u)
        elif "QUIZ%202" in u:
            papers[year]["quiz2"].append(u)
        else:
            papers[year]["mid"].append(u)

    logging.info("Sorting Papers for 1st year")

    papers = {k: papers[k] for k in sorted(papers.keys())}
    for year in papers:
        papers[year]["mid"].sort()
        papers[year]["end"].sort()
        papers[year]["quiz1"].sort()
        papers[year]["quiz2"].sort()

    data: Subject = {"code": p, "display": subjects_1st[p], "papers": papers}

    if subjects_1st[p] in extra_links:
        data["links"] = extra_links[subjects_1st[p]]

    writable_file["1"].append(data)

logging.info("Creating subjects JSON structure for 2nd year")

for p in pdfs_2nd:
    _urls = pdfs_2nd[p]
    papers = {}

    for u in _urls:
        m = re.search(re.compile(r"(SP|MO)(\d{4})"), u)
        if m is None:
            continue

        year = m.group(2)
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

        year = m.group(2)
        if "MID" in u:
            papers[year]["mid"].append(u)
        elif "END" in u:
            papers[year]["end"].append(u)
        elif "QUIZ%201" in u:
            papers[year]["quiz1"].append(u)
        elif "QUIZ%202" in u:
            papers[year]["quiz2"].append(u)
        else:
            papers[year]["mid"].append(u)

    logging.info("Sorting Papers for 2nd year")

    for year in papers:
        papers[year]["mid"].sort()
        papers[year]["end"].sort()
        papers[year]["quiz1"].sort()
        papers[year]["quiz2"].sort()

    papers = {k: papers[k] for k in sorted(papers.keys())}

    data = {"code": p, "display": subjects_2nd[p], "papers": papers}

    if subjects_2nd[p] in extra_links:
        data["links"] = extra_links[subjects_2nd[p]]

    writable_file["2"].append(data)

logging.info("Writing to hosted/subjects.json")

with open("hosted/subjects.json", "w") as fp:
    json.dump(writable_file, fp, indent=2, separators=(",", ": "))
