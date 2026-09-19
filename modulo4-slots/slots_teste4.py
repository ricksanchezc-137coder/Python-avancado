import weakref

class SemSlots:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

class ComSlots:
    __slots__ = ('nome', 'saldo')
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

class ComSlotsWeakref:
    __slots__ = ('nome', 'saldo', '__weakref__')
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

obj = ComSlots("teste", 50)
#ref = weakref.ref(obj)
#print("Weakref OK:", ref())


obj2 = ComSlotsWeakref("teste2", 60)
ref2 = weakref.ref(obj2)
print("Weakref OK:", ref2())
