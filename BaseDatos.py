from Desfribilador import *
from ResonanciaMag import *
from funciones import *
from Maquina import *
from ECG import *


class BaseDatos(Maquina):
    def __init__(self):
        self.__inventario = {}

    def agregarMaquina(self, Equipo):
        self.__inventario[Maquina.modelo] = Equipo
