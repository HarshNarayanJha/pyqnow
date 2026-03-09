#!/usr/bin/env bash

set -euo pipefail

if [ $# -eq 0 ]; then
  echo "Usage: $0 <year_code> (i.e. SP2026)"
  exit 1
fi

INPUT_DIR="pyqs/$1/new"
OUTPUT_DIR="pyqs/$1"

# Check if directory exists
if [ ! -d "$INPUT_DIR" ]; then
  echo "Directory $INPUT_DIR not found"
  exit 1
fi

# Process each PDF
for pdf in "$INPUT_DIR"/*.pdf; do
  [ -e "$pdf" ] || continue

  filename=$(basename "$pdf" .pdf)

  # Compress
  echo "Compressing $pdf to ${INPUT_DIR}/${filename}_compressed.pdf"
  gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/ebook \
    -dNOPAUSE -dQUIET -dBATCH -sOutputFile="${INPUT_DIR}/${filename}_compressed.pdf" "$pdf"

  # # Run OCR
  echo "OCR'ing $pdf to ${INPUT_DIR}/${filename}_ocr.pdf"
  ocrmypdf "${INPUT_DIR}/${filename}_compressed.pdf" "${INPUT_DIR}/${filename}_ocr.pdf"

  # Move to output directory
  echo "Moving ${INPUT_DIR}/${filename}_ocr.pdf to $OUTPUT_DIR/${filename}.pdf"
  mv "${INPUT_DIR}/${filename}_ocr.pdf" "$OUTPUT_DIR/${filename}.pdf"
  rm "${INPUT_DIR}/${filename}_compressed.pdf"
done
