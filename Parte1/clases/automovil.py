from .vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindradas):
        super().__init__(marca, modelo, num_ruedas)
        self.__velocidad = velocidad
        self.__cilindradas = cilindradas
    
    def get_velocidad(self):
        return self.__velocidad

    def get_cilindradas(self):
        return self.__cilindradas
    
    def __str__(self):
        return super().__str__() + f", velocidad: {self.get_velocidad()} Km/h, clindradas: {self.get_cilindradas()}cc"