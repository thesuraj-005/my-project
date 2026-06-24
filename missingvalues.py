import pandas as pd
import numpy as np

data ={
    'col1':[2,np.nan,np.nan,4],
    'col2':[1,pd.NA,pd.NA,2]

}

df=pd.DataFrame(data)
#f=df.fillna('-') #replace missing vaalues by'-'
#f=df.ffill() #fill the forward line
f =df.ffill()# fill the backward line
print(f)