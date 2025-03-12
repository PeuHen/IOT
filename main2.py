import tkinter as tk




#cricao da janela principal
root = tk.Tk();
root.title("Entrada de texto")


#rotulo
label = tk.Label(root,text="teste")
label.pack()

#Função para exibir o texto de entrada
def mostrar_texto():
    texto = entrada.get();


#entrada de texto
entrada = tk.Entry(root)
entrada.pack()
#botao
button = tk.Button(root, text="Mostrar texto", command=mostrar_texto())
button.pack()


root.mainloop()