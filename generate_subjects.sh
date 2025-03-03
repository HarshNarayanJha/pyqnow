#!/bin/bash

# Check if the required Python scripts exist
if [ ! -f "scripts/bit_links.py" ]; then
    echo "Error: scripts/bit_links.py does not exist."
    exit 1
fi

if [ ! -f "scripts/branch_gen.py" ]; then
    echo "Error: scripts/branch_gen.py does not exist."
    exit 1
fi
# Check if UV is installed
if ! command -v uv &> /dev/null; then
    echo "UV not found, using python3 instead"
    python3 scripts/bit_links.py
    python3 scripts/branch_gen.py
else
    uv run scripts/bit_links.py
    uv run scripts/branch_gen.py
fi
