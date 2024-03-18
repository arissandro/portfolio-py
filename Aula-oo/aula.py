from conta import Conta

conta = Conta('123-4', 'maria', 500, 990.9)
conta2 = Conta('132-3', 'carlos', 500, 9000)

print('titular da conta: ' + str(conta.titular))
print('saldo da conta: {}'.format(conta.saldo))

conta.transfere(50, conta2)

print('titular da conta: ' + str(conta.titular))
print('saldo da conta: {}'.format(conta.saldo))

print('titular da conta: ' + str(conta2.titular))
print('saldo da conta: {}'.format(conta2.saldo))
