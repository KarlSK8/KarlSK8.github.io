# generate_card.py
from jinja2 import Environment, FileSystemLoader
import json
import os

# Load data
with open('data.json', 'r') as f:
    data = json.load(f)

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('links_template.html')

# Render HTML with context
rendered_html = template.render(data)

# Output file
output_dir = "links"
os.makedirs(output_dir, exist_ok=True)
with open(f"{output_dir}/lavaleur.html", "w", encoding="utf-8") as f:
    f.write(rendered_html)

print("✅ business_card.html generated successfully.")