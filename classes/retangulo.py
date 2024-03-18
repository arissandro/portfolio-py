class Retangulo:
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def calcula_area(self):
        return self.altura * self.largura

    def calcula_perimetro(self):
        return (self.altura * 2) + (self.largura * 2)


retangulo = Retangulo(10, 10)

print(retangulo.calcula_area())
print(retangulo.calcula_perimetro())
