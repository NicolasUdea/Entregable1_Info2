class Maquina:
    def __init__(self):
        self.__precio = 0
        self.__stock = 0
        self.__modelo = ""
        self.__empresa = ""
        self.__ID = 0

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, identificacion):
        self.__ID = identificacion

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        self.__precio = valor

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
        self.__empresa = empresa

    def __str__(self):
        return f"""Datos de la maquina:
        ID: {self.__ID}
        Precio: {self.__precio}
        Stock: {self.__stock}
        Empresa: {self.__empresa}
        Modelo: {self.__modelo}"""
