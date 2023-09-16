class Maquina:
    def __init__(self):
        self.__precio = 0
        self.__stock = 0
        self.__modelo = 0
        self.__empresa = ""
    
    @property  
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, b):
        self.__precio = b

    @property  
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, b):
        self.__stock = b

    @property  
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, b):
        self.__modelo = b
    

    @property  
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, empresa):
        self.__empresa= empresa
    
    def __str__(self):
        return f"precio: {self.precio}su stock es {self.stock}, modelo: {self.modelo},de la empresa:{self.empresa}"
    

class ECG(Maquina):
    def __init__(self):
        super().__init__(self)
        self.__derivaciones=""
    
    @property  
    def derivaciones(self):
        return self.__derivaciones

    @derivaciones.setter
    def derivaciones(self, b):
        self.__derivaciones = b

    def __str__(self):
        return f'{super().__str__()}, numero de derivaciones: {self.derivaciones}'
    
class Desfribilador(Maquina):
    def __init__(self,precio,stock,modelo,emrpesa,energia):
        super().__init__(precio,stock,modelo,emrpesa)
        self.__energia=energia
    
    @property  
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, energia):
        self.__energia = energia

    def __str__(self):
        return f'{super().__str__()}, energia máxima del desfibrilador: {self.energia}'
    
class ResonanciaMag(Maquina):
    def __init__(self):
        super().__init__()
        self.__intensidad=""
    
    @property  
    def intensidad(self):
        return self.__intensidad

    @intensidad.setter
    def energia(self, b):
        self.__intensidad = b

    def __str__(self):
        return f'{super().__str__()}, intensidad del campo magnetico en teslas: {self.intensidad}'

class BaseDatos(Maquina):
    def __init__(self):
        self.__inventario = {}

    
    
    def agregarMaquina(self, Maquina):
        self.__inventario[Maquina.verModelo()] = Maquina