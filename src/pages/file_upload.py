import streamlit as st
from pathlib import Path
from io import BytesIO
from src.extract.extractor import DataExtractor


def page_setup() -> None:
    """
    Sets up the file upload page.

    - Allows users to upload financial reports in CSV, Excel, JSON, or PDF format.
    - If a PDF is scanned, enables OCR processing.
    - Extracts and displays text and tables from the uploaded document.
    """
    # -- Page title
    st.title("Upload File")
    st.write("Upload your file to start analyzing your financial data.")

    # -- File uploader
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=["csv", "xlsx", "xls", "xlsm", "xlsb", "json", "pdf"],
        accept_multiple_files=False,
        label_visibility="hidden",
    )

    # -- Checkbox for scanning PDF files
    # TODO: Add advanced configuration options for the extractor
    scan_pdf = st.checkbox("Scanned PDF file")

    # -- Check if the file was uploaded
    if uploaded_file:
        st.success("File uploaded successfully!")
        st.divider()

        # -- Extract data from the file
        config = {"scan": scan_pdf}
        extractor = process_uploaded_file(uploaded_file, config)

        # -- Show the file content
        st.header("File Content")
        if extractor.data:
            show_extracted_content(extractor)
        else:
            st.error("No data extracted from the file.")


def process_uploaded_file(uploaded_file: BytesIO, config: dict) -> DataExtractor:
    """
    Process the uploaded file and extract data from it.

    Parameters:
        uploaded_file - BytesIO: Uploaded file
        config - dict: Configuration for the extractor

    Returns:
        DataExtractor: Extractor object with the extracted data
    """
    # TODO: Save the file in a temporary folder defined in the config file
    # -- Extract data from the file
    file_path = Path("data/upload") / uploaded_file.name
    file_path.write_bytes(uploaded_file.getvalue())
    extractor = DataExtractor(file_path, config)

    return extractor


def show_extracted_content(extractor: DataExtractor) -> None:
    """
    Show the extracted content from the file.

    Parameters:
        extractor - DataExtractor: Extractor object with the extracted data
    """
    # -- Show the file content
    if extractor.file_format == "pdf":
        for page, text in extractor.data["texts"].items():
            st.subheader(f"Page {page + 1}")
            st.write(text)
            if "tables" in extractor.data and extractor.data["tables"]:
                st.write(extractor.data["tables"][page])
    else:
        st.dataframe(extractor.data)


page_setup()
