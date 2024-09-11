import random

def jogo_adivinha():
    numero_sorteado = random.randint(1, 100)
    chute = None
    while chute != numero_sorteado:
        chute = int(input("Digite um número entre 1 e 100: "))
        if chute < numero_sorteado:
            print("O número que você digitou é menor que o número sorteado.")
        elif chute > numero_sorteado:
            print("O número que você digitou é maior que o número sorteado.")
        else:
            print("Parabéns! Você acertou.")
    print(f"O número sorteado era {numero_sorteado}!")

jogo_adivinha()
