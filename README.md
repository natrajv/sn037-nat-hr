# SN037-Nat-HR
Demo Python webapp for CRUD of HR database of pno, name, unit [Git](https://github.com/natrajv/sn037-nat-hr)


# Version History
## v1.0.0
* Release Date: 26 Sep 2026 (Tag: v1.0.0)
* Read source excel (hr.xlsx) and insert into target SQLite DB (hr.db)
* SQLite DB (hr.db) created automatically
* Key learings, key concepts
    + Libraries needed: pandas, sqlite3, openpyxl
    + Pandas Dataframe: df
    + `df = pd.read_excel(*Excel file*)`
    + `conn = sqlite3.connect(*SQLite DB file*)`
    + `conn.execute(""" CREATE TABLE <...> """)`
    + `records = list(df[["emp_no", "emp_name"]].itertuples(index=False, name=None))`
    + `conn.executemany("""INSERT INTO <...> """, records)`
    * `conn.commit(), conn.close`

    
