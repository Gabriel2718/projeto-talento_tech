from memoria import Memoria
class Ram(Memoria):
    def __init__(self, preco, marca, modelo, tipo, capacidade, clock):
        super().__init__(preco, marca, modelo, tipo, capacidade)
        self.__clock = clock

    #getters
    def getClock(self):
        return self.__clock
    
    #setters
    def setClock(self, clock):
        self.__clock = clock

    
    def consultarDados(self):
        return (f'Preco: {self.getPreco()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}\n,
                Tipo: {self.getTipo()}\nCapacidade: {self.getCapacidade()} GB\nClock: {self.getClock()} MHz')