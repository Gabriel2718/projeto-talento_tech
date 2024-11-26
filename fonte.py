from componente import Componente
class Fonte(Componente):
    def __init__(self):
        super().__init__()
        self.__potencia = 0
        self.__formato = None

    #getters
    def getPotencia(self):
        return self.__potencia

    def getFormato(self):
        return self.__formato

    #setters
    def setPotencia(self, potencia):
        self.__potencia = potencia

    def setFormato(self, formato):
        self.__formato = formato


    def consultarDados(self):
        return (f'Fonte\nPreço: R${self.getPreco()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}\nPotência: {self.getPotencia()}\nFormato: {self.getFormato()}')