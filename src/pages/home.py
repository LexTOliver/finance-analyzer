import streamlit as st


def page_setup() -> None:
    """
    Home page setup.
    """
    # -- Page title
    st.title("📊 Finance Analyzer")
    st.write(
        "Welcome to the Finance Analyzer! This app allows you to analyze your financial data."
    )

    # -- Page content
    st.write("To start, upload your financial data file and then you can analyze it.")
    st.write(
        "You can upload files with the following extensions: CSV, Excel, JSON, and PDF."
    )
    st.write("For PDF files, you can also scan them to extract the text data.")


page_setup()
