from .automovil import Automovil

class Particular(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindradas, num_puestos):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindradas)
        self.__num_puestos = num_puestos
        
    def get_num_puestos(self):
        return self.__num_puestos
    
    def set_num_puestos(self, num_puestos):
        self.__num_puestos = num_puestos
    
    def __str__(self):
        return super().__str__() + f", numero de puestos: {self.get_num_puestos()}"