import weakref
import gc


class Sessao:
    def __init__(self, usuario):
        self.usuario = usuario

    def __repr__(self):
        return f"Sessao({self.usuario})"


cache = weakref.WeakValueDictionary()

s1 = Sessao("joao")
s2 = Sessao("maria")

cache["joao"] = s1
cache["maria"] = s2

print("Antes de deletar:")
print("chaves no cache:", list(cache.keys()))
print("cache['joao']:", cache["joao"])

# Remove a referência forte só de s1
del s1
gc.collect()

print("\nDepois de deletar s1:")
print("chaves no cache:", list(cache.keys()))

try:
    print("cache['joao']:", cache["joao"])
except KeyError as e:
    print("KeyError capturado:", e)

print("cache['maria'] ainda existe:", cache["maria"])
