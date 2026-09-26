import pandas as pd
import sqlite3

# --------------------------------------------------
# Configuration
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