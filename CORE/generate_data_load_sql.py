import pandas as pd
import os

df = pd.read_csv('data/Final_recipees.csv')
df = df.rename(columns={'recipe': 'pattern_name'})

def sql_literal(val):
    if pd.isna(val):
        return "NULL"
    elif isinstance(val, str):
        return "'" + val.replace("'", "''") + "'"
    else:
        return str(val)


yarns = df['yarn'].dropna().unique()
needles = df['needle'].dropna().unique()

recipe_fields = ['pattern_name', 'size', 'overvidde_cm', 'length_cm', 'strikkefasthed', 'diff']
unique_recipes = df[recipe_fields].drop_duplicates()

sql_lines = []


for y in sorted(yarns):
    sql_lines.append(f"INSERT INTO yarns(name) VALUES ({sql_literal(y)});")


for n in sorted(needles):
    sql_lines.append(f"INSERT INTO needles(size) VALUES ({sql_literal(n)});")


for _, row in unique_recipes.iterrows():
    vals = ", ".join([
        sql_literal(row['pattern_name']),
        sql_literal(row['size']),
        sql_literal(row['overvidde_cm']),
        sql_literal(row['length_cm']),
        sql_literal(row['strikkefasthed']),
        sql_literal(row['diff'])
    ])
    sql_lines.append(
        f"INSERT INTO recipes(pattern_name, size, overvidde_cm, length_cm, strikkefasthed, diff) VALUES ({vals});"
    )


for _, row in df.iterrows():
    patt = sql_literal(row['pattern_name'])
    sz   = sql_literal(row['size'])
    yarn = sql_literal(row['yarn'])
    ndl  = sql_literal(row['needle'])
    mat  = sql_literal(row['material_g'])
    line = (
      "INSERT INTO knitted_by(recipe_id, yarn_id, needle_id, material_g) VALUES ("
      f"(SELECT id FROM recipes WHERE pattern_name={patt} AND size={sz}), "
      f"(SELECT id FROM yarns   WHERE name={yarn}), "
      f"(SELECT id FROM needles WHERE size={ndl}), "
      f"{mat}"
      ");"
    )
    sql_lines.append(line)


os.makedirs("sql", exist_ok=True)
with open("sql/02_data_load.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(sql_lines))

print("✅ 02_data_load.sql generated with normalized inserts.")
