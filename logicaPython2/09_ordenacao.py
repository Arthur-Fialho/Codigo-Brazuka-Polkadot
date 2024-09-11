def ordenacao():
    num1 = int(input("Digite o 1º número: "))
    num2 = int(input("Digite o 2º número: "))
    num3 = int(input("Digite o 3º número: "))

    if num1 < num2:
        if num2 < num3:
            return [num1, num2, num3]
        elif num1 < num3:
            return [num1, num3, num2]
        else:
            return [num3, num1, num2]
    else:
        if num1 < num3:
            return [num2, num1, num3]
        elif num2 < num3:
            return [num2, num3, num1]
        else:
            return [num3, num2, num1]

print(ordenacao())
