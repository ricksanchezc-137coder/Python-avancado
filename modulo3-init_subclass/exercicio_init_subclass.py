class Plugin:
    registro = {}

    def __init_subclass__(cls, categoria=None, **kwargs):
        super().__init_subclass__(**kwargs)
        if categoria is None:
            raise TypeError(f"{cls.__name__} precisa definir 'categoria'")
        cls.categoria = categoria
        cls.registro[cls.__name__] = cls

class PluginA(Plugin, categoria="pagamento"):
    pass


class PluginB(Plugin, categoria="notificacao"):
    pass

#class PluginC(Plugin):
#    pass


print(Plugin.registro)
print(PluginA.categoria, PluginB.categoria)

