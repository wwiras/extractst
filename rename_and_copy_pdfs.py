import os
import sys
import shutil
import pandas as pd


# Function to extract the actual file path from the Mendeley file URL
# def extract_file_path(file_url):
#     # Assuming the file URL is in the format:
#     # ":Users/wwiras/Library/Application Support/Mendeley Desktop/Downloaded/filename.pdf:pdf"
#     return '/'+file_url.split(':')[1] if ':' in file_url else file_url

# Function to extract the actual file path from the Mendeley file URL
def extract_file_path(file_url):
    # Assuming the file URL is in the format:
    # ":Users/wwiras/Library/Application Support/Mendeley Desktop/Downloaded/filename.pdf:pdf"
    file_path = file_url.split(':')[1] if ':' in file_url else file_url
    if '/' in file_path:
        # Linux/Unix file path
        file_path = '/' + file_path if not file_path.startswith('/') else file_path
    elif '\\' in file_path:
        # Windows file path
        file_path = 'C:\\' + file_path if not (file_path[1] == ':' and file_path[2] == '\\') else file_path
    return file_path


# Function to rename and copy PDFs based on worksheet
def rename_and_copy_pdfs_based_on_worksheet(worksheet_file):
    # Create a new directory named 'papers'
    output_directory = 'papers'
    os.makedirs(output_directory, exist_ok=True)

    # Load the Excel worksheet
    df = pd.read_excel(worksheet_file, sheet_name='Paper_Metadata')

    for _, row in df.iterrows():
        number = row['Number']
        file_url = row['File URL']

        if pd.isna(file_url):
            print(f"No file URL for entry {number}")
            continue

        file_path = extract_file_path(file_url)

        if not os.path.exists(file_path):
            print(f"File not found: {file_path}")
            continue

        new_filepath = os.path.join(output_directory, f"{number}.pdf")
        shutil.copy(file_path, new_filepath)
        print(f"Copied: {file_path} -> {new_filepath}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python rename_and_copy_pdfs.py <worksheet_file>")
        sys.exit(1)

    worksheet_file = sys.argv[1]

    if not worksheet_file.endswith(".xlsx"):
        print("No .xlsx file specified")
        sys.exit(1)
    else:
        rename_and_copy_pdfs_based_on_worksheet(worksheet_file)
