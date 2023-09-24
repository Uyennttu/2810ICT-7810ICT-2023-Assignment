import sqlite3
con = sqlite3.connect('airbnb.db')
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")
tables = cursor.fetchall()
print(tables)


# For each table
for table_info in tables:
    table_name = table_info[0]
    sql_cmd = f"SELECT * FROM {table_name}"
    cursor.execute(sql_cmd)
    column_names = sqlite3.Row(cursor,(1,)).keys()
    print(f'{table_name}: {column_names}')
    print()