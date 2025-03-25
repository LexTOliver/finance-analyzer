import pytest
import pandas as pd
from fpdf import FPDF
from pathlib import Path
from src.extract.extractor import DataExtractor


# -- Define the test data
@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    """
    Create a sample CSV file for testing.

    Parameters:
        tmp_path - Path: Temporary directory path

    Returns:
        file - Path: Path to the sample CSV file
    """
    # -- Set file path
    file = tmp_path / "sample.csv"

    # -- Write data to the file
    file.write_text("col1,col2\n1,2\n3,4")

    return file


@pytest.fixture
def sample_excel(tmp_path: Path) -> Path:
    """
    Create a sample Excel file for testing.

    Parameters:
        tmp_path - Path: Temporary directory path

    Returns:
        file - Path: Path to the sample Excel file
    """
    # -- Set file path
    file = tmp_path / "sample.xlsx"

    # -- Write data to the file
    df = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    df.to_excel(file, index=False)

    return file


@pytest.fixture
def sample_json(tmp_path: Path) -> Path:
    """
    Create a sample JSON file for testing.

    Parameters:
        tmp_path - Path: Temporary directory path

    Returns:
        file - Path: Path to the sample JSON file
    """
    # -- Set file path
    file = tmp_path / "sample.json"

    # -- Write data to the file
    file.write_text('{"name": "Alice", "age": 30}')

    return file


@pytest.fixture
def sample_pdf(tmp_path: Path) -> Path:
    """
    Create a sample PDF file for testing.

    Parameters:
        tmp_path - Path: Temporary directory path

    Returns:
        file - Path: Path to the sample PDF file
    """
    # -- Set file path
    file = tmp_path / "sample.pdf"

    # -- Write data to the file
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="This is a test PDF file.", ln=True, align="C")
    pdf.output(str(file))

    return file


@pytest.fixture
def sample_unsupported_format(tmp_path: Path) -> Path:
    """
    Create a sample txt file (unsupported file) for testing.

    Parameters:
        tmp_path - Path: Temporary directory path

    Returns:
        file - Path: Path to the sample txt file
    """
    # -- Set file path
    unsupported_file = tmp_path / "unsupported.txt"

    # -- Write data to the file
    unsupported_file.write_text("This is a test file.")

    return unsupported_file


# -- Test cases for the Extractor class
def test_extract_csv(sample_csv) -> None:
    """
    Test the extract method for CSV files.

    Parameters:
        sample_csv - Path: Path to the sample CSV file
    """
    # -- Initialize the Extractor class
    extractor = DataExtractor(sample_csv, {})

    # -- Check the extracted data
    # -- Assert extractor.data
    assert isinstance(extractor.data, dict)

    # -- Assert the file path
    assert extractor.file_path == sample_csv

    # -- Assert the file format
    assert extractor.file_format == "csv"


def test_extract_excel(sample_excel) -> None:
    """
    Test the extract method for Excel files.

    Parameters:
        sample_excel - Path: Path to the sample Excel file
    """
    # -- Initialize the Extractor class
    extractor = DataExtractor(sample_excel, {})

    # -- Check the extracted data
    # -- Assert extractor.data
    assert isinstance(extractor.data, dict)

    # -- Assert the file path
    assert extractor.file_path == sample_excel

    # -- Assert the file type
    assert extractor.file_format == "xlsx"


def test_extract_json(sample_json) -> None:
    """
    Test the extract method for JSON files.

    Parameters:
        sample_json - Path: Path to the sample JSON file
    """
    # -- Initialize the Extractor class
    extractor = DataExtractor(sample_json, {})

    # -- Check the extracted data
    # -- Assert extractor.data
    assert isinstance(extractor.data, dict)

    # -- Assert the file path
    assert extractor.file_path == sample_json

    # -- Assert the file type
    assert extractor.file_format == "json"


def test_extract_pdf(sample_pdf) -> None:
    """
    Test the extract method for PDF files.

    Parameters:
        sample_pdf - Path: Path to the sample PDF file
    """
    # -- Initialize the Extractor class
    extractor = DataExtractor(sample_pdf, {"scan": False})

    # -- Check the extracted data
    # -- Assert extractor.data
    assert isinstance(extractor.data, dict)
    assert "texts" in extractor.data
    assert len(extractor.data["texts"]) > 0

    # -- Assert the file path
    assert extractor.file_path == sample_pdf

    # -- Assert the file type
    assert extractor.file_format == "pdf"


def test_extract_unsupported_format(sample_unsupported_format) -> None:
    """
    Test the extract method for unsupported file formats.

    Parameters:
        sample_unsupported_format - Path: Path to the sample unsupported file
    """
    # -- Initialize the Extractor class and expect a ValueError
    with pytest.raises(ValueError, match="File format not supported: txt"):
        DataExtractor(sample_unsupported_format, {})


def test_extract_missing_file() -> None:
    """
    Test the extract method for a missing file.
    """
    # -- Create a non-existent file path
    missing_file = Path("non_existent_file.csv")

    # -- Initialize the Extractor class and expect a FileNotFoundError
    with pytest.raises(FileNotFoundError, match=f"File not found: {missing_file}"):
        DataExtractor(missing_file, {})
