class MetaSingleton(type):
    _instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            print(f"[__call__] criando a primeira (e unica) instancia de {cls.__name__}")
            cls._instancias[cls] = super().__call__(*args, **kwargs)
        else:
            print(f"[__call__] reaproveitando instancia existente de {cls.__name__}")
        return cls._instancias[cls]


class Configuracao(metaclass=MetaSingleton):
    def __init__(self, valor):
        print(f"__init__ rodando com valor={valor}")
        self.valor = valor

c1 = Configuracao(10)
c2 = Configuracao(20)

print(c1 is c2)
print(c1.valor, c2.valor)
