import csv
import os
from jinja2 import Template

TEMPLATE_PATH = "templates/card_template.html"
CARDS_DIR = "data/cards.csv"

os.makedirs(CARDS_DIR, exist_ok=True)

with open(TEMPLATE_PATH, encoding="utf-8") as f:
    template = Template(f.read())

with open("cards.csv", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        filename = f"{CARDS_DIR}/{row['name'].replace(' ', '_').lower()}.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(template.render(**row))