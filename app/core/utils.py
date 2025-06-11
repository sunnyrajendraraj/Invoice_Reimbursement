import zipfile
from io import BytesIO

def extract_pdfs_from_zip(zip_bytes_io):
    """
    Extract PDF files from a ZIP archive (BytesIO object).
    Returns a list of file-like objects for each PDF.
    """
    pdf_files = []
    with zipfile.ZipFile(zip_bytes_io) as z:
        for filename in z.namelist():
            if filename.lower().endswith('.pdf'):
                pdf_bytes = z.read(filename)
                pdf_files.append(BytesIO(pdf_bytes))
    return pdf_files
