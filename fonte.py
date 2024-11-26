from componente import Componente
class Fonte(Componente):
    def __init__(self, preco, marca, modelo, potencia, formato):
        super().__init__(preco, marca, modelo)
        self.__potencia = potencia
        self.__formato = formato

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
        return (f'Preco: {self.getPreco()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}\n,
                Potência: {self.getPotencia()}\nFormato: {self.getFormato()}')