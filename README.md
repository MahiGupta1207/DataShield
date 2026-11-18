# DataShield — Cybersecurity Data Engineering Pipeline

DataShield is an end-to-end Data Engineering project that collects, cleans, validates, stores, and analyzes cybersecurity vulnerability data using the CISA Known Exploited Vulnerabilities (KEV) Catalog.

## Project Objectives

- Automate cybersecurity dataset ingestion.
- Perform data cleaning and validation.
- Implement reusable data quality checks.
- Store structured data in MySQL.
- Perform SQL-based cybersecurity analytics.
- Build a reliable and reusable data pipeline.

## Technology Stack

- **Programming:** Python
- **Data Processing:** Pandas
- **Database:** MySQL
- **Query Language:** SQL
- **Database Connectivity:** MySQL Connector
- **Environment Management:** python-dotenv
- **Logging:** Python Logging
- **Version Control:** Git and GitHub

## Pipeline Execution

DataShield includes an automated pipeline runner that executes the complete workflow sequentially.

Run the following command from the project root:

```bash
python src/run_pipeline.py
```
## Logging and Error Handling

DataShield uses Python's logging module to maintain pipeline execution records.

- Logs pipeline start and completion.
- Records successful execution of individual stages.
- Captures errors when a script fails.
- Stops execution when a pipeline stage encounters an error.

Logs are stored in `logs/pipeline.log`.

The pipeline automatically performs:

1. Downloads the latest CISA KEV dataset.
2. Cleans and validates vulnerability records.
3. Loads processed data into the MySQL database.
4. Displays execution status for each stage.

This reduces manual execution and makes the data pipeline easier to run.

## Project Architecture

1. **Data Ingestion:** Download CISA KEV vulnerability data.
2. **Data Exploration:** Inspect dataset structure and data types.
3. **Data Cleaning:** Handle missing values and convert date columns.
4. **Data Validation:** Check required columns, duplicate CVEs, CVE formats, and date logic.
5. **Data Quality:** Implement reusable validation functions.
6. **Data Storage:** Load cleaned records into MySQL.
7. **SQL Analytics:** Analyze vendors, products, ransomware associations, and vulnerability trends.
8. **Pipeline Automation:** Execute ingestion, validation, cleaning, and MySQL loading sequentially using a single Python script.
- Logging and Monitoring: Tracks pipeline execution, successful stages, and errors using Python logging.
- Error Handling: Detects failed tasks and stops pipeline execution to prevent incomplete processing.

## Project Structure

```text
DataShield/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── inspect_data.py
│   ├── validate_data.py
│   ├── quality_checks.py
│   ├── ingest_data.py
│   ├── data_utils.py
│   ├── mysql_connection.py
│   └── load_to_mysql.py
├── sql/
│   ├── analytics.sql
│   └── views_procedures.sql
├── logs/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## SQL Analytics

- Total vulnerability counts
- Top vulnerable vendors and products
- Ransomware-related vulnerability analysis
- Year-wise vulnerability trends
- SQL views and stored procedures
- Ranking using SQL window functions

## Dataset Source

CISA Known Exploited Vulnerabilities Catalog:

https://github.com/cisagov/kev-data

The project uses publicly available cybersecurity vulnerability metadata.

## Security

Database credentials are stored in a local `.env` file and excluded from Git using `.gitignore`. A `.env.example` template is provided without real credentials.

## Future Enhancements

- Apache Airflow pipeline orchestration
- Advanced monitoring and logging
- Automated data quality reporting
- Data visualization dashboards

## Project Status

Implemented:
- Automated data ingestion
- Data cleaning and validation
- Reusable data quality checks
- MySQL database integration
- SQL analytics, views, and stored procedures
- Automated pipeline execution

## License and Attribution

Dataset source: CISA KEV Catalog. Refer to the official repository for its licensing and attribution information.
