# -*- coding: utf-8 -*-
class Agenda:
    def __init__(self):
        self.contatos = {}

    def add_contato(self, nome, numero):
        self.contatos[nome] = numero

    def mostrar_contatos(self):
        print("Lista de Contatos:")
        for nome, numero in self.contatos.items():
            print("Nome: {} - Número: {}".format(nome, numero))


agenda = Agenda()

agenda.add_contato("Maria", "123456789")
agenda.add_contato("João", "987654321")

agenda.mostrar_contatos()
