import pandas as pd
import numpy as np
from numpy.random import randn as rn
np.random.seed(0)
matrix_data=rn(5,5)
row_label=['a','b','c','d','e']
col_label=['f','g','h','i','j']
df=pd.DataFrame(matrix_data,row_label,col_label)
print(df)
print(df[['f','g']])
print(type(df[['f','g']]))
df.drop('j',axis=1,inplace=True)
print(df)

print(df.loc['a'])#for single row usind index names
print(df.iloc[0])#for single row using index values
print(df.iloc[[0,1]])#double rows


np.random.seed(0)
matrix_data=rn(5,5)
row_label=['a','b','c','d','e']
col_label=['v','w','x','y','z']
df=pd.DataFrame(matrix_data,row_label,col_label)
print(df)
print(df.loc['a','v'])   #row value with column position(0,0)
print(df.loc[['a','b'],['v','w']])    #[rows],[column]comprising
