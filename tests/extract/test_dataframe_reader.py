import pytest
import pandas as pd
from pathlib import Path
from src.extract.dataframe_reader import extract_data


# -- Fixtures for the tests --
@pytest.fixture
def sample_csv(tmp_path: Path) -> Path:
    """
    Creates a temporary CSV file for testing.

    Parameters:
        tmp_path - Path: Temporary directory path

    Returns:
        file - Path: Path to the sample CSV file
    """
    # -- Set the file path
    file = tmp_path / "sample.csv"

    # -- Write data to the file
    file.write_text("col1,col2\n1,2\n3,4")
    return file


@pytest.fixture
def sample_excel(tmp_path: Path) -> Path:
    """
    Creates a temporary Excel file for testing.

    Parameters:
        tmp_path - Path: Temporary directory path

    Returns:
        file - Path: Path to the sample
    """
    # -- Set the file path
    file = tmp_path / "sample.xlsx"

    # -- Write data to the file
    df = pd.DataFrame({"col1": [1, 3], "col2": [2, 4]})
    df.to_excel(file, index=False)
    return file


@pytest.fixture
def empty_csv(tmp_path: Path) -> Path:
    """
    Creates an empty CSV file for testing.

    Parameters:
        tmp_path - Path: Temporary directory path

    Returns:
        file - Path: Path to the empty CSV file
    """
    # -- Set the file path
    file = tmp_path / "empty.csv"

    # -- Write data to the file
    file.write_text("")
    return file


@pytest.fixture
def corrupted_csv(tmp_path: Path) -> Path:
    """
    Creates a corrupted CSV file for testing.

    Parameters:
        tmp_path - Path: Temporary directory path

    Returns:
        file - Path: Path to the corrupted CSV file
    """
    # -- Set the file path
    file = tmp_path / "corrupted.csv"

    # -- Write data to the file
    file.write_text("col1,col2\n1,2\n3,,,,")
    return file


# -- Tests --
def test_extract_csv(sample_csv) -> None:
    """
    Tests CSV extraction.

    Parameters:
        sample_csv - Path: Path to the sample CSV file
    """
    # -- Extract data
    extracted_data = extract_data(sample_csv)

    # -- Check the extracted data
    assert isinstance(extracted_data, dict)
    assert "col1" in extracted_data and "col2" in extracted_data
    assert extracted_data["col1"] == {0: 1, 1: 3}
    assert extracted_data["col2"] == {0: 2, 1: 4}


def test_extract_excel(sample_excel) -> None:
    """
    Tests Excel extraction.

    Parameters:
        sample_excel - Path: Path to the sample Excel file
    """
    # -- Extract data
    extracted_data = extract_data(sample_excel)

    # -- Check the extracted data
    assert isinstance(extracted_data, dict)
    assert "col1" in extracted_data and "col2" in extracted_data
    assert extracted_data["col1"] == {0: 1, 1: 3}
    assert extracted_data["col2"] == {0: 2, 1: 4}


def test_extract_empty_csv(empty_csv, caplog) -> None:
    """
    Tests extraction of an empty CSV file.

    Parameters:
        empty_csv - Path: Path to the empty CSV file
        caplog - pytest fixture: Capture log messages
    """
    # -- Extract data
    extracted_data = extract_data(empty_csv)

    # -- Check the extracted data
    assert extracted_data == {}

    # -- Check the log message
    assert "Empty file" in caplog.text


def test_extract_corrupted_csv(corrupted_csv, caplog) -> None:
    """
    Tests extraction of a corrupted Excel file.

    Parameters:
        corrupted_excel - Path: Path to the corrupted Excel file
        caplog - pytest fixture: Capture log messages
    """
    # -- Extract data
    extracted_data = extract_data(corrupted_csv)

    # -- Check the extracted data
    assert extracted_data == {}

    # -- Check the log message
    assert "Error parsing the file" in caplog.text
