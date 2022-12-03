import numpy as np
import pandas as pd

from pandas import Series, DataFrame

empty_data = np.nan
np.random.seed(25)
df = DataFrame(np.random.randn(36).reshape(6,6))
df.loc[3:5, 0] = empty_data
df.loc[1:4, 5] = empty_data

#quantidade de dados vazios
qtt_empty = df.isnull().sum()

#excluir linhas que possuem dados vazios
df_limpoRow = df.dropna()

#excluir colunas que possuem dados vazios
df_limpoColumn = df.dropna(axis=1)

print(df_limpoColumn)
