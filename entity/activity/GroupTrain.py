from entity.activity.Train import Train
class GroupTrain(Train):
    
    def calcular_precio(self):
        return self.precioBase
    
    def descripcion(self):
        return super().descripcion() + "\nClase: Común"