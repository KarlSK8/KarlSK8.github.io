from jinja2 import Environment, FileSystemLoader
import json
import os

with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

env = Environment(
    loader=FileSystemLoader("templates"),
    trim_blocks=True,
    lstrip_blocks=True,
)
template = env.get_template("links_template.html")

rendered_html = template.render(data)

output_dir = "links"
os.makedirs(output_dir, exist_ok=True)
with open(f"{output_dir}/lavaleur.html", "w", encoding="utf-8") as f:
    f.write(rendered_html)

print("Generated links/lavaleur.html")
