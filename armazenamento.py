from memoria import Memoria
class Armazenamento(Memoria):
    def __init__(self, preco, marca, modelo, tipo, capacidade, leitura, escrita):
        super().__init__(preco, marca, modelo, tipo, capacidade)
        self.__leitura = leitura
        self.__escrita = escrita

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
        return (f'Preco: {self.getPreco()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}\n,
                Tipo: {self.getTipo()}\nCapacidade: {self.getCapacidade()} GB\nLeitura: {self.getLeitura()} MB/s\n,
                Escrita: {self.getEscrita()} MB/s')