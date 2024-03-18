# -*- coding: utf-8 -*-
class Conta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def deposita(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


conta = Conta("Ari", 10)

print("Titular da conta: " + conta.titular)
print("saldo da conta: " + str(conta.saldo))
deposito = conta.deposita(10)

conta.sacar(3)
