''' 15. Construa uma página/programa onde o usuário digitará três números e o programa
exibirá, na tela, o maior entre eles.'''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
print(f"O maior número é: {maior}")
