#class Base1:
#    __slots__ = ('a',)

#class Base2:
#    __slots__ = ('b',)

#class Combinada(Base1, Base2):
#    __slots__ = ()

class ComDefault:
    __slots__ = ('saldo')
    saldo = 0

obj = ComDefault()
