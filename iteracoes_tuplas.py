import pandas as pd

nomes_carros = tuple(['Jetta Variant', 'Passat', 'Crossfox', 'DS5'])
carro_1, carro_2, carro_3, carro_4 = nomes_carros

# for item in nomes_carros:
#     print(item)
#
# print("---------------------------")
#
# print(carro_1)
# print(carro_2)
# print(carro_3)
# print(carro_4)
#
# print("---------------------------")
#
# _, A, _, B = nomes_carros
# print(A)
# print(B)
#
# print("---------------------------")


carros = ['Jetta Variant', 'Passat', 'Crossfox', 'DS5']
valores = [88078.64, 106161.94, 72832.16, 124549.07]

# print(list(zip(carros, valores)))

for carro, valor in zip(carros, valores):
    print(carro, valor)