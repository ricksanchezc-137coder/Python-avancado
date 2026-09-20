from functools import singledispatch

@singledispatch
def descrever(obj):
    return f"Objeto generico: {obj!r} (tipo: {type(obj).__name__})"

@descrever.register
def _(obj: int):
    return f"Inteiro: {obj} (par: {obj % 2 == 0})"

@descrever.register
def _(obj: str):
    return f"Texto com {len(obj)} caracteres: {obj!r}"

@descrever.register
def _(obj: list):
    return f"Lista com {len(obj)} itens: {obj!r})"

@descrever.register
def _(obj: dict):
    return f"Dicionario com {len(obj)} chaves: {list(obj.keys())}"

@descrever.register(set)
@descrever.register(frozenset)
def _(obj):
    return f"Conjunto ({type(obj).__name__}) com {len(obj)} itens: {obj}"

@descrever.register
def _(obj: bytes | bytearray):
    return f"Dados binarios ({type(obj).__name__}) com {len(obj)} bytes: {obj!r}"

print(descrever(10))
print(descrever(7))
print(descrever("python"))
print(descrever([1, 2, 3]))
print(descrever({"a": 1, "b": 2}))
print(descrever(3.14))
print(descrever(True))
print(descrever({1, 2, 3}))
print(descrever(frozenset([4, 5])))
print(descrever.registry.keys())
print(descrever.dispatch(bool))
print(descrever.dispatch(int))
print(descrever(b"abc"))
print(descrever(bytearray(b"xyz")))
