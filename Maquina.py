from funciones import *

class Maquina:
    def __init__(self):
        self.__precio = 0
        self.__stock = 0
        self.__modelo = "Juan"
        self.__empresa = "Mox"
        
    def __str__(self):
        return f'''{separador()}Datos de la maquina "{self.__modelo}" de la empresa "{self.__empresa}":
        Precio: {self.__precio}
        Stock: {self.__stock}'''
        
    def editarPrecio(self, float):
        self.__precio = float
        return True
    def editarStock(self, int):
        self.__stock = int
        return True
    def editarModelo(self, str):
        self.__modelo = str
        return True
    def editarEmpresa(self, str):
        self.__empresa = str
        return True