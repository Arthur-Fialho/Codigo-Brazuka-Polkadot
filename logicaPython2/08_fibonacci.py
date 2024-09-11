def fibonacci():
    numero = int(input("Digite o número até o qual você deseja ver a sequência de Fibonacci: "))
    fibonacci_array = [0]
    a, b = 0, 1

    while b <= numero:
        fibonacci_array.append(b)
        a, b = b, a + b

    return fibonacci_array

print(fibonacci())
