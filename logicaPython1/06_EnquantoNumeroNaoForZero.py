def enquanto_numero_nao_for_zero():
    soma = 0
    numero = int(input("Digite um número: "))

    while numero != 0:
        soma += numero
        numero = int(input("Digite um número: "))

    print(f"A soma dos números digitados é: {soma}")

enquanto_numero_nao_for_zero()
