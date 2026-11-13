import pandas as pd
import logging
import sys
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
file_path = "data/raw/known_exploited_vulnerabilities (2).csv"
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
required_columns = ['cveID','vendorProject','product','dateAdded','dueDate']
missing_columns=[]
for column in required_columns:
    if column not in df.columns:
        missing_columns.append(column)
if len(missing_columns)==0:
    print('\nAll required columns are present.')
    logging.info("All required columns are present")
else:
    print('\nMissing required columns:', missing_columns)
    logging.error("Missing required columns: %s", missing_columns)
    sys.exit(1)
missing_values=df.isnull().sum()
print('\nMissing Values in each Column:')
print(missing_values)
print('\nTotal Missing Values:',missing_values.sum())
duplicate_cves=df['cveID'].duplicated().sum()
date_columns = ['dateAdded', 'dueDate']
for column in date_columns:
    df[column] = pd.to_datetime(df[column], errors='coerce')
print('\nDuplicate CVE IDs:',duplicate_cves)
date_columns=['dateAdded','dueDate']
for column in date_columns:
    df[column]=pd.to_datetime(df[column],errors='coerce')
    invalid_dates=df[column].isnull().sum()
    print(f'\nInvalid dates in {column}:{invalid_dates}')
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
invalid_cve_ide=df[~df['cveID'].str.match(r"^CVE-\d{4}-\d{4,}$",na=False)]
print("\nInvalid CVE IDs:", len(invalid_cve_ide))
print(invalid_cve_ide['cveID'])
invalid_dates=df[df['dueDate']<df['dateAdded']]
print('\nInvalid Data Records:',len(invalid_dates))
print(invalid_dates[['cveID','dateAdded','dueDate']])
print("\nData validation and cleaning completed successfully!")