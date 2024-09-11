def celsius_para_fahrenheit_e_kelvin(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    kelvin = celsius + 273.15
    print(f"A temperatura em fahrenheit é {fahrenheit} e em kelvin é {kelvin}")

temperatura_celsius = float(input("Digite a temperatura em celsius: "))
celsius_para_fahrenheit_e_kelvin(temperatura_celsius)
