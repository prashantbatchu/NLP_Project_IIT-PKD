from pdf2image import convert_from_path
import pytesseract
import os

# Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Hindi traineddata folder
os.environ["TESSDATA_PREFIX"] = r"C:\tessdata"
pdf_path = "../data/manifestos/NDA's-Sankalp-Patra-for-Bihar-Assembly-Elections-2025.pdf"

images = convert_from_path(
    pdf_path,
    poppler_path=r"C:\poppler-26.02.0\Library\bin",
    dpi=300         
)

full_text = ""

for i, image in enumerate(images):

    text = pytesseract.image_to_string(image, lang='hin')

    full_text += text + "\n"

    print(f"Processed Page {i+1}")

# Create output folder
os.makedirs("../data/extracted_text_from_manifestos", exist_ok=True)

# Save extracted text
output_file = "../data/extracted_text_from_manifestos/NDA.txt"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(full_text)

print("\nOCR text extraction completed.")