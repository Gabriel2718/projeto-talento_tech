from componente import Componente
class PlacaMae(Componente):
    def __init__(self, preco, marca, modelo, chipSet, formato):
        super().__init__(preco, marca, modelo)
        self.__chipSet = chipSet
        self.__formato = formato

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
        return (f'Preco: {self.getPreco()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}\n,
                Chip set: {self.getChipSet()}\nFormato: {self.getFormato()}')