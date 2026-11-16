import pandas as pd
from mysql_connection import create_connection
df = pd.read_csv("data/processed/cleaned_vulnerabilities.csv")
columns = [
    "cveID", "vendorProject", "product", "vulnerabilityName",
    "dateAdded", "shortDescription", "requiredAction", "dueDate",
    "knownRansomwareCampaignUse", "forensicTriage", "notes", "cwes"
]
df = df[columns]
df = df.astype(object).where(pd.notna(df), None)
for column in ["dateAdded", "dueDate"]:
    df[column] = pd.to_datetime(df[column], errors="coerce")
    df[column] = df[column].apply(
        lambda x: x.date() if pd.notna(x) else None
    )
connection = create_connection()
cursor = connection.cursor()
query = """
INSERT INTO vulnerabilities (
    cveID, vendorProject, product, vulnerabilityName,
    dateAdded, shortDescription, requiredAction, dueDate,
    knownRansomwareCampaignUse, forensicTriage, notes, cwes
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
ON DUPLICATE KEY UPDATE
    vendorProject = VALUES(vendorProject),
    product = VALUES(product),
    vulnerabilityName = VALUES(vulnerabilityName),
    dateAdded = VALUES(dateAdded),
    shortDescription = VALUES(shortDescription),
    requiredAction = VALUES(requiredAction),
    dueDate = VALUES(dueDate),
    knownRansomwareCampaignUse = VALUES(knownRansomwareCampaignUse),
    forensicTriage = VALUES(forensicTriage),
    notes = VALUES(notes),
    cwes = VALUES(cwes)
"""
data = [tuple(row) for row in df.values]
cursor.executemany(query, data)
connection.commit()
print("Data loaded successfully!")
print("Total records processed:", len(data))
cursor.close()
connection.close()
