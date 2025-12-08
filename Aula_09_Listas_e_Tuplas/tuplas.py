# Tuplas
# Tuplas são como listas, mas imutáveis. Elas são criadas com parênteses ( ).

cores = ("vermelho", "azul", "verde")
numeros = (1, 2, 3, 4, 5)

print(cores)
print(numeros)

# Acessando elementos
print(cores[0]) # "vermelho"
print(cores[-1]) # verde
print(numeros[2]) # 3
print(numeros[-2]) # 4

# Tentando modificar uma tupla (Erro!)
cores [1] = "amarelo" # ❌Isso gera um erro, pois tuplas são imutáveis!

# Quando usar tuplas?
#  - Quando queremos garantir que os valores não sejam alterados.
#  - Para armazenar dados fixos como coordenadas, meses do ano, dias da semana, etc.

# meses = ("janeiro", "fevereiro", "março", "abril")
# print(meses[2])