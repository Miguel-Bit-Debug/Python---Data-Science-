import matplotlib.pyplot as plt

notas_matematica = [8, 7, 7, 8, 9, 3, 2, 8]

eixo_x = list(range(1, 9))
eixo_y = notas_matematica

print(plt.plot(eixo_x, eixo_y))