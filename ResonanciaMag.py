from Maquina import *

class ResonanciaMag(Maquina):
    def __init__(self):
        super().__init__()
        self.__intensidad = ""

    @property
    def intensidad(self):
        return self.__intensidad

    @intensidad.setter
    def energia(self, b):
        self.__intensidad = b

    def __str__(self):
        return f'{super().__str__()}, intensidad del campo magnetico en teslas: {self.intensidad}'
