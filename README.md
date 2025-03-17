# 📊 Financial Report Analyzer

## 📝 Project Description
This project is an LLM-based application for automated financial and business report analysis. It allows data extraction from different files, generates insights using Large Language Models (LLMs) with **LangChain** and **OpenAI API**, and visualizes key metrics through an interactive **Streamlit** interface.

## 🚀 Technologies Used
- **Python 3.10+**
- **Streamlit** (interactive interface)
- **Pandas** (data manipulation)
- **LangChain + OpenAI API** (financial insights generation)
- **pdfplumber** (PDF text extraction)
- **Matplotlib / Plotly** (data visualization)
- **pytest** (automated testing)

## 📂 Project Structure
```
finance-analyzer/
│── src/
│   ├── app.py              # Main application (Streamlit)
│   ├── extract/            # Data extraction
│   ├── analysis/           # Financial processing and analysis
│   ├── models/             # AI models and processing
│   ├── api/                # Internal APIs for processing
│   ├── visualization/      # Graph and report generation
│   ├── config/             # Project configurations
│── tests/                  # Automated tests
│── data/                   # Directory for input files
│── pyproject.toml          # Dependency management
│── README.md               # Project documentation
```

## 🛠️ Setting Up the Environment
### With Astral UV
```bash
uv venv
source .venv/bin/activate
uv sync
```

### With Pip
```bash
pip install -r requirements.txt
```

## ▶️ Running the Project
After installing the dependencies, run the following command:
```bash
streamlit run src/app.py
```
Streamlit will open the interface in your browser.

## 🧪 Running Tests
TODO: Add instructions for running tests

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
