from .bicicleta import Bicicleta

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, num_ruedas, tipo, nro_radios, cuadro, motor):
        super().__init__(marca, modelo, num_ruedas, tipo)
        self.__nro_radios = nro_radios
        self.__cuadro = cuadro
        self.__motor = motor
    
    def get_nro_radios(self):
        return self.__nro_radios
    
    def get_cuadro(self):
        return self.__cuadro

    def get_motor(self):
        return self.__motor
    
    def set_nro_radios(self, nro_radios):
        self.__nro_radios = nro_radios
    
    def set_cuadro(self, cuadro):
        self.__cuadro = cuadro
        
    def set_motor(self, motor):
        self.__motor = motor
    
    def __str__(self):
        return super().__str__() + f", numero de radios: {self.get_nro_radios()}, cuadros: {self.get_cuadro()}, motor: {self.get_motor()}"
    
    def __dic__(self):
        return {'marca': self._marca, 'modelo': self._modelo, 'num_ruedas': self._num_ruedas, 'tipo': self._tipo, 'nro_radios':self.get_nro_radios(), 'cuadro':self.get_cuadro(), 'motor': self.get_motor()}