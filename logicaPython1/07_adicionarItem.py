def adicionar_item():
    lista_compras = ["café", "leite"]
    item = input("Escreva o item para adicionar à lista de compras: ")
    lista_compras.append(item)
    return lista_compras

print(adicionar_item())
