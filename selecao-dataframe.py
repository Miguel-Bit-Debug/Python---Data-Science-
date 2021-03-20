import pandas as pd

dataset = pd.read_csv('db.csv', sep=';', index_col=0)
# select = dataset.Motor == 'Motor Diesel'

# print(dataset[select])
# print(dataset[(dataset.Motor == 'Motor Diesel') & (dataset.Zero_km == True)])
# print(dataset[(dataset.Motor == 'Motor Diesel') | (dataset.Zero_km == True)])
# print(dataset.query('Motor == "Motor Diesel" and Zero_km == True'))
# print(dataset.query('Motor == "Motor Diesel" or Zero_km == True'))
# print(select)

# data = dataset.iterrows()

for index, row in dataset.iterrows():
    dataset.fillna(0)
    if(2021 - row['Ano'] != 0):
        dataset.loc[index, 'Km_media'] = row['Quilometragem'] / (2021 - row['Ano'])
    else:
        dataset.loc[index, 'Km_media'] = 0
    print(dataset)