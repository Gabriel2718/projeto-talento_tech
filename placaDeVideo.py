from componente import Componente
class PlacaDeVideo(Componente):
    def __init__(self, preco, marca, modelo, chipGrafico, clockGpu, vram, clockVram):
        super().__init__(preco, marca, modelo)
        self.__chipGrafico = chipGrafico
        self.__clockGpu = clockGpu
        self.__vram = vram
        self.__clockVram = clockVram

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
        return (f'Preco: {self.getPreco()}\nMarca: {self.getMarca()}\nModelo: {self.getModelo()}\n,
                Chip gráfico: {self.getChipGrafico()}\nClock (GPU): {self.getClockGpu()} MHz\n,
                VRAM: {self.getVram()} GB\nClock (VRAM): {self.getVram()} MHz')