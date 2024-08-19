import pandas as pd
df1 = pd.DataFrame({'A': [1, 2, 3],
                    'B': [4, 5, 6],
                    'C': [7, 8, 9]}, index=[0,1,10])

df2 = pd.DataFrame({'A': [4, 5, 6],
                    'D': [10, 11, 12],
                    'E': [13, 14, 15]}, index=[0,2,10])

# join='outer'으로 설정하여 모든 열을 유지
pd.concat([df1, df2], axis=0, join='outer')

# join='outer'으로 설정하여 모든 행을 유지
pd.concat([df1, df2], axis=1, join='outer')

# join='inner'으로 설정하면 공통된 행만 유지
pd.concat([df1, df2], axis=1, join='inner')
