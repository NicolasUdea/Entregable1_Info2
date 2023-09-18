from Maquina import *

class ECG(Maquina):
    def __init__(self):
        super().__init__()
        self.__derivaciones = 0

    @property
    def derivaciones(self):
        return self.__derivaciones

    @derivaciones.setter
    def derivaciones(self, b):
        self.__derivaciones = b

    def __str__(self):
        return f'{super().__str__()}, numero de derivaciones: {self.derivaciones}'
