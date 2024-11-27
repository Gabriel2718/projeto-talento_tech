from componente import Componente
class Processador(Componente):
    def __init__(self):
        super().__init__()
        self.__clock = 0.0
        self.__socket = None
        self.__nucleos = 0

    #getters
    def getClock(self):
        return self.__clock
    
    def getSocket(self):
        return self.__socket
    
    def getNucleos(self):
        return self.__nucleos
    
    #setters
    def setClock(self, clock):
        self.__clock = clock

    def setSocket(self, socket):
        self.__socket = socket

    def setNucleos(self, nucleos):
        self.__nucleos = nucleos

    
    def consultarDados(self):
        return (f'Processador \nPreço: R${self.getPreco()} \nMarca: {self.getMarca()} \nModelo: {self.getModelo()} \nClock: {self.getClock()} GHz \nSocket: {self.getSocket()} \nNucleos: {self.getNucleos()}')