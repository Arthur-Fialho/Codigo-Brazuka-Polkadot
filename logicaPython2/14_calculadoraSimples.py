def calculadora_simples():
    try:
        numero1 = float(input("Digite o primeiro número: "))
        operador = input("Digite o operador (+, -, *, /): ")
        numero2 = float(input("Digite o segundo número: "))

        if operador == '+':
            print(f"Resultado: {numero1 + numero2}")
        elif operador == '-':
            print(f"Resultado: {numero1 - numero2}")
        elif operador == '*':
            print(f"Resultado: {numero1 * numero2}")
        elif operador == '/':
            if numero2 != 0:
                print(f"Resultado: {numero1 / numero2}")
            else:
                print("Erro - não é possível dividir por zero")
        else:
            print("Erro - operador inválido")
    except ValueError:
        print("Erro - insira números válidos.")

calculadora_simples()
