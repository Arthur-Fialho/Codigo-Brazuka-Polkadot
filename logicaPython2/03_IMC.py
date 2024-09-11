def calcular_imc():
    altura = float(input("Qual é sua altura em metros? "))
    peso = float(input("Qual é seu peso em quilogramas? "))
    imc = peso / (altura ** 2)
    print(f"Seu IMC é {imc:.2f}")

calcular_imc()
