from Maquina import *

class Desfribilador(Maquina):
    def __init__(self, precio, stock, modelo, emrpesa, energia):
        super().__init__(precio, stock, modelo, emrpesa)
        self.__energia = energia

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, energia):
        self.__energia = energia

    def __str__(self):
        return f'{super().__str__()}, energia máxima del desfibrilador: {self.energia}'
