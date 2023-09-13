from Maquina import *
from funciones import *

class ResonanciaMag(Maquina):
    def __init__(self):
        super().__init__()
        self.__intensidadCM = 0
    
    def __str__(self):
        return f'''{super().__str__()}
Datos de la resonancia magnética:
        Intensidad del campo magnético: {self.__intensidadCM} T{separador()}'''