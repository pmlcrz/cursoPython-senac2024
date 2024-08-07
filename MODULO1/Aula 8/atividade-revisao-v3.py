*************************************** PYTHON VERSION ***************************************************

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
senhaCorreta = 1234

def pagamento():
    # Insira o cartão
    print('Insira o cartão')
    # Conferindo a senha
    senha = input("Digite sua senha: ")
    if (senha == str(senhaCorreta)):
        print('Senha confirmada. Espere a entrega do produto.')
    else:
        print('Senha incorreta, por favor tente novamente')
        menuprincipal()

# INÍCIO DA FUNÇÃO MENU PRINCIPAL
def menuprincipal():
    opcao = input('Menu: 1. Café (R$ 2,00) | 2. Capuccino (R$ 3,50) | 3. Café com Leite (R$ 3,00) | 4. Chocolate (R$ 4,00) | 5. Sair | Digite o número do produto: ')

    if (opcao == '1'):
    #opção 1. Café
        print('Você escolheu: ' + produtos[0])
        print(produtos[0] + ' R$ 2,00')
        pagamento()
    
    elif(opcao == '2'):
        #opção 2. Capuccino
        print('Você escolheu: ' + produtos[1])
        print(produtos[1] + ' R$ 3,50')
        pagamento()

    elif(opcao == '3'):
        #opção 3. Café com Leite
        print('Você escolheu: ' + produtos[2])
        print(produtos[2] + ' R$ 3,00')
        pagamento()
    elif(opcao == '4'):
        #opção 4. Chocolate
        print('Você escolheu: ' + produtos[3])
        print(produtos[3] + ' R$ 4,00')
        pagamento()
    elif(opcao == '5'):
        print("Obrigado pela preferência")
        exit()
    else:
        print('Você digitou uma opção inválida. Por favor, tente novamente.')
        menuprincipal()
    # AQUI É O FIM DA FUNÇÃO

menuprincipal()
