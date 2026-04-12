# WSAA Coursework

This repository contains coursework for the **Web Scraping and API Analysis (WSAA)** course. It includes assignments and laboratory exercises that demonstrate practical applications of web scraping techniques, API integration, and data analysis using Python.

## Repository Structure

### Assignments (`assignments/`)
This folder contains completed assignment submissions:

- `assignment02-carddraw.ipynb` - Card drawing simulation and analysis
- `assignment03-cso.ipynb` - Central Statistics Office (CSO) data analysis
- `assignment04-github.py` - GitHub API integration and repository management
- `config.py` - API keys and configuration settings
- `cso.json` - CSO data in JSON format
- `file.txt` - Sample text file for GitHub API demonstration

### Labs (`labs/`)
This folder contains laboratory exercises and data files:

- `Lab2_Data.ipynb` - CSV data processing and analysis
- `Lab2_Trains.ipynb` - Train data analysis and visualization
- `lab4_api.ipynb` - API integration examples (HTML to PDF, GitHub API)
- `config.py` - API keys and configuration settings
- `data.csv` - Sample dataset for data analysis
- `repo_info.json` - GitHub repository information (JSON format)
- `repo_info_contents.json` - Repository contents data
- `trainxml.xml` - Train data in XML format
- `week03_train.csv` - Weekly train schedule data
- `document.pdf` - Generated PDF document from API

## Prerequisites

To run the code in this repository, you'll need:

- Python 3.7+
- Required Python packages:
  - `requests` (for API calls)
  - `PyGithub` (for GitHub API)
  - `pandas` (for data analysis)
  - `matplotlib` / `seaborn` (for visualizations)

Install dependencies using:
```bash
pip install requests PyGithub pandas matplotlib seaborn
```

## Configuration

1. Create a `config.py` file in the appropriate directory with your API keys:
   ```python
   apikeys = {
       "htmltopdfkey": "your_html2pdf_api_key",
       "mygithub": "your_github_personal_access_token"
   }
   ```

2. For GitHub API access, create a Personal Access Token with appropriate permissions.

## Usage

### Running Jupyter Notebooks
```bash
jupyter notebook
```
Then navigate to the desired `.ipynb` file.

### Running Python Scripts
```bash
python assignments/assignment04-github.py
```

## Course Topics Covered

- **Data Processing**: CSV and JSON data manipulation
- **API Integration**: RESTful API calls and authentication
- **GitHub API**: Repository management and file operations
- **Web Services**: HTML to PDF conversion, data retrieval
- **Data Analysis**: Statistical analysis and visualization
- **Web Scraping**: Data extraction techniques (demonstrated in labs)

## Contributing

This is a coursework repository. For academic integrity, please complete assignments independently unless collaboration is explicitly permitted.

## License

This project is for educational purposes as part of the WSAA course.