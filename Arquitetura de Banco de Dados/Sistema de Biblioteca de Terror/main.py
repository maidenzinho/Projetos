import sys
import bcrypt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QListWidget, QInputDialog
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, Numeric
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

URL_BANCO = "mysql+pymysql://root:@localhost/tde"
engine = create_engine(URL_BANCO)
Base = declarative_base()

class Autor(Base):
    __tablename__ = 'autores_sombrios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    biografia = Column(Text)
    livros = relationship('Livro', back_populates='autor')

class Editora(Base):
    __tablename__ = 'editoras_assombradas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    endereco = Column(String(255))
    livros = relationship('Livro', back_populates='editora')

class Frete(Base):
    __tablename__ = 'fretes_do_inferno'
    id = Column(Integer, primary_key=True, autoincrement=True)
    custo = Column(Numeric(10, 2))
    metodo = Column(String(255))
    livros = relationship('Livro', back_populates='frete')

class Livro(Base):
    __tablename__ = 'livros_malditos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    sinopse = Column(Text)
    preco = Column(Numeric(10, 2))
    autor_id = Column(Integer, ForeignKey('autores_sombrios.id'), nullable=False)
    editora_id = Column(Integer, ForeignKey('editoras_assombradas.id'), nullable=False)
    frete_id = Column(Integer, ForeignKey('fretes_do_inferno.id'))

    autor = relationship('Autor', back_populates='livros')
    editora = relationship('Editora', back_populates='livros')
    frete = relationship('Frete', back_populates='livros')

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
sessao = Session()

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.label_username = QLabel('Nome de Usuário:')
        self.input_username = QLineEdit()
        self.label_password = QLabel('Senha:')
        self.input_password = QLineEdit()
        self.input_password.setEchoMode(QLineEdit.Password)

        self.botao_login = QPushButton('Login')
        self.botao_adicionar_usuario = QPushButton('Adicionar Usuário')

        layout.addWidget(self.label_username)
        layout.addWidget(self.input_username)
        layout.addWidget(self.label_password)
        layout.addWidget(self.input_password)
        layout.addWidget(self.botao_login)
        layout.addWidget(self.botao_adicionar_usuario)

        self.setLayout(layout)

        self.botao_login.clicked.connect(self.login)
        self.botao_adicionar_usuario.clicked.connect(self.adicionar_usuario)

    def adicionar_usuario(self):
        username, ok1 = QInputDialog.getText(self, 'Adicionar Usuário', 'Nome de Usuário:')
        password, ok2 = QInputDialog.getText(self, 'Adicionar Usuário', 'Senha:', QLineEdit.Password)
        role, ok3 = QInputDialog.getItem(self, 'Adicionar Usuário', 'Papel:', ['gerente', 'funcionario'], 0, False)

        if ok1 and ok2 and ok3 and username and password:

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
            novo_usuario = Usuario(username=username, password=hashed_password.decode('utf-8'), role=role)
            sessao.add(novo_usuario)
            sessao.commit()
            QMessageBox.information(self, 'Sucesso', 'Usuário adicionado com sucesso!')

    def login(self):
        username = self.input_username.text()
        password = self.input_password.text()

        usuario = sessao.query(Usuario).filter_by(username=username).first()

        if usuario and bcrypt.checkpw(password.encode('utf-8'), usuario.password.encode('utf-8')):
            self.close()
            self.main_app = MainApp(is_manager=(usuario.role == 'gerente'))
            self.main_app.show()
        else:
            QMessageBox.warning(self, 'Erro', 'Usuário ou senha incorretos! O terror está à espreita!')

class MainApp(QWidget):
    def __init__(self, is_manager):
        super().__init__()
        self.is_manager = is_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Sistema de Gerenciamento de Livros Malditos')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.botao_autores = QPushButton('Visualizar Autores Sombrio', self)
        self.botao_editoras = QPushButton('Visualizar Editoras Assombradas', self)
        self.botao_livros = QPushButton('Visualizar Livros Malditos', self)
        self.botao_fretes = QPushButton('Visualizar Fretes do Inferno', self)

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

class AutorApp(QWidget):
    def __init__(self, is_manager):
        super().__init__()
        self.is_manager = is_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Autores das Trevas')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.lista_autores = QListWidget(self)
        self.carregar_autores()

        layout.addWidget(self.lista_autores)

        if self.is_manager:
            self.botao_adicionar = QPushButton('Adicionar Autor Maldito', self)
            self.botao_adicionar.clicked.connect(self.adicionar_autor)
            layout.addWidget(self.botao_adicionar)

            self.botao_remover = QPushButton('Remover Autor das Sombras', self)
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

class EditoraApp(QWidget):
    def __init__(self, is_manager):
        super().__init__()
        self.is_manager = is_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Editoras Assombradas')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.lista_editoras = QListWidget(self)
        self.carregar_editoras()

        layout.addWidget(self.lista_editoras)

        if self.is_manager:
            self.botao_adicionar = QPushButton('Adicionar Editora Maldita', self)
            self.botao_adicionar.clicked.connect(self.adicionar_editora)
            layout.addWidget(self.botao_adicionar)

            self.botao_remover = QPushButton('Remover Editora das Sombras', self)
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
            sessao.delete(editora)
            sessao.commit()
            self.carregar_editoras()

class LivroApp(QWidget):
    def __init__(self, is_manager):
        super().__init__()
        self.is_manager = is_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Livros Malditos')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.lista_livros = QListWidget(self)
        self.carregar_livros()

        layout.addWidget(self.lista_livros)

        if self.is_manager:
            self.botao_adicionar = QPushButton('Adicionar Livro Maldito', self)
            self.botao_adicionar.clicked.connect(self.adicionar_livro)
            layout.addWidget(self.botao_adicionar)

            self.botao_remover = QPushButton('Remover Livro das Sombras', self)
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
            novo_livro = Livro(titulo=titulo, sinopse=f"{sinopse} (Um conto de terror)", preco=preco)
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

class FreteApp(QWidget):
    def __init__(self, is_manager):
        super().__init__()
        self.is_manager = is_manager
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Fretes do Inferno')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()
        self.lista_fretes = QListWidget(self)
        self.carregar_fretes()

        layout.addWidget(self.lista_fretes)

        if self.is_manager:
            self.botao_adicionar = QPushButton('Adicionar Frete Maldito', self)
            self.botao_adicionar.clicked.connect(self.adicionar_frete)
            layout.addWidget(self.botao_adicionar)

            self.botao_remover = QPushButton('Remover Frete das Sombras', self)
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
            novo_frete = Frete(metodo=f"{metodo} (do além)", custo=custo)
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
    login_app = LoginWindow()
    login_app.show()
    sys.exit(app.exec_())