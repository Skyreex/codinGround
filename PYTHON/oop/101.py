class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def afficher(self):
        return self.a, self.b, self.c

class B(A):
    id = 0
    ls = []
    def __init__(self, a, b, c, d, e):
        A.__init__(self, a, b, c)
        self.d = d
        self.e = e

    def afficher(self):
        return self.a, self.b, self.c, self.d, self.e

    def cree_A(self, a, b, c):
        B.id += 1
        nameInstance = f"A_{B.id}"
        print(nameInstance)
        nameInstance = A(a, b, c)
        print(nameInstance.afficher())
        B.ls.append(nameInstance)

    def afficher_instance(self, nameOfInstance):
        val = B.ls.index(nameOfInstance)
        print(B.ls)



a = A('a', 'b', 'c')
b = B('a', 'b', 'c', 'e', 'd')

print(a.afficher())
print(b.afficher())

b.cree_A('d', 'e', 'k')
b.cree_A('w', 'z', 'j')

b.afficher_instance("A_1")