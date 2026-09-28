def ler_comando(partes):
    match partes:
        case []:
            return "vazio"
        case ["sair"]:
            return "saindo"
        case ["ir", destino]:
            return f"indo para {destino}"
        case ["copiar", origem, destino]:
            return f"copiando {origem} -> {destino}"
        case ["somar", *numeros]:
            return f"soma = {sum(numeros)}"
        case [primeiro, *resto]:
            return f"comando '{primeiro}' com {len(resto)} args"
testes = [
    [],
    ["sair"],
    ["ir", "casa"],
    ["copiar", "a.txt", "b.txt"],
    ["somar", 1, 2, 3, 4],
    ["somar"],
    ["xyz", 1, 2],
    ("ir", "rua"),
    "ir",
]

for t in testes:
    print(t, "->", ler_comando(t))
