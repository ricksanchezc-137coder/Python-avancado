from typing import Generic, TypeVar

T = TypeVar("T")

class Pilha(Generic[T]):
    def __init__(self) -> None:
        self._itens: list[T] = []

    def empilhar(self, item: T) -> None:
        self._itens.append(item)

    def desempilhar(self) -> T:
        return self._itens.pop()

    def topo(self) -> T:
        return self._itens[-1]

    def vazia(self) -> bool:
        return len(self._itens) == 0

    def __len__(self) -> int:
        return len(self._itens)

pilha_int: Pilha[int] = Pilha()
pilha_int.empilhar(1)
pilha_int.empilhar(2)
pilha_int.empilhar(3)

print(f"Topo: {pilha_int.topo()}")
print(f"Tamanho: {len(pilha_int)}")
print(f"Desempilhado: {pilha_int.desempilhar()}")
print(f"Tamanho depois: {len(pilha_int)}")

pilha_str: Pilha[str] = Pilha()
pilha_str.empilhar("a")
pilha_str.empilhar("b")

print(f"Topo (str): {pilha_str.topo()}")
print(f"Vazia? {pilha_str.vazia()}")
