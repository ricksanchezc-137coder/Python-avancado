from typing import overload

@overload
def buscar(chave: str) -> str | None: ...
@overload
def buscar(chave: str, padrao: str) -> str: ...


def buscar(chave, padrao=None):
    dados = {"nome": "joao", "linguagem": "python"}
    if chave in dados:
        return dados[chave]
    return padrao

r1 = buscar("nome")
r2 = buscar("idade")
r3 = buscar("idade", "nao informado")

print(f"buscar('nome') -> {r1!r}")
print(f"buscar('idade') -> {r2!r}")
print(f"buscar('idade', 'nao informado') -> {r3!r}")

