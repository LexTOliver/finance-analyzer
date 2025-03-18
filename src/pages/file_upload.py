import streamlit as st
from pathlib import Path
from src.extract.extractor import DataExtractor

def page_setup() -> None:
    '''
    File upload page setup.
    '''
    # -- Page title
    st.title("Upload File")
    st.write("Upload your file to start analyzing your financial data.")
    
    # -- File uploader
    uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "xls", "xlsm", "xlsb", "json", "pdf"])

    # -- Checkbox for scanning PDF files
    scan_pdf = st.checkbox("Scanned PDF file")
    
    # -- Check if the file was uploaded
    if uploaded_file is not None:
        st.write("File uploaded successfully!")
        
        # -- Extract data from the file
        file_path = Path(uploaded_file.name)
        file_path.write_bytes(uploaded_file.getvalue())
        extractor = DataExtractor(file_path, {"scan": scan_pdf})

        # -- Show the file content
        st.header("File Content")
        if extractor.data:
            if "texts" in extractor.data:
                for page, text in extractor.data["texts"].items():
                    # st.write(f"Page {page + 1}")
                    st.write(text)
            if "tables" in extractor.data:
                for table in extractor.data["tables"]:
                    st.dataframe(table)
        else:
            st.write("No data extracted from the file.")

    else:
        st.write("Please upload a file to start analyzing your financial data.")

page_setup()