'''
54. Construa uma página/programa cadastrando cinco funcionários de uma escola, sendo
que dois deles são professores. Todos os funcionários terão cadastrados seus nomes e
salários e, os professores, terão cadastrados a disciplina às quais lecionam.
'''

funcionarios = []

for i in range(5):
    nome = input(f"Digite o nome do funcionário {i + 1}: ")
    salario = float(input(f"Digite o salário do funcionário {i + 1}: "))

    if i < 2:  
        disciplina = input(f"Digite a disciplina que o professor {i + 1} leciona: ")
        funcionarios.append({'nome': nome, 'salario': salario, 'disciplina': disciplina})
    else:
        funcionarios.append({'nome': nome, 'salario': salario, 'disciplina': None})

print("\nFuncionários cadastrados:")
for funcionario in funcionarios:
    if funcionario['disciplina'] is not None:
        print(f"Professor: {funcionario['nome']}, Salário: R${funcionario['salario']:.2f}, Disciplina: {funcionario['disciplina']}")
    else:
        print(f"Funcionário: {funcionario['nome']}, Salário: R${funcionario['salario']:.2f}")
