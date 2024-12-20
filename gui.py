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
campos = []
entradas = []

def cadastrar():
        tipo = 0
        entradaVazia = False
        match varTipo.get():
            case "Processador":
                tipo = 1
            case "Ram":
                tipo = 2
            case "Armazenamento":
                tipo = 3
            case "PlacaMae":
                tipo = 4
            case "PlacaDeVideo":
                tipo = 5
            case "Fonte":
                tipo = 6
            case "Gabinete":
                tipo = 7

        valores = []

        for val in entradas:
            valores.append(val.get())
            if val.get() == "":
                entradaVazia= True
        
        if not entradaVazia:
            cadastrarComponente(tipo, estoque, valores)
            messagebox.showinfo(f'Componente do tipo {varTipo.get()} cadastrado com sucesso')
        else:
            messagebox.showinfo("Todos os campos devem estar preenchidos")
            
def atualizarLista():
    listabox.delete(0, tk.END)
    for obj in estoque:
        listabox.insert(tk.END, obj.consultarDados())

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

labelPreco = tk.Label(tab1, text="Preço", font=("", 15)).grid(row=1, column=0, sticky="w", padx=10, pady=10)
entryPreco = tk.Entry(tab1, font=("", 15))
entryPreco.grid(row=1, column=1, sticky="w", padx=10, pady=10)

labelMarca = tk.Label(tab1, text="Marca", font=("", 15)).grid(row=2, column=0, sticky="w", padx=10, pady=10)
entryMarca = tk.Entry(tab1, font=("", 15))
entryMarca.grid(row=2, column=1, sticky="w", padx=10, pady=10)

labelModelo = tk.Label(tab1, text="Modelo", font=("", 15)).grid(row=3, column=0, sticky="w", padx=10, pady=10)
entryModelo = tk.Entry(tab1, font=("", 15))
entryModelo.grid(row=3, column=1, sticky="w", padx=10, pady=10)



labelClock = tk.Label(tab1, text="", font=("", 15))
entryClock = tk.Entry(tab1, font=("", 15))

labelTipo = tk.Label(tab1, text="Tipo", font=("", 15))
entryTipo = tk.Entry(tab1, font=("", 15))

labelCapacidade = tk.Label(tab1, text="Capacidade", font=("", 15))
entryCapacidade = tk.Entry(tab1, font=("", 15))

labelNucleos  = tk.Label(tab1, text="Quantidade de núcleos", font=("", 15))
entryNucleos = tk.Entry(tab1, font=("", 15))

labelSocket = tk.Label(tab1, text="Socket", font=("", 15))
entrySocket = tk.Entry(tab1, font=("", 15))

labelChipSet = tk.Label(tab1, text="Chip set", font=("", 15))
entryChipSet = tk.Entry(tab1, font=("", 15))

labelLeitura = tk.Label(tab1, text="Leitura (em MB/s)", font=("", 15))
entryLeitura = tk.Entry(tab1, font=("", 15))

labelEscrita = tk.Label(tab1, text="Escrita (em MB/s)", font=("", 15))
entryEscrita = tk.Entry(tab1, font=("", 15))

labelChipGrafico = tk.Label(tab1, text="Chip gráfico", font=("", 15))
entryChipGrafico = tk.Entry(tab1, font=("", 15))

labelClockGpu = tk.Label(tab1, text="Clock da GPU (em MHz)", font=("", 15))
entryClockGpu = tk.Entry(tab1, font=("", 15))

labelVram = tk.Label(tab1, text="VRAM (em GB)", font=("", 15))
entryVram = tk.Entry(tab1, font=("", 15))

labelClockVram = tk.Label(tab1, text="Clock da VRAM (em MHz)", font=("", 15))
entryClockVram = tk.Entry(tab1, font=("", 15))

labelPotencia = tk.Label(tab1, text="Potência (em Watts)", font=("", 15))
entryPotencia = tk.Entry(tab1, font=("", 15))

labelAltura = tk.Label(tab1, text="Altura (em Cm)", font=("", 15))
entryAltura = tk.Entry(tab1, font=("", 15))

labelLargura = tk.Label(tab1, text="Largura (em Cm)", font=("", 15))
entryLargura = tk.Entry(tab1, font=("", 15))

labelComprimento = tk.Label(tab1, text="Comprimento (em Cm)", font=("", 15))
entryComprimento = tk.Entry(tab1, font=("", 15))

labelFormato = tk.Label(tab1, text="Formato", font=("", 15))
entryFormato = tk.Entry(tab1, font=("", 15))

tipos = ["Processador", "Ram", "Armazenamento", "PlacaMae", "PlacaDeVideo", "Fonte", "Gabinete"]

tk.Label(tab1, text="Tipo", font=("", 15)).grid(row=0, column=0, sticky="w", padx=10, pady=10)
varTipo = tk.StringVar(value="Processador")

botaoCadastrar = tk.Button(tab1, text="Cadastrar", command=cadastrar, font=("", 15))

def atualizarCampos():
    for campo in campos:
        campo.grid_remove()

    for entrada in entradas:
        entrada.grid_remove()

    campos.clear()

    entradas.clear()
    entradas.append(entryPreco)
    entradas.append(entryMarca)
    entradas.append(entryModelo)

    match varTipo.get():
        case "Processador":
            labelClock.config(text="Clock (em GHz)")
            campos.append(labelClock)
            campos.append(labelNucleos)
            campos.append(labelSocket)
            entradas.append(entryClock)
            entradas.append(entryNucleos)
            entradas.append(entrySocket)
        case "Ram":
            labelClock.config(text="Clock (em MHz)")
            campos.append(labelClock)
            campos.append(labelTipo)
            campos.append(labelCapacidade)
            entradas.append(entryTipo)
            entradas.append(entryCapacidade)
            entradas.append(entryClock)
        case "Armazenamento":
            campos.append(labelTipo)
            campos.append(labelCapacidade)
            campos.append(labelLeitura)
            campos.append(labelEscrita)
            entradas.append(entryTipo)
            entradas.append(entryCapacidade)
            entradas.append(entryLeitura)
            entradas.append(entryEscrita)
        case "PlacaMae":
            campos.append(labelFormato)
            campos.append(labelChipSet)
            entradas.append(entryFormato)
            entradas.append(entryChipSet)
        case "PlacaDeVideo":
            campos.append(labelChipGrafico)
            campos.append(labelClockGpu)
            campos.append(labelVram)
            campos.append(labelClockVram)
            entradas.append(entryChipGrafico)
            entradas.append(entryClockGpu)
            entradas.append(entryVram)
            entradas.append(entryClockVram)
        case "Fonte":
            campos.append(labelFormato)
            campos.append(labelPotencia)
            entradas.append(entryFormato)
            entradas.append(entryPotencia)
        case "Gabinete":
            campos.append(labelFormato)
            campos.append(labelAltura)
            campos.append(labelLargura)
            campos.append(labelComprimento)
            entradas.append(entryFormato)
            entradas.append(entryAltura)
            entradas.append(entryLargura)
            entradas.append(entryComprimento)

    for i, campo in enumerate(campos, start=4):
        campo.grid(row=i, column=0, sticky="w", padx=10, pady=10)

    for i, entrada in enumerate(entradas, start=0):
        entrada.grid(row=(i+1), column=1, sticky="w", padx=10, pady=10)

    botaoCadastrar.grid(row=len(campos)+4, column=1, sticky="nsew",padx=15, pady=15)
        

for i, tipo in enumerate(tipos, start=1):
        tk.Radiobutton(tab1, text=tipo, font=("", 15), variable=varTipo, value=tipo, command=atualizarCampos).grid(row=0, column=i, sticky="w", padx=10, pady=10)


tab2 = tk.Frame(aba)
tab2.grid_rowconfigure(0, weight=1)
tab2.grid_columnconfigure(0, weight=1)

aba.add(tab2, text="Lista")

listabox = tk.Listbox(tab2)
listabox.config(font=("", 15))
listabox.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
tk.Button(tab2, text="Atualizar", command=atualizarLista, font=("", 15)).grid(row=1, column=0)

atualizarCampos()

janela.mainloop()