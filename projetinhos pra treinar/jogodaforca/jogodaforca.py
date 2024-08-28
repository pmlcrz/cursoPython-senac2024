import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'desenvolvimento', 'computador']
    return random.choice(palavras)

def exibir_palavra(palavra, letras_adivinhadas):
    return ''.join([letra if letra in letras_adivinhadas else '_' for letra in palavra])

def jogo_da_forca():
    palavra = escolher_palavra()
    letras_adivinhadas = set()
    tentativas_restantes = 6

    while tentativas_restantes > 0:
        print(f"Palavra: {exibir_palavra(palavra, letras_adivinhadas)}")
        print(f"Tentativas restantes: {tentativas_restantes}")
        letra = input("Adivinhe uma letra: ").lower()

        if letra in palavra:
            letras_adivinhadas.add(letra)
            print("Correto!")
        else:
            tentativas_restantes -= 1
            print("Incorreto!")

        if set(palavra) == letras_adivinhadas:
            print(f"Parabéns! Você ganhou! A palavra era '{palavra}'.")
            break
    else:
        print(f"Você perdeu! A palavra era '{palavra}'.")

if __name__ == "__main__":
    jogo_da_forca()
