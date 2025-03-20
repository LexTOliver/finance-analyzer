import streamlit as st
from pathlib import Path
from src.extract.extractor import DataExtractor


def page_setup() -> None:
    """
    File upload page setup.
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
    scan_pdf = st.checkbox("Scanned PDF file")

    # -- Check if the file was uploaded
    if uploaded_file:
        st.write("File uploaded successfully!")
        st.divider()

        # -- Extract data from the file
        # TODO: Save the file in a temporary folder defined in the config file
        file_path = Path("data/upload") / uploaded_file.name
        file_path.write_bytes(uploaded_file.getvalue())
        extractor = DataExtractor(file_path, {"scan": scan_pdf})

        # -- Show the file content
        st.header("File Content")
        if extractor.data:
            if extractor.file_format == "pdf":
                for page, text in extractor.data["texts"].items():
                    st.subheader(f"Page {page + 1}")
                    st.write(text)
                    if "tables" in extractor.data and extractor.data["tables"]:
                        st.write(extractor.data["tables"][page])
            else:
                st.dataframe(extractor.data)
        else:
            st.error("No data extracted from the file.")

    else:
        st.write("Please upload a file to start analyzing your financial data.")


page_setup()
