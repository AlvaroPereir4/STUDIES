import numpy as np
import pandas as pd

from pandas import Series, DataFrame

dados = {
    'coluna 1': [1, 1, 2, 2, 3, 3, 3],
    'coluna 2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
    'coluna 3': ['A', 'A', 'B', 'B', 'C', 'C', 'C']
}

df = DataFrame(dados)

#exibir as linhas que possuem dados duplicados
duplicacao = df.duplicated()

#excluir as linhas que possuem dados duplicados
duplicacaoOff = df.drop_duplicates()



print(df.drop_duplicates(['coluna 3']))
