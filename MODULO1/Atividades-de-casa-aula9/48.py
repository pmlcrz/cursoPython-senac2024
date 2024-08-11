pessoas = []

for i in range(10):
    nome = input(f"Digite o nome da pessoa {i + 1}: ")
    bairro = input(f"Digite o bairro da pessoa {i + 1}: ")
    pessoas.append((nome, bairro))

pessoas.sort()

print("\nLista de pessoas em ordem alfabética:")
for pessoa in pessoas:
    print(f"Nome: {pessoa[0]}, Bairro: {pessoa[1]}")
