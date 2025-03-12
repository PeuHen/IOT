import tkinter
from tkinter import *
from tkinter import ttk

co0 ="#444466"
co1 = '#FeFFFF'
co2 = "#bfb86d"

fundo_dia = "#6cc4cc"
fundo_noite = "#484F60"
fundo_tarde = '#bfb86d'

fundo = fundo_tarde

janela = Tk()
janela.title("")
janela.geometry("320x350")
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0,columnspan=1, ipadx=157)

frame_top = Frame(janela, width=320,height=50, bg=fundo, pady=0, padx=0)
frame_top.grid(row=1, column=0)


estilo=ttk.Style(janela)
estilo.theme_use("clam")
janela.mainloop()