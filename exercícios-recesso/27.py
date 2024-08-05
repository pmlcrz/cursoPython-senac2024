while True:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if 0 <= nota <= 10:
        print("Nota válida")
        break
    else:
        print("Nota inválida, tente novamente.")
