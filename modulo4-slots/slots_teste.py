class SemSlots:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

class ComSlots:
    __slots__ = ('nome', 'saldo')
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

sem_slots = SemSlots("joao", 100)
com_slots = ComSlots("joao", 100)

sem_slots.email = "teste@teste.com"
print("SemSlots OK:", sem_slots.email)

com_slots.email = "teste@teste.com"
print("ComSlots OK:", com_slots.email)
