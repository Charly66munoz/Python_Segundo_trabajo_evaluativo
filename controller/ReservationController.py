from entity.reservation.Reserva import Reserva
from entity.activity.GroupTrain import GroupTrain
from entity.user.Client import Client
from entity.activity.Train import Train

from typing import List


class ReservationController:
    def __init__(self, reserva : List[Reserva] | None = None):
        self.reserva : List[Reserva] =  reserva if reserva is not None else []
        #aqui ponemos a List como valor por defecto y luego utilizamos operador ternario para evitar duplicados
        
    def agregar_reserva(self, client:Client, train:Train):
        nuevaReserva = Reserva(client, train)
        train.agregar_inscripto(client)
        self.reserva.append(nuevaReserva)
        print("Usuario creado correctamente")
        print(f"Precio: {train.calcular_precio()}")

    def ver_detalle_reservas(self):
        print("RESERVAS:")
        for r in self.reserva:
            print(r.ver_reserva())

    def ver_detalle_reservas_c(self, user: Client):
        print(f"RESERVAS DE {user.get_nombre()}:")
        tieneReservas = False

        for r in self.reserva:
            if r.cliente == user:
                print(r.ver_reserva())
                tieneReservas = True

        if not tieneReservas:
            print("El usuario no tiene reservas.")

