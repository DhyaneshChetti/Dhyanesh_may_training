import PyPDF2, docx

def extract_text(file):
    if file.name.endswith('.pdf'): return " ".join([p.extract_text() for p in PyPDF2.PdfReader(file).pages if p.extract_text()])
    if file.name.endswith('.docx'): return " ".join([p.text for p in docx.Document(file).paragraphs])
    return file.read().decode('utf-8', errors='ignore')