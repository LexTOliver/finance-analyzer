import pandas as pd
from pathlib import Path
from src.utils.logger import get_logger

# -- Get the logger
logger = get_logger()


def extract_data(file_path: Path) -> dict:
    """
    Extract data from a table-like file.

    Parameters:
        file_path - Path: Path of the file

    Returns:
        dict: Data extracted from the file
    """
    try:
        # -- Read the file based on the file extension
        df = {}
        match file_path.suffix:
            case ".csv":
                df = pd.read_csv(file_path).to_dict()
            case ".xlsx" | ".xls" | ".xlsm" | ".xlsb":
                df = pd.read_excel(file_path).to_dict()
    except pd.errors.ParserError as e:
        logger.error(f"Error parsing the file: {e}")
    return df
