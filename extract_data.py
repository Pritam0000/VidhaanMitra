import PyPDF2

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def save_extracted_data():
    # Extract text from both PDFs
    constitution_text = extract_text_from_pdf("data/indian_constitution.pdf")
    polity_text = extract_text_from_pdf("data/laxmikant_polity.pdf")
    
    # Save as text files
    with open("data/constitution.txt", "w", encoding="utf-8") as f:
        f.write(constitution_text)

    with open("data/polity.txt", "w", encoding="utf-8") as f:
        f.write(polity_text)

if __name__ == "__main__":
    save_extracted_data()
    print("PDFs extracted and saved as text files.")
