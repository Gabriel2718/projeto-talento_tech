from componente import Componente
class Gabinete(Componente):
    def __init__(self):
        super().__init__()
        self.__formato = None
        self.__altura = 0
        self.__largura = 0
        self.__comprimento = 0

    #getters
    def getFormato(self):
        return self.__formato
    
    def getAltura(self):
        return self.__altura
    
    def getLargura(self):
        return self.__largura
    
    def getComprimento(self):
        return self.__comprimento

    #setters
    def setFormato(self, formato):
        self.__formato = formato

    def setAltura(self, altura):
        self.__altura = altura

    def setLargura(self, largura):
        self.__largura = largura

    def setComprimento(self, comprimento):
        self.__comprimento = comprimento


    def consultarDados(self):
        return (f'Gabinete \nPreço: R${self.getPreco()} \nMarca: {self.getMarca()} \nModelo: {self.getModelo()} \nFormato: {self.getFormato()} \nAltura: {self.getAltura()} Cm \nLargura: {self.getLargura()} Cm \nComprimento: {self.getComprimento()} Cm')