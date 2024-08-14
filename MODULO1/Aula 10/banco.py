class Conta:
    
    def __init__(self, numeroConta, usuario, cpf, saldo = 0):
        self.saldo = saldo
        self.numeroConta = numeroConta
        self.titular = usuario
        self.cpf = cpf
    
    
    def saque(self, valor):
        if valor <= 0:
            print('Valor incompatível com a ação')
        elif self.saldo >= valor:
            self.saldo = self.saldo - valor
            print('Saque realixado com sucesso')
        else:
            print('saldo insuficiente')
            
    def deposito(self, conta, valor):
        if valor <= 0:
            print('insira valor valido para deposito')        
        else: 
            conta.saldo = conta.saldo + valor
            print('Deposito feito com sucesso')
        
        
    def transferencia(self, destino, valor):
        self.saque(valor)
        self.deposito(destino, valor)
        print('transferencia feita com sucesso')
        
        
conta1 = Conta('1234', 'Fulana', '987654321-00', 100)
conta2 = Conta('1234', 'Fulana', '987654321-00', 30)
conta1.transferencia(conta2, 30)
print('Saldo após transferencia da conta 1:', conta1.saldo)
print('Saldo após transferencia da conta 2:', conta2.saldo)
        
        

print(conta2.titular, conta2.saldo)
conta1.deposito(conta2, 0)
print(conta2.titular, conta2.saldo)

#conta.saque(30)

#print(conta1.titular, conta1.saldo)
