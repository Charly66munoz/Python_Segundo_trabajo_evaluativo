from entity.user.User import User
from typing import List
#Clase hija de user
class Trainer(User):


    def __init__(self, _nombre, _email, _speacility: List[str] | None):
        super().__init__(_nombre, _email)
        self._speacility: List[str] = _speacility if _speacility is not None else[]
        
    def descripcion(self):
        print("-------------")
        return f"Nombre:{self._nombre},\nEmail: {self._email},\nEspecialidad: {self.to_string_my()}" 
    
    def to_string_my(self):
        
        string = ""
        index = len(self._speacility)
        puntosComa = ","
            
        for speciality in self._speacility:
            index = index -1
            if index > 0:
                string += f"{speciality}{puntosComa}\n" 
            else:
                puntosComa = "."
                string += f"{speciality}{puntosComa}\n" 
            
        return string
                

    