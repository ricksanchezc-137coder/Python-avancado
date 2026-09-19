import tracemalloc

class SemSlots:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

class ComSlots:
    __slots__ = ('nome', 'saldo')
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

tracemalloc.start()
lista_sem_slots = [SemSlots("nome", i) for i in range(100_000)]
_, pico_sem = tracemalloc.get_traced_memory()
tracemalloc.stop()

tracemalloc.start()
lista_com_slots = [ComSlots("nome", i) for i in range(100_000)]
_, pico_com = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Pico SemSlots: {pico_sem / 1024:.1f} KB")
print(f"Pico ComSlots: {pico_com / 1024:.1f} KB")
