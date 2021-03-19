import pandas as pd

nome = 'Passat'
valor = 153000
preco = (nome, valor)

nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
type(nomes_carros)


# ---------------------------- #

# selecao em tuplas

nomes_carros2 = ('Jetta Variant', 'Passat', 'Crossfox', 'DS5', ('Fusca', 'Gol', 'C4'))
# print(nomes_carros[0])
# print(nomes_carros[1])
# print(nomes_carros[2])
# print(nomes_carros[-1])
# print(nomes_carros[0:4:2])
print(nomes_carros2[-1][1])