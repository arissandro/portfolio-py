# -*- coding: utf-8 -*-
class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def informacaos(self):
        print("Título: " + self.titulo + "\n"
              + "Autor: " + self.autor + "\n"
              + "Ano: " + self.ano)


livro = Livro("Itesei", "eumesmo", "2018")

livro.informacaos()
