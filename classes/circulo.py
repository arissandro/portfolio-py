# -*- coding: utf-8 -*-
import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcula_area(self):
        return math.pi * self.raio ** 2


circulo = Circulo(5)

print(circulo.calcula_area())
