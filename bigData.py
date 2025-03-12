import tkinter as tk
from tkinter import ttk

## Dados fixos para simulação

data = {
    "Temperatura": [21,35,32,35],
    "Umidade": [50,60,70,80],
    "Movimento": [0,1,0,1]
}

def update_data():
    temperatura = data["Temperatura"].pop(0)
    umidade = data['Umidade'].pop(0)
    movimento= data["Movimento"].pop(0)

    label_temp.config(text=f"Temperatura:{temperatura}ºC")
    label_hum.config(text=f"Umidade:{umidade}%")
    label_mov.config(text=f"Movimento:{'Detectado' if movimento else 'Não detectado'}")

    if data["Temperatura"]:
        root.after(1000,update_data)

root = tk.Tk()
root.title("Visualizador de dados Iot")
root.geometry("400x200")
label_temp = ttk.Label(root,text="Aguardando dados....")
label_temp.pack()

label_hum = ttk.Label(root,text='Esperando dados da umidade...')
label_hum.pack(pady=10)

label_mov = ttk.Label(root,text="Aguardando dados do movimento... ")
label_mov.pack(pady=10)


update_data()
root.mainloop()