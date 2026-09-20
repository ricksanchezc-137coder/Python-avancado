import math
from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        ...

    @property
    @abstractmethod
    def nome(self):
        ...

    def descricao(self):
        return f"{self.nome} tem area de {self.area():.2f}"

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pi * self.raio ** 2

    @property
    def nome(self):
        return "Circulo"

class Quadrado(FormaGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    @property
    def nome(self):
        return "Quadrado"

c = Circulo(5)
q = Quadrado(4)
print(c.descricao())
print(q.descricao())
