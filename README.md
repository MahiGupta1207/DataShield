# DataShield – Cybersecurity Data Engineering Pipeline

DataShield is an end-to-end Data Engineering project focused on collecting, processing, validating, cleaning, and analyzing cybersecurity vulnerability data from the **CISA Known Exploited Vulnerabilities (KEV) Catalog**.

The project demonstrates how raw cybersecurity data can be transformed into structured and reliable data using Python, Pandas, SQL, PostgreSQL, and Apache Airflow.

## Project Overview

The CISA KEV Catalog contains information about vulnerabilities that have been exploited in real-world attacks.

DataShield aims to build a data pipeline that automates the collection and processing of this information while maintaining data quality and reliability.

## Technology Stack

- **Programming Language:** Python
- **Data Processing:** Pandas
- **Database:** PostgreSQL
- **Query Language:** SQL
- **Workflow Orchestration:** Apache Airflow
- **Logging:** Python Logging
- **Version Control:** Git and GitHub
- **Development Environment:** VS Code

## Dataset

**Source:** [CISA Known Exploited Vulnerabilities Catalog](https://github.com/cisagov/kev-data)

The dataset contains vulnerability information such as:

- CVE ID
- Vendor and Product
- Vulnerability Name
- Date Added
- Due Date
- Short Description
- Required Action
- Known Ransomware Campaign Usage
- CWE Information

## Project Structure

```text
DataShield/
│
├── data/
│   ├── raw/
│   │   └── known_exploited_vulnerabilities.csv
│   │
│   └── processed/
│       └── cleaned_vulnerabilities.csv
│
├── notebooks/
│
├── src/
│   ├── ingest_data.py
│   ├── inspect_data.py
│   ├── validate_data.py
│   └── quality_checks.py
│
├── sql/
│
├── logs/
│   └── pipeline.log
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Implemented Features

### 1. Automated Data Ingestion

- Downloads the latest CISA KEV dataset directly from the official GitHub repository.
- Uses Python's `urllib.request` library for downloading CSV data.
- Stores downloaded data in the `data/raw/` directory.
- Includes exception handling and logging for download operations.

### 2. Data Exploration

- Loads the dataset using Pandas.
- Examines the first few records.
- Checks dataset dimensions, column names, and data types.
- Identifies missing values and duplicate records.

### 3. Data Validation

- Checks the presence of required columns.
- Identifies missing values.
- Detects duplicate CVE IDs.
- Validates CVE ID formats.
- Checks date fields and date logic.
- Handles file-loading errors using exception handling.

### 4. Data Cleaning

- Converts date columns into datetime format.
- Replaces missing CWE values with `Unknown`.
- Preserves the original raw dataset.
- Saves the cleaned dataset separately in `data/processed/`.

### 5. Reusable Data Quality Checks

- Created reusable functions in `quality_checks.py`.
- Checks required columns, missing values, and duplicate CVE IDs.
- Validates CVE formats and date logic.
- Integrates reusable checks into the validation pipeline.

### 6. Logging and Error Handling

- Uses Python's Logging module to record pipeline activities.
- Records successful dataset downloads and verification.
- Logs errors during file loading and ingestion.
- Stores logs in `logs/pipeline.log`.

## Pipeline Workflow

```text
CISA KEV Catalog
       |
       v
Automated Data Ingestion
       |
       v
Raw CSV Storage
       |
       v
Data Exploration
       |
       v
Data Validation
       |
       v
Data Cleaning
       |
       v
Data Quality Checks
       |
       v
Processed CSV Storage
       |
       v
Future: PostgreSQL and SQL Analytics
```

## Current Dataset Results

The latest downloaded dataset was successfully processed and validated.

| Metric | Result |
|---|---:|
| Total Records | 1,781 |
| Total Columns | 12 |
| Missing CWE Values Before Cleaning | 175 |
| Missing CWE Values After Cleaning | 0 |
| Duplicate CVE IDs | 0 |
| Empty CVE IDs | 0 |
| Invalid CVE IDs | 0 |
| Invalid Dates | 0 |
| Invalid Date Records | 0 |

*Dataset counts may change as CISA updates its catalog.*

## Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/MahiGupta1207/DataShield.git
cd DataShield
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Data Ingestion

```bash
python src/ingest_data.py
```

### 6. Run Data Validation and Cleaning

```bash
python src/validate_data.py
```

The cleaned dataset will be saved in:

```text
data/processed/cleaned_vulnerabilities.csv
```

## Future Enhancements

- Store processed vulnerability data in PostgreSQL.
- Perform SQL-based cybersecurity data analysis.
- Build automated workflows using Apache Airflow.
- Implement additional data quality checks and testing.
- Add pipeline monitoring and reporting.
- Improve incremental data loading and historical tracking.

## License and Data Attribution

Dataset sourced from the [CISA KEV Catalog](https://github.com/cisagov/kev-data), identified as CC0 1.0 Universal.

DataShield is an independent educational project and is not affiliated with or endorsed by CISA or DHS.

## Author

**Mahi Gupta**

GitHub: [MahiGupta1207](https://github.com/MahiGupta1207)