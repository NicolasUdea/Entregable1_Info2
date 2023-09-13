from Desfribilador import *
from ResonanciaMag import *
from funciones import *
from Maquina import *
from ECG import *

class BaseDatos():
    def __init__(self):
        self.__inventario = {}
    
    def agregarMaquina(self, Maquina):
        self.__inventario[Maquina.verModelo()] = Maquina
    