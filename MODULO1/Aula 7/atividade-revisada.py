nome = "Marcio"
cpf = "145.678.910-11"
endereco = "Rua vasco da gama"
taxa = False

print(f"Olá, {nome}!")

if endereco == "RJ":
    print(f"Eu, {nome}, portador do cpf {cpf}, residente no endereco {endereco}, declaro que as minhas informações são verdadeiras.")
else:
    if taxa:
        print(f"Eu, {nome}, portador do cpf {cpf}, residente no endereco {endereco}, declaro que as minhas informações são verdadeiras.")
    else:
        print("Por favor, pague a taxa")
