''' MÁQUINA DE CAFÉ:
    1º Pedir o número do produto
    2º Valor do produto
    3º Inserir o cartão
    4º Senha do cartão
    5º Entregar o produto
'''

# Produtos disponíveis
produtos = ['Café', 'Capuccino', 'Café com Leite', 'Chocolate']

# Senha do cartão do usuário
senha_correta = 1234

def pagamento():
    # Insira o cartão
    print('Insira o cartão')
    # Conferindo a senha
    try:
        senha = int(input("Digite sua senha: "))
    except ValueError:
        print("Senha inválida. Por favor, tente novamente.")
        menu_principal()
        return

    if senha == senha_correta:
        print('Senha confirmada. Espere a entrega do produto.')
    else:
        print('Senha incorreta, por favor tente novamente.')
        menu_principal()

def menu_principal():
    print('Menu:')
    print('1. Café (R$ 2,00)')
    print('2. Capuccino (R$ 3,50)')
    print('3. Café com Leite (R$ 3,00)')
    print('4. Chocolate (R$ 4,00)')
    print('5. Sair')
    
    try:
        opcao = int(input('Digite o número do produto: '))
    except ValueError:
        print('Você digitou uma opção inválida. Por favor, tente novamente.')
        menu_principal()
        return

    if opcao == 1:
        # opção 1. Café
        print(f'Você escolheu: {produtos[0]}')
        print(f'{produtos[0]} R$ 2,00')
        pagamento()

    elif opcao == 2:
        # opção 2. Capuccino
        print(f'Você escolheu: {produtos[1]}')
        print(f'{produtos[1]} R$ 3,50')
        pagamento()

    elif opcao == 3:
        # opção 3. Café com Leite
        print(f'Você escolheu: {produtos[2]}')
        print(f'{produtos[2]} R$ 3,00')
        pagamento()

    elif opcao == 4:
        # opção 4. Chocolate
        print(f'Você escolheu: {produtos[3]}')
        print(f'{produtos[3]} R$ 4,00')
        pagamento()

    elif opcao == 5:
        print("Obrigado pela preferência")

    else:
        print('Você digitou uma opção inválida. Por favor, tente novamente.')
        menu_principal()

# Início do programa
menu_principal()
