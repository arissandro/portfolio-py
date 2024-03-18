
print('\nInsira as 3 informações para saber a taboada, potencia e os numeros subsequentes\n')

#Pede ao usuário um numero inteiro e imprime a tabuada do numero (1 ao 10)
num = int(input('Digite um número inteiro para saber sua tabuada: '))
print("A tabuada de", num, "é:")
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
print('\n')

#Pede ao usuário um número inteiro e imprima o potencial desse número
numero = int(input("Digite um número inteiro para saber seu potencial: "))
potencia = numero ** 2
print("O potencial de", numero, "é", potencia)
print('\n')

#Pede ao usuário um número inteiro e imprime 20 números subsequntes ao digitado.
numero = int(input("Digite um número inteiro para saber ver seus números subsequentes: "))
for i in range(numero+1, numero+21):
    print(i)