class Conta:
    
    def__init__(self, numeroConta, usuario, cpf, saldo = 0): # type: ignore
    self.saldo = saldo
    self.numeroConta = numeroConta
    self.titular = usuario
    self.cpf = cpf
    
    
    def saque(delf, valor):
        if valor <= 0:
            print('Valor incompatível com a ação')
        elif self.saldo >= valor:
             self.saldo = self.saldo - valor
             
             print('Saque realixado com sucesso')
        else:
            print('saldo insuficiente')
            
    #def deposito(conta, valor):
    
    
    conta1 = Conta('1234', 'Fulana', '987654321-00', 100)
    
    print(conta1.titular, conta1.saldo)
    
    conta1.saque(30)
    
    print(conta1.titular, conta1.saldo)