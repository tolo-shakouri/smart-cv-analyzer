import pdfplumber
from skills import SKILLS


def extract_text_from_pdf(pdf_file):
    """Extract text from an uploaded PDF file."""
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text


def find_skills(text):
    """Find matching skills in the extracted text."""
    found = []

    for skill in SKILLS:
        if skill.lower() in text.lower():
            found.append(skill)

    return found
