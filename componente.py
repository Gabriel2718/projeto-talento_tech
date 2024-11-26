from abc import ABC, abstractmethod
class Componente(ABC):
    def __init__(self, preco, marca, modelo):
        self.__preco = preco
        self.__marca = marca
        self.__modelo = modelo

    #getters
    def getPreco(self):
        return self.__preco
    
    def getMarca(self):
        return self.__marca
    
    def getModelo(self):
        return self.__modelo
    
    #setters
    def setPreco(self, preco):
        self.__preco = preco
    
    def setMarca(self, marca):
        self.__marca = marca

    def setModelo(self, modelo):
        self.__modelo = modelo

    
    @abstractmethod
    def consultarDados():
        pass
    
