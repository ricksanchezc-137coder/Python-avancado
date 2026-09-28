from dataclasses import dataclass

@dataclass
class Ponto:
    x: int
    y: int

@dataclass
class Retangulo:
    largura: int
    altura: int

class Conta:
    __match_args__ = ("titular", "saldo")

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

def descrever(obj):
    match obj:
        case Ponto(0, 0):
            return "origem"
        case Ponto(x, 0):
            return f"ponto no eixo x ({x})"
        case Ponto(x=0, y=y):
            return f" ponto no eixo y ({y})"
        case Ponto(x, y):
            return f" ponto({x}, {y})"
        case Retangulo(largura=l, altura=a):
            return f"retangulo {l}x{a}, area {l * a}"
        case Conta(titular, saldo):
            return f" conta de {titular}, saldo {saldo}"
        case int() | float():
            return "numero"
        case str():
            return "texto"
        case _:
            return "desconhecido"

testes = [
    Ponto(0, 0),
    Ponto(5, 0),
    Ponto(0, 7),
    Ponto(3, 4),
    Retangulo(3, 4),
    Conta("Joao", 100),
    42,
    "oi",
    None,
]

for t in testes:
    print(t, "->", descrever(t))
