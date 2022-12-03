import numpy as np
import pandas as pd

from pandas import Series, DataFrame

df = pd.DataFrame(np.arange(36).reshape(6,6))

df2 = pd.DataFrame(np.arange(15).reshape(5,3))

df0102 = pd.concat([df, df2], axis=1)

print(df0102)
