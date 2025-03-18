import tkinter as tk
from tkinter import ttk

# Definir as cores
co0 = "#444466"
co1 = '#FeFFFF'
co2 = "#bfb86d"

fundo_dia = "#6cc4cc"
fundo_noite = "#484F60"
fundo_tarde = '#bfb86d'

fundo = fundo_tarde

# Criar a janela principal
janela = tk.Tk()
janela.title("Visualizador de Dados IoT")
janela.geometry("320x350")
janela.configure(bg=fundo)

# Dados de exemplo
data = {
    "Temperatura": [21, 35, 32, 35],
    "Umidade": [50, 60, 70, 80],
    "Movimento": [0, 1, 0, 1]
}

# Função para atualizar os dados
def update_data(index=0):
    if index < len(data["Temperatura"]):
        temperatura = data["Temperatura"][index]
        umidade = data["Umidade"][index]
        movimento = data["Movimento"][index]

        # Atualizar os rótulos com os dados mais recentes
        label_temp.config(text=f"Temperatura: {temperatura}ºC")
        label_hum.config(text=f"Umidade: {umidade}%")
        label_mov.config(text=f"Movimento: {'Detectado' if movimento else 'Não detectado'}")

        # Atualizar os dados a cada segundo
        janela.after(1000, update_data, index + 1)

# Criar um separador horizontal
ttk.Separator(janela, orient=tk.HORIZONTAL).grid(row=0, columnspan=2, ipadx=157, pady=0)

# Criar o frame superior
frame_top = tk.Frame(janela, width=320, height=10, bg=fundo)
frame_top.grid(row=1, column=0, columnspan=2, pady=0)

# Criar os rótulos de exibição dos dados
label_temp = ttk.Label(janela, text="Aguardando dados...", font=("Arial", 12), background=fundo)
label_temp.grid(row=2, column=0, padx=10, pady=5, sticky="w")

label_hum = ttk.Label(janela, text="Esperando dados da umidade...", font=("Arial", 12), background=fundo)
label_hum.grid(row=3, column=0, padx=10, pady=5, sticky="w")

label_mov = ttk.Label(janela, text="Aguardando dados do movimento...", font=("Arial", 12), background=fundo)
label_mov.grid(row=4, column=0, padx=10, pady=5, sticky="w")

# Estilo para os widgets
estilo = ttk.Style()
estilo.configure("TLabel", background=fundo, font=("Arial", 12))

# Chamar a função para começar a atualização dos dados
update_data()

# Iniciar o loop principal da janela
janela.mainloop()
