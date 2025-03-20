import pandas as pd
import pdfplumber
import pytesseract
from pdf2image import convert_from_path
from pathlib import Path


def extract_data(pdf_path: Path, scan: bool) -> dict:
    """
    Extract the text from a PDF file.

    Parameters:
        pdf_path - Path: Path to the PDF file
        scan - bool: Flag to indicate if the PDF file is scanned

    Returns:
        dict: Dictionary with the text and tables extracted from the PDF file
    """
    # -- Read the PDF file based on the scan flag
    return _read_scanned_pdf(pdf_path) if scan else _read_pdf(pdf_path)


def _read_scanned_pdf(file_path: Path) -> dict:
    """
    Read scanned PDF file and get the text data.

    Parameters:
        file_path - Path: Path to the PDF file

    Returns:
        dict: Text data from the file
    """
    # -- Get images from PDF conversion
    images = convert_from_path(file_path)

    # -- Get text from the images
    texts = {}
    for idx, img in enumerate(images):
        texts[idx] = pytesseract.image_to_string(img)

    return {"texts": texts}


def _read_pdf(file_path: Path) -> dict:
    """
    Read PDF file and get text data and tables.

    Parameters:
        file_path - Path: Path to the PDF file

    Returns:
        dict: Text data and tables from the file
    """
    # -- Open the file and read data
    texts = {}
    tables = {}
    with pdfplumber.open(file_path) as pdf:
        for i, page in enumerate(pdf.pages):
            # -- Extract text from the page
            texts[i] = page.extract_text()
            # -- Extract tables from the page
            for table in page.extract_tables():
                df_table = pd.DataFrame(table[1:], columns=table[0])
                tables[i] = df_table.to_dict()

    return {"texts": texts, "tables": tables} if texts or tables else {}
