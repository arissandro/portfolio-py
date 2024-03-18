class Triangulo:
    def __init__(self, lado_a, lado_b, lado_c):
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

    def calcular_perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c


triangulo = Triangulo(1, 1, 1)

print(triangulo.calcular_perimetro())
