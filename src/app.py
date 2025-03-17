import streamlit as st

def page_setup():
    '''
    Page setup
    '''
    st.title("📊 Finance Analyzer")
    st.write("Welcome to the Finance Analyzer! This app allows you to analyze your financial data.")

def main():
    page_setup()

if __name__ == "__main__":
    main()