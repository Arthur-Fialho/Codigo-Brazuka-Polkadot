def fatorial():
    numero = int(input("Digite um número para saber seu fatorial: "))
    fatorial = 1
    for i in range(numero, 1, -1):
        fatorial *= i
    print(f"O fatorial é {fatorial}")

fatorial()
