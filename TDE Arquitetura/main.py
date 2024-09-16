import os
import time
from sqlalchemy import create_engine, Column, Integer, String, Text, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

DATABASE_URL = "mysql+pymysql://root:@localhost/tde"

engine = create_engine(DATABASE_URL)
Base = declarative_base()
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
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

def limpar_terminal():
    sistema = os.name
    if sistema == 'posix':
        os.system('clear')
    elif sistema == 'nt':
        os.system('cls')

def adicionar_cliente(nome, telefone, email):
    novo_cliente = Cliente(nome=nome, telefone=telefone, email=email)
    session.add(novo_cliente)
    session.commit()
    print(f"Cliente '{nome}' adicionado com sucesso!")

def ler_cliente(id_cliente):
    cliente = session.query(Cliente).filter(Cliente.id == id_cliente).first()
    if cliente:
        return cliente
    print(f"Cliente com ID {id_cliente} não encontrado.")
    return None

def atualizar_cliente(id_cliente, nome=None, telefone=None, email=None):
    cliente = session.query(Cliente).filter(Cliente.id == id_cliente).first()
    if cliente:
        if nome:
            cliente.nome = nome
        if telefone:
            cliente.telefone = telefone
        if email:
            cliente.email = email
        session.commit()
        print(f"Cliente '{id_cliente}' atualizado com sucesso!")
    else:
        print(f"Cliente com ID {id_cliente} não encontrado.")

def deletar_cliente(id_cliente):
    cliente = session.query(Cliente).filter(Cliente.id == id_cliente).first()
    if cliente:
        session.delete(cliente)
        session.commit()
        print(f"Cliente '{id_cliente}' deletado com sucesso!")
    else:
        print(f"Cliente com ID {id_cliente} não encontrado.")

def adicionar_pet(nome, especie, raca, idade, id_dono):
    novo_pet = Pet(nome=nome, especie=especie, raca=raca, idade=idade, id_dono=id_dono)
    session.add(novo_pet)
    session.commit()
    print(f"Pet '{nome}' adicionado com sucesso!")

def ler_pet(id_pet):
    pet = session.query(Pet).filter(Pet.id == id_pet).first()
    if pet:
        return pet
    print(f"Pet com ID {id_pet} não encontrado.")
    return None

def atualizar_pet(id_pet, nome=None, especie=None, raca=None, idade=None, id_dono=None):
    pet = session.query(Pet).filter(Pet.id == id_pet).first()
    if pet:
        if nome:
            pet.nome = nome
        if especie:
            pet.especie = especie
        if raca:
            pet.raca = raca
        if idade is not None:
            pet.idade = idade
        if id_dono is not None:
            pet.id_dono = id_dono
        session.commit()
        print(f"Pet '{id_pet}' atualizado com sucesso!")
    else:
        print(f"Pet com ID {id_pet} não encontrado.")

def deletar_pet(id_pet):
    pet = session.query(Pet).filter(Pet.id == id_pet).first()
    if pet:
        session.delete(pet)
        session.commit()
        print(f"Pet '{id_pet}' deletado com sucesso!")
    else:
        print(f"Pet com ID {id_pet} não encontrado.")

def adicionar_servico(nome, descricao, preco):
    novo_servico = Servico(nome=nome, descricao=descricao, preco=preco)
    session.add(novo_servico)
    session.commit()
    print(f"Serviço '{nome}' adicionado com sucesso!")

def ler_servico(id_servico):
    servico = session.query(Servico).filter(Servico.id == id_servico).first()
    if servico:
        return servico
    print(f"Serviço com ID {id_servico} não encontrado.")
    return None

def atualizar_servico(id_servico, nome=None, descricao=None, preco=None):
    servico = session.query(Servico).filter(Servico.id == id_servico).first()
    if servico:
        if nome:
            servico.nome = nome
        if descricao:
            servico.descricao = descricao
        if preco is not None:
            servico.preco = preco
        session.commit()
        print(f"Serviço '{id_servico}' atualizado com sucesso!")
    else:
        print(f"Serviço com ID {id_servico} não encontrado.")

def deletar_servico(id_servico):
    servico = session.query(Servico).filter(Servico.id == id_servico).first()
    if servico:
        session.delete(servico)
        session.commit()
        print(f"Serviço '{id_servico}' deletado com sucesso!")
    else:
        print(f"Serviço com ID {id_servico} não encontrado.")

def adicionar_taxidog(preco, tempo_ida, tempo_volta):
    nova_taxa = Taxidog(preco=preco, tempo_ida=tempo_ida, tempo_volta=tempo_volta)
    session.add(nova_taxa)
    session.commit()
    print("Taxa de transporte adicionada com sucesso!")

def ler_taxidog(id_taxa):
    taxa = session.query(Taxidog).filter(Taxidog.id == id_taxa).first()
    if taxa:
        return taxa
    print(f"Taxa com ID {id_taxa} não encontrada.")
    return None

def atualizar_taxidog(id_taxa, preco=None, tempo_ida=None, tempo_volta=None):
    taxa = session.query(Taxidog).filter(Taxidog.id == id_taxa).first()
    if taxa:
        if preco is not None:
            taxa.preco = preco
        if tempo_ida is not None:
            taxa.tempo_ida = tempo_ida
        if tempo_volta is not None:
            taxa.tempo_volta = tempo_volta
        session.commit()
        print(f"Taxa de transporte '{id_taxa}' atualizada com sucesso!")
    else:
        print(f"Taxa com ID {id_taxa} não encontrada.")

def deletar_taxidog(id_taxa):
    taxa = session.query(Taxidog).filter(Taxidog.id == id_taxa).first()
    if taxa:
        session.delete(taxa)
        session.commit()
        print(f"Taxa de transporte '{id_taxa}' deletada com sucesso!")
    else:
        print(f"Taxa com ID {id_taxa} não encontrada.")

def principal():
    while True:
        limpar_terminal()
        print("\nMenu do Petshop")
        print("1. Adicionar Cliente")
        print("2. Ler Cliente")
        print("3. Atualizar Cliente")
        print("4. Deletar Cliente")
        print("5. Adicionar Pet")
        print("6. Ler Pet")
        print("7. Atualizar Pet")
        print("8. Deletar Pet")
        print("9. Adicionar Serviço")
        print("10. Ler Serviço")
        print("11. Atualizar Serviço")
        print("12. Deletar Serviço")
        print("13. Adicionar Taxa de Transporte")
        print("14. Ler Taxa de Transporte")
        print("15. Atualizar Taxa de Transporte")
        print("16. Deletar Taxa de Transporte")
        print("0. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == "0":
            break
        
        if escolha == "1":
            nome = input("Nome do cliente: ")
            telefone = input("Telefone do cliente: ")
            email = input("Email do cliente: ")
            adicionar_cliente(nome, telefone, email)
        
        elif escolha == "2":
            id_cliente = int(input("ID do cliente: "))
            cliente = ler_cliente(id_cliente)
            if cliente:
                print(f"ID: {cliente.id}, Nome: {cliente.nome}, Telefone: {cliente.telefone}, Email: {cliente.email}")
        
        elif escolha == "3":
            id_cliente = int(input("ID do cliente: "))
            nome = input("Novo nome (deixe em branco para não alterar): ")
            telefone = input("Novo telefone (deixe em branco para não alterar): ")
            email = input("Novo email (deixe em branco para não alterar): ")
            atualizar_cliente(id_cliente, nome if nome else None, telefone if telefone else None, email if email else None)
        
        elif escolha == "4":
            id_cliente = int(input("ID do cliente: "))
            deletar_cliente(id_cliente)
        
        elif escolha == "5":
            nome = input("Nome do pet: ")
            especie = input("Espécie do pet: ")
            raca = input("Raça do pet: ")
            idade = int(input("Idade do pet: "))
            id_dono = int(input("ID do dono (cliente): "))
            adicionar_pet(nome, especie, raca, idade, id_dono)
        
        elif escolha == "6":
            id_pet = int(input("ID do pet: "))
            pet = ler_pet(id_pet)
            if pet:
                print(f"ID: {pet.id}, Nome: {pet.nome}, Espécie: {pet.especie}, Raça: {pet.raca}, Idade: {pet.idade}, ID do Dono: {pet.id_dono}")
        
        elif escolha == "7":
            id_pet = int(input("ID do pet: "))
            nome = input("Novo nome (deixe em branco para não alterar): ")
            especie = input("Nova espécie (deixe em branco para não alterar): ")
            raca = input("Nova raça (deixe em branco para não alterar): ")
            idade = input("Nova idade (deixe em branco para não alterar): ")
            id_dono = input("Novo ID do dono (deixe em branco para não alterar): ")
            atualizar_pet(id_pet, nome if nome else None, especie if especie else None, raca if raca else None, int(idade) if idade else None, int(id_dono) if id_dono else None)
        
        elif escolha == "8":
            id_pet = int(input("ID do pet: "))
            deletar_pet(id_pet)
        
        elif escolha == "9":
            nome = input("Nome do serviço: ")
            descricao = input("Descrição do serviço: ")
            preco = float(input("Preço do serviço: "))
            adicionar_servico(nome, descricao, preco)
        
        elif escolha == "10":
            id_servico = int(input("ID do serviço: "))
            servico = ler_servico(id_servico)
            if servico:
                print(f"ID: {servico.id}, Nome: {servico.nome}, Descrição: {servico.descricao}, Preço: {servico.preco}")
        
        elif escolha == "11":
            id_servico = int(input("ID do serviço: "))
            nome = input("Novo nome (deixe em branco para não alterar): ")
            descricao = input("Nova descrição (deixe em branco para não alterar): ")
            preco = input("Novo preço (deixe em branco para não alterar): ")
            atualizar_servico(id_servico, nome if nome else None, descricao if descricao else None, float(preco) if preco else None)
        
        elif escolha == "12":
            id_servico = int(input("ID do serviço: "))
            deletar_servico(id_servico)
        
        elif escolha == "13":
            preco = float(input("Preço da taxa de transporte: "))
            tempo_ida = int(input("Tempo de ida (em minutos): "))
            tempo_volta = int(input("Tempo de volta (em minutos): "))
            adicionar_taxidog(preco, tempo_ida, tempo_volta)
        
        elif escolha == "14":
            id_taxa = int(input("ID da taxa de transporte: "))
            taxa = ler_taxidog(id_taxa)
            if taxa:
                print(f"ID: {taxa.id}, Preço: {taxa.preco}, Tempo de Ida: {taxa.tempo_ida}, Tempo de Volta: {taxa.tempo_volta}")
        
        elif escolha == "15":
            id_taxa = int(input("ID da taxa de transporte: "))
            preco = input("Novo preço (deixe em branco para não alterar): ")
            tempo_ida = input("Novo tempo de ida (deixe em branco para não alterar): ")
            tempo_volta = input("Novo tempo de volta (deixe em branco para não alterar): ")
            atualizar_taxidog(id_taxa, float(preco) if preco else None, int(tempo_ida) if tempo_ida else None, int(tempo_volta) if tempo_volta else None)
        
        elif escolha == "16":
            id_taxa = int(input("ID da taxa de transporte: "))
            deletar_taxidog(id_taxa)

if __name__ == "__main__":
    principal()