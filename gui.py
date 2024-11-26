from processador import Processador
from ram import Ram
from armazenamento import Armazenamento
from placaMae import PlacaMae
from placaDeVideo import PlacaDeVideo 
from fonte import Fonte
from gabinete import Gabinete

from cadastro import cadastrarComponente

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

janela = tk.Tk()

janela.title("Cadastro de Componentes no Estoque")
janela.geometry("1500x500")

estoque = []

def cadastrar():
    pass

def atualizarLista():
    pass

janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

aba = ttk.Notebook(janela)
aba.grid(row=0, column=0, sticky="nsew")

tab1 = ttk.Frame(aba)
#quantidade máxima de linhas: 7
for i in range(7):
    tab1.grid_rowconfigure(i,weight=1)

#quantidade de objetos: 7
for i in range(7):
    tab1.grid_columnconfigure(i,weight=1)

aba.add(tab1, text="Cadastro")

tab2 = tk.Frame(aba)
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)

aba.add(tab2, text="Lista")



#labels fixos
#label1 = tipo
#label2 = preço
#label3 = marca
#label4 = modelo

labelPreco = tk.Label(tab1, text="Preço", font=("", 15)).grid(row=1, column=0, sticky="w", padx=10, pady=10)
labelMarca = tk.Label(tab1, text="Marca", font=("", 15)).grid(row=2, column=0, sticky="w", padx=10, pady=10)
labelModelo = tk.Label(tab1, text="Modelo", font=("", 15)).grid(row=3, column=0, sticky="w", padx=10, pady=10)

labelClock = tk.Label(tab1, text="", font=("", 15))
labelTipo = tk.Label(tab1, text="Tipo", font=("", 15))
labelCapacidade = tk.Label(tab1, text="Capacidade", font=("", 15))
labelNucleos  = tk.Label(tab1, text="Quantidade de núcleos", font=("", 15))
labelSocket = tk.Label(tab1, text="Socket", font=("", 15))
labelChipSet = tk.Label(tab1, text="Chip set", font=("", 15))
labelLeitura = tk.Label(tab1, text="Leitura (em MB/s)", font=("", 15))
labelEscrita = tk.Label(tab1, text="Escrita (em MB/s)", font=("", 15))
labelChipGrafico = tk.Label(tab1, text="Chip gráfico", font=("", 15))
labelClockGpu = tk.Label(tab1, text="Clock da GPU (em MHz)", font=("", 15))
labelVram = tk.Label(tab1, text="VRAM (em GB)", font=("", 15))
labelClockVram = tk.Label(tab1, text="Clock da VRAM (em MHz)", font=("", 15))
labelPotencia = tk.Label(tab1, text="Potência (em Watts)", font=("", 15))
labelAltura = tk.Label(tab1, text="Alura (em Cm)", font=("", 15))
labelLargura = tk.Label(tab1, text="Largura (em Cm)", font=("", 15))
labelComprimento = tk.Label(tab1, text="Comprimento (em Cm)", font=("", 15))
labelFormato = tk.Label(tab1, text="Formato", font=("", 15))

tipos = ["Processador", "Ram", "Armazenamento", "PlacaMae", "PlacaDeVideo", "Fonte", "Gabinete"]

tk.Label(tab1, text="Tipo", font=("", 15)).grid(row=0, column=0, sticky="w", padx=10, pady=10)
varTipo = tk.StringVar(value="Processador")

campos = []

def atualizarCampos():
    for campo in campos:
        campo.grid_remove()
    campos.clear()
    match varTipo.get():
        case "Processador":
            labelClock.config(text="Clock (em GHz)")
            campos.append(labelClock)
            campos.append(labelNucleos)
            campos.append(labelSocket)
        case "Ram":
            labelClock.config(text="Clock (em MHz)")
            campos.append(labelClock)
            campos.append(labelTipo)
            campos.append(labelCapacidade)
        case "Armazenamento":
            campos.append(labelTipo)
            campos.append(labelCapacidade)
            campos.append(labelLeitura)
            campos.append(labelEscrita)
        case "PlacaMae":
            campos.append(labelFormato)
            campos.append(labelChipSet)
        case "PlacaDeVideo":
            campos.append(labelChipGrafico)
            campos.append(labelClockGpu)
            campos.append(labelVram)
            campos.append(labelClockVram)
        case "Fonte":
            campos.append(labelFormato)
            campos.append(labelPotencia)
        case "Gabinete":
            campos.append(labelFormato)
            campos.append(labelAltura)
            campos.append(labelLargura)
            campos.append(labelComprimento)

    for i, campo in enumerate(campos, start=4):
        campo.grid(row=i, column=0, sticky="w", padx=10, pady=10)

    for i, tipo in enumerate(tipos, start=1):
        tk.Radiobutton(tab1, text=tipo, font=("", 15), variable=varTipo, value=tipo, command=atualizarCampos).grid(row=0, column=i, sticky="w", padx=10, pady=10)

atualizarCampos()

janela.mainloop()