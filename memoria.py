from componente import Componente
class Memoria(Componente):
    def __init__(self):
        super().__init__()
        self.__tipo = None
        self.__capacidade = 0

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