import pandas as pd
import numpy as np


data={
    'Name':['ABC','XYZ','PQR'],
    'Age':[28,22,34]
}

df=pd.DataFrame(data)
print(df)
# res=df.sort_values(by='Age')
res=df.sort_values(by='Age',ascending=False)
print(res)