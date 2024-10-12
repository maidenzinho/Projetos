import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QStackedWidget, QLabel, QInputDialog,
    QTableWidget, QTableWidgetItem, QMessageBox
)
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Configurações do banco de dados
URLBANCO = "mysql+pymysql://root@localhost/mercearia"
motor = create_engine(URLBANCO)
Base = declarative_base()
Sessao = sessionmaker(bind=motor)
sessao = Sessao()

# Modelos
class Categoria(Base):
    __tablename__ = 'categorias'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    
    produtos = relationship('Produto', back_populates='categoria')

class Produto(Base):
    __tablename__ = 'produtos'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False)
    categoriaid = Column(Integer, ForeignKey('categorias.id'), nullable=False)
    
    categoria = relationship('Categoria', back_populates='produtos')

class Cliente(Base):
    __tablename__ = 'clientes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=False)
    
    vendas = relationship('Venda', back_populates='cliente')

class Venda(Base):
    __tablename__ = 'vendas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    produtoid = Column(Integer, ForeignKey('produtos.id'), nullable=False)
    clienteid = Column(Integer, ForeignKey('clientes.id'), nullable=False)
    quantidade = Column(Integer, nullable=False)
    
    produto = relationship('Produto')
    cliente = relationship('Cliente', back_populates='vendas')

# Função para criar tabelas
def criartabelas():
    Base.metadata.create_all(motor)

# Janela Principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Mercearia")
        self.setGeometry(100, 100, 800, 600)
        
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        
        self.add_main_menu()
        
    def add_main_menu(self):
        menu_widget = QWidget()
        layout = QVBoxLayout(menu_widget)

        btn_add_product = QPushButton("Adicionar Produto")
        btn_add_product.clicked.connect(self.add_product_screen)
        layout.addWidget(btn_add_product)

        btn_add_client = QPushButton("Adicionar Cliente")
        btn_add_client.clicked.connect(self.add_client_screen)
        layout.addWidget(btn_add_client)

        btn_add_sale = QPushButton("Adicionar Venda")
        btn_add_sale.clicked.connect(self.add_sale_screen)
        layout.addWidget(btn_add_sale)

        btn_list_products = QPushButton("Listar Produtos")
        btn_list_products.clicked.connect(self.list_products)
        layout.addWidget(btn_list_products)

        btn_list_clients = QPushButton("Listar Clientes")
        btn_list_clients.clicked.connect(self.list_clients)
        layout.addWidget(btn_list_clients)

        btn_list_sales = QPushButton("Listar Vendas")
        btn_list_sales.clicked.connect(self.list_sales)
        layout.addWidget(btn_list_sales)

        self.stacked_widget.addWidget(menu_widget)

    def add_product_screen(self):
        product_widget = QWidget()
        layout = QVBoxLayout(product_widget)

        btn_add_product = QPushButton("Criar Produto")
        btn_add_product.clicked.connect(self.create_product)
        layout.addWidget(btn_add_product)

        btn_back = QPushButton("Voltar")
        btn_back.clicked.connect(self.add_main_menu)
        layout.addWidget(btn_back)

        self.stacked_widget.addWidget(product_widget)
        self.stacked_widget.setCurrentWidget(product_widget)

    def add_client_screen(self):
        client_widget = QWidget()
        layout = QVBoxLayout(client_widget)

        btn_add_client = QPushButton("Criar Cliente")
        btn_add_client.clicked.connect(self.create_client)
        layout.addWidget(btn_add_client)

        btn_back = QPushButton("Voltar")
        btn_back.clicked.connect(self.add_main_menu)
        layout.addWidget(btn_back)

        self.stacked_widget.addWidget(client_widget)
        self.stacked_widget.setCurrentWidget(client_widget)

    def add_sale_screen(self):
        sale_widget = QWidget()
        layout = QVBoxLayout(sale_widget)

        btn_add_sale = QPushButton("Criar Venda")
        btn_add_sale.clicked.connect(self.create_sale)
        layout.addWidget(btn_add_sale)

        btn_back = QPushButton("Voltar")
        btn_back.clicked.connect(self.add_main_menu)
        layout.addWidget(btn_back)

        self.stacked_widget.addWidget(sale_widget)
        self.stacked_widget.setCurrentWidget(sale_widget)

    def create_product(self):
        nome, ok = QInputDialog.getText(self, 'Criar Produto', 'Digite o nome do produto:')
        if ok:
            preco, ok = QInputDialog.getDouble(self, 'Criar Produto', 'Digite o preço do produto:')
            if ok:
                estoque, ok = QInputDialog.getInt(self, 'Criar Produto', 'Digite a quantidade em estoque:')
                if ok:
                    categoriaid, ok = QInputDialog.getInt(self, 'Criar Produto', 'Digite o ID da categoria:')
                    if ok:
                        produto = Produto(nome=nome, preco=preco, estoque=estoque, categoriaid=categoriaid)
                        sessao.add(produto)
                        sessao.commit()
                        QMessageBox.information(self, 'Sucesso', 'Produto criado com sucesso!')

    def create_client(self):
        nome, ok = QInputDialog.getText(self, 'Criar Cliente', 'Digite o nome do cliente:')
        if ok:
            email, ok = QInputDialog.getText(self, 'Criar Cliente', 'Digite o e-mail do cliente:')
            if ok:
                telefone, ok = QInputDialog.getText(self, 'Criar Cliente', 'Digite o telefone do cliente:')
                if ok:
                    cliente = Cliente(nome=nome, email=email, telefone=telefone)
                    sessao.add(cliente)
                    sessao.commit()
                    QMessageBox.information(self, 'Sucesso', 'Cliente criado com sucesso!')

    def create_sale(self):
        produto_id, ok_produto = QInputDialog.getInt(self, 'Criar Venda', 'Digite o ID do produto:')
        if ok_produto:
            cliente_id, ok_cliente = QInputDialog.getInt(self, 'Criar Venda', 'Digite o ID do cliente:')
            if ok_cliente:
                quantidade, ok_quantidade = QInputDialog.getInt(self, 'Criar Venda', 'Digite a quantidade:')
                if ok_quantidade:
                    venda = Venda(produtoid=produto_id, clienteid=cliente_id, quantidade=quantidade)
                    sessao.add(venda)
                    sessao.commit()
                    QMessageBox.information(self, 'Sucesso', 'Venda criada com sucesso!')

    def list_products(self):
        produtos = sessao.query(Produto).all()
        self.show_table(produtos, ['ID', 'Nome', 'Preço', 'Estoque', 'Categoria ID'])

    def list_clients(self):
        clientes = sessao.query(Cliente).all()
        self.show_table(clientes, ['ID', 'Nome', 'Email', 'Telefone'])

    def list_sales(self):
        vendas = sessao.query(Venda).all()
        self.show_table(vendas, ['ID', 'Produto ID', 'Cliente ID', 'Quantidade'])

    def show_table(self, data, headers):
        self.stacked_widget.setCurrentIndex(0)  # Muda para o índice inicial
        table = QTableWidget()
        table.setColumnCount(len(headers))
        table.setRowCount(len(data))
        table.setHorizontalHeaderLabels(headers)

        for row_idx, row_data in enumerate(data):
            if isinstance(row_data, Cliente):
                table.setItem(row_idx, 0, QTableWidgetItem(str(row_data.id)))
                table.setItem(row_idx, 1, QTableWidgetItem(row_data.nome))
                table.setItem(row_idx, 2, QTableWidgetItem(row_data.email))
                table.setItem(row_idx, 3, QTableWidgetItem(row_data.telefone))
            elif isinstance(row_data, Produto):
                table.setItem(row_idx, 0, QTableWidgetItem(str(row_data.id)))
                table.setItem(row_idx, 1, QTableWidgetItem(row_data.nome))
                table.setItem(row_idx, 2, QTableWidgetItem(str(row_data.preco)))
                table.setItem(row_idx, 3, QTableWidgetItem(str(row_data.estoque)))
                table.setItem(row_idx, 4, QTableWidgetItem(str(row_data.categoriaid)))
            elif isinstance(row_data, Venda):
                table.setItem(row_idx, 0, QTableWidgetItem(str(row_data.id)))
                table.setItem(row_idx, 1, QTableWidgetItem(str(row_data.produtoid)))
                table.setItem(row_idx, 2, QTableWidgetItem(str(row_data.clienteid)))
                table.setItem(row_idx, 3, QTableWidgetItem(str(row_data.quantidade)))

        self.stacked_widget.addWidget(table)
        self.stacked_widget.setCurrentWidget(table)

if __name__ == "__main__":
    criartabelas()
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    sys.exit(app.exec_())
