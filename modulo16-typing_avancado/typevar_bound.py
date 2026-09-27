from typing import TypeVar

NumeroT = TypeVar("NumeroT", bound=float)

def dobrar(valor: NumeroT) -> NumeroT:
    return valor * 2

ChaveT = TypeVar("ChaveT", int, str)

def repetir_chave(chave: ChaveT, vezes: int) -> list[ChaveT]:
    return [chave] * vezes

print(dobrar(5))
print(dobrar(3.5))

print(repetir_chave(7, 3))
print(repetir_chave("x", 2))
