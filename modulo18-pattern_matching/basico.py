def comando(texto):
    match texto:
        case "start":
            return "iniciando"
        case "stop" | "quit":
            return "parando"
        case _:
            return "desconhecido"

def status(codigo):
    match codigo:
        case 200:
            return "ok"
        case 404:
            return "nao encontrado"
        case 500 | 502 | 503:
            return "erro do servidor"
        case _:
            return "outro"

for c in ["start", "stop", "quit", "abc"]:
    print(c, "->", comando(c))

for s in [200, 404, 502, 301]:
    print(s, "->", status(s))
