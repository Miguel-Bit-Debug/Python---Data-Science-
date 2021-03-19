dados = {'Jetta Variant': 88078.64, 'Passat': 106161.94, 'Crossfox': 72832.16}

print(dados.keys())
print(len(dados))
print(dados.values())
dados['DS5'] = 124549.07
print(dados)
del dados['Passat']
print(dados)

dados.update({'Passat': 106161.94})
dados.update({'Passat': 106161.95})
print(dados)
dados.update(({'Fusca': 106161.94}))
print(dados)

dadosCopy = dados.copy()
print(f'dados copy{dadosCopy}')
del dadosCopy['Fusca']
print(f'dados copy{dadosCopy}')
print(f'dados {dados}')


dadosCopy.pop("Passat")
print(f'dados copy{dadosCopy}')

dadosCopy.clear()
print(dadosCopy)