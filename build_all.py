import subprocess

def build_all():
    try:
        subprocess.run(["python", "scripts/generate_vcf.py"], check=True)
        print("vCards generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating vCards: {e}")

    try:
        subprocess.run(["python", "scripts/generate_cards.py"], check=True)
        print("HTML cards generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating HTML cards: {e}")

    try:
        subprocess.run(["python", "scripts/generate_links.py"], check=True)
        print("HTML links generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating HTML cards: {e}")

build_all()