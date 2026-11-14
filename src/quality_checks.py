def check_required_columns(df):
    required_columns=['cveID','vendorProject','product','dateAdded','dueDate']
    missing_columns=[]
    for column in required_columns:
        if column not in df.columns:
            missing_columns.append(column)
    if len(missing_columns)==0:
        print('All required columns are present.')
    else:
        print('Missing columns:',missing_columns)
    return len(missing_columns)==0
def check_missing_values(df):
    missing_values=df.isnull().sum()
    print('\nMissing Values in each column:')
    print(missing_values)
    return missing_values
def check_duplicate_cves(df):
    duplicate_cves=df['cveID'].duplicated().sum()
    print('\nDuplicate CVE IDs:',duplicate_cves)
    return duplicate_cves
def check_cve_format(df):
    invalid_cves=df[~df['cveID'].str.match(r"^CVE-\d{4}-\d{4,}$",na=False)]
    print('\nInvalid CVE IDs:',len(invalid_cves))
    print(invalid_cves['cveID'])
    return invalid_cves
def check_date_logic(df):
    invalid_dates=df[df['dueDate']<df['dateAdded']]
    print('\nInvalid Date Records:',len(invalid_dates))
    print(invalid_dates[['cveID','dateAdded','dueDate']])
    return invalid_dates
