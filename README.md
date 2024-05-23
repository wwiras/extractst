# extractst
The purpose of this repo is to assist on how to prepare journals or research papers for softwaretheses version 2

# PDF Metadata Extractor and Renamer

This repository contains two Python scripts to automate the extraction of metadata from BibTeX files and renaming PDF files based on the extracted metadata. The process involves creating an Excel worksheet with the metadata and then using this worksheet to rename and copy the PDF files into a new directory.

## Prerequisites

- Python 3.6 or higher
- Install the required packages:
  ```bash
  pip install -r requirements.txt
- Make sure you export bibtex from Mendeley Desktop and all the files
are downloaded or uploaded to this Mendeley Desktop. Trust me. 
You will thank me due to this automated process. 

## Scripts
1. create_worksheet.py
- This script extracts data from a BibTeX file and creates an Excel worksheet with the necessary metadata.
  ```bash
  python create_worksheet.py <input_bibtex_file> <output_excel_file>
  
- Example
  ```bash
  python create_worksheet.py my_references.bib output.xlsx
  
2. rename_and_copy_pdfs.py
- This script renames and copies PDF files based on the metadata in the Excel worksheet.
  ```bash
  python rename_and_copy_pdfs.py <worksheet_file>
- Example
  ```bash
  python rename_and_copy_pdfs.py output.xlsx

## Details
### The create_worksheet.py script will:
- Extract metadata from the provided BibTeX file.
- Save the extracted data as a temporary CSV file.
- Convert the CSV file to an Excel worksheet.
- Clean up the temporary CSV file.

### The rename_and_copy_pdfs.py script will:
- Create a new directory named papers.
- Load the Excel worksheet.
- Extract the actual file paths from the Mendeley file URLs.
- Check if the file paths correspond to Linux/Unix or Windows systems and adjust the paths accordingly.
- Rename and copy the PDF files into the papers directory based on the extracted metadata.
