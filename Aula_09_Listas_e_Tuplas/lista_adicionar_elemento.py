# adicionado elementos à lista

# append(): adiciona um item ao final
# insert(): adiciona um item em uma posição específica

numeros = [1, 2, 3]
print(numeros)

numeros.append(4)
print(numeros) # [1, 2, 3, 4] após o append adiciona o 4 a lista.


numeros.insert(1, 10) # (posição, valor)
print(numeros) # [1, 10, 2, 3, 4] (insere o nuemro 10 na posição 1 da lista numeros)