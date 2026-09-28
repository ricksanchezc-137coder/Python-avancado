from enum import Enum

# Parte 1: o nome solto captura e sobrescreve
COR = "vermelho"
valor = "azul"

match valor:
    case COR:
        print("casou! COR agora vale:", COR)

print("depois do match, COR =", COR)


# Parte 2: nomes com ponto comparam de verdade
class Cor(Enum):
    VERMELHO = 1
    AZUL = 2


class Config:
    PADRAO = "vermelho"


def certo(valor):
    match valor:
        case Cor.VERMELHO:
            return "enum vermelho"
        case Config.PADRAO:
            return "padrao"
        case Cor.AZUL:
            return "enum azul"
        case _:
            return "outro"


for v in [Cor.VERMELHO, "vermelho", Cor.AZUL, "azul"]:
    print(repr(v), "->", certo(v))
