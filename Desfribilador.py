from Maquina import *

class Desfribilador(Maquina):
    def __init__(self):
        super().__init__(self)
        self.__energia = 0

    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self, energia):
        self.__energia = energia

    def __str__(self):
        return f'{super().__str__()}, energia máxima del desfibrilador: {self.energia}'
