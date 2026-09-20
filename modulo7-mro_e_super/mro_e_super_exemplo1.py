class A:
    def quem_sou(self):
        print("metodo de A")

class B(A):
    def quem_sou(self):
        print("metodo B")

class C(A):
    def quem_sou(self):
        print("metodo C")

class D(B, C):
    pass

d = D()
d.quem_sou()
