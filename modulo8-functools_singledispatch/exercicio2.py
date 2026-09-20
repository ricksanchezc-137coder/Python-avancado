from functools import singledispatchmethod
class Formatador:
    @singledispatchmethod
    def formatar(self, valor):
        return f"Valor generico: {valor!r}"

    @formatar.register
    def _(self, valor: int):
        return f"Inteiro formatado: {valor:,}".replace(",", ".")

    @formatar.register
    def _(self, valor: float):
        return f"Valor monetario: R$ {valor:.2f}"

    @formatar.register
    def _(self, valor: str):
        return f"Texto: {valor.upper()}"


f = Formatador()
print(f.formatar(1000000))
print(f.formatar(49.9))
print(f.formatar("python"))
