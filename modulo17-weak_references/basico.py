import weakref
import gc

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"Pessoa({self.nome})"

p = Pessoa("Ana")

ref = weakref.ref(p)

print("Antes de deletar:")
print("ref():", ref())
print("ref() is p: ", ref() is p)

del p
gc.collect()
print("\nDepois de deletar:")
print("ref():", ref())
