import numpy as np

arrl = np.array([[1,2,3,4],[4,5,6,7],[8,9,10,11]])
arr2 = np.array([4,5,6,7])
result = arrl + arr2
print(result)
def switch(x,y):

       x,y = y,x

       print("x = ", x, ", y = ",y,end = "; ")

x = 5

y = 7

print("x = ", x, ", y = ",y,end = "; ")

switch(x,y)

print("x = ", x, ", y = ",y)
import pandas as pd
import numpy as np
df = pd.DataFrame([[4,7,10],
                    [6,8,2],
                    [1,3,4],
                    [2,10,5]])
df.iloc[1:4]
print(df)