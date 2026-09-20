class A:
    def quem_sou(self):
        print("metodo de A")

class B(A):
    def quem_sou(self):
        print("metodo B")
        super().quem_sou()

class C(A):
    def quem_sou(self):
        print("metodo C")
        super().quem_sou()

class D(B, C):
    pass

d = D()
d.quem_sou()
