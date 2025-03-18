from pathlib import Path
from src.extract.pdf_reader import extract_data as extract_from_pdf
from src.extract.dataframe_reader import extract_data as extract_from_dataframe

class DataExtractor:
    """
    Class responsible for extracting from files.
    
    Supported file formats:
    - CSV
    - Excel (xlsx, xls, xlsm, xlsb)
    - JSON
    - PDF

    Attributes:
        file_path - Path: Path to the file
        file_format - str: File format
        config - dict: Configuration for the extractor
        data - dict: Data extracted from the file (text and tables)
    """
    
    def __init__(self, file_path: Path, config: dict):
        '''
        Initialize the DataExtractor class.
        
        Parameters:
            file_path (Path): Path to the file
        '''
        self.file_path = file_path
        self.file_format = file_path.suffix[1:]
        # TODO: Add validation for the config based on the file format
        # TODO: Add more configurations for the extractor (for the dataframes)
        self.config = config
        self.data = self.extract()

    def extract(self) -> dict:
        '''
        Extract data from the file.
        
        Returns:
            dict: Data extracted from the file with text and tables
        '''
        # -- Check if the file exists
        if not self.file_path.exists():
            # TODO: Add logger configuration with logging
            raise FileNotFoundError(f"File not found: {self.file_path}")

        # -- Extract data based on the file format
        if self.file_format == "pdf":
            return extract_from_pdf(self.file_path, self.config["scan"])
        elif self.file_format in ["csv", "xlsx", "xls", "xlsm", "xlsb", "json"]:
            return {"tables": extract_from_dataframe(self.file_path)}
        else:
            raise ValueError(f"File format not supported: {self.file_format}")