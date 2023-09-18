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
            if objeto.tipo == "ECG":
                variable = "número de derivaciones."
            elif objeto.tipo == "Desfribilador":
                variable = "energía máxima del desfibrilador."
            elif objeto.tipo == "ResonanciaMag":
                variable = "la intensidad del campo magnético en teslas."

            menu = verificarInt(f"""Seleccione una opción:
            1. Editar precio de la maquina.
            2. Editar stock de la maquina.
            3. Editar nombre de la empresa.
            4. Editar modelo de la maquina.
            5. Editar número de {variable}
            > """)
            if menu == 1:
                objeto.precio = verificarFloat("ingrese el precio de la máquina: ")
            elif menu == 2:
                objeto.stock = verificarInt("ingrese el stock: ")
            elif menu == 3:
                objeto.empresa = input("ingrese la empresa: ")
            elif menu == 4:
                objeto.modelo = input("ingrese el modelo de la maquina: ")
            elif menu == 5:
                if objeto.tipo == "ECG":
                    objeto.derivaciones = verificarFloat("ingrese el número de derivaciones: ")
                elif objeto.tipo == "Desfribilador":
                    objeto.energia = verificarFloat("ingrese la energía máxima del desfibrilador: ")
                elif objeto.tipo == "ResonanciaMag":
                    objeto.intensidad = verificarFloat("ingrese la intensidad del campo magnético en teslas: ")
            else:
                print("Opción no válida")
            return self.__inventario[objeto.ID]
        else:
            return "No se encuentra en la base de datos"
