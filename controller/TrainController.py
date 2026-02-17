from entity.activity.GroupTrain import GroupTrain
from entity.activity.PersonalTrain import PersonalTrain
from entity.activity.Train import Train
from typing import List

class TrainController:
    def __init__(self, trains: List[Train] | None = None):
        self.trains: List[Train] = trains if trains is not None else []
        #aqui ponemos a List como valor por defecto y luego utilizamos operador ternario para evitar duplicados


    def crear_clase(self):
        print("1-Grupal \n2-Personal")
        print("Elija el tipo de clase que desea crear")

        while True:
            try:
                opcion = int(input())
                if opcion in (1, 2):
                    break
                print("Opción inválida")
            except ValueError:
                print("Debe ingresar un número")

        capacidad = 0
        print("Nombre: ")
        nombre = input()
        while len(nombre) < 3:
            nombre = input("Ingrese un nombre valido: ")

        while True:
            try:
                print("Precio base: ")
                precioBase = int(input())
                break
            except ValueError:
                print("Debe ingresar un número")

        if opcion == 1:
            while True:
                try:
                    print("Capacidad: ")
                    capacidad = int(input())
                    break
                except ValueError:
                    print("Debe ingresar un número")
        else:
            capacidad = 1
                

        if opcion == 1:
            train = GroupTrain(nombre, precioBase, capacidad)
            self.trains.append(train)
            print("Clase grupal creada correctamente")

        elif opcion == 2:
            print("Ingrese el recargo que desea: ")
            print("1 - 10%")
            print("2 - 25%")
            print("3 - 50%")
            recargoOpcion = -1
            try:
                while recargoOpcion <= 0 or recargoOpcion > 3:
                    recargoOpcion = int(input())

                if recargoOpcion == 1:
                    recargo = 0.10
                elif recargoOpcion == 2:
                    recargo = 0.25
                elif recargoOpcion == 3:
                    recargo = 0.50
                

                train = PersonalTrain(nombre, precioBase, capacidad, recargo)
                self.trains.append(train)
                print("Clase personal creada correctamente")

            except ValueError:
                print("Recargo inválido, no se pudo crear la clase")

        else:
            print("No se ha podido crear el entrenamiento, vuelva a intentarlo")
            return
        
    def mostrar_info(self):
        if not self.trains:
            print("Aun no existen clases creadas, cree una clase primero")
            return
        else:
            groups = []
            individuals = []

        for u in self.trains:
            if isinstance(u, GroupTrain):                       
                groups.append(u)
            elif isinstance(u, PersonalTrain):
                individuals.append(u)
            
            if groups:
                print("----------\nCLASES GRUPALES:")
                for group in groups:
                    print(f"{group.descripcion()}")
            
            if individuals:
                for indiv in individuals:
                    print(f"----------\nCLASES PERSONALES: {indiv.descripcion()}")

    #Nos retorna un array con el tipo de clase que se haya especificado.
    #En un futuro se puede hacer por medio de texto.
    def filtrar_por_tipo(self, tipo):
        if tipo == 1:
            return [u for u in self.trains if isinstance(u, GroupTrain)]

        elif tipo == 2:
            return [u for u in self.trains if isinstance(u, PersonalTrain)]
        else:
            return []
        
    #Funcion creada para ver cupos
    def mostrar_cupos(self):
        if self.trains == []:
            print("No existen entrenamientos aun")
            return
        print("Cupos:")
        for t in self.trains:
            print(f"{t.getNombre()} - {len(t.getInscriptos())}/{t.getCapacidad()}")