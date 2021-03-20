import pandas as pd


dataset = pd.read_csv('db.csv', sep=';', index_col=0)


print(dataset[dataset.Quilometragem.isna()])
dataset.fillna(0, inplace=True)
print(dataset.query('Zero_km == True'))
# print(dataset)