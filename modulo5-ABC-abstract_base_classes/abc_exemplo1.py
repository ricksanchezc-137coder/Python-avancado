from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        ...

class Circulo(FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio

c = Circulo(5)
