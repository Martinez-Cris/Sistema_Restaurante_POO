from abc import ABC, abstractmethod
from typing import List

# Creacion de clases abastractas
class Persona(ABC): 
    #Constructor -> esto permite crear los atributod y metodos o Variables y funciones
    def __init__(self, nombre: str) -> None: #El none dignifica que no me va a devolver ningun valor en el return
        self.nombre= nombre
    # Getter, Muestra la informacion. (por cada atributo que se cree, debe haber un Getter)
    #Vamos a crear el getter con decoradores "@" (tambien llamada programacion profesional)
    @property #Todo lo que tenga un property es un Getter
    def nombre(self) -> str:
        return self.nombre
    @nombre.setter #Este me ayuda a remplazar un valor 
    def nombre(self, nuevo_nombre: str) -> None:
        if isinstance(nuevo_nombre, str) and nuevo_nombre != "" and nuevo_nombre.strip():
            self.nombre = nuevo_nombre
        else: 
            raise ValueError("El nombre digitado debe ser una cadena de texto valido")
    @abstractmethod
    def presentar(self) -> None: # Todo hijo que lo herede debe utilizarlo obligatoriamente
        pass # obligamos a que cada clase hija modifique ese metodo. lo personalice

    #Vamos a crear clases hijas
class Cliente(Persona):
    def presentar(self) -> None:
        print(f"El cliente {self.nombre}, llego al restaurante y pidio una mesa ") 
class Empleado(Persona):
    @abstractmethod
    def trabajar(self) -> None:
        pass
class Mesero(Empleado):
    def presentar(self) -> None:
        print(f"El mesero {self.nombre} esta dirigiendose a la mesa con la carta")
    def trabajar(self) -> None: 
        print(f"El mesero {self.nombre} esta toamndo el pedido de una mesa")
class Chef(Empleado):
    def presentar(self) -> None:
        print(f"El Chef {self.nombre} esta en la cocina")
    def trabajar(self) -> None: 
        print(f"El Chef {self.nombre} esta preparando la comida")



#composicion
#tengo 1 cocina y muchos cocineros o chefs (1:N en Entidad - Relacion)
