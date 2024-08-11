'''37. Construa um programa/página onde o usuário irá digitar seu nome e cidade de onde
está digitando. Essas informações passarão para uma função e, caso a cidade seja
“Rio de Janeiro”, a resposta, além do nome da pessoa, escreverá “Seja Bem-vindo
à Cidade Maravilhosa”. Caso contrário, exibirá apenas o nome e a cidade digitada
(utilizar passagem de parâmetros).
'''

def saudacao(nome, cidade):
    if cidade.lower() == "rio de janeiro":
        print(f"{nome}, Seja bem-vindo(a) à bidade baravilhosa!")
    else:
        print(f"{nome}, de {cidade}")

nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")

saudacao(nome, cidade)
