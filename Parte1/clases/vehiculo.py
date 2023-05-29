class Vehiculo:
    def __init__(self, marca, modelo, num_ruedas):
        self._marca = marca
        self._modelo = modelo
        self._num_ruedas = num_ruedas
    
    def __str__(self):
        return f"Marca: {self._marca}, modelo: {self._modelo}, num_ruedas: {self._num_ruedas}"