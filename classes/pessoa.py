# -*- coding: utf-8 -*-

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print('Oi, meu nome é {} e eu tenho {} anos de idade'.format(
            self.nome, str(self.idade)))


pessoa = Pessoa("Ari", 45)

pessoa.apresentar()
