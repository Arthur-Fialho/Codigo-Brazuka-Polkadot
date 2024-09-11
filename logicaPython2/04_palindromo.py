def palindromo():
    palavra = input("Digite uma palavra para saber se é um palíndromo: ")
    if palavra == palavra[::-1]:
        print(f"A palavra {palavra} é um palíndromo.")
    else:
        print(f"A palavra {palavra} não é um palíndromo.")

palindromo()
