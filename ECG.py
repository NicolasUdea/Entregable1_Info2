from Maquina import *
from funciones import *

class ECG(Maquina):
    def __init__(self):
        super().__init__()
        self.__numDerivaciones = 0
    
    def __str__(self):
        return f'''{super().__str__()}
        
Datos del electrocardiograma:
        Numero de derivaciones: {self.__numDerivaciones}{separador()}'''
    
    def editarDerivaciones(self, int):
        self.__numDerivaciones = int
        return True