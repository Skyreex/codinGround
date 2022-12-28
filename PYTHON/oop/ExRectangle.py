class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def __str__(self):
        return f"l = {self.longueur} // L = {self.largeur}"

    def perimetre(self):
        P = (self.largeur + self.longueur) * 2
        return f"{P}m"

    def surface(self):
        S = self.largeur * self.longueur
        return f"{S}m2"


class Paralepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.hauteur = hauteur

    def __str__(self):
        return f"l = {self.longueur} // L = {self.largeur} // h = {self.hauteur}"

    def volume(self):
        V = self.largeur * self.hauteur * self.longueur
        return f"{V}m3"


rec1 = Rectangle(1, 3)
para1 = Paralepipede(1, 4, 6)
print(para1)
print(rec1)
print(rec1.perimetre())
print(rec1.surface())
print(para1.volume())
