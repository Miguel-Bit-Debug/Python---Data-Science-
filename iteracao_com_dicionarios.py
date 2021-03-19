dados = {'Crossfox': 72832.16, 'DS5': 124549.07,  'Fusca': 150000,  'Jetta Variant': 88078.64,  'Passat': 106161.95}

for key in dados.keys():
  print(dados[key])

for key, value in dados.items():
  print(key, value)

for key, value in dados.items():
  if (value > 100000):
    print(key)