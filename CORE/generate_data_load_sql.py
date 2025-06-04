# generate_data_load_sql.py

import pandas as pd
import os

# Load CSV
df = pd.read_csv('data/Final_recipees.csv')

# Helper to format values
def sql_literal(val):
    if pd.isna(val):
        return "NULL"
    elif isinstance(val, str):
        return "'" + val.replace("'", "''") + "'"
    else:
        return str(val)

# Prepare insert statements
insert_lines = []
for _, row in df.iterrows():
    values = ", ".join([
        sql_literal(row['recipe']),
        sql_literal(row['size']),
        sql_literal(row['overvidde_cm']),
        sql_literal(row['length_cm']),
        sql_literal(row['material_g']),
        sql_literal(row['strikkefasthed']),
        sql_literal(row['needle']),
        sql_literal(row['diff']),
        sql_literal(row['yarn'])
    ])
    line = f"INSERT INTO recipes (recipe, size, overvidde_cm, length_cm, material_g, strikkefasthed, needle, diff, yarn) VALUES ({values});"
    insert_lines.append(line)

# Output file path
os.makedirs("sql", exist_ok=True)
with open("sql/data_load.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(insert_lines))

print("✅ data_load.sql generated successfully.")
