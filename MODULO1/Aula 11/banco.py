#saque, depósito, extrato, transferência.
#conta: Saldo, numero da conta, nome do ususario, cpf

class Conta:

    def __init__(self,  numeroConta, titular, cpf, saldo = 0):
        self.saldo = saldo
        self.numeroConta = numeroConta
        self.titular = titular
        self.cpf = cpf
        self.extrato= []

    def saque(self, valor):
        if valor <= 0:
            print('Valor informado incompativel com a acao') 
        elif self.saldo >= valor:
            self.saldo = self.saldo - valor
            self.extrato.append('Saque de R$ ' + str(valor) +
                                ' realizado com sucesso.\n'+
                                'Saldo atual: R$ ' + str(self.saldo)+'\n')
        else:
            print('Saldo insuficiente')


    def deposito(self, conta, valor):
        if(valor<=0):
            print('Insira um valor valido para realizar um deposito')
        else:
            conta.saldo = conta.saldo + valor
            self.extrato.append('Deposito de R$ '+str(valor)+
                                ' realizado com sucesso.\n'+
                                'saldo atual R$ '+str(self.saldo)+'\n')
            

    def transferencia(self, destino, valor):
        self.extrato.append('Iniciando transferência do valor R$ '
                            +str(valor)+ ' para a conta '+
                            destino.numeroConta +'.\n')
        self.saque(valor)
        destino.saldo = destino.saldo+valor
        self.extrato.append('Saldo atual R$ '
                            +str(self.saldo)+ 
                            ', transferencia realizado com sucesso')

    def imprimirExtrato(self):
        for item in self.extrato:
            print(item)

conta1 = Conta('11111','Renan', '05794884703', 100)
conta2 = Conta('22222', 'Denise', '5651511611', 30)
conta1.saque(30)
conta1.deposito(conta1,40)
conta1.transferencia(conta2,20)
conta1.imprimirExtrato()

# conta1.transferencia(conta2,100)
# print('Saldo depois da transferencia de conta 1: ', conta1.saldo)
# print('Saldo depois da transferencia de conta 1: ', conta2.saldo)

