from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class Par(Generic[K, V]):
    def __init__(self, chave: K, valor: V) -> None:
        self.chave = chave
        self.valor = valor

    def __repr__(self) -> str:
        return f"Par({self.chave!r}, {self.valor!r})"

    def inverter(self) -> "Par[V, K]":
        return Par(self.valor, self.chave)


# Testes
p1: Par[str, int] = Par("idade", 30)
print(p1)

p2 = p1.inverter()
print(p2)

p3: Par[str, list[int]] = Par("notas", [8, 9, 10])
print(p3)
