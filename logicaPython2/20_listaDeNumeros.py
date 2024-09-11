def main():
    numeros = []

    while True:
        try:
            numero = float(input("Digite um número (ou qualquer letra para encerrar): "))
            numeros.append(numero)
        except ValueError:
            break

    if numeros:
        maior = max(numeros)
        menor = min(numeros)
        media = sum(numeros) / len(numeros)

        print(f"Maior número: {maior}")
        print(f"Menor número: {menor}")
        print(f"Média dos números: {media:.2f}")
    else:
        print("Nenhum número foi inserido.")

main()
