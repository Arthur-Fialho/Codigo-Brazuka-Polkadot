def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

frase_usuario = input("Digite uma frase: ")
quantidade_palavras = contar_palavras(frase_usuario)
print(f"A frase possui {quantidade_palavras} palavra(s).")
