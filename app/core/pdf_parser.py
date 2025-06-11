import fitz  # PyMuPDF

async def extract_text_from_pdf(file) -> str:
    """
    Extract text from a PDF file-like object using PyMuPDF.
    """
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    file.seek(0)  # Reset file pointer after reading
    return text
