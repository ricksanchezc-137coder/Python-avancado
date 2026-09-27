from typing import overload

@overload
def processar(valor: int) -> str: ...
@overload
def processar(valor: str) -> int: ...


def processar(valor):
    if isinstance(valor, int):
        return f"numero: {valor}"
    elif isinstance(valor, str):
        return len(valor)
    else:
        raise TypeError("Tipo nao suportado")

resultado1 = processar(42)
resultado2 = processar("python")

print(f"processar(42) -> {resultado1!r} tipo: {type(resultado1).__name__})")
print(f"processar('python') -> {resultado2!r} tipo: {type(resultado2).__name__})")
