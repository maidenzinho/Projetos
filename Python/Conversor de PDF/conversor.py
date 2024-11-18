from pdf2docx import Converter
import os

def pdf_to_docx(pdf_file, docx_file):
    # Converte PDF para DOCX
    cv = Converter(pdf_file)
    cv.convert(docx_file, start=0, end=None)
    cv.close()
    print(f'Arquivo convertido: {docx_file}')

def pdf_to_doc(pdf_file, doc_file):
    # Para converter PDF para DOC, primeiro converta para DOCX e depois renomeie
    docx_file = doc_file.replace('.doc', '.docx')
    pdf_to_docx(pdf_file, docx_file)
    
    # Renomeia o arquivo .docx para .doc
    os.rename(docx_file, doc_file)
    print(f'Arquivo convertido: {doc_file}')

def main():
    pdf_file = input("Digite o caminho do arquivo PDF: ")
    
    if not os.path.exists(pdf_file):
        print("Arquivo PDF não encontrado.")
        return
    
    # Converte para DOCX
    docx_file = pdf_file.replace('.pdf', '.docx')
    pdf_to_docx(pdf_file, docx_file)

    # Converte para DOC
    doc_file = pdf_file.replace('.pdf', '.doc')
    pdf_to_doc(pdf_file, doc_file)

if __name__ == "__main__":
    main()