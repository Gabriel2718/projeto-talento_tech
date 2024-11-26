from processador import Processador
from ram import Ram
from armazenamento import Armazenamento
from placaMae import PlacaMae
from placaDeVideo import PlacaDeVideo 
from fonte import Fonte
from gabinete import Gabinete

def cadastrarInfoBasicas(c):
    c.setPreco(float(input('Preço: ')))
    c.setMarca(str(input('Marca: ')))
    c.setModelo(str(input('Modelo: ')))
    return c


def cadastrarProcessador():
    p = cadastrarInfoBasicas(Processador())
    p.setClock(float(input('Clock (em GHz): ')))
    p.setSocket(str(input('Socket: ')))
    p.setNucleos(int(input('Quantidade de núcleos: ')))
    return p

def cadastrarRam():
    r = cadastrarInfoBasicas(Ram())
    r.setTipo(str(input('Tipo: ')))
    r.setCapacidade(int(input('Capacidade (em GB): ')))
    r.setClock(int(input('Clock (em MHz): ')))
    return r

def cadastrarArmazenamento():
    a = cadastrarInfoBasicas(Armazenamento())
    a.setTipo(str(input('Tipo: ')))
    a.setCapacidade(int(input('Capacidade (em GB): ')))
    a.setLeitura(int(input('Leitura (em MB/s): ')))
    a.setEscrita(int(input('Escrita (em MB/s): ')))
    return a

def cadastrarPlacaMae():
    pm = cadastrarInfoBasicas(PlacaMae())
    pm.setChipSet(str(input('Chip set: ')))
    pm.setFormato(str(input('Formato: ')))
    return pm

def cadastrarPlacaDeVideo():
    pv = cadastrarInfoBasicas(PlacaDeVideo())
    pv.setChipGrafico(str(input('Chip gráfico: ')))
    pv.setClockGpu(int(input('Clock da GPU (em MHz): ')))
    pv.setVram(int(input('VRAM (em GB): ')))
    pv.setClockVram(int(input('Clock da VRAM (em MHz): ')))
    return pv

def cadastrarFonte():
    f = cadastrarInfoBasicas(Fonte())
    f.setPotencia(int(input('Potência (em Watts): ')))
    f.setFormato(str(input('Formato: ')))
    return f

def cadastrarGabinete():
    g = cadastrarInfoBasicas(Gabinete())
    g.setFormato(str(input('Formato: ')))
    g.setAltura(int(input('Altura (em Cm): ')))
    g.setLargura(int(input('Largura (em Cm): ')))
    g.setComprimento(int(input('Comprimento (em Cm): ')))
    return g

def cadastrarComponente(op, lista):
    match op:
        case 1:
            lista.append(cadastrarProcessador())
        case 2:
            lista.append(cadastrarRam())
        case 3:
            lista.append(cadastrarArmazenamento())
        case 4:
            lista.append(cadastrarPlacaMae())
        case 5:
            lista.append(cadastrarPlacaDeVideo())
        case 6:
            lista.append(cadastrarFonte())
        case 7:
            lista.append(cadastrarGabinete())