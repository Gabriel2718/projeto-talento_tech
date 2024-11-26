from componente import Componente
class PlacaMae(Componente):
    def __init__(self):
        super().__init__()
        self.__chipSet = None
        self.__formato = None

    #getters
    def getChipSet(self):
        return self.__chipSet
    
    def getFormato(self):
        return self.__formato
    
    #setters
    def setChipSet(self, chipSet):
        self.__chipSet = chipSet

    def setFormato(self, formato):
        self.__formato = formato

    
    def consultarDados(self):
        return (f'PLaca-mãe\nPreço: R${self.getPreco()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}\nChip set: {self.getChipSet()}\nFormato: {self.getFormato()}')