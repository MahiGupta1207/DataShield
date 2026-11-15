import pandas as pd
def read_csv_file():
    df = pd.read_csv("data/raw/known_exploited_vulnerabilities.csv")
    print("CSV file loaded successfully!")
    print(df.head())
def display_message():
    print('Welcome to DataShield!')
def display_project():
    print('Cybersecurity Data Engineering Pipeline')
def save_message():
    file=open("data/message.txt", "w")
    file.write("DataShield pipeline started successfully!")
    file.close()
    print("Message saved successfully!")
def read_message():
    file = open("data/message.txt", "r")
    content = file.read()
    file.close()
    print(content)
def save_message_safely():
    with open("data/message.txt", "w") as file:
        file.write("DataShield pipeline is running successfully!")
    print("Message saved successfully!")
def add_log():
    with open("data/message.txt", "a") as file:
        file.write("\nNew pipeline execution recorded.")
    print("New log added successfully!")
def save_csv_file():
    df = pd.read_csv("data/raw/known_exploited_vulnerabilities.csv")
    df.head(10).to_csv(
        "data/processed/sample_vulnerabilities.csv",
        index=False
    )
    print("CSV file saved successfully!")
def safe_read_csv():
    try:
        df = pd.read_csv("data/raw/known_exploited_vulnerabilities.csv")
        print("Dataset loaded successfully!")
        print(df.head())
    except FileNotFoundError:
        print("Error: CSV file not found!")
    except Exception as e:
        print("Something went wrong:", e)
def get_dataset_summary():
    df = pd.read_csv("data/raw/known_exploited_vulnerabilities.csv")
    print("Total Records:", len(df))
    print("Total Columns:", len(df.columns))
    print("Column Names:", df.columns.tolist())