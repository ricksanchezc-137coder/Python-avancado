class Log:
    def __get__(self, obj, objtype=None):
        print(f"Lendo o atributo em {obj!r}")
        return 42

class Exemplo:
    atributo = Log()

e = Exemplo()

#print(e.atributo)

#print(Exemplo.atributo)

e2 = Exemplo()
#e2.__dict__["atributo"] = "valor direto na instancia"
#print(e2.atributo)


class Positivo:
    def __set_name__(self, owner, name):
        self.nome_privado = "_" + name

    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.nome_privado, 0)

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("valor nao pode ser negativo")
        obj.__dict__[self.nome_privado] = value

    def __delete__(self, obj):
        print(f"deletando {self.nome_privado}")
        del obj.__dict__[self.nome_privado]

class Conta:
    saldo = Positivo()
    limite = Positivo()

c = Conta()

c.saldo = 100
c.limite = 500
print(c.saldo, c.limite)
print(c.__dict__)

del c.saldo
print(c.saldo)
