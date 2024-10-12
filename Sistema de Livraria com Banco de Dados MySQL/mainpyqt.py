import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QTextEdit, 
    QFormLayout, QMessageBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QInputDialog
)
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

URL_BANCO = "mysql+pymysql://root:@localhost/tde"
engine = create_engine(URL_BANCO)
Base = declarative_base()

class Autor(Base):
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    biografia = Column(Text)
    livros = relationship('Livro', back_populates='autor')

class Editora(Base):
    __tablename__ = 'editoras'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    endereco = Column(String(255))
    livros = relationship('Livro', back_populates='editora')

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    sinopse = Column(Text)
    preco = Column(Numeric(10, 2))
    autor_id = Column(Integer, ForeignKey('autores.id'), nullable=False)
    editora_id = Column(Integer, ForeignKey('editoras.id'), nullable=False)
    frete_id = Column(Integer, ForeignKey('fretes.id'))

    autor = relationship('Autor', back_populates='livros')
    editora = relationship('Editora', back_populates='livros')
    frete = relationship('Frete', back_populates='livros')

class Frete(Base):
    __tablename__ = 'fretes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    custo = Column(Numeric(10, 2))
    metodo = Column(String(255))
    livros = relationship('Livro', back_populates='frete')

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
sessao = Session()

def adicionar_autor(nome, biografia):
    autor_novo = Autor(nome=nome, biografia=biografia)
    sessao.add(autor_novo)
    sessao.commit()

def consultar_autores():
    return sessao.query(Autor).all()

def atualizar_autor(id, nome=None, biografia=None):
    autor = sessao.query(Autor).filter_by(id=id).first()
    if autor:
        if nome:
            autor.nome = nome
        if biografia:
            autor.biografia = biografia
        sessao.commit()

def deletar_autor(id):
    autor = sessao.query(Autor).filter_by(id=id).first()
    if autor:
        sessao.delete(autor)
        sessao.commit()

def adicionar_editora(nome, endereco):
    editora_nova = Editora(nome=nome, endereco=endereco)
    sessao.add(editora_nova)
    sessao.commit()

def consultar_editoras():
    return sessao.query(Editora).all()

def atualizar_editora(id, nome=None, endereco=None):
    editora = sessao.query(Editora).filter_by(id=id).first()
    if editora:
        if nome:
            editora.nome = nome
        if endereco:
            editora.endereco = endereco
        sessao.commit()

def deletar_editora(id):
    editora = sessao.query(Editora).filter_by(id=id).first()
    if editora:
        sessao.delete(editora)
        sessao.commit()

def adicionar_livro(titulo, sinopse, preco, autor_id, editora_id, frete_id):
    livro_novo = Livro(titulo=titulo, sinopse=sinopse, preco=preco, autor_id=autor_id, editora_id=editora_id, frete_id=frete_id)
    sessao.add(livro_novo)
    sessao.commit()

def consultar_livros():
    return sessao.query(Livro).all()

def atualizar_livro(id, titulo=None, sinopse=None, preco=None):
    livro = sessao.query(Livro).filter_by(id=id).first()
    if livro:
        if titulo:
            livro.titulo = titulo
        if sinopse:
            livro.sinopse = sinopse
        if preco is not None:
            livro.preco = preco
        sessao.commit()

def deletar_livro(id):
    livro = sessao.query(Livro).filter_by(id=id).first()
    if livro:
        sessao.delete(livro)
        sessao.commit()

def adicionar_frete(custo, metodo):
    frete_novo = Frete(custo=custo, metodo=metodo)
    sessao.add(frete_novo)
    sessao.commit()

def consultar_fretes():
    return sessao.query(Frete).all()

def atualizar_frete(id, custo=None, metodo=None):
    frete = sessao.query(Frete).filter_by(id=id).first()
    if frete:
        if custo is not None:
            frete.custo = custo
        if metodo:
            frete.metodo = metodo
        sessao.commit()

def deletar_frete(id):
    frete = sessao.query(Frete).filter_by(id=id).first()
    if frete:
        sessao.delete(frete)
        sessao.commit()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gerenciamento de Livraria")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        self.label = QLabel("Escolha uma entidade para gerenciar:")

        self.btn_autores = QPushButton("Gerenciar Autores")
        self.btn_autores.clicked.connect(self.abrir_autores)

        self.btn_editoras = QPushButton("Gerenciar Editoras")
        self.btn_editoras.clicked.connect(self.abrir_editoras)

        self.btn_livros = QPushButton("Gerenciar Livros")
        self.btn_livros.clicked.connect(self.abrir_livros)

        self.btn_fretes = QPushButton("Gerenciar Fretes")
        self.btn_fretes.clicked.connect(self.abrir_fretes)

        layout.addWidget(self.label)
        layout.addWidget(self.btn_autores)
        layout.addWidget(self.btn_editoras)
        layout.addWidget(self.btn_livros)
        layout.addWidget(self.btn_fretes)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def abrir_autores(self):
        self.form_window = FormAutores()
        self.form_window.show()

    def abrir_editoras(self):
        self.form_window = FormEditoras()
        self.form_window.show()

    def abrir_livros(self):
        self.form_window = FormLivros()
        self.form_window.show()

    def abrir_fretes(self):
        self.form_window = FormFretes()
        self.form_window.show()

class EntityList(QWidget):
    def __init__(self, title, data_callback, delete_callback, update_callback, add_form_class):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(300, 300, 600, 400)

        layout = QVBoxLayout()

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['ID', 'Nome'])
        self.carregar_dados(data_callback)

        layout.addWidget(self.table)

        btn_add = QPushButton("Adicionar")
        btn_add.clicked.connect(lambda: self.abrir_formulario(add_form_class))

        btn_update = QPushButton("Atualizar")
        btn_update.clicked.connect(lambda: self.atualizar_dado(update_callback))

        btn_delete = QPushButton("Deletar")
        btn_delete.clicked.connect(lambda: self.deletar_dado(delete_callback))

        layout.addWidget(btn_add)
        layout.addWidget(btn_update)
        layout.addWidget(btn_delete)

        self.setLayout(layout)

    def carregar_dados(self, data_callback):
        dados = data_callback()
        self.table.setRowCount(len(dados))
        for row, item in enumerate(dados):
            self.table.setItem(row, 0, QTableWidgetItem(str(item.id)))
            self.table.setItem(row, 1, QTableWidgetItem(item.nome))

    def abrir_formulario(self, form_class):
        self.form = form_class()
        self.form.show()

    def atualizar_dado(self, update_callback):
        id, ok = QInputDialog.getInt(self, "Atualizar", "Digite o ID do item:")
        if ok:
            nome, ok_nome = QInputDialog.getText(self, "Atualizar", "Novo Nome:")
            if ok_nome:
                update_callback(id, nome)

    def deletar_dado(self, delete_callback):
        id, ok = QInputDialog.getInt(self, "Deletar", "Digite o ID do item:")
        if ok:
            delete_callback(id)

class FormAutores(EntityList):
    def __init__(self):
        super().__init__("Gerenciar Autores", consultar_autores, deletar_autor, atualizar_autor, FormAdicionarAutor)

class FormAdicionarAutor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Adicionar Autor")
        self.setGeometry(300, 300, 400, 200)

        layout = QFormLayout()

        self.nome_input = QLineEdit()
        self.biografia_input = QTextEdit()

        layout.addRow("Nome:", self.nome_input)
        layout.addRow("Biografia:", self.biografia_input)

        btn_salvar = QPushButton("Salvar")
        btn_salvar.clicked.connect(self.salvar_autor)

        layout.addWidget(btn_salvar)
        self.setLayout(layout)

    def salvar_autor(self):
        nome = self.nome_input.text()
        biografia = self.biografia_input.toPlainText()
        if nome:
            adicionar_autor(nome, biografia)
            QMessageBox.information(self, "Sucesso", "Autor adicionado com sucesso!")
            self.close()
        else:
            QMessageBox.warning(self, "Erro", "Nome do autor é obrigatório.")

if __name__ == '__main__':
    app = QApplication([])

    window = MainWindow()
    window.show()

    app.exec_()
