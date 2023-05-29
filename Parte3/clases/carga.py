from .automovil import Automovil

class Carga(Automovil):
    def __init__(self, marca, modelo, num_ruedas, velocidad, cilindradas, carga):
        super().__init__(marca, modelo, num_ruedas, velocidad, cilindradas)
        self.__carga = carga
    
    def get_carga(self):
        return self.__carga
    
    def set_carga(self, carga):
        self.__carga = carga
    
    def __str__(self):
        return super().__str__() + f", carga: {self.get_carga()}kg"
    
    def __dic__(self):
        return {'marca': self._marca, 'modelo': self._modelo, 'num_ruedas': self._num_ruedas, 'velocidad':self._velocidad, 'cilindradas':self._cilindradas, 'carga': self.get_carga()}