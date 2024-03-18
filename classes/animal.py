# -*- coding: utf-8 -*-
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def fazer_barulho(self):
        pass


class Cachorro(Animal):
    def fazer_barulho(self):
        return "Au Au!"


class Gato(Animal):
    def fazer_barulho(self):
        return "Miau Miau!"


cachorro = Cachorro("Rex")
gato = Gato("Whiskers")


print(cachorro.nome + " faz: " + cachorro.fazer_barulho())
print(gato.nome + " faz: " + gato.fazer_barulho())
