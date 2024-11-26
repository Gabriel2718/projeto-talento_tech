from memoria import Memoria
class Ram(Memoria):
    def __init__(self):
        super().__init__()
        self.__clock = 0

    #getters
    def getClock(self):
        return self.__clock
    
    #setters
    def setClock(self, clock):
        self.__clock = clock

    
    def consultarDados(self):
        return (f'Preco: {self.getPreco()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}\nTipo: {self.getTipo()}\nCapacidade: {self.getCapacidade()} GB\nClock: {self.getClock()} MHz')