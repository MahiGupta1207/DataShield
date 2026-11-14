import pandas as pd
import logging
import sys
from quality_checks import(check_required_columns,check_missing_values,check_duplicate_cves,check_cve_format,check_date_logic)
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
file_path = "data/raw/known_exploited_vulnerabilities.csv"
try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!")
    logging.info("Dataset loaded successfully")
except FileNotFoundError:
    print("Error: CSV file not found!")
    logging.error("CSV file not found")
    sys.exit(1)
except Exception as e:
    print("Something went wrong:", e)
    logging.error("Unexpected error: %s", e)
    sys.exit(1)
print('Total Rows:',len(df))
print('Total Columns:',len(df.columns))
print('\nColumn Names:')
print(df.columns.tolist())
if not check_required_columns(df):
    logging.error("Required columns are missing")
    sys.exit(1)
logging.info("Required columns check passed")
missing_values = check_missing_values(df)
print("\nTotal Missing Values:", missing_values.sum())
logging.info("Missing values check completed")
duplicate_cves = check_duplicate_cves(df)
logging.info("Duplicate CVE check completed")
date_columns = ['dateAdded', 'dueDate']
for column in date_columns:
    df[column] = pd.to_datetime(df[column], errors='coerce')
    invalid_date_count = df[column].isnull().sum()
    print(f"\nInvalid dates in {column}: {invalid_date_count}")
print('\nDuplicate CVE IDs:',duplicate_cves)
df['cwes']=df['cwes'].fillna('Unknown')
print('\nMissing CWE values after handling:')
print(df['cwes'].isnull().sum())
print('\nCWE values handled successfully')
output_path = "data/processed/cleaned_vulnerabilities.csv"
df.to_csv(output_path, index=False)
logging.info("Cleaned dataset saved successfully")
print('\nCleaned dataset saved successfully!!')
print('Output locations:',output_path)
cleaned_df = pd.read_csv(output_path)
print('\n--- Final Dataset Verification ---')
print('Rows:', cleaned_df.shape[0])
print('Columns:', cleaned_df.shape[1])
print('Missing CWE values:', cleaned_df["cwes"].isnull().sum())
print('Duplicate CVE IDs:', cleaned_df["cveID"].duplicated().sum())
logging.info("Final dataset verification completed")
empty_cve_ids=df['cveID'].isnull().sum()
print('\nEmpty CVE IDs:',empty_cve_ids)
invalid_cves = check_cve_format(df)
logging.info("CVE format check completed")
invalid_dates = check_date_logic(df)
logging.info("Date logic check completed")
print("\nData validation and cleaning completed successfully!")