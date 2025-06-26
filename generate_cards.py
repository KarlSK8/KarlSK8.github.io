import csv, os
from jinja2 import Template

def clean_keys(row):
    return {str(k).strip(): str(v).strip() if v else "" for k, v in row.items()}

with open("card_template.html", encoding="utf-8") as f:
    template = Template(f.read())

with open("employees.csv", newline="", encoding="utf-8-sig") as csvfile:
    for raw_row in csv.DictReader(csvfile):
        row = clean_keys(raw_row)
        folder = row["username"]
        os.makedirs(folder, exist_ok=True)
        with open(f"{folder}/index.html", "w", encoding="utf-8") as f:
            f.write(template.render(**row))
