# Convertendo entre lista e tupla
# Podemos converter uma tupla para uma lista e modificar os elementos.

tupla = (1, 2, 3)
print(tupla) # (1, 2, 3)
lista = list(tupla) # Converte para lista
lista.append(4)
tupla = tuple(lista) # Converte de volta para tupla
print(tupla) # (1, 2, 3, 4)

