import json
import pytest
import streamlit.testing.v1 as stt
from pathlib import Path
from src.pages.file_upload import page_setup


# -- Fixtures for testing --
@pytest.fixture
def sample_json(tmp_path: Path) -> Path:
    """
    Creates a valid JSON file for testing.

    Parameters:
        tmp_path - Path : Pytest fixture for creating temporary files.

    Returns:"
        Path: Path to the created JSON file.
    """
    # -- Set the file path
    file = tmp_path / "sample.json"

    # -- Write JSON data to the file
    file.write_text(json.dumps({"name": "Alice", "age": 30}))

    return file


# -- Tests --
# TODO: Not working yet due to the lack of support for the file uploader.
#       Add tests for the file uploader when supported.
@pytest.mark.skip
def test_file_upload_ui(sample_json: Path) -> None:
    """
    Test the UI elements of the File Upload page.
    
    Parameters:
        sample_json - Path : Pytest fixture for a valid JSON file.
    """
    # -- Execute the AppTest on the page_setup function
    at = stt.AppTest.from_function(page_setup).run()

    # -- Check the page title
    assert "Upload File" in at.title

    # -- Check the file uploader
    # OBS: The test for the file uploader is not supported yet.
    # TODO: Add checks for the file uploader when supported

    # -- Check the checkbox for scanning PDF files
    assert "Scanned PDF file" in at.checkbox
    at.checkbox[0].check().run()
    assert at.checkbox[0].value is True