import csv
import os

def clean_row(row):
    return {str(key).strip(): str(value).strip() for key, value in row.items() if key}

def full_name(row):
    return " ".join(part for part in [
        row.get("first_name", ""),
        row.get("middle_name", "") or row.get("additional_names", ""),
        row.get("last_name", "")
    ] if part)

with open("templates/vcard_template.vcf", "r", encoding="utf-8") as template_file:
    template = template_file.read()

vcards_dir = "vcards"
os.makedirs(vcards_dir, exist_ok=True)

generated_cards = set()

with open("cards.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for raw_row in reader:
        row = clean_row(raw_row)
        name = full_name(row)
        vcard_content = template.format(
            full_name=row.get("full_name", name),
            first_name=row.get("first_name", ""),
            last_name=row.get("last_name", ""),
            additional_names=row.get("middle_name", "") or row.get("additional_names", ""),
            company=row.get("company", ""),
            prefix=row.get("prefix", ""),
            suffix=row.get("suffix", ""),
            nickname=row.get("nickname", ""),
            location=row.get("location", ""),
            street=row.get("street", "") or row.get("location", ""),
            city=row.get("city", ""),
            country=row.get("country", ""),
            home_phone=row.get("home_phone", ""),
            work_phone=row.get("work_phone", ""),
            cell_phone=row.get("cell_phone", ""),
            fax_number=row.get("fax_number", ""),
            home_email=row.get("home_email", ""),
            work_email=row.get("work_email", ""),
            website=row.get("website", ""),
            job_title=row.get("job_title", ""),
            role=row.get("role", ""),
            organization=row.get("organization", ""),
            department=row.get("department", ""),
            categories=row.get("categories", ""),
            note=row.get("note", ""),
            revision=row.get("revision", ""),
            uid=row.get("uid", ""),
            public_key=row.get("public_key", ""),
            twitter=row.get("twitter", ""),
            linkedin=row.get("linkedin", ""),
            skype=row.get("skype", "")
        )

        filename = f"{row.get('first_name', '').lower()}_{row.get('last_name', '').lower()}.vcf"
        filepath = os.path.join(vcards_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(vcard_content)

        generated_cards.add(filename)
        print(f"Created vCard: {filepath}")

for file in os.listdir(vcards_dir):
    if file.endswith(".vcf") and file not in generated_cards:
        file_path = os.path.join(vcards_dir, file)
        os.remove(file_path)
        print(f"Deleted orphaned vCard: {file_path}")
