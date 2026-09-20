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

class Triangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2

FormaGeometrica.register(Triangulo)

t = Triangulo(6, 4)
print(isinstance(t, FormaGeometrica))
print(issubclass(Triangulo, FormaGeometrica))
