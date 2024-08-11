''' Construa uma página/programa onde o usuário digitará um número, a página fará
uma contagem regressiva até zero e, depois, contará de zero até o número que o
usuário digitou.
'''

numero = int(input("Digite um número: "))

for i in range(numero, -1, -1):
    print(i, end=" ")

print("\n")

for i in range(0, numero + 1):
    print(i, end=" ")
