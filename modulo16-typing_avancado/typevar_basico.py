from typing import TypeVar

T = TypeVar("T")

def primeiro_item(lista: list[T]) -> T:
    return lista[0]

numeros = [1, 2, 3]

nomes = ["ana", "bruno", "carla"]

primeiro_numero = primeiro_item(numeros)
primeiro_nome = primeiro_item(nomes)

print(f"Primeiro numero: {primeiro_numero}")
print(f"Primeiro nome: {primeiro_nome}")

print(f"Tipo de primeiro_numero: {type(primeiro_numero)}")
print(f"Tipo de priemiro_nome: {type(primeiro_nome)}")
