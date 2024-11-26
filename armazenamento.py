from memoria import Memoria
class Armazenamento(Memoria):
    def __init__(self):
        super().__init__()
        self.__leitura = 0
        self.__escrita = 0

    #getters
    def getLeitura(self):
        return self.__leitura
    
    def getEscrita(self):
        return self.__escrita
    
    #setters
    def setLeitura(self, leitura):
        self.__leitura = leitura

    def setEscrita(self, escrita):
        self.__escrita = escrita

    
    def consultarDados(self):
        return (f'Módulo de armazenamento\nPreço: R${self.getPreco()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}\nTipo: {self.getTipo()}\nCapacidade: {self.getCapacidade()} GB\nLeitura: {self.getLeitura()} MB/s\nEscrita: {self.getEscrita()} MB/s')