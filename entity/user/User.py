#definimos la clase abstracta para no poder ser instanciada
from abc import ABC, abstractmethod 

class User(ABC):
        
    def __init__(self,_nombre,_email):
        self._nombre = _nombre
        self._email = _email

    @abstractmethod
    def descripcion(self):
        pass

    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, _nombre):
        self._nombre = _nombre
    
    
    def get_email(self):
        return self._email

    def set_email(self, _email):
        self._email = _email




       
