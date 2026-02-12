from entity.user.User import User
#Clase hija de user
class Client(User):


    def __init__(self, _nombre, _email ):
        super().__init__(_nombre, _email)
        
    def borrar_reserva():
        pass

    def agregar_reserva():
        pass

    def descripcion(self):
        print("-------------")
        return f"{self._nombre} , ${self._email}" 

    