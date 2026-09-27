import weakref
import gc


class Observador:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"Observador({self.nome})"


registrados = weakref.WeakSet()

o1 = Observador("A")
o2 = Observador("B")

registrados.add(o1)
registrados.add(o2)

print("Antes de deletar:")
print("registrados:", list(registrados))
print("total:", len(registrados))

del o1
gc.collect()

print("\nDepois de deletar o1:")
print("registrados:", list(registrados))
print("total:", len(registrados))
