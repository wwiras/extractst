# extractst
The purpose of this repo is to assist on how to prepare journals or research papers for softwaretheses version 2

# PDF Metadata Extractor and Renamer

This repository contains two Python scripts to automate the extraction of metadata from BibTeX files and renaming PDF files based on the extracted metadata. The process involves creating an Excel worksheet with the metadata and then using this worksheet to rename and copy the PDF files into a new directory.

## Prerequisites

- Python 3.6 or higher
- Install the required packages:
  ```bash
  pip install bibtexparser pandas openpyxl PyPDF2
- Make sure you export bibtex from Mendeley Desktop and all the files
are downloaded or uploaded to this Mendeley Desktop. Trust me. 
You will thank me due to this automated process. 

## Scripts
1. create_worksheet.py
- This script extracts data from a BibTeX file and creates an Excel worksheet with the necessary metadata.
```bash
python create_worksheet.py <input_bibtex_file> <output_excel_file>
