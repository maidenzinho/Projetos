import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QListWidget, QFormLayout, QComboBox
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Configuração do banco de dados
URL_BANCO = "mysql+pymysql://root:@localhost/tde"
engine = create_engine(URL_BANCO)
Base = declarative_base()

# Modelos de dados
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

class Frete(Base):
    __tablename__ = 'fretes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    custo = Column(Numeric(10, 2))
    metodo = Column(String(255))
    livros = relationship('Livro', back_populates='frete')

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

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
sessao = Session()

# Classe de Login
class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.username_input = QLineEdit(self)
        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.Password)

        username_label = QLabel('Usuário:')
        password_label = QLabel('Senha:')

        login_button = QPushButton('Login', self)
        login_button.clicked.connect(self.login)

        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Consultar o banco de dados para verificar as credenciais
        usuario = sessao.query(Usuario).filter_by(username=username, password=password).first()

        if usuario:
            self.close()
            self.main_app = MainApp(is_manager=(usuario.role == 'gerente'))
            self.main_app.show()
        else:
            QMessageBox.warning(self, 'Erro', 'Usuário ou senha incorretos!')

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)  # Pode ser 'gerente' ou 'bibliotecario'

# Classe Principal
class MainApp(QWidget):
    def __init__(self, is_manager):
        super().__init__()
        self.is_manager = is_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Sistema de Gerenciamento de Livros')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.botao_autores = QPushButton('Visualizar Autores', self)
        self.botao_editoras = QPushButton('Visualizar Editoras', self)
        self.botao_livros = QPushButton('Visualizar Livros', self)
        self.botao_fretes = QPushButton('Visualizar Fretes', self)

        self.botao_autores.clicked.connect(self.abrir_autores)
        self.botao_editoras.clicked.connect(self.abrir_editoras)
        self.botao_livros.clicked.connect(self.abrir_livros)
        self.botao_fretes.clicked.connect(self.abrir_fretes)

        layout.addWidget(self.botao_autores)
        layout.addWidget(self.botao_editoras)
        layout.addWidget(self.botao_livros)
        layout.addWidget(self.botao_fretes)

        self.setLayout(layout)

    def abrir_autores(self):
        self.autor_window = AutorApp(is_manager=self.is_manager)
        self.autor_window.show()

    def abrir_editoras(self):
        self.editora_window = EditoraApp(is_manager=self.is_manager)
        self.editora_window.show()

    def abrir_livros(self):
        self.livro_window = LivroApp(is_manager=self.is_manager)
        self.livro_window.show()

    def abrir_fretes(self):
        self.frete_window = FreteApp(is_manager=self.is_manager)
        self.frete_window.show()

# Classe AutorApp
class AutorApp(QWidget):
    def __init__(self, is_manager):
        super().__init__()
        self.is_manager = is_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Autores')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.lista_autores = QListWidget(self)
        self.carregar_autores()

        layout.addWidget(self.lista_autores)

        if self.is_manager:
            self.botao_adicionar = QPushButton('Adicionar Autor', self)
            self.botao_adicionar.clicked.connect(self.adicionar_autor)
            layout.addWidget(self.botao_adicionar)

            self.botao_remover = QPushButton('Remover Autor', self)
            self.botao_remover.clicked.connect(self.remover_autor)
            layout.addWidget(self.botao_remover)

        self.setLayout(layout)

    def carregar_autores(self):
        self.lista_autores.clear()
        autores = sessao.query(Autor).all()
        for autor in autores:
            self.lista_autores.addItem(autor.nome)

    def adicionar_autor(self):
        nome, ok = QInputDialog.getText(self, 'Adicionar Autor', 'Nome do Autor:')
        if ok and nome:
            novo_autor = Autor(nome=nome)
            sessao.add(novo_autor)
            sessao.commit()
            self.carregar_autores()

    def remover_autor(self):
        autor_selecionado = self.lista_autores.currentItem()
        if autor_selecionado:
            autor = sessao.query(Autor).filter_by(nome=autor_selecionado.text()).first()
            sessao.delete(autor)
            sessao.commit()
            self.carregar_autores()

# Classe EditoraApp
class EditoraApp(QWidget):
    def __init__(self, is_manager):
        super().__init__()
        self.is_manager = is_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Editoras')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.lista_editoras = QListWidget(self)
        self.carregar_editoras()

        layout.addWidget(self.lista_editoras)

        if self.is_manager:
            self.botao_adicionar = QPushButton('Adicionar Editora', self)
            self.botao_adicionar.clicked.connect(self.adicionar_editora)
            layout.addWidget(self.botao_adicionar)

            self.botao_remover = QPushButton('Remover Editora', self)
            self.botao_remover.clicked.connect(self.remover_editora)
            layout.addWidget(self.botao_remover)

        self.setLayout(layout)

    def carregar_editoras(self):
        self.lista_editoras.clear()
        editoras = sessao.query(Editora).all()
        for editora in editoras:
            self.lista_editoras.addItem(editora.nome)

    def adicionar_editora(self):
        nome, ok = QInputDialog.getText(self, 'Adicionar Editora', 'Nome da Editora:')
        if ok and nome:
            nova_editora = Editora(nome=nome)
            sessao.add(nova_editora)
            sessao.commit()
            self.carregar_editoras()

    def remover_editora(self):
        editora_selecionada = self.lista_editoras.currentItem()
        if editora_selecionada:
            editora = sessao.query(Editora).filter_by(nome=editora_selecionada.text()).first()
            sessao.delete(editora )
            sessao.commit()
            self.carregar_editoras()

# Classe LivroApp
class LivroApp(QWidget):
    def __init__(self, is_manager):
        super().__init__()
        self.is_manager = is_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Livros')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.lista_livros = QListWidget(self)
        self.carregar_livros()

        layout.addWidget(self.lista_livros)

        if self.is_manager:
            self.botao_adicionar = QPushButton('Adicionar Livro', self)
            self.botao_adicionar.clicked.connect(self.adicionar_livro)
            layout.addWidget(self.botao_adicionar)

            self.botao_remover = QPushButton('Remover Livro', self)
            self.botao_remover.clicked.connect(self.remover_livro)
            layout.addWidget(self.botao_remover)

        self.setLayout(layout)

    def carregar_livros(self):
        self.lista_livros.clear()
        livros = sessao.query(Livro).all()
        for livro in livros:
            self.lista_livros.addItem(livro.titulo)

    def adicionar_livro(self):
        titulo, ok1 = QInputDialog.getText(self, 'Adicionar Livro', 'Título do Livro:')
        sinopse, ok2 = QInputDialog.getText(self, 'Adicionar Livro', 'Sinopse do Livro:')
        preco, ok3 = QInputDialog.getDouble(self, 'Adicionar Livro', 'Preço do Livro:')
        if ok1 and ok2 and ok3 and titulo:
            novo_livro = Livro(titulo=titulo, sinopse=sinopse, preco=preco)
            sessao.add(novo_livro)
            sessao.commit()
            self.carregar_livros()

    def remover_livro(self):
        livro_selecionado = self.lista_livros.currentItem()
        if livro_selecionado:
            livro = sessao.query(Livro).filter_by(titulo=livro_selecionado.text()).first()
            sessao.delete(livro)
            sessao.commit()
            self.carregar_livros()

# Classe FreteApp
class FreteApp(QWidget):
    def __init__(self, is_manager):
        super().__init__()
        self.is_manager = is_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Fretes')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.lista_fretes = QListWidget(self)
        self.carregar_fretes()

        layout.addWidget(self.lista_fretes)

        if self.is_manager:
            self.botao_adicionar = QPushButton('Adicionar Frete', self)
            self.botao_adicionar.clicked.connect(self.adicionar_frete)
            layout.addWidget(self.botao_adicionar)

            self.botao_remover = QPushButton('Remover Frete', self)
            self.botao_remover.clicked.connect(self.remover_frete)
            layout.addWidget(self.botao_remover)

        self.setLayout(layout)

    def carregar_fretes(self):
        self.lista_fretes.clear()
        fretes = sessao.query(Frete).all()
        for frete in fretes:
            self.lista_fretes.addItem(frete.metodo)

    def adicionar_frete(self):
        metodo, ok1 = QInputDialog.getText(self, 'Adicionar Frete', 'Método de Frete:')
        custo, ok2 = QInputDialog.getDouble(self, 'Adicionar Frete', 'Custo do Frete:')
        if ok1 and ok2 and metodo:
            novo_frete = Frete(metodo=metodo, custo=custo)
            sessao.add(novo_frete)
            sessao.commit()
            self.carregar_fretes()

    def remover_frete(self):
        frete_selecionado = self.lista_fretes.currentItem()
        if frete_selecionado:
            frete = sessao.query(Frete).filter_by(metodo=frete_selecionado.text()).first()
            sessao.delete(frete)
            sessao.commit()
            self.carregar_fretes()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_app = LoginApp()
    login_app.show()
    sys.exit(app.exec_())