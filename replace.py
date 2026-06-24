import pandas as pd

data={
    'one':["A","B","C","D"],
    'two':[5,60,2000,45]
}

df=pd.DataFrame(data)
print(df)
gd=df.groupby('one')['two'].sum()
print(gd)