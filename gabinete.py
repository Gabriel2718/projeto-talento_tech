from componente import Componente
class Gabinete(Componente):
    def __init__(self, preco, marca, modelo, formato, altura, largura, comprimento):
        super().__init__(preco, marca, modelo)
        self.__formato = formato
        self.__altura = altura
        self.__largura = largura
        self.__comprimento = comprimento

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
        return (f'Preco: {self.getPreco()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}\n,
                Formato: {self.getFormato()}\nAltura: {self.getAltura()} Cm\nLargura: {self.getLargura()} Cm\n,
                Comprimento: {self.getComprimento()} Cm')