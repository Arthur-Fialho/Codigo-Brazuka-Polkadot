def soma_pares():
    soma = 0
    for i in range(1, 101):
        if i % 2 == 0:
            soma += i
    print(f'A soma de todos os números pares é: {soma}')

soma_pares()
