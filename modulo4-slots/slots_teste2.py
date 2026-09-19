class SemSlots:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

class ComSlots:
    __slots__ = ('nome', 'saldo')
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

class ComSlotsFilha(ComSlots):
    pass

class ComSlotsFilhaCorrigida(ComSlots):
    __slots__ = ()

filha = ComSlotsFilha("maria", 200)
filha.email = "novo@teste.com"
#print("ComSlotsFilha OK:", filha.email)
#print("Tem __dict__?", hasattr(filha, '__dict__'))

filha2 = ComSlotsFilhaCorrigida("pedro", 300)
print("Tem __dict__?", hasattr(filha2, '__dict__'))
filha2.email = "outro@teste.com"
