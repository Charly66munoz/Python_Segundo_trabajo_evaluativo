from entity.activity.Train import Train

class PersonalTrain(Train):

    def __init__(self, nombre, precioBase, capacidad, recargo):
        super().__init__(nombre, precioBase, capacidad)
        self.recargo = recargo  

    def calcular_precio(self):
        return self.precioBase * (1 + self.recargo)
       
    def descripcion(self):
        return super().descripcion() + f"\nClase: personal \nPrecio final: {self.calcular_precio()}€"