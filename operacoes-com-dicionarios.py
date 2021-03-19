dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}

print(dados.keys())
print(len(dados))
print(dados.values())
dados['DS5'] = 124549.07
print(dados)
del dados['Passat']
dados.pop("Crossfox")
print(dados)