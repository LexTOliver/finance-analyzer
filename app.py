"""
This file contains the main code for the Streamlit app.
"""

import streamlit as st


# Setting the pages
pages = [
    st.Page("src/pages/home.py", title="Finance Analyzer", icon="📊"),
    st.Page("src/pages/file_upload.py", title="Upload File", icon="📂"),
    # st.Page("src/pages/analysis.py", title="Analysis", icon="📈"),
]

# Running the app
pg = st.navigation(pages)
st.set_page_config(page_title="Finance Analyzer", page_icon="💰", layout="wide")
pg.run()
