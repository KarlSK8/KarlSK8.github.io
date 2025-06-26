# generate_cards.py
import csv, os, jinja2, pathlib

TEMPLATE = pathlib.Path("card_template.html").read_text()
tpl = jinja2.Template(TEMPLATE)

with open("employees.csv", newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        folder = pathlib.Path(row["username"])
        folder.mkdir(exist_ok=True)
        # Render template with row fields (name, title, email, etc.)
        rendered = tpl.render(**row)
        (folder / "index.html").write_text(rendered, encoding="utf-8")

print("✅ Cards generated!")
