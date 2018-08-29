import numpy as np
import pandas as pd

#printing 2D array
my_2dArr = np.array([[1,2,3,4],[5,6,7,8]])
print(pd.DataFrame(my_2dArr))


#take Dictonary and print it.
my_dictionary = {"cowboys":['Dak','Zek','Martin'], "redskins":['alex','ap','tyron']}
print(pd.DataFrame(my_dictionary))



df = pd.DataFrame(my_2dArr)
print(df.shape)
