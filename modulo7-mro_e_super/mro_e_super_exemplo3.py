class A:
    def __init__(self, **kwargs):
        print("Inicializando A")
        self.a = True
        super().__init__(**kwargs)

class B(A):
    def __init__(self, **kwargs):
        print("Inicializando B")
        self.b = True
        super().__init__(**kwargs)

class C(A):
    def __init__(self, **kwargs):
        print("Inicializando C")
        self.c = True
#        super().__init__(**kwargs)

class D(B, C):
    def __init__(self, **kwargs):
        print("Inicializando D")
        self.d = True
        super().__init__(**kwargs)

d = D()
print(vars(d))
