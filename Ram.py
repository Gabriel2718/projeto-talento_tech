from memoria import Memoria
class Ram(Memoria):
    def __init__(self, preco, marca, modelo, tipo, capacidade, frequencia):
        super().__init__(preco, marca, modelo, tipo, capacidade)
        self.__frequencia = frequencia

    #getters
    def getFrequencia(self):
        return self.__frequencia
    
    #setters
    def setFrequencia(self, frequencia):
        self.__frequencia = frequencia

    
    def consultarDados(self):
        return (f'Preco: {self.getPreco()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}\n,
                Tipo: {self.getTipo()}\nCapacidade: {self.getCapacidade()} GB\nFrequência: {self.getFrequencia()} MHz')