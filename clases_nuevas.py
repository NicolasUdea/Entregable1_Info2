def main():

    b=Maquina()
    while True:
        print("Seleccione una opción: \n1.inresar una nueva máquina. \n 2.Eliminar una máquina \n 3.Selección de una máquina. \n 4.Editar datos de máquina \n 5.Salir")
        a=input("ingrese un opción: ")
        if a == "1": 
            b=BaseDatos
            b.precio=(float(input("ingrese el precio de la máquina: ")))
            b.stock=(float(input("ingrese el stock: ")))
            b.empresa=(input("ingrese la empresa: "))
            b.modelo=(float(input("ingrese el modelo de la maquina: ")))
            
            c=input("ingrese el tipo de máqiuina que desea ingresar: \n 1 máquina para electrocardiografía \n 2 Desfibrilador hospitalario \n 3 máquina para resonancia magnética ")
            if c == "1":
                b.derivaciones=(float(input("ingrese el número de derivaciones: ")))

            elif c == "2":
                b.energia=(float(input("ingrese la energía máxima del desfibrilador: ")))

            else:
                b.intensidad=(float(input("ingrese la intensidad del campo magnético en teslas: ")))
        
        b.agrearMaquina(b)


if __name__ == '__main__':
    main()