class MetaLog(type):
    def __new__(mcs, nome, bases, namespace):
        print(f"[__new__] criando a classe {nome}")
        print(namespace)
        return super().__new__(mcs, nome, bases, namespace)

    def __init__(cls, nome, bases, namespace):
        print(f"[__init__] classe {nome} ja foi criada, agora inicializando")
        super().__init__(nome, bases, namespace)

class Exemplo(metaclass=MetaLog):
    atributo = 42

    def metodo(self):
        pass

#print("--- classe definida, criando instancia agora ---")
#obj = Exemplo()

class MetaValidada(type):
    def __new__(mcs, nome, bases, namespace):
        if bases and "executar" not in namespace:
            raise TypeError(f"A classe {nome} precisa implementar o metodo 'executar'")
        return super().__new__(mcs, nome, bases, namespace)

class TarefaBase(metaclass=MetaValidada):
    pass


class TarefaValida(TarefaBase):
    def executar(self):
        print("executando....")

#class TarefaInvalida(TarefaBase):
#    pass

#__________

class MetaRegistro(type):
    registro = {}

    def __new__(mcs, nome, bases, namespace):
        cls = super().__new__(mcs, nome, bases, namespace)
        if bases:
            mcs.registro[nome] = cls
        return cls

class ComandoBase(metaclass=MetaRegistro):
    pass 

class ComandoSaque(ComandoBase):
    def executar(self):
        print("executando saque")

class ComandoDeposito(ComandoBase):
    def executar(self):
        print("executando deposito")

print(MetaRegistro.registro)

comando = MetaRegistro.registro["ComandoSaque"]()
comando.executar()

#_______

class MetaOrdem(type):
    @classmethod
    def __prepare__(mcs, nome, bases, **kwargs):
        print(f"[__prepare__] preparando namespace do {nome}")
        return {}

    def __new__(mcs, nome, bases, namespace):
        print(f"[__new__] namespace recebido: {list(namespace.keys())}")
        return super().__new__(mcs, nome, bases, namespace)

class Ordenada(metaclass=MetaOrdem):
    primeiro = 1
    segundo = 2
    terceiro = 3
