import sys
import os
import bibtexparser
import pandas as pd


# Function to extract data from BibTeX file and save as CSV
def extract_bibtex_to_csv(bibtex_file, output_csv):
    with open(bibtex_file, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    entries = bib_database.entries

    # Create a DataFrame with the desired columns
    data = []
    for i, entry in enumerate(entries, start=1):
        number = f"F{i:03d}"
        title = entry.get('title', 'N/A').strip('{}')
        journal = entry.get('journal', 'N/A')
        year = entry.get('year', 'N/A')
        authors = entry.get('author', 'N/A')
        authors_initial = entry.get('ID', 'N/A')
        abstract = entry.get('abstract', 'N/A')
        file_url = entry.get('file', 'N/A')  # Assuming the file URL is stored in the 'file' field
        data.append([number, title, journal, year, authors, authors_initial, abstract, file_url])

    df = pd.DataFrame(data, columns=["Number", "Title", "Journal", "Year", "Authors", "Authors Initial", "Abstract",
                                     "File URL"])

    # Save the DataFrame to a CSV file
    df.to_csv(output_csv, index=False)
    print(f"CSV file saved as {output_csv}")


# Function to convert CSV to Excel
def convert_csv_to_excel(csv_file, output_excel):
    df = pd.read_csv(csv_file)
    df.to_excel(output_excel, sheet_name='Paper_Metadata', index=False)
    print(f"Excel file saved as {output_excel}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python create_worksheet.py <input_bibtex_file> <output_excel_file>")
        sys.exit(1)

    bibtex_file = sys.argv[1]
    output_excel = sys.argv[2]
    output_csv = 'temp_output.csv'  # temporary CSV file for intermediate step

    if not bibtex_file.endswith(".bib"):
        print("No .bib file specified")
        sys.exit(1)
    elif not output_excel.endswith(".xlsx"):
        print("No .xlsx file specified")
        sys.exit(1)
    else:
        extract_bibtex_to_csv(bibtex_file, output_csv)
        convert_csv_to_excel(output_csv, output_excel)
        os.remove(output_csv)  # clean up the temporary CSV file
