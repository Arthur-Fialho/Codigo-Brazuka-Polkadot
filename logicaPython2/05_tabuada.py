def tabuada():
    x = int(input("Digite um número para ver a tabuada: "))
    for i in range(1, 11):
        print(f"{x} x {i} = {x * i}")

tabuada()
