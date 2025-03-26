import streamlit as st


def page_setup() -> None:
    """
    Sets up the Home page.

    - Provides an overview of the app.
    """
    # -- Page title
    st.title("📊 Finance Analyzer")
    st.write(
        "Welcome to the Finance Analyzer! This app allows you to analyze your financial data."
    )
    st.divider()

    # -- Page content
    st.write("To start, upload your financial data file and then you can analyze it.")
    st.write(
        "* You can upload files with the following extensions: CSV, Excel, JSON, and PDF."
    )


page_setup()
