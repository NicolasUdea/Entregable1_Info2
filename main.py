from ResonanciaMag import *
from Desfribilador import *
from BaseDatos import *
from funciones import *
from Maquina import *
from ECG import *


def main():
    # Inicio del programa
    print(f"""{separador()}
    Bienvenido al sistema de máquinas médicas.
    {separador()}""")
    presionaEnter()
    print(separador())
    base = BaseDatos()

    # Menú principal
    while True:
        menu = verificarInt("""Seleccione una opción:
        1. Ingresar una nueva máquina.
        2. Eliminar una máquina.
        3. Selección de una máquina.
        4. Editar datos de máquina.
        5. Salir.
        > """)
        if menu == 1:  # Ingresar una nueva máquina.
            b = Maquina()
            b.precio = verificarFloat("ingrese el precio de la máquina: ")
            b.stock = verificarInt("ingrese el stock: ")
            b.empresa = input("ingrese la empresa: ")
            b.modelo = input("ingrese el modelo de la maquina: ")

            tipo_maquina = verificarInt("""Ingrese el tipo de máquina que desea ingresar:
            1. Máquina para electrocardiografía
            2. Desfibrilador hospitalario
            3. Máquina para resonancia magnética
            > """)
            if tipo_maquina == 1:
                b.derivaciones = verificarFloat("ingrese el número de derivaciones: ")

            elif tipo_maquina == 2:
                b.energia = verificarFloat("ingrese la energía máxima del desfibrilador: ")

            elif tipo_maquina == 3:
                b.intensidad = verificarFloat("ingrese la intensidad del campo magnético en teslas: ")
        
        base.agregarMaquina(b)


if __name__ == '__main__':
    main()
