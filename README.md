# DataShield – Cybersecurity Data Engineering Pipeline

DataShield is an end-to-end Data Engineering project focused on processing, validating, cleaning, and analysing cybersecurity vulnerability data from the CISA Known Exploited Vulnerabilities (KEV) Catalog.

The project demonstrates how raw cybersecurity data can be transformed into structured, reliable data for further analysis using Python, Pandas, SQL, PostgreSQL, and Apache Airflow.

## Project Objectives

- Build an end-to-end Data Engineering pipeline.
- Work with real-world cybersecurity vulnerability metadata.
- Perform data ingestion, validation, and cleaning.
- Maintain separate raw and processed datasets.
- Store structured data for further analysis.
- Perform SQL-based cybersecurity analytics.
- Automate pipeline execution and monitor data quality.

## Dataset Information

**Dataset:** CISA Known Exploited Vulnerabilities (KEV) Catalog

**Official Repository:** https://github.com/cisagov/kev-data

**Source File:** `known_exploited_vulnerabilities.csv`

The CISA KEV Catalog contains information about vulnerabilities that have been identified as exploited in real-world cyberattacks.

The official repository identifies the dataset as CC0 1.0 Universal.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and pipeline development |
| Pandas | Data manipulation and cleaning |
| NumPy | Numerical operations |
| CSV | Dataset storage |
| PostgreSQL | Relational database |
| SQL | Data analysis and querying |
| Apache Airflow | Pipeline orchestration |
| Git and GitHub | Version control |
| VS Code | Development environment |

## Project Structure

```text
DataShield/
│
├── data/
│   ├── raw/
│   │   └── known_exploited_vulnerabilities (2).csv
│   │
│   └── processed/
│       └── cleaned_vulnerabilities.csv
│
├── notebooks/
│
├── src/
│   ├── inspect_data.py
│   └── validate_data.py
│
├── sql/
│
├── logs/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Project Development Progress

### 1. Project Setup

- Selected cybersecurity as the project domain.
- Identified the CISA KEV Catalog as the primary data source.
- Downloaded the original vulnerability dataset.
- Created the project directory structure.
- Created README.md, requirements.txt, and .gitignore.
- Initialized the Git repository.
- Connected the local project to GitHub.
- Pushed the initial project setup to the remote repository.

### 2. Python Environment Setup

- Created an isolated Python virtual environment using `venv`.
- Installed Pandas and its dependencies.
- Verified the Pandas installation.
- Prepared the development environment for data processing.

### 3. Exploratory Data Analysis (EDA)

Created `src/inspect_data.py` to inspect and understand the original CISA dataset.

The following operations were performed:

- Displayed the first five records using `head()`.
- Checked the dataset dimensions using `shape`.
- Retrieved column names using `columns`.
- Examined column data types using `dtypes`.
- Identified missing values using `isnull().sum()`.
- Detected duplicate rows using `duplicated().sum()`.

**Initial Dataset Findings**

| Metric | Result |
|---|---:|
| Total records | 1,779 |
| Total columns | 12 |
| Missing CWE values | 175 |
| Duplicate rows | 0 |

### 4. Data Validation

Created `src/validate_data.py` to perform initial data quality checks.

The following validations were implemented:

- Checked the presence of required columns.
- Identified missing values in individual columns.
- Checked duplicate CVE IDs.
- Converted `dateAdded` and `dueDate` into datetime format.
- Used `errors="coerce"` to identify invalid or missing date values.

**Required columns checked:**
- `cveID`
- `vendorProject`
- `product`
- `dateAdded`
- `dueDate`

### 5. Data Cleaning and Processing

Initial data cleaning operations included:

- Replaced missing values in the `cwes` column with `"Unknown"`.
- Preserved vulnerability records instead of deleting incomplete rows.
- Converted date columns into datetime values during processing.
- Kept the original raw dataset unchanged.
- Exported the processed dataset separately using Pandas `to_csv()`.

**Processed Dataset Location:**

`data/processed/cleaned_vulnerabilities.csv`

The CSV is saved with `index=False` to avoid adding an unnecessary DataFrame index column.

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/MahiGupta1207/DataShield.git
```

### 2. Navigate to the Project Directory

```bash
cd DataShield
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate the Environment (Windows PowerShell)

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Run Dataset Inspection

```bash
python src/inspect_data.py
```

### 7. Run Data Validation and Cleaning

```bash
python src/validate_data.py
```

The processed CSV will be generated inside `data/processed/`.

## Data Integrity

DataShield maintains separate storage for original and processed data.

- `data/raw/` stores the original CISA dataset.
- `data/processed/` stores the cleaned and processed dataset.
- The original dataset is not overwritten during processing.

This separation helps maintain data integrity and allows the processed output to be compared with the original source.

## Future Development Roadmap

The following features are planned for upcoming development:

- Advanced data quality checks.
- Improved error handling and logging.
- Automated data ingestion.
- PostgreSQL database integration.
- SQL-based cybersecurity analytics.
- Apache Airflow pipeline orchestration.
- Automated pipeline monitoring.
- Pipeline testing and performance improvements.

## License and Data Attribution

The vulnerability metadata used in this project is sourced from the official CISA Known Exploited Vulnerabilities (KEV) Catalog.

**Source:** https://github.com/cisagov/kev-data

The source repository identifies the dataset as CC0 1.0 Universal. Refer to the original repository and license information for details.

DataShield is an independent educational project and is not affiliated with or endorsed by CISA or the U.S. Department of Homeland Security.