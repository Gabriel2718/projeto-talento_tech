from componente import Componente
class PlacaDeVideo(Componente):
    def __init__(self):
        super().__init__()
        self.__chipGrafico = None
        self.__clockGpu = 0
        self.__vram = 0
        self.__clockVram = 0

    #getters
    def getChipGrafico(self):
        return self.__chipGrafico
    
    def getClockGpu(self):
        return self.__clockGpu
    
    def getVram(self):
        return self.__vram
    
    def getClockVram(self):
        return self.__clockVram
    
    #setters
    def setChipGrafico(self, chipGrafico):
        self.__chipGrafico = chipGrafico

    def setClockGpu(self, clockGpu):
        self.__clockGpu = clockGpu

    def setVram(self, vram):
        self.__vram = vram

    def setClockVram(self, clockVram):
        self.__clockVram = clockVram

    
    def consultarDados(self):
        return (f'Preco: {self.getPreco()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}\nChip gráfico: {self.getChipGrafico()}\nClock (GPU): {self.getClockGpu()} MHz\nVRAM: {self.getVram()} GB\nClock (VRAM): {self.getVram()} MHz')