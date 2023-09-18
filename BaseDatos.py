from Desfribilador import *
from ResonanciaMag import *
from funciones import *
from Maquina import *
from ECG import *


class BaseDatos(Maquina):
    def __init__(self):
        self.__inventario = {123: "hola"}

    def agregarMaquina(self, objeto):
        self.__inventario[objeto.ID] = objeto
        return self.__inventario[objeto.ID]

    def seleccionMaquina(self, clave):
        if clave in self.__inventario:
            return self.__inventario[clave]
        else:
            return "No se encuentra en la base de datos"

    def eliminarMaquina(self, clave):
        if clave in self.__inventario:
            del self.__inventario[clave]
            print("Se ha eliminado la máquina de la base de datos")
        else:
            print("No se encuentra en la base de datos")

    def editarMaquina(self, clave):
        if clave in self.__inventario:
            objeto = self.__inventario[clave]
            objeto.ID = verificarInt("ingrese el ID de la máquina: ")
            objeto.precio = verificarFloat("ingrese el precio de la máquina: ")
            objeto.stock = verificarInt("ingrese el stock: ")
            objeto.empresa = input("ingrese la empresa: ")
            objeto.modelo = input("ingrese el modelo de la maquina: ")
            tipo_maquina = verificarInt("""Ingrese el tipo de máquina que desea ingresar:
            1. Máquina para electrocardiografía
            2. Desfibrilador hospitalario
            3. Máquina para resonancia magnética
            > """)
            if tipo_maquina == 1:
                objeto.derivaciones = verificarFloat("ingrese el número de derivaciones: ")
            elif tipo_maquina == 2:
                objeto.energia = verificarFloat("ingrese la energía máxima del desfibrilador: ")
            elif tipo_maquina == 3:
                objeto.intensidad = verificarFloat("ingrese la intensidad del campo magnético en teslas: ")
            return self.__inventario[objeto.ID]
        else:
            return "No se encuentra en la base de datos"
