import tkinter as tk
import time

def atualizar_relogio():
    # Pega o tempo atual
    hora_atual = time.strftime('%H:%M:%S')
    # Atualiza o texto do rótulo com a hora atual
    rotulo_relogio.config(text=hora_atual)
    # Atualiza o relógio a cada 1000 milissegundos (1 segundo)
    raiz.after(1000, atualizar_relogio)

# Cria a janela principal
raiz = tk.Tk()
raiz.title('Relógio Digital')

# Define o tamanho da fonte e cria o rótulo do relógio
rotulo_relogio = tk.Label(raiz, font=('Helvetica', 48), fg='black')
rotulo_relogio.pack()

# Inicia o relógio
atualizar_relogio()

# Inicia o loop principal da interface gráfica
raiz.mainloop()
