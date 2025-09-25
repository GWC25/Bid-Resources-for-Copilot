import os
import pdfplumber
from docx import Document
import requests
from bs4 import BeautifulSoup

def extract_text_from_pdf(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + '\n'
    return text

def extract_text_from_docx(docx_path):
    doc = Document(docx_path)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return text

def extract_text_from_html(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        text = soup.get_text(separator='\n', strip=True)
    return text

def save_text(text, out_path):
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(text)

def main():
    docs_dir = 'docs'
    websites_dir = 'websites'
    # Process PDFs and DOCX
    if os.path.exists(docs_dir):
        for filename in os.listdir(docs_dir):
            if filename.endswith('.pdf'):
                path = os.path.join(docs_dir, filename)
                text = extract_text_from_pdf(path)
                out_path = os.path.splitext(path)[0] + '.txt'
                save_text(text, out_path)
                print(f"Extracted PDF text to {out_path}")
            elif filename.endswith('.docx'):
                path = os.path.join(docs_dir, filename)
                text = extract_text_from_docx(path)
                out_path = os.path.splitext(path)[0] + '.txt'
                save_text(text, out_path)
                print(f"Extracted Word text to {out_path}")
    # Process HTML
    if os.path.exists(websites_dir):
        for filename in os.listdir(websites_dir):
            if filename.endswith('.html'):
                path = os.path.join(websites_dir, filename)
                text = extract_text_from_html(path)
                out_path = os.path.splitext(path)[0] + '.txt'
                save_text(text, out_path)
                print(f"Extracted HTML text to {out_path}")

if __name__ == "__main__":
    main()
