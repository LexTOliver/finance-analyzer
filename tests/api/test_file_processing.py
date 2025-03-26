import pytest
from fpdf import FPDF
from pathlib import Path
from src.api.file_processing import process_uploaded_file


@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    """
    Create a sample CSV file for testing.
    
    Parameters:
        tmp_path - Path: Temporary directory path
    
    Returns:
        Path: Path to the sample CSV file
    """
    # -- Set file path
    sample_csv = tmp_path / "sample.csv"

    # -- Write sample CSV data
    sample_csv.write_text("Name, Age\nAlice, 25\nBob, 30")

    return sample_csv


@pytest.fixture
def sample_pdf(tmp_path: Path) -> Path:
    """
    Create a sample PDF file for testing.
    
    Parameters:
        tmp_path - Path: Temporary directory path
    
    Returns:
        Path: Path to the sample PDF file
    """
    # -- Set file path
    sample_pdf = tmp_path / "sample.pdf"

    # -- Create a PDF file
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Sample PDF file", ln=True, align="C")
    pdf.output(sample_pdf)

    return sample_pdf

# TODO: Not working yet, because of the BytesIO object
# The FileUploader object from Streamlit returns a UploadedFile object, which is a BytesIO object
# We need to mock this object to test the process_uploaded_file function
# This is a more complex process, and we will cover it in a future moment
@pytest.mark.skip
def test_process_uploaded_file(sample_csv, sample_pdf) -> None:
    """
    Tests file processing from Streamlit UI.
    
    Parameters:
        sample_csv - Path: Path to the sample CSV file
        sample_pdf - Path: Path to the sample PDF file
    """
    # -- Test CSV file
    csv_extractor = process_uploaded_file(sample_csv, config={"scan": False})
    assert csv_extractor.file_format == "csv"
    assert isinstance(csv_extractor.data, dict)
    
    # -- Test PDF file
    pdf_extractor = process_uploaded_file(sample_pdf, config={"scan": False})
    assert pdf_extractor.file_format == "pdf"
    assert isinstance(pdf_extractor.data, dict)
    