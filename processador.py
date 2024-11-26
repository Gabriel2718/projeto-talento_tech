from componente import Componente
class Processador(Componente):
    def __init__(self, preco, marca, modelo, clock, socket, nucleos):
        super().__init__(preco, marca, modelo)
        self.__clock = clock
        self.__socket = socket
        self.__nucleos = nucleos

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
        return (f'Preco: {self.getPreco()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}\n,
                Clock: {self.getClock()} GHz\nSocket: {self.getSocket()}\nNucleos: {self.getNucleos()}')