
from clases_nuevas import*
from BaseDatos import*

def main():

    base=BaseDatos()
    while True:
        print("Seleccione una opción: \n1.inresar una nueva máquina. \n 2.Eliminar una máquina \n 3.Selección de una máquina. \n 4.Editar datos de máquina \n 5.Salir")
        a=input("ingrese un opción: ")
        if a == 1: 
            b=Maquina
            b.precio(input("ingrese el precio de la máquina: "))
            b.stock(input("ingrese el stock: "))
            b.empresa(input("ingrese la empresa: "))
            b.modelo(input("ingrese el modelo de la maquina: "))
           
        
        base.agregarMaquina(b)
        
    

