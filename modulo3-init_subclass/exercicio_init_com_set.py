class Campo:
    def __set_name__(self, owner, nome):
        self.nome_privado = f"_{nome}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.nome_privado, None)

    def __set__(self, obj, valor):
        setattr(obj, self.nome_privado, valor)


class Modelo:
    registro = {}
    
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.registro[cls.__name__] = cls


class Produto(Modelo):
    nome = Campo()
    preco = Campo()

p = Produto()
p.nome = "teclado"
p.preco = 150
print(Modelo.registro)
print(p.nome, p.preco)
