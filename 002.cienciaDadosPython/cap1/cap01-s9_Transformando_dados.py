import numpy as np
import pandas as pd

from pandas import Series, DataFrame

df = pd.DataFrame(np.arange(36).reshape(6,6))


df.drop([0, 2],axis=1)

serie = Series(np.arange(6))
serie.name = "variavel_somada"

variavel_somada = DataFrame.join(df, serie)

df_ordenado = variavel_somada.sort_values(by=['variavel_somada'], ascending=[False])

print(df_ordenado)
