from entity.user.Client import Client
from entity.activity.Train import Train


class Reserva:
    def __init__(self, cliente: Client, actividad: Train):
        self.cliente: Client = cliente
        self.actividad: Train = actividad
        self.precioFinal : float = actividad.calcular_precio()

    def ver_reserva(self):
        
        return f"\nCliente: {self.cliente.descripcion()} \nActiviadad: {self.actividad.getNombre()} \nPrecio: {self.precioFinal}€\n"