from pathlib import Path
from src.extract.pdf_reader import extract_data as extract_from_pdf
from src.extract.dataframe_reader import extract_data as extract_from_dataframe
from src.extract.json_reader import extract_data as extract_from_json
from src.utils.logger import get_logger

# -- Get the logger
logger = get_logger()


class DataExtractor:
    """
    Class responsible for extracting data from files.

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

    Methods:
        extract: Extract data from the file
        validate_config: Validate the configuration based on the file format
    """

    def __init__(self, file_path: Path, config: dict) -> None:
        """
        Initialize the DataExtractor class.

        Parameters:
            file_path - Path: Path to the file
            config - dict: Configuration for the extractor
        """
        # -- Set the file path and format
        self.file_path = file_path
        self.file_format = file_path.suffix[1:]

        # -- Validate the configuration and set it
        self.validate_config()
        self.config = config

        # -- Extract data from the file
        self.data = self.extract()

    def validate_config(self) -> None:
        """
        Validate the configuration based on the file format.
        """
        # TODO: Add more configurations for the extractor
        # -- Validation for PDF files
        # if self.file_format == "pdf":
        #     assert "scan" in self.config, "Scan flag is required for PDF files"
        #     assert isinstance(self.config["scan"], bool), "Scan flag must be a boolean"

        # -- Validation for CSV files
        # elif self.file_format == "csv":

        # -- Validation for Excel files
        # elif self.file_format in ["xlsx", "xls", "xlsm", "xlsb"]:

        # -- Validation for JSON files
        # elif self.file_format == "json":
        logger.debug(f"Configuration validated for {self.file_format} file")

    def extract(self) -> dict:
        """
        Extract data from the file.

        Returns:
            dict: Data extracted from the file with text and tables
        """
        # -- Check if the file exists
        if not self.file_path.exists():
            logger.error(f"File not found: {self.file_path}")
            raise FileNotFoundError(f"File not found: {self.file_path}")

        # -- Extract data based on the file format
        extracted_data = {}
        try:
            if self.file_format == "pdf":
                extracted_data = extract_from_pdf(self.file_path, self.config["scan"])
            elif self.file_format in ["csv", "xlsx", "xls", "xlsm", "xlsb"]:
                extracted_data = extract_from_dataframe(self.file_path)
            elif self.file_format == "json":
                extracted_data = extract_from_json(self.file_path)
            else:
                raise ValueError(f"File format not supported: {self.file_format}")
        except Exception as e:
            logger.error(f"Error extracting data from {self.file_path}: {e}")
            raise RuntimeError(f"Error extracting data from {self.file_path}: {e}")

        if extracted_data:
            logger.info(f"Data extracted from {self.file_path}")

        return extracted_data
