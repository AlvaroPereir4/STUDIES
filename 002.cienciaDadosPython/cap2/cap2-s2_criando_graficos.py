import pandas as pd

from matplotlib import pyplot as plt # criação de graficos
from matplotlib import rcParams # definir o tamanho das imagens
import seaborn as sns # padrão de dados

%matplotlib inline
rcParams['figure.figsize'] = 10, 8
sns.set_style('whitegrid')
x = range(1, 10)
y = [1, 2, 3, 4, 0, 4, 3, 2, 1]


plt.plot(x, y)

caminho = 'C:/Users/alvar/Downloads/arquivos_de_exercicios_python_para_ciencia_dados_basico/dados/mtcars.csv'

carros = pd.read_csv(caminho)
carros.columns = ['nomes', 'mpg', 'cyl', 'disp', 'hp', 'drat', 'wt', 'qsec', 'vs', 'am', 'gear', 'carb']

df = carros[['cyl', 'wt', 'mpg']]


a = df.plot()
print(a)