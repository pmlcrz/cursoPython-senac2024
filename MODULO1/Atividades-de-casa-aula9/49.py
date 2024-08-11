'''
49. Construa uma página onde o usuário digitará o nome e a média de cinco alunos e o
programa só aceitará a média do aluno caso ela esteja entre zero e dez.
'''

alunos = []

for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    while True:
        media = float(input(f"Digite a média do aluno {i + 1} (0 a 10): "))
        if 0 <= media <= 10:
            alunos.append((nome, media))
            break
        else:
            print("Média inválida! Por favor, insira uma média entre 0 e 10.")

print("\nAlunos e suas médias:")
for aluno in alunos:
    print(f"Nome: {aluno[0]}, Média: {aluno[1]}")
