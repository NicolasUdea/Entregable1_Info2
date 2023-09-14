class Maquina:
    def __init__(self,precio,stock,modelo,empresa):
        self.__precio = precio
        self.__stock = stock
        self.__modelo = modelo
        self.__empresa = empresa
    
    @property  
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property  
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock):
        self.__stock = stock

    @property  
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo
    

    @property  
    def empresa(self):
        return self.__empresa

    @empresa.setter
    def empresa(self, empresa):
        self.__empresa= empresa
    
    def __str__(self):
        return f"precio: {self.precio}su stock es {self.stock}, modelo: {self.modelo},de la empresa:{self.empresa}"
    

class ECG(Maquina):
    def __init__(self,precio,stock,modelo,emrpesa,derivaciones):
        super().__init__(self,precio,stock,modelo,emrpesa)
        self.__derivaciones=derivaciones
    
    @property  
    def derivaciones(self):
        return self.__derivaciones

    @derivaciones.setter
    def derivaciones(self, derivaciones):
        self.__derivaciones = derivaciones

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
    def __init__(self,precio,stock,modelo,emrpesa,intensidad):
        super().__init__(precio,stock,modelo,emrpesa)
        self.__intensidad=intensidad
    
    @property  
    def intensidad(self):
        return self.__intensidad

    @intensidad.setter
    def energia(self, intensidad):
        self.__intensidad = intensidad

    def __str__(self):
        return f'{super().__str__()}, intensidad del campo magnetico en teslas: {self.intensidad}'
    