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
    BD = BaseDatos()

    # Menú principal
    while True:
        menu = verificarInt("""Seleccione una opción:
        1. Ingresar una nueva máquina.
        2. Eliminar una máquina.
        3. Selección de una máquina.
        4. Editar datos de máquina.
        5. Salir.
        > """)
        print(separador())
        if menu == 1:  # Ingresar una nueva máquina.
            ID = verificarInt("ingrese el ID de la máquina: ")
            precio = verificarFloat("ingrese el precio de la máquina: ")
            stock = verificarInt("ingrese el stock: ")
            empresa = input("ingrese la empresa: ")
            modelo = input("ingrese el modelo de la maquina: ")

            tipo_maquina = verificarInt("""Seleccione el tipo de máquina que desea ingresar:
            1. Máquina para electrocardiografía
            2. Desfibrilador hospitalario
            3. Máquina para resonancia magnética
            > """)
            if tipo_maquina == 1:
                objeto = ECG()
                objeto.derivaciones = verificarFloat("ingrese el número de derivaciones: ")

            elif tipo_maquina == 2:
                objeto = Desfribilador()
                objeto.energia = verificarFloat("ingrese la energía máxima del desfibrilador: ")

            elif tipo_maquina == 3:
                objeto = ResonanciaMag()
                objeto.intensidad = verificarFloat("ingrese la intensidad del campo magnético en teslas: ")
            objeto.ID = ID
            objeto.precio = precio
            objeto.stock = stock
            objeto.empresa = empresa
            objeto.modelo = modelo
            BD.agregarMaquina(objeto)
            print(separador())
            print("Se ha agregado la máquina a la BD de datos")
            print(separador())

        elif menu == 2:  # Eliminar una máquina.
            clave = verificarInt("Ingrese el ID de la máquina que desea eliminar: ")
            BD.eliminarMaquina(clave)
            print(separador())

        elif menu == 3:  # Selección de una máquina.
            clave = verificarInt("Ingrese el ID de la máquina que desea seleccionar: ")
            print(BD.seleccionMaquina(clave))

        elif menu == 4:  # Editar datos de máquina.
            clave = verificarInt("Ingrese el ID de la máquina que desea editar: ")
            print(BD.editarMaquina(clave))

        elif menu == 5:  # Salir.
            print("Gracias por usar el sistema de máquinas médicas.")
            break

        else:
            print("Ingrese una opción válida.")
            print(separador())

if __name__ == '__main__':
    main()
