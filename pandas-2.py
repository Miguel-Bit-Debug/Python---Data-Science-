import pandas as pd

pd.set_option('max_rows', 10)
pd.set_option('max_columns', 10)

dataset = pd.read_csv('db.csv', sep=';', index_col=0)

# print(dataset[['Valor']])
# print(dataset[0:3])
# print(dataset.loc['Passat'])
# print(dataset.loc[['Passat', 'DS5'], ['Motor', 'Valor']])
# print(dataset.loc[:, ['Motor', 'Valor']])
# print(dataset.iloc[[1]])
# print(dataset.iloc[1:4])
# print(dataset.iloc[1:4, [0, 5, 2]])
print(dataset.iloc[[1, 42, 22], [0, 5, 2]])
# print(dataset.head())