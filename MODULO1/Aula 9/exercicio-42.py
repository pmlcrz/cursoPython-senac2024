# O usuário digitará dez números.
# O programa deverá calcular quantos eles são maiores que dez.


controle = 0
for i in range(0,2):
    entrada = input('Digite um numero:')
    numero = int(entrada)
    # Pega o input e antes de guardar transforma em int | entrada = int(input('Digite um numero:'))
    
    if numero > 10:
        controle+=1
        
        print('Existem', controle, 'numero(s) maiores que 10')
        
        
        