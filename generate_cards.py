import csv, os
from jinja2 import Template

with open("card_template.html", encoding="utf-8") as f:
    template = Template(f.read())

with open("employees.csv", newline="", encoding="utf-8") as csvfile:
    for row in csv.DictReader(csvfile):
        folder = row["username"]
        os.makedirs(folder, exist_ok=True)
        with open(f"{folder}/index.html", "w", encoding="utf-8") as f:
            f.write(template.render(**row))
