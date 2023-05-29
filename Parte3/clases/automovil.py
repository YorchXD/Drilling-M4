from .vehiculo import Vehiculo
import csv
import os

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindradas):
        super().__init__(marca, modelo, num_ruedas)
        self._velocidad = velocidad
        self._cilindradas = cilindradas
    
    def __str__(self):
        return super().__str__() + f", velocidad: {self._velocidad} Km/h, clindradas: {self._cilindradas}cc"
    
    def __dic__(self):
        return {'marca': self._marca, 'modelo': self._modelo, 'num_ruedas': self._num_ruedas, 'velocidad':self._velocidad, 'cilindradas':self._cilindradas}