import streamlit as st

import pandas as pd
import numpy as np

np.arange(12).reshape(3, 4)
aa = [['one', 'two'], [1, 2, 3], ['방가'],[],[],[]]
bb = [500, 1000, 600]

k = 10
df_01 = pd.DataFrame(index=range(k), columns=['구분', '약정개월/층위치', '주차면 수', '단가', '금액', '비고'])

df_01.iloc[5,2] = "80,000"
df_01.iloc[5,1] = ""
df_01.loc[len(df_01)]=  [['one', 'two'], [1, 2, 3], ['방가'],[],[],[]]

df_01.drop([5])

print(df_01)

