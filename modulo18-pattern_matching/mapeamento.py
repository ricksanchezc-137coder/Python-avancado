def tratar_evento(evento):
    match evento:
        case {"tipo": "clique", "x": x, "y": y}:
            return f"clique em ({x}, {y})"
        case {"tipo": "tecla", "tecla": t}:
            return f"tecla {t}"
        case {"tipo": "saque", "valor": v, **resto}:
            return f"saque de {v}, extras: {resto}"
        case {"tipo": _}:
            return "tipo desconhecido"
        case _:
            return "nao e um evento"

testes = [
    {"tipo": "clique", "x": 10, "y": 20},
    {"tipo": "clique", "x": 10, "y": 20, "botao": "esq"},
    {"tipo": "clique", "x": 10},
    {"tipo": "tecla", "tecla": "a"},
    {"tipo": "saque", "valor": 50, "conta": 1, "moeda": "BRL"},
    {"nome": "joao"},
    "clique",
    [1, 2],
]
for t in testes:
    print(t, "->", tratar_evento(t))
