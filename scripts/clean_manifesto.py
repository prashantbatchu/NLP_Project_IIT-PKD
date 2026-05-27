import re

with open("../data/extracted_text_from_manifestos/NDA.txt", "r", encoding="utf-8") as f:
    text = f.read()

text = text.translate(str.maketrans(
    "०१२३४५६७८९",
    "0123456789"
))

text = re.sub(r'[^\u0900-\u097F0-9a-zA-Z\s₹.,!?()%:-]', ' ', text)
text = re.sub(r'(\S+)( \1){2,}', r'\1', text)
text = re.sub(r'[()]', ' ', text)
text = re.sub(r'[ \t]+', ' ', text)

corrections = {
    "हंडिया": "इंडिया",
    "थिक्षा": "शिक्षा",
    "हलाज": "इलाज"
}

for w, c in corrections.items():
    text = text.replace(w, c)

# Save
with open("../data/cleaned_manifesto/NDA.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Cleaning completed")