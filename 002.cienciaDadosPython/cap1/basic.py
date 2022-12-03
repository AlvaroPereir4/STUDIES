import numpy as np
import pandas as pd

from pandas import Series, DataFrame


# df geral
np.random.seed(25)
indice = ['linha 1', 'linha 2', 'linha 3', 'linha 4', 'linha 5', 'linha 6']
colunas = ['coluna 1', 'coluna 2', 'coluna 3', 'coluna 4', 'coluna 5', 'coluna 6']
df = DataFrame(np.random.rand(36).reshape((6,6)), index=indice, columns=colunas)

# comparações:
#comparacao = df<.2
#print("Todos os dados menores que 2:\n\n", comparacao)


# filtro com valor escalar
#series_obj = Series(np.arange(6),index=indice)
#filtro = series_obj > 6
#filtragem = series_obj[filtro]
#print("Filtro de dados, maiores que 6:\n\n", filtragem)

# ATUALIZANDO VALORES
df["linha 1", "linha 2", "linha 3"] = 0
print("DF Atualizado:\n\n", df)



