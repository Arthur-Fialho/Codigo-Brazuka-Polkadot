def numero_perfeito(numero):
    soma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i
    return soma_divisores == numero

numero_dado = int(input("Digite um número: "))
if numero_perfeito(numero_dado):
    print(f"{numero_dado} é um número perfeito.")
else:
    print(f"{numero_dado} não é um número perfeito.")
