import csv
import os
from jinja2 import Environment, FileSystemLoader

output_dir = "cards"
os.makedirs(output_dir, exist_ok=True)

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("card_template.html")

def clean_keys(row):
    return {str(k).strip(): str(v).strip() for k, v in row.items() if k}

generated_files = set()

with open("cards.csv", newline='', encoding="latin") as csvfile:
    reader = csv.DictReader(csvfile)
    for raw_row in reader:
        row = clean_keys(raw_row)
        filename = f"{row['first_name'].lower()}_{row['last_name'].lower()}.html"
        output_path = os.path.join(output_dir, filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(template.render(**row))
        generated_files.add(filename)
        print(f"✅ Generated {output_path}")

for file in os.listdir(output_dir):
    if file.endswith(".html") and file not in generated_files:
        file_path = os.path.join(output_dir, file)
        os.remove(file_path)
        print(f"🗑️ Deleted orphaned file: {file_path}")
