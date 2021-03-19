import pandas as pd
pd.set_option('display.max_rows', 10)
pd.set_option('display.max_columns', 1000)
dataset = pd.read_csv('db.csv', sep=';')
estatistica = dataset[['Quilometragem', 'Valor']].describe()
info = dataset.info()


print(info)
# print(estatistica)
# print(dataset.dtypes)
# print(dataset)