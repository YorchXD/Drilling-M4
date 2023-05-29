from .vehiculo import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, tipo):
        super().__init__(marca, modelo, num_ruedas)
        self._tipo = tipo
    
    def __str__(self):
        return super().__str__() + f", tipo: {self._tipo}"
    
    def __dic__(self):
        return {'marca': self._marca, 'modelo': self._modelo, 'num_ruedas': self._num_ruedas, 'tipo': self._tipo}