# -*- coding: utf-8 -*-
class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def atualizar(self, novo_preco, nova_quantidade):
        self.preco = novo_preco
        self.quantidade = nova_quantidade

    def mostrar_info(self):
        print("Nome: " + self.nome)
        print("Preço: R$%.2f" % self.preco)
        print("Quantidade: " + str(self.quantidade))


produto1 = Produto("Notebook", 3500.00, 5)


print("Informações do Produto:")
produto1.mostrar_info()

produto1.atualizar(3800.00, 3)


print("\nInformações Atualizadas do Produto:")
produto1.mostrar_info()
