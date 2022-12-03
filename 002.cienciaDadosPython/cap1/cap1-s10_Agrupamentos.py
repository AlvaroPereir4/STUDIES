import pandas as pd
caminho = 'C:/Users/alvar/Downloads/arquivos_de_exercicios_python_para_ciencia_dados_basico/dados/mtcars.csv'
carros = pd.read_csv(caminho)
carros.columns = ['nomes','mpg','cyl','disp', 'hpt', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

coluna_agrupamento = carros['cyl']
grupos_carros = carros.groupby(coluna_agrupamento)
grupos_carros.mean()


print(grupos_carros.mean())
