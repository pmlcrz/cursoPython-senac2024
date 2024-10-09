class Copo:
    def encher(self):
        print("O copo foi enchido com cerveja!")

def main():
    print('''Bem-vindo à festa! 
             Qual o seu nome?''')
    nome = input("R: ")
    print(f"Olá, {nome}!")  # O 'f' serve para usar variáveis dentro do texto

    print("Qual a sua idade?")
    idade = input("R: ")

    # Verifique se a entrada é um número válido
    if idade.isdigit():
        idade = int(idade)
        
        if idade >= 18:
            print("Você é maior de idade, então pode entrar na festa.")
            copo = Copo()
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


