import pandas as pd
file_path = "data/raw/known_exploited_vulnerabilities (2).csv"
df=pd.read_csv(file_path)
print('Dataset Loaded Successfully!')
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
    print('All columns are present.')
else:
    print('\nMissing Columns required:',missing_columns)
missing_values=df.isnull().sum()
print('\nMissing Values in each Column:')
print(missing_values)
print('\nTotal Missing Values:',missing_values.sum())
duplicate_cves=df['cveID'].duplicated().sum()
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
print('\nCleaned dataset saved successfully!!')
print('Output locations:',output_path)
cleaned_df = pd.read_csv(output_path)
print('\n--- Final Dataset Verification ---')
print('Rows:', cleaned_df.shape[0])
print('Columns:', cleaned_df.shape[1])
print('Missing CWE values:', cleaned_df["cwes"].isnull().sum())
print('Duplicate CVE IDs:', cleaned_df["cveID"].duplicated().sum())