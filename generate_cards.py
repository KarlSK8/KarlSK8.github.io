import csv
import os
from jinja2 import Environment, FileSystemLoader

# Ensure output directory exists
output_dir = "cards"
os.makedirs(output_dir, exist_ok=True)

# Load the Jinja2 environment
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("card_template.html")

def clean_keys(row):
    return {str(k).strip(): str(v).strip() for k, v in row.items() if k}

with open("cards.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for raw_row in reader:
        row = clean_keys(raw_row)
        filename = f"{row['name'].lower().replace(' ', '_')}.html"
        output_path = os.path.join(output_dir, filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(template.render(**row))
        print(f"✅ Generated {output_path}")