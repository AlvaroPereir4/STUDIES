import numpy as np
import pandas as pd

from pandas import Series, DataFrame

dado_vazio = np.nan
serie=Series(['linha 1', 'linha 2', dado_vazio, 'linha 4', 'linha 5', 'linha 6', dado_vazio, 'linha 8'])

# Esse comando retorna False/True p/ dados vazio ou cheios: print(serie.isnull())

np.random.seed(25)
df = DataFrame(np.random.randn(36).reshape(6,6))
df.loc[3:5, 0] = dado_vazio
df.loc[1:4, 5] = dado_vazio

df_preenchido = df.fillna(0)

dicio = {0: 0.1, 5: 1.25}
df_preenchido = df.fillna(dicio)

print(df_preenchido)


