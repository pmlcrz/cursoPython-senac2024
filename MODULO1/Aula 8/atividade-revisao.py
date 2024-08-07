# Produtos disponíveis
produtos = ['Café', 'Capuccino', 'Café com Leite', 'Chocolate']
# Senha do cartão do usuário
senhaCorreta = 1234

def menu_principal():
    # Pedir o número do produto
    print("Menu: 1 Café (R$2,40) | 2 Capuccino (R$3,50) | 3 Café com Leite (R$3,00) | 4 Chocolate (R$4,00)")
    opcao = input("Digite o número do pedido: ")
    
    if opcao == '1':
        produto = produtos[0]
        valor = 'R$ 2,40'
    elif opcao == '2':
        produto = produtos[1]
        valor = 'R$ 3,50'
    elif opcao == '3':
        produto = produtos[2]
        valor = 'R$ 3,00'
    elif opcao == '4':
        produto = produtos[3]
        valor = 'R$ 4,00'
    else:
        print('Você digitou uma opção inválida. Por favor, tente novamente.')
        menu_principal()
        return
    
    print(f'Você escolheu: {produto}')
    print(f'{produto} {valor}')
    
    # Insira o cartão
    input('Insira o cartão e pressione Enter para continuar...')
    
    # Conferindo a senha
    senha = int(input("Digite sua senha: "))
    if senha == senhaCorreta:
        print('Senha confirmada. Espere a entrega do produto.')
    else:
        print('Senha incorreta, por favor tente novamente.')
        menu_principal()

# Chamando a função 'menu_principal'
menu_principal()
