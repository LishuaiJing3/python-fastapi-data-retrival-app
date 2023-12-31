# %%
import os

import dotenv
import pyodbc

dotenv.load_dotenv()

# Replace <table-name> with the name of the database table to query.
table_name = os.getenv("TABLE_NAME")
# %%

# Connect to the SQL warehouse by using the
# Data Source Name (DSN) that you created earlier.
conn = pyodbc.connect("DSN=Databricks_Cluster", autocommit=True)

# Run a SQL query by using the preceding connection.
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM {table_name} LIMIT 2")

# Print the rows retrieved from the query.
print(f"Query output: SELECT * FROM {table_name} LIMIT 2\n")
for row in cursor.fetchall():
    print(row)
# %%
