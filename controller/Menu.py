#Entidades
from entity.user.Client import Client
from entity.user.Trainer import Trainer
#Controllers
from controller.UserController import UserController
from controller.GlobalFuncion import GlobaFunction
from controller.TrainController import TrainController
from controller.ReservationController import ReservationController

class Menu:
    def __init__(self):
        self.userController = UserController()
        self.trainController = TrainController()
        self.reservationController = ReservationController()

    def menu(self):
        while True:
            print(
                "Elija la opcion:\n"
                "1-Crear Usuario\n"
                "2-Mostrar usuarios\n"
                "3-Buscar usuario (Puede consultar existencia, agregar reserva y ver las reservas creadas)\n"
                "4-Crear clase\n"
                "5-Mostrar clases\n"
                "6-Buscar clases\n"
                "0-Salir"
                    )
            try:
                option = int(input())
            except ValueError:
                print("Valor ingresado incorrectamente, debe escribir un numero")
                continue
            
            match option:
                case 1:
                    self.menu_crear_usuario()
                case 2:
                    self.userController.mostrar_info()
                case 3:
                    user = self.busqueda_user()
                    if user:
                        print("usuario seleccionado correctamente")
                        if isinstance(user, Client):
                            self.menu_cliente(user)
                        elif isinstance(user, Trainer):
                            self.menu_entrenador()
                        
                case 4:
                    self.menu_crear_clase()
                case 5:
                    self.trainController.mostrar_info()
                case 6:
                    self.busqueda_clase()
                    

                case 0:
                    print("Saliendo del sistema")
                    return
                case _:
                    print("Opción inválida")



    def menu_crear_usuario(self):
        while True:
            self.userController.crear_usuario()

            value = input("¿Desea crear otro usuario? s/n: ")
            result = GlobaFunction.valor_valido(value)

            if result is True:
                continue     
            elif result is False:
                return       
            else:
                print("Valor inválido, use s/n")
    
    
    def busqueda_user(self):
        print("¿Que tipo de usuario desea buscar?")
        print("1-Cliente")
        print("2-Entrenador")
        print("Seleccione una opción: ")
        try:
            tipo = int(input())
        except ValueError:
            print("Debe ingresar un número")
            return

        usuarios = self.userController.filtrar_por_tipo(tipo)

        if not usuarios:
            print("Aun no existen usuarios de este tipo usuarios de este tipo")
            return False                  
        print()
        #i seria nuestro indice, mientras que u es el objeto. Ponemos start para que comienze desde el 1 la lista
        for i, u in enumerate(usuarios, start=1):
            print(f"{i}- {u.descripcion()}")
        print("Seleccione un usuario:")
        print("Ingrese el numero del usuario")
        indice = int(input())

        if indice <0 or indice >= len(usuarios):
            print("Seleccion invalida")
            return
        return usuarios[indice]
    
    def menu_crear_clase(self):
        while True:
            self.trainController.crear_clase()

            value = input("¿Desea crear otra clase? s/n: ")
            result = GlobaFunction.valor_valido(value)

            if result is True:
                continue
            elif result is False:
                return
            else:
                print("Valor inválido, use s/n")

    def busqueda_clase(self):


        print("¿Qué tipo de clase desea buscar?")
        print("1-Grupal")
        print("2-Personal")

        try:
            tipo = int(input())
        except ValueError:
            print("Debe ingresar un número")
            return
        if tipo > 2 or tipo < 0:
            print("El valor ingresado es incorrecto, debe ser un numero entre 1 o 2")
            return

        clases = self.trainController.filtrar_por_tipo(tipo)

        if not clases:
            print("Aun no hay clases de este tipo")
            return

        for i, c in enumerate(clases, start=1):
            print(f"{i}- {c.descripcion()}")
        print("Seleccione un entrenamiento:")
        
    

    #sub menu creado para manejar opciones de cliente
    def menu_cliente(self, user):
        while True:
            print(
                "Elija la opcion:\n"
                "1-Crear reserva\n"
                "2-mostrar reservas\n"
                
                "0-Salir"
                    )
            try:
                option = int(input())
            except ValueError:
                print("Valor ingresado incorrectamente, debe escribir un numero")
                continue
            
            match option:
                case 1:
                    self.agregar_reserva(user)
                case 2:
                    self.reservationController.ver_detalle_reservas_c(user)
                case 0:
                    print("Saliendo del sistema")
                    return
                case _:
                    print("Opción inválida")

    
    
    def agregar_reserva(self, user):
        estado = False
        while estado == False:
            activity =  self.busqueda_clase()
            if activity.consultar_dispo():
                self.reservationController.agregar_reserva(user, activity)
                print("Reserva hecha correctamente")
                return
            else:
                print("No hay mas disponiblidad")
                print("Seleccione otra actividad")
                estado = False

    
    #sub menu creado para manejar opciones de entrenador
    def menu_entrenador(self):
        while True:
            print(
                "Elija la opcion:\n"
                "1-Ver reservas\n"
                "2-Ver cupos\n"
                
                "0-Salir"
                    )
            try:
                option = int(input())
            except ValueError:
                print("Valor ingresado incorrectamente, debe escribir un numero")
                continue
            
            match option:
                case 1:
                    self.reservationController.ver_detalle_reservas()
                case 2:
                    self.trainController.mostrar_cupos()
                case 0:
                    print("Saliendo del sistema")
                    return
                case _:
                    print("Opción inválida")