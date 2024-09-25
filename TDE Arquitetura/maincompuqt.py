import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Text, Numeric, ForeignKey
from sqlalchemy.orm import relationship

DATABASE_URL = "mysql+pymysql://root:@localhost/tde"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    nome = Column(String(255), nullable=False)
    telefone = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    pets = relationship('Pet', back_populates='dono')

class Pet(Base):
    __tablename__ = 'pets'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    especie = Column(String(255), nullable=False)
    raca = Column(String(255), default=None)
    idade = Column(Integer, default=None)
    id_dono = Column(Integer, ForeignKey('clientes.id'))
    dono = relationship('Cliente', back_populates='pets')

class Servico(Base):
    __tablename__ = 'servicos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255), nullable=False)
    descricao = Column(Text, default=None)
    preco = Column(Numeric(10, 2), nullable=False)

class Taxidog(Base):
    __tablename__ = 'taxidog'
    id = Column(Integer, primary_key=True, autoincrement=True)
    preco = Column(Numeric(10, 2), nullable=False)
    tempo_ida = Column(Integer, nullable=False)
    tempo_volta = Column(Integer, nullable=False)

Base.metadata.create_all(engine)

class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Petshop")
        self.setGeometry(100, 100, 400, 400)

        self.secao_menu = QLabel("Escolha uma seção:")
        self.combobox_secao = QComboBox()
        self.combobox_secao.addItems(["Cliente", "Pet", "Serviço", "TaxiDog"])
        self.combobox_secao.currentIndexChanged.connect(self.alterar_secao)

        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.secao_menu)
        self.layout_principal.addWidget(self.combobox_secao)

        self.widget_secao = QWidget()
        self.layout_secao = QVBoxLayout()
        self.widget_secao.setLayout(self.layout_secao)
        self.layout_principal.addWidget(self.widget_secao)

        self.setLayout(self.layout_principal)
        self.alterar_secao()

    def alterar_secao(self):
        secao = self.combobox_secao.currentText()
        self.limpar_secao()

        if secao == "Cliente":
            self.secao_cliente()
        elif secao == "Pet":
            self.secao_pet()
        elif secao == "Serviço":
            self.secao_servico()
        elif secao == "TaxiDog":
            self.secao_taxidog()

    def limpar_secao(self):
        for i in reversed(range(self.layout_secao.count())):
            widget = self.layout_secao.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def secao_cliente(self):
        self.nome_label = QLabel("Nome:")
        self.nome_input = QLineEdit()

        self.telefone_label = QLabel("Telefone:")
        self.telefone_input = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        self.botao_adicionar_cliente = QPushButton("Adicionar Cliente")
        self.botao_adicionar_cliente.clicked.connect(self.adicionar_cliente)

        self.botao_atualizar_cliente = QPushButton("Atualizar Cliente")
        self.botao_atualizar_cliente.clicked.connect(self.atualizar_cliente)

        self.layout_secao.addWidget(self.nome_label)
        self.layout_secao.addWidget(self.nome_input)
        self.layout_secao.addWidget(self.telefone_label)
        self.layout_secao.addWidget(self.telefone_input)
        self.layout_secao.addWidget(self.email_label)
        self.layout_secao.addWidget(self.email_input)
        self.layout_secao.addWidget(self.botao_adicionar_cliente)
        self.layout_secao.addWidget(self.botao_atualizar_cliente)

    def adicionar_cliente(self):
        nome = self.nome_input.text()
        telefone = self.telefone_input.text()
        email = self.email_input.text()
        if nome and telefone and email:
            novo_cliente = Cliente(nome=nome, telefone=telefone, email=email)
            session.add(novo_cliente)
            session.commit()
            QMessageBox.information(self, "Sucesso", f"Cliente '{nome}' adicionado com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos")

    def atualizar_cliente(self):
        email = self.email_input.text()
        cliente = session.query(Cliente).filter(Cliente.email == email).first()
        if cliente:
            nome = self.nome_input.text()
            telefone = self.telefone_input.text()
            if nome:
                cliente.nome = nome
            if telefone:
                cliente.telefone = telefone
            session.commit()
            QMessageBox.information(self, "Sucesso", f"Cliente '{email}' atualizado com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", f"Cliente com email '{email}' não encontrado.")

    def secao_pet(self):
        self.nome_pet_label = QLabel("Nome do Pet:")
        self.nome_pet_input = QLineEdit()

        self.especie_label = QLabel("Espécie:")
        self.especie_input = QLineEdit()

        self.raca_label = QLabel("Raça:")
        self.raca_input = QLineEdit()

        self.idade_label = QLabel("Idade:")
        self.idade_input = QLineEdit()

        self.dono_label = QLabel("ID do Dono:")
        self.dono_input = QLineEdit()

        self.botao_adicionar_pet = QPushButton("Adicionar Pet")
        self.botao_adicionar_pet.clicked.connect(self.adicionar_pet)

        self.botao_atualizar_pet = QPushButton("Atualizar Pet")
        self.botao_atualizar_pet.clicked.connect(self.atualizar_pet)

        self.layout_secao.addWidget(self.nome_pet_label)
        self.layout_secao.addWidget(self.nome_pet_input)
        self.layout_secao.addWidget(self.especie_label)
        self.layout_secao.addWidget(self.especie_input)
        self.layout_secao.addWidget(self.raca_label)
        self.layout_secao.addWidget(self.raca_input)
        self.layout_secao.addWidget(self.idade_label)
        self.layout_secao.addWidget(self.idade_input)
        self.layout_secao.addWidget(self.dono_label)
        self.layout_secao.addWidget(self.dono_input)
        self.layout_secao.addWidget(self.botao_adicionar_pet)
        self.layout_secao.addWidget(self.botao_atualizar_pet)

    def adicionar_pet(self):
        nome = self.nome_pet_input.text()
        especie = self.especie_input.text()
        raca = self.raca_input.text()
        idade = self.idade_input.text()
        id_dono = self.dono_input.text()
        if nome and especie and id_dono:
            novo_pet = Pet(nome=nome, especie=especie, raca=raca, idade=idade, id_dono=id_dono)
            session.add(novo_pet)
            session.commit()
            QMessageBox.information(self, "Sucesso", f"Pet '{nome}' adicionado com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", "Preencha os campos obrigatórios.")

    def atualizar_pet(self):
        id_dono = self.dono_input.text()
        pet = session.query(Pet).filter(Pet.id_dono == id_dono).first()
        if pet:
            nome = self.nome_pet_input.text()
            especie = self.especie_input.text()
            raca = self.raca_input.text()
            idade = self.idade_input.text()
            if nome:
                pet.nome = nome
            if especie:
                pet.especie = especie
            if raca:
                pet.raca = raca
            if idade:
                pet.idade = idade
            session.commit()
            QMessageBox.information(self, "Sucesso", f"Pet atualizado com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", f"Pet não encontrado.")

    def secao_servico(self):
        self.nome_servico_label = QLabel("Nome do Serviço:")
        self.nome_servico_input = QLineEdit()

        self.descricao_label = QLabel("Descrição:")
        self.descricao_input = QLineEdit()

        self.preco_label = QLabel("Preço:")
        self.preco_input = QLineEdit()

        self.botao_adicionar_servico = QPushButton("Adicionar Serviço")
        self.botao_adicionar_servico.clicked.connect(self.adicionar_servico)

        self.botao_atualizar_servico = QPushButton("Atualizar Serviço")
        self.botao_atualizar_servico.clicked.connect(self.atualizar_servico)

        self.layout_secao.addWidget(self.nome_servico_label)
        self.layout_secao.addWidget(self.nome_servico_input)
        self.layout_secao.addWidget(self.descricao_label)
        self.layout_secao.addWidget(self.descricao_input)
        self.layout_secao.addWidget(self.preco_label)
        self.layout_secao.addWidget(self.preco_input)
        self.layout_secao.addWidget(self.botao_adicionar_servico)
        self.layout_secao.addWidget(self.botao_atualizar_servico)

    def adicionar_servico(self):
        nome = self.nome_servico_input.text()
        descricao = self.descricao_input.text()
        preco = self.preco_input.text()
        if nome and preco:
            novo_servico = Servico(nome=nome, descricao=descricao, preco=preco)
            session.add(novo_servico)
            session.commit()
            QMessageBox.information(self, "Sucesso", f"Serviço '{nome}' adicionado com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", "Preencha os campos obrigatórios.")

    def atualizar_servico(self):
        nome = self.nome_servico_input.text()
        servico = session.query(Servico).filter(Servico.nome == nome).first()
        if servico:
            descricao = self.descricao_input.text()
            preco = self.preco_input.text()
            if descricao:
                servico.descricao = descricao
            if preco:
                servico.preco = preco
            session.commit()
            QMessageBox.information(self, "Sucesso", f"Serviço '{nome}' atualizado com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", f"Serviço '{nome}' não encontrado.")

    def secao_taxidog(self):
        self.preco_taxidog_label = QLabel("Preço do TaxiDog:")
        self.preco_taxidog_input = QLineEdit()

        self.tempo_ida_label = QLabel("Tempo de Ida:")
        self.tempo_ida_input = QLineEdit()

        self.tempo_volta_label = QLabel("Tempo de Volta:")
        self.tempo_volta_input = QLineEdit()

        self.botao_adicionar_taxidog = QPushButton("Adicionar TaxiDog")
        self.botao_adicionar_taxidog.clicked.connect(self.adicionar_taxidog)

        self.botao_atualizar_taxidog = QPushButton("Atualizar TaxiDog")
        self.botao_atualizar_taxidog.clicked.connect(self.atualizar_taxidog)

        self.layout_secao.addWidget(self.preco_taxidog_label)
        self.layout_secao.addWidget(self.preco_taxidog_input)
        self.layout_secao.addWidget(self.tempo_ida_label)
        self.layout_secao.addWidget(self.tempo_ida_input)
        self.layout_secao.addWidget(self.tempo_volta_label)
        self.layout_secao.addWidget(self.tempo_volta_input)
        self.layout_secao.addWidget(self.botao_adicionar_taxidog)
        self.layout_secao.addWidget(self.botao_atualizar_taxidog)

    def adicionar_taxidog(self):
        preco = self.preco_taxidog_input.text()
        tempo_ida = self.tempo_ida_input.text()
        tempo_volta = self.tempo_volta_input.text()
        if preco and tempo_ida and tempo_volta:
            novo_taxidog = Taxidog(preco=preco, tempo_ida=tempo_ida, tempo_volta=tempo_volta)
            session.add(novo_taxidog)
            session.commit()
            QMessageBox.information(self, "Sucesso", "TaxiDog adicionado com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")

    def atualizar_taxidog(self):
        preco = self.preco_taxidog_input.text()
        taxidog = session.query(Taxidog).filter(Taxidog.preco == preco).first()
        if taxidog:
            tempo_ida = self.tempo_ida_input.text()
            tempo_volta = self.tempo_volta_input.text()
            if tempo_ida:
                taxidog.tempo_ida = tempo_ida
            if tempo_volta:
                taxidog.tempo_volta = tempo_volta
            session.commit()
            QMessageBox.information(self, "Sucesso", "TaxiDog atualizado com sucesso!")
        else:
            QMessageBox.warning(self, "Erro", "TaxiDog não encontrado.")

def iniciar_interface():
    app = QApplication(sys.argv)
    interface = Interface()
    interface.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    iniciar_interface()
