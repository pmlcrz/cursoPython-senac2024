'''
Crie um jogo de par ou ímpar onde o computador irá gerar um número aleatório e o
usuário irá digitar um número. Após digitar o número, o programa irá utilizar um vetor
para resolver o jogo. Se a soma dos números for par, o usuário vence. Se for ímpar, o
computador vence.
'''

import random

computador = random.randint(0, 10)

usuario = int(input("Digite um número: "))

numeros = [computador, usuario]

soma = sum(numeros)

if soma % 2 == 0:
    print(f"Você escolheu {usuario} e o computador escolheu {computador}.")
    print("A soma é par. Você venceu!")
else:
    print(f"Você escolheu {usuario} e o computador escolheu {computador}.")
    print("A soma é ímpar. Computador venceu!")
