import numpy as np

dados = np.array([[4410., 37123., 0., 25757.],
                 [2003., 1991., 2019, 2006. ]])


print(dados[:, :] / (2021 - dados[:, :]))

data = [x for x in dados for y in x if y ]

print(0)
print("-----------------------")

print(dados.dtype)
print(dados[:, :][:])