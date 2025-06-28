import csv
import os

vcards_dir = "vcards"
os.makedirs(vcards_dir, exist_ok=True)

def generate_vcard(name, title, company, email, phone, website):
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
ORG:{company}
TITLE:{title}
EMAIL;TYPE=INTERNET:{email}
TEL;TYPE=CELL:{phone}
URL:{website}
END:VCARD
"""
    return vcard

with open("cards.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        name = row.get("name", "").strip()
        title = row.get("title", "").strip()
        company = row.get("company", "").strip()
        email = row.get("email", "").strip()
        phone = row.get("phone", "").strip()
        website = row.get("website", "").strip()

        filename = f"{name.lower().replace(' ', '_')}.vcf"
        filepath = os.path.join(vcards_dir, filename)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(generate_vcard(name, title, company, email, phone, website))

        print(f"✅ Created vCard: {filepath}")