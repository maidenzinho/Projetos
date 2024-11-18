import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QLabel, QPushButton, QLineEdit, QListWidget, QFormLayout, QMessageBox, QHBoxLayout,
    QFrame, QStackedWidget, QListWidgetItem
)
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Game:
    def __init__(self, name, price, discount, cover_link, purchase_date, purchase_id):
        self.name = name
        self.price = price
        self.discount = discount
        self.cover_link = cover_link
        self.purchase_date = purchase_date
        self.purchase_id = purchase_id

class GameManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciador de Jogos")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)

        self.init_sidebar()
        self.init_main_area()

        self.jogos = []
        self.carregar_jogos()

    def init_sidebar(self):
        self.sidebar = QFrame()
        self.sidebar.setFixedWidth(200)
        self.sidebar_layout = QVBoxLayout(self.sidebar)

        # Adicionando o logo em texto
        self.logo_label = QLabel("Maiden")
        self.logo_label.setStyleSheet("font-size: 24px; font-weight: bold; margin-bottom: 20px;")
        self.sidebar_layout.addWidget(self.logo_label)

        self.biblioteca_button = QPushButton("Biblioteca")
        self.biblioteca_button.clicked.connect(self.show_biblioteca)
        self.sidebar_layout.addWidget(self.biblioteca_button)

        self.adicionar_button = QPushButton("Adicionar Jogos")
        self.adicionar_button.clicked.connect(self.show_adicionar)
        self.sidebar_layout.addWidget(self.adicionar_button)

        self.configuracoes_button = QPushButton("Configurações")
        self.configuracoes_button.clicked.connect(self.show_configuracoes)
        self.sidebar_layout.addWidget(self.configuracoes_button)

        self.pesquisa_input = QLineEdit()
        self.pesquisa_input.setPlaceholderText("Pesquisar jogos...")
        self.pesquisa_input.textChanged.connect(self.pesquisar_jogos)
        self.sidebar_layout.addWidget(self.pesquisa_input)

        self.layout.addWidget(self.sidebar)

    def init_main_area(self):
        self.main_area = QStackedWidget()
        self.layout.addWidget(self.main_area)

        self.biblioteca_tab = QWidget()
        self.adicionar_tab = QWidget()
        self.configuracoes_tab = QWidget()

        self.init_biblioteca_tab()
        self.init_adicionar_tab()
        self.init_configuracoes_tab()

        self.main_area.addWidget(self.biblioteca_tab)
        self.main_area.addWidget(self.adicionar_tab)
        self.main_area.addWidget(self.configuracoes_tab)

    def init_biblioteca_tab(self):
        layout = QVBoxLayout()
        self.jogos_list = QListWidget()
        self.jogos_list.itemClicked.connect(self.mostrar_detalhes_jogo)
        layout.addWidget(self.jogos_list)

        self.detalhes_jogo_area = QFrame()
        self.detalhes_jogo_layout = QVBoxLayout(self.detalhes_jogo_area)
        self.detalhes_jogo_label = QLabel("Selecione um jogo para ver os detalhes.")
        self.detalhes_jogo_layout.addWidget(self.detalhes_jogo_label)
        self.detalhes_jogo_area.setStyleSheet("margin-top: 20px;")
        layout.addWidget(self.detalhes_jogo_area)

        self.biblioteca_tab.setLayout(layout)

    def init_adicionar_tab(self):
        layout = QFormLayout()
        self.nome_jogo_input = QLineEdit()
        self.preco_input = QLineEdit()
        self.desconto_input = QLineEdit()
        self.link_capa_input = QLineEdit()
        self.data_compra_input = QLineEdit()
        self.id_compra_input = QLineEdit()

        self.adicionar_button = QPushButton("Adicionar Jogo")
        self.adicionar_button.clicked.connect(self.adicionar_jogo)
        layout.addRow("Nome do Jogo:", self.nome_jogo_input)
        layout.addRow("Preço:", self.preco_input)
        layout.addRow("Desconto:", self.desconto_input)
        layout.addRow("Link da Capa:", self.link_capa_input)
        layout.addRow("Data da Compra:", self.data_compra_input)
        layout.addRow("ID da Compra:", self.id_compra_input)
        layout.addRow(self.adicionar_button)

        self.adicionar_tab.setLayout(layout)

    def init_configuracoes_tab(self):
        layout = QVBoxLayout()
        configuracoes_label = QLabel("Configurações")
        layout.addWidget(configuracoes_label)
        self.configuracoes_tab.setLayout(layout)

    def carregar_jogos(self):
        # Aqui você pode carregar os jogos de um arquivo ou banco de dados
        pass

    def adicionar_jogo(self):
        nome = self.nome_jogo_input.text()
        preco = self.preco_input.text()
        desconto = self.desconto_input.text()
        link_capa = self.link_capa_input.text()
        data_compra = self.data_compra_input.text()
        id_compra = self.id_compra_input.text()

        novo_jogo = Game(nome, preco, desconto, link_capa, data_compra, id_compra)
        self.jogos.append(novo_jogo)

        item = QListWidgetItem(nome)
        self.jogos_list.addItem(item)

        QMessageBox.information(self, "Sucesso", "Jogo adicionado com sucesso!")
        self.limpar_campos()

    def limpar_campos(self):
        self.nome_jogo_input.clear()
        self.preco_input.clear()
        self.desconto_input.clear()
        self.link_capa_input.clear()
        self.data_compra_input.clear()
        self.id_compra_input.clear()

    def mostrar_detalhes_jogo(self, item):
        index = self.jogos_list.row(item)
        jogo_selecionado = self.jogos[index]
        self.detalhes_jogo_label.setText(
            f"Nome: {jogo_selecionado.name}\nPreço: {jogo_selecionado.price}\nDesconto: {jogo_selecionado.discount}\n"
            f"Data de Compra: {jogo_selecionado.purchase_date}\nID de Compra: {jogo_selecionado.purchase_id}"
        )

    def pesquisar_jogos(self):
        query = self.pesquisa_input.text().lower()
        self.jogos_list.clear()
        for jogo in self.jogos:
            if query in jogo.name.lower():
                self.jogos_list.addItem(QListWidgetItem(jogo.name))

    def show_biblioteca(self):
        self.main_area.setCurrentWidget(self.biblioteca_tab)

    def show_adicionar(self):
        self.main_area.setCurrentWidget(self.adicionar_tab)

    def show_configuracoes(self):
        self.main_area.setCurrentWidget(self.configuracoes_tab)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game_manager = GameManager()
    game_manager.show()
    sys.exit(app.exec_())
