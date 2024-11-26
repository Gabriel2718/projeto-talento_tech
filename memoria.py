from componente import Componente
class Memoria(Componente):
    def __init__(self, preco, marca, modelo, tipo, capacidade):
        super().__init__(preco, marca, modelo)
        self.__tipo = tipo
        self.__capacidade = capacidade

    #getters
    def getTipo(self):
        return self.__tipo
    
    def getCapacidade(self):
        return self.__capacidade
    
    #setters
    def setTipo(self, tipo):
        self.__tipo = tipo

    def setCapacidade(self, capacidade):
        self.__capacidade = capacidade

    
    def consultarDados(self):
        pass