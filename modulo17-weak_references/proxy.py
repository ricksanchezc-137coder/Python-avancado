import weakref
import gc

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"Pessoa({self.nome})"

p = Pessoa("Bruno")
prox = weakref.proxy(p)

print("Antes de deletar:")
print("prox.nome:", prox.nome)
print("prox:", prox)

del p
gc.collect()

print("\nDepois de deletar:")
try:
    print("prox.nome:", prox.nome)
except ReferenceError as e:
    print("ReferenceError capturado:", e)
