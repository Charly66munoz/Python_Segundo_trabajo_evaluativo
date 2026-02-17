from abc import ABC, abstractmethod

class Train(ABC):
    def __init__(self, nombre, precioBase, capacidad):
        self.nombre = nombre
        self.precioBase = precioBase
        self.capacidad = capacidad
        self.inscriptos = []

    @abstractmethod
    def calcular_precio(self):
        pass

    
    def descripcion(self):
        return (
            f"\nNombre: {self.nombre},\nCapacidad:{self.capacidad},\nInscriptos:{len(self.inscriptos)},\nPrecio {self.precioBase}€,"
        )
    def agregar_inscripto(self, user):
        self.inscriptos.append(user)
        
    
    def consultar_dispo(self):
        return len(self.inscriptos) < self.capacidad
    
    def getNombre(self):
        return self.nombre

    def getPrecioBase(self):
        return self.precioBase

    def getCapacidad(self):
        return self.capacidad
    
    def getInscriptos(self):
        return self.inscriptos

    def setNombre(self, nombre):
        self.nombre = nombre

    def setPrecioBase(self, precioBase):
        self.precioBase = precioBase

    def setCapacidad(self, capacidad):
        self.capacidad = capacidad
    

    def setInscriptos(self, inscriptos):
        self.inscriptos = inscriptos
    



    
