import sqlalchemy
import pandas as pd

df = pd.read_csv('D:/mart_djy_03.txt', delimiter='|', nrows= 10, header=None)
print (df)

df.to_csv("D:/save10.txt", sep='|', header=False, index=False)

df2 = pd.read_csv('D:/save10.txt', delimiter='|', nrows= 10, header=None)
print (df2)

