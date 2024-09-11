def contagem_de_vogais():
    palavra = input("Digite uma palavra para saber quantas letras são vogais: ")
    vogais = 'aeiouAEIOU'
    contagem = 0
    
    for char in palavra:
        if char in vogais:
            contagem += 1
    
    print(f"A palavra '{palavra}' tem {contagem} vogais.")

contagem_de_vogais()
