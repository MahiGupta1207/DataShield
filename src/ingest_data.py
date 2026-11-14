import urllib.request
import logging
import pandas as pd
url = "https://raw.githubusercontent.com/cisagov/kev-data/develop/known_exploited_vulnerabilities.csv"
output_path = "data/raw/known_exploited_vulnerabilities.csv"
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
try:
    urllib.request.urlretrieve(url,output_path)
    print('Dataset download successfully!!')
    logging.info('Dataset download successfully!!')
    df=pd.read_csv(output_path)
    print('\nDataset Verification:')
    print('Total Rows:', len(df))
    print('Total Columns:', len(df.columns))
    logging.info('Dataset verification completed')
    logging.info('Total rows: %s', len(df))
    logging.info('Total columns: %s', len(df.columns))
    print('\nFirst 5 Rows:')
    print(df.head())
except Exception as e:
    print('Download failed:',e)
    logging.error('Dataset download failed %s',e)
