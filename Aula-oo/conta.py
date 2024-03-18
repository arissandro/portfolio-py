# -*- coding: utf-8 -*-

class Conta:
    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limit = limite

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        if valor > self.saldo:
            print('valor insuficienta na conta')
        else:
            self.saldo -= valor
            print('sucesso:')

    def extrato(self):
        print(self.numero)
        print(self.saldo)

    def transfere(self, valor, outra_conta):
        if self.saldo < valor:
            print(
                'É impossível realizar a transferência por falta de saldo. Seu saldo é de: ' + str(self.saldo))
        else:
            self.saldo -= valor
            outra_conta.deposita(valor)
            print("Transferência de R$" + str(valor) + " realizada com sucesso.")
