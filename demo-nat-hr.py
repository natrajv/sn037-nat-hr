import pandas as pd
import sqlite3
# --------------------------------------------------
# Note: Ensure you have the required libraries installed:
# pip install pandas openpyxl (or)
# uv add pandas and openpyxl to your environment if not already installed.
# --Housekeeping
# Make sure to have hr.xlsx in the same directory as this script.
# Truncate the hr table in hr.db before running this script to avoid duplicate entries.
# PS> sqlite3 .\hr.db "delete from hr;"
# --------------------------------------------------
# Configuration
# --------------------------------------------------
# Sample data in hr.xlsx:
# | emp_no | emp_name |
# | -----: | -------- |
# |   1001 | Ravi     |
# |   1002 | Kumar    |
# |   1003 | Suresh   |
# --------------------------------------------------

SOURCE_EXCEL = "hr.xlsx"
TARGET_DB = "hr.db"

# --------------------------------------------------
# 1. Read Excel
# --------------------------------------------------
df = pd.read_excel(SOURCE_EXCEL)

print("Excel data:")
print(df)

# --------------------------------------------------
# 2. Connect to SQLite database
# --------------------------------------------------
conn = sqlite3.connect(TARGET_DB)

# --------------------------------------------------
# 3. Create target table
# --------------------------------------------------
conn.execute("""
    CREATE TABLE IF NOT EXISTS employee (
        emp_no   INTEGER PRIMARY KEY,
        emp_name TEXT
    )
""")

# --------------------------------------------------
# 4. Insert Excel records into SQLite
# --------------------------------------------------
records = list(
    df[["emp_no", "emp_name"]]
    .itertuples(index=False, name=None)
)

conn.executemany(
    """
    INSERT INTO employee (emp_no, emp_name)
    VALUES (?, ?)
    """,
    records
)

# --------------------------------------------------
# 5. Commit transaction
# --------------------------------------------------
conn.commit()

# --------------------------------------------------
# 6. Close database
# --------------------------------------------------
conn.close()

print(f"{len(records)} records inserted successfully.")