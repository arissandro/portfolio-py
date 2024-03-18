# -*- coding: utf-8 -*-
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def informacaos(self):
        print("A Marca é: " + self.marca + "\n"
              + "O modelo é: " + self.modelo + "\n"
              + "O ano é: " + self.ano + "\n")


carro = Carro("heida", "pacre", "2232")

carro.informacaos()
