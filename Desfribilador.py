from Maquina import *
from funciones import *

class Desfribilador(Maquina):
    def __init__(self):
        super().__init__()
        self.__energiaMax = 0
    
    def __str__(self):
        return f'''{super().__str__()}
    
Datos desfribilador:
        Energia maxima: {self.__energiaMax}{separador()}'''
        
    def editarEnergiaMax(self, float):
        self.__energiaMax = float
        return True