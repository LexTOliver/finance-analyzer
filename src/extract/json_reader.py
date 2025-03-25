import json
from pathlib import Path
from src.utils.logger import get_logger

# -- Get logger
logger = get_logger()


def extract_data(file_path: Path) -> dict:
    """
    Extract data from JSON file.

    Parameters:
        file_path - Path : Path to JSON file.

    Returns:
        dict: Dictionary with data from JSON file
    """
    data_json = {}

    try:
        # -- Open and read JSON file
        with open(file_path, "r", encoding="utf-8") as f:
            data_json = json.load(f)
    except json.JSONDecodeError as e:
        logger.error(f"Failed to decode JSON from the file {file_path}: {e}")

    return data_json
