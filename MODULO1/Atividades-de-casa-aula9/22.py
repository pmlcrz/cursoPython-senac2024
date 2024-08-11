'''Construa uma página/programa onde o usuário digitará um número e o programa
completará o número digitado até cem, apenas com números pares.
'''
numero = int(input("Digite um número: "))

for i in range(numero + 1, 101):
    if i % 2 == 0:
        print(i, end=" ")
