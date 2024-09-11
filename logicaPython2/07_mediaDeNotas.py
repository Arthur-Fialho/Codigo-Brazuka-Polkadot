def media_de_notas():
    soma = 0
    quantidade = 0
    
    while True:
        nota = float(input("Digite a nota (ou -1 para encerrar): "))
        if nota == -1:
            break
        soma += nota
        quantidade += 1
    
    media = soma / quantidade
    print(media)

media_de_notas()
