from pathlib import Path
from io import BytesIO
from src.extract.extractor import DataExtractor

def process_uploaded_file(uploaded_file: BytesIO, config: dict) -> DataExtractor:
    """
    Process the uploaded file and extract data from it.

    Parameters:
        uploaded_file - BytesIO: Uploaded file
        config - dict: Configuration for the extractor

    Returns:
        DataExtractor: Extractor object with the extracted data
    """
    # -- Save the uploaded file
    # TODO: Set the temp directory on a file with environment variables
    # TODO: Get the temp directory from the config saved in session state
    file_path = Path("data/temp") / uploaded_file.name
    file_path.write_bytes(uploaded_file.getvalue())
    
    # -- Extract data from the file
    extractor = DataExtractor(file_path, config)

    return extractor