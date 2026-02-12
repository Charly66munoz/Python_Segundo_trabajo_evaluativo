from entity.user.Client import Client
from entity.user.User import User
from entity.user.Trainer import Trainer
from controller.GlobalFuncion import GlobaFunction
from typing import List

class UserController:
    #Aqui ponemos un valor por defecto para evitar que la lista se cree cada ves que se instancie
    def __init__(self, usuarios: List[User] | None = None):
        self.usuarios: List[User] = usuarios if usuarios is not None else []
        #aqui ponemos a List como valor por defecto y luego utilizamos operador ternario para evitar duplicados
    
    
    def crear_usuario(self):
        print("1-Cliente \n2-Entrenador")
        try:
            valor = int(input("Elija el tipo de usuario que desea crear \n"))
        except ValueError:
            print("Valor ingresado incorrectamente, debe escribir un numero")
            return
        if valor > 2 or valor < 0:
            print("El valor ingresado es incorrecto, debe ser un numero entre 1 o 2")
            return
        nombre= input("Nombre: ") 
        while len(nombre) < 3:
            nombre= input("Ingrese un nombre valido: ") 
        email = input("Email: ") 
        while self.email_valido(email) == False:
            email = input("Email: ")
        if valor == 1:
            user = Client(nombre,email)
            self.usuarios.append(user)
        elif valor == 2:
            splty = input("Ingrese la espeacilidad: ")
            speacility = []
            while self.tex_valido(splty) == False:
                splty = input("Ingrese un texto valido: ")
            speacility.append(splty)
            option = True
            while option:
                value = input("¿Desea agregar otra especialidad? s/n: ")
                respuesta = GlobaFunction.valor_valido(value)
                if respuesta is True:
                    other = input("Ingrese la especialidad: ")
                    while not self.tex_valido(other):
                        other = input("Ingrese un texto válido: ")
                    speacility.append(other)
                elif respuesta is False:
                    option = False
                else:
                    print("Valor incorrecto. Use s/n")
            user = Trainer(nombre,email,speacility)
            self.usuarios.append(user)
            print("Usuario creado correctamente")
        else:
            print("No se a podido crear el usuario, vuelva a intentarlo")
            self.crear_usuario() #cambiar a return para que salga
    
    #Funcion creada para hacer una pequeña validez de email
    def email_valido(self, email: str) -> bool:
        if "@" not in email:
            print("El email debe contener '@', vuelva ha intentarlo")
            return False
        if "." not in email.split("@")[1]:
            print("El email es incorrecto, debe contener un ., vuelva ha intentarlo")

            return False
        return True
    

    def mostrar_info(self):
        if not self.usuarios:
            print("Aun no existen usuarios, cree un usario primero")
            return
        else:
            
            clientes = []
            entrenadores = []

            for u in self.usuarios:
                if isinstance(u, Client):                       
                    clientes.append(u)
                elif isinstance(u, Trainer):
                    entrenadores.append(u)
            if clientes:
                print("----------\nClientes")
                for client in clientes:
                    print(f"{client.descripcion()}")
            if entrenadores:
                for client in entrenadores:
                    print(f"----------\nEntrenadores: {client.descripcion()}")
            
    #tex_valido nos permite evitar textos en blanco 
    def tex_valido(self, tex) -> bool:
        if tex is None:
            return False
        if not tex.strip():
            return False
        return True
          
    #Funcion creada para filtrar tipo de usuario, retorna una lista para luego ser enumerada
    # En un futuro esta funcion podria filtrar directamente por texto, teniendo en cuenta que el gym tiene mas de 800 usuarios   
    def filtrar_por_tipo(self, tipo):
        if tipo == 1:
            return [u for u in self.usuarios if isinstance(u, Client)]

        elif tipo == 2:
            return [u for u in self.usuarios if isinstance(u, Trainer)]
        else:
            return []
        
        
    
    