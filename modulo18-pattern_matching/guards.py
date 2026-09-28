def classificar(valor):
    match valor:
        case int(n) if n < 0:
            return f"{n} e negativo"
        case int(n) if n == 0:
            return "zero"
        case int(n) if n % 2 == 0:
            return f"{n} e par positivo"
        case int():
            return "impar positivo"
        case [x, y] if x == y:
            return f"par igual: {x}"
        case [x, y]:
            return f"par diferente: {x}, {y}"
        case ("ok" | "erro") as status:
            return f"status: {status}"
        case [("a" | "b") as letra, *_]:
            return f"lista comecando com {letra}"
        case _:
            return "outro"


testes = [-5, 0, 8, 7, [3, 3], [3, 4], "ok", "erro",
          ["a", 1, 2], ["z", 1, 2], True, 3.5]

for t in testes:
    print(repr(t), "->", classificar(t))
