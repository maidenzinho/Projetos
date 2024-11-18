import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog, QLabel
from pdf2docx import Converter

class PDFConverterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Conversor de PDF')
        self.setGeometry(100, 100, 300, 200)

        self.layout = QVBoxLayout()

        self.label = QLabel('Selecione um arquivo PDF para converter:', self)
        self.layout.addWidget(self.label)

        self.selectButton = QPushButton('Selecionar PDF', self)
        self.selectButton.clicked.connect(self.select_pdf)
        self.layout.addWidget(self.selectButton)

        self.convertDocxButton = QPushButton('Converter para DOCX', self)
        self.convertDocxButton.clicked.connect(self.convert_to_docx)
        self.layout.addWidget(self.convertDocxButton)

        self.convertDocButton = QPushButton('Converter para DOC', self)
        self.convertDocButton.clicked.connect(self.convert_to_doc)
        self.layout.addWidget(self.convertDocButton)

        self.setLayout(self.layout)

        self.pdf_file = None

    def select_pdf(self):
        options = QFileDialog.Options()
        self.pdf_file, _ = QFileDialog.getOpenFileName(self, "Selecionar PDF", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if self.pdf_file:
            self.label.setText(f'Selecionado: {os.path.basename(self.pdf_file)}')

    def convert_to_docx(self):
        if self.pdf_file:
            docx_file = self.pdf_file.replace('.pdf', '.docx')
            cv = Converter(self.pdf_file)
            cv.convert(docx_file, start=0, end=None)
            cv.close()
            self.label.setText(f'Arquivo convertido para: {os.path.basename(docx_file)}')
        else:
            self.label.setText('Por favor, selecione um arquivo PDF primeiro.')

    def convert_to_doc(self):
        if self.pdf_file:
            docx_file = self.pdf_file.replace('.pdf', '.docx')
            cv = Converter(self.pdf_file)
            cv.convert(docx_file, start=0, end=None)
            cv.close()
            doc_file = self.pdf_file.replace('.pdf', '.doc')
            os.rename(docx_file, doc_file)
            self.label.setText(f'Arquivo convertido para: {os.path.basename(doc_file)}')
        else:
            self.label.setText('Por favor, selecione um arquivo PDF primeiro.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    converter = PDFConverterApp()
    converter.show()
    sys.exit(app.exec_())