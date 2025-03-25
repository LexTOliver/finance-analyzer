import pytest
import json
from pathlib import Path
from src.extract.json_reader import extract_data


# -- Fixtures for testing --
@pytest.fixture
def sample_json(tmp_path: Path) -> Path:
    """
    Creates a valid JSON file for testing.

    Parameters:
        tmp_path - Path : Pytest fixture for creating temporary files.

    Returns:
        Path: Path to the created JSON file.
    """
    # -- Set the file path
    file = tmp_path / "sample.json"

    # -- Write JSON data to the file
    file.write_text(json.dumps({"name": "Alice", "age": 30}))

    return file


@pytest.fixture
def malformed_json(tmp_path: Path) -> Path:
    """
    Creates a malformed JSON file for testing.

    Parameters:
        tmp_path - Path : Pytest fixture for creating temporary files.

    Returns:
        Path: Path to the created JSON file.
    """
    # -- Set the file path
    file = tmp_path / "malformed.json"

    # -- Write invalid JSON data to the file
    file.write_text("{name: Alice, age: 30}")

    return file


@pytest.fixture
def empty_json(tmp_path: Path) -> Path:
    """
    Creates an empty JSON file for testing.

    Parameters:
        tmp_path - Path : Pytest fixture for creating temporary files.

    Returns:
        Path: Path to the created JSON file.
    """
    # -- Set the file path
    file = tmp_path / "empty.json"

    # -- Create an empty file
    file.write_text("")
    return file


# -- Tests --
def test_extract_valid_json(sample_json) -> None:
    """
    Tests JSON extraction with a valid file.

    Parameters:
        sample_json - Path : Path to a valid JSON file.
    """
    # -- Extract data from the JSON file
    extracted_data = extract_data(sample_json)

    # -- Check if the extracted data is correct
    assert isinstance(extracted_data, dict)
    assert "name" in extracted_data
    assert extracted_data["name"] == "Alice"
    assert extracted_data["age"] == 30


def test_extract_malformed_json(malformed_json, caplog) -> None:
    """
    Tests JSON extraction from a malformed file.

    Parameters:
        malformed_json - Path : Path to a malformed JSON file.
        caplog - pytest fixture for capturing log messages.
    """
    # -- Extract data from the malformed JSON file
    extracted_data = extract_data(malformed_json)

    # -- Check if the extracted data is correct
    assert extracted_data == {}  # Must return an empty dictionary

    # -- Check if the error message was logged
    assert "Failed to decode JSON" in caplog.text


def test_extract_empty_json(empty_json) -> None:
    """
    Tests extraction from an empty JSON file.

    Parameters:
        empty_json - Path : Path to an empty JSON file.
    """
    # -- Extract data from the empty JSON file
    extracted_data = extract_data(empty_json)

    # -- Check if the extracted data is correct
    assert extracted_data == {}
