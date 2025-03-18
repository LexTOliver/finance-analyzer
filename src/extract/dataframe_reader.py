import pandas as pd
from pathlib import Path


def extract_data(file_path: Path) -> list[pd.DataFrame]:
    '''
    Extract data from a file and return a DataFrame.
    
    Parameters:
        file_path (Path): Path of the file
        
    Returns:
        pd.DataFrame | None: DataFrame with data from file; None if occurs an error
    '''
    try:
        # -- Read the file based on the file extension
        df = None
        match file_path.suffix:
            case ".csv":
                df = pd.read_csv(file_path)
            case ".xlsx" | ".xls" | ".xlsm" | ".xlsb": 
                df = pd.read_excel(file_path)
            case ".json":
                df = pd.read_json(file_path)
    except pd.errors.ParserError as e:
        # TODO: Add logger configuration with logging
        print(f"Error reading the file: {e}")
    except Exception as e:
        print(f"Some error occurred: {e}")
    return [df]
