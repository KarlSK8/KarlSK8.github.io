import csv
import os

# Load the vCard template
with open("vcard_template.vcf", "r", encoding="utf-8") as template_file:
    template = template_file.read()

# Create output directory
vcards_dir = "vcards"
os.makedirs(vcards_dir, exist_ok=True)

# Read CSV and generate vCards
with open("cards.csv", newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        vcard_content = template.format(
            full_name=row.get("full_name", ""),
            first_name=row.get("first_name", ""),
            last_name=row.get("last_name", ""),
            additional_names=row.get("additional_names", ""),
            prefix=row.get("prefix", ""),
            suffix=row.get("suffix", ""),
            nickname=row.get("nickname", ""),
            location=row.get("location", ""),
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

        # Save the vCard
        filename = f"{row.get('first_name', '').lower()}_{row.get('last_name', '').lower()}.vcf"
        filepath = os.path.join(vcards_dir, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(vcard_content)

        print(f"✅ Created vCard: {filepath}")
