class Campo:
    def __set_name__(self, owner, nome):
        self.nome_publico = nome
        self.nome_privado = (f"_{nome}")

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.nome_privado, None)

    def __set__(self, obj, valor):
        setattr(obj, self.nome_privado, valor)

class Usuario:
    nome = Campo()
    email = Campo()

u = Usuario()
u.nome = "João"
print(u.nome)
print(Usuario.nome.nome_publico, Usuario.nome.nome_privado)
