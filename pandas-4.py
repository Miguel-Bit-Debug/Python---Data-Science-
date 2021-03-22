import pandas as pd

dados = [
    [
        {
            'carro':
                [
                    'Fusca',
                    'Ferrari',
                    'Fiesta'
                ]
        }
    ],
    [
        {
            'ano':
                [
                    2013,
                    2021,
                    2015
                ]
        }
    ],
    [
        {
        'quilometragem':
            [
                2400.,
                5000.,
                3000.
            ]
        }
    ]
]


dataset = pd.DataFrame(dados)
print(dataset[0:1][:])