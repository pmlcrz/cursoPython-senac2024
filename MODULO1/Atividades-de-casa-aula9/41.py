'''
41. Construa uma página/programa onde o usuário digitará oito números, o programa
escreverá na tela qual deles é o maior e qual deles é o menor.
'''

numeros = []

for i in range(8):
    numero = int(input(f"Digite o número {i + 1}: "))
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
