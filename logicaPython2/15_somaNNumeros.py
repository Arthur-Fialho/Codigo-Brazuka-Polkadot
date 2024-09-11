def soma_numeros(numero):
    resultado = 0
    for i in range(1, numero + 1):
        resultado += i
    return resultado

print(soma_numeros(int(input("Digite o número: "))))
