import pandas as pd

# df=pd.DataFrame({
#     'Col1':range(12),
#     'Col2':['A']*3+['B']*3+['C']*3+['D']*3,
#     'Date':pd.to_datetime(["2026-05-21","2026-05-22","2026-05-23"]*4)
# })
# print(df)

# pivoted=df.pivot(index="Date",columns="Col2",values="Col1")
# print(pivoted)

data = {
    'course':['cs','civil','cs','civil','cs'],
    'year':[1,2,1,1,2],
    'Student':[100,150,120,90,100]} 

df = pd.DataFrame(data)
df['Marks'] = df['Student'][:3]
print(df)

#Missing values

import numpy as np


