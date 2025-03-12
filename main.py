import tkinter as tk;

root = tk.Tk()
root.title = ("MInha tela em Tkinker")

#rotulos
label = tk.Label(root, text="Olá mundo")
label.pack()

#Botao
button = tk.Button(root,text="Clique aqui")
button.pack()

#iniciando
root.mainloop();