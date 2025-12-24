# PYQNow

[![Logo](public/pyqnow_half.png)](https://pyqnow.netlify.app)

PYQs at your fingertips, success in sight

PYQNow is a free website which provides one click access to all PYQs PDFs of BIT Exams.

PYQNow has papers for both CSE and ECE branches now. Enjoy!

## Contributors

- @dev-satyamjha assisted with decoding subjects from other branches

## Project Setup

```sh
bun install
```

### Compile and Hot-Reload for Development

```sh
bun dev
```

### Compile and Minify for Production

```sh
bun run build
```

## Instructions

### Fetch latest papers from BIT website and update local PDF index

```sh
./generate_subjects.sh
```

This will run `scripts/bit_links.py`, `scripts/branch_gen.py` which will format and update `hosted/subjects.json`,
then `scripts/subjects_split_json.py` which will split that big file to `server/data/subjects/*`, which are ultimately used by the deployed server.

### Add a new syllabus entry

```sh
uv run scripts/add_syllabus.py
```

It will scaffold a new syllabus code file at `server/data/syllabus/`.

### Deploy Server

Just go to the render dashboard and deploy the latest commit

### Deploy Client

```sh
bun run build
```

and then upload `build/` as a new deploy on netlify.

## Analytics

**Note:** PYQNow uses [Litlyx](https://litlyx.com) for minimal, privacy-respecting analytics to enhance your experience and help us make continuous improvements to the platform.
