import weakref
import gc

class Recurso:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return f"Recursos({self.nome})"

def ao_coletar(referencia_morta):
    print(f"[callback] objeto foi coletado! referencia agora e: {referencia_morta}")

r = Recurso("conexao_db")
ref = weakref.ref(r, ao_coletar)

print("Objeto criado", ref())
print("\nDeletando o objeto")
del r
gc.collect()

print("Depois da coleta, ref():", ref())
