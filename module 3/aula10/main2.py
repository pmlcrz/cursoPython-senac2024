class Copo:
    def __init__(self, tipo):
        self.tipo = tipo

    def encher(self):
        print(f"O copo de {self.tipo} foi enchido com cerveja!")

def escolher_copo():
    print("Escolha um copo:")
    print("1. Vidro (transparente, 200 ml)")
    print("2. Stanley (prata, 500 ml, inox)")
    
    while True:
        escolha = input("Digite o número da sua escolha: ")
        if escolha == "1":
            return Copo("vidro (transparente, 200 ml)")
        elif escolha == "2":
            return Copo("Stanley (prata, 500 ml, inox)")
        else:
            print("Escolha inválida! Tente novamente.")

def main():
    print('''Bem-vindo à festa! 
             Qual o seu nome?''')
    nome = input("R: ")
    print(f"Olá, {nome}!")  # O 'f' serve para usar variáveis dentro do texto

    print("Qual a sua idade?")
    idade = input("R: ")

    if idade.isdigit():
        idade = int(idade)
        
        if idade >= 18:
            print("Você é maior de idade, então pode entrar na festa.")
            copo = escolher_copo()  # Chama a função para escolher o copo
            copo.encher()
        else:
            print("Você está com seus pais?")
            pais = input("Digite [S] para sim ou [N] para não: ")
            if pais.upper() == "S":
                print("Você é menor! \nMas você pode entrar na festa, pois está acompanhado dos pais.")
            else:
                print("Você foi barrado(a)")
    else:
        print("Você não digitou um valor válido.")

if __name__ == "__main__":
    main()
