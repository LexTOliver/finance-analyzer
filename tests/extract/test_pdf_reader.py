import pytest
from fpdf import FPDF
from pathlib import Path
from PIL import Image, ImageDraw
from src.extract.pdf_reader import extract_data


# -- Fixtures for testing --
@pytest.fixture
def sample_pdf(tmp_path: Path) -> Path:
    """
    Creates a sample PDF file with text for testing.

    Parameters:
        tmp_path - Path: Path to the temporary directory

    Returns:
        Path: Path to the sample PDF file
    """
    # -- Set the file path
    file = tmp_path / "sample.pdf"

    # -- Create a PDF file with text
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="This is a test PDF file.", ln=True, align="C")
    pdf.output(str(file))

    return file


@pytest.fixture
def sample_empty_pdf(tmp_path: Path) -> Path:
    """
    Creates an empty PDF file for testing.

    Parameters:
        tmp_path - Path: Path to the temporary directory

    Returns:
        Path: Path to the empty PDF file
    """
    # -- Set the file path
    file = tmp_path / "empty.pdf"

    # -- Create an empty PDF file
    pdf = FPDF()
    pdf.add_page()
    pdf.output(str(file))
    return file


@pytest.fixture
def sample_scanned_pdf(tmp_path: Path) -> Path:
    """
    Creates a sample scanned PDF (text as image) for OCR testing.

    Parameters:
        tmp_path - Path: Path to the temporary directory

    Returns:
        Path: Path to the scanned PDF file
    """
    # -- Set the file path
    file = tmp_path / "scanned.pdf"

    # -- Create an image with text
    img = Image.new("RGB", (400, 200), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    draw.text((50, 80), "Scanned Text", fill=(0, 0, 0))

    img_path = tmp_path / "text_image.png"
    img.save(img_path)

    # -- Create a PDF file with the image
    pdf = FPDF()
    pdf.add_page()
    pdf.image(str(img_path), x=10, y=10, w=100)
    pdf.output(str(file))

    return file


@pytest.fixture
def sample_pdf_with_table(tmp_path: Path) -> Path:
    """
    Creates a sample PDF file with a table for testing.

    Parameters:
        tmp_path - Path: Path to the temporary directory

    Returns:
        Path: Path to the sample PDF file with a table
    """
    # -- Set the file path
    file = tmp_path / "sample_table.pdf"

    # -- Create a PDF file with a table
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt="Table in PDF", ln=True, align="C")
    pdf.set_font("Arial", size=10)

    # Define table headers and rows
    headers = ["col1", "col2"]
    rows = [["1", "2"], ["3", "4"]]

    # Add headers
    for header in headers:
        pdf.cell(40, 10, txt=header, border=1, align="C")
    pdf.ln()

    # Add rows
    for row in rows:
        for cell in row:
            pdf.cell(40, 10, txt=cell, border=1, align="C")
        pdf.ln()

    pdf.output(str(file))

    return file


# -- Tests --
def test_extract_pdf(sample_pdf) -> None:
    """
    Tests text extraction from a normal PDF.

    Parameters:
        sample_pdf - Path: Path to the sample PDF file
    """
    # -- Extract data from the PDF file
    extracted_data = extract_data(sample_pdf, scan=False)

    # -- Check the extracted data
    assert "texts" in extracted_data
    assert isinstance(extracted_data["texts"], dict)
    assert len(extracted_data["texts"]) > 0  # Must have at least one page
    assert any(
        text.strip() for text in extracted_data["texts"].values()
    )  # Text must not be empty


def test_extract_empty_pdf(sample_empty_pdf) -> None:
    """
    Tests extraction from an empty PDF file.

    Parameters:
        sample_empty_pdf - Path: Path to the empty PDF file
    """
    # -- Extract data from the PDF file
    extracted_data = extract_data(sample_empty_pdf, scan=False)

    # -- Check the extracted data
    assert extracted_data == {}


def test_extract_scanned_pdf(sample_scanned_pdf) -> None:
    """
    Tests OCR extraction from a scanned PDF.

    Parameters:
        sample_scanned_pdf - Path: Path to the scanned PDF file
    """
    # -- Extract data from the PDF file
    extracted_data = extract_data(sample_scanned_pdf, scan=True)

    # -- Check the extracted data
    assert "texts" in extracted_data
    assert isinstance(extracted_data["texts"], dict)
    assert len(extracted_data["texts"]) > 0  # At least one page
    assert any(
        text.strip() for text in extracted_data["texts"].values()
    )  # Text must not be empty


def test_extract_pdf_with_table(sample_pdf_with_table) -> None:
    """
    Tests table extraction from a PDF file.

    Parameters:
        sample_pdf_with_table - Path: Path to the PDF file with a table
    """
    # -- Extract data from the PDF file
    extracted_data = extract_data(sample_pdf_with_table, scan=False)

    # -- Check the extracted data
    assert "texts" in extracted_data
    assert "tables" in extracted_data
    assert isinstance(extracted_data["texts"], dict)
    assert isinstance(extracted_data["tables"], dict)
    assert len(extracted_data["texts"]) > 0  # At least one page
    assert any(
        text.strip() for text in extracted_data["texts"].values()
    )  # Text must not be empty
    assert len(extracted_data["tables"]) > 0  # At least one table
    assert any(
        table for table in extracted_data["tables"].values()
    )  # Table must not be empty
