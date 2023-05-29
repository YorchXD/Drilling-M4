from .vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo):
        super().__init__(marca, modelo, num_ruedas)
        self.tipo = tipo
    
    def __str__(self):
        return super().__str__() + f", tipo: {self.tipo}"