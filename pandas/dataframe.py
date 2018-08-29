import numpy as np
import pandas as pd
print("*"*50)
#printing 2D array
print("INPUT-> np.array([[1,2,3,4],[5,6,7,8]]) ")
my_2dArr = np.array([[1,2,3,4],[5,6,7,8]])
print(pd.DataFrame(my_2dArr))

print("*"*50)

#take Dictonary and print it.
my_dictionary = {"cowboys":['Dak','Zek','Martin'], "redskins":['alex','ap','tyron']}
print(pd.DataFrame(my_dictionary))

print("*"*50)

print("INPUT-> DataFrame(data=[1,2,3,4,5], index=range(0,5), columns=['A'])")
my_df = pd.DataFrame(data=[1,2,3,4,5], index=range(0,5), columns=['A'])
print(pd.DataFrame(my_df))

print("*"*50)

df = pd.DataFrame(my_2dArr)
print(df.shape)
