def contar_letras():
    frase = input("Digite uma frase: ")
    contador = 0
    
    for letra in frase:
        if letra == 'a' or letra == 'A':
            contador += 1
    
    return contador

print(contar_letras())
