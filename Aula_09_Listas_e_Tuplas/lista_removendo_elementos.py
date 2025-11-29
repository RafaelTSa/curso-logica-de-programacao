# Removendo elementos da lista

# Remove(): remove um item da lista
# pop(): remove um item pelo índice (ou o último item se nenhum "for" passado)

frutas = ["maça", "banana", "laranja", "uva"]
frutas.remove("banana")
print(frutas) # ["maça", "laranja"]

frutas.pop(0)
print(frutas) # ["laranja"] apenas "laranja" aparece ja que o .remove retirou o "banana" antes.