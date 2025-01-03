import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.rand(3, 2))
print(df1)

for m,n in df1.iterrows():
   print(n[0], n[1], end='\n')

for m,n in df1.items():
   print(m, n[0], n[1], n[2], end='\n')


# 행과 내용의 반복자 반환: DataFrame.iterrows()
# iterrows 메서드는 데이터의 행-열/데이터 정보를 튜플 형태의 generator 객체로 반환하는 메서드입니다.
# (행 이름, 내용의 Series객체) 형태로 반환하는데, Series객체는 열, 값 형태로 반환됩니다.

# 열과 내용의 반복자 반환: DataFrame.items()
# items 메서드는 데이터의 열-행/데이터 정보를 튜플 형태의 generator 객체로 반환하는 메서드입니다.
# (열 이름, 내용의 Series객체) 형태로 반환하는데, Series객체는 행, 값 형태로 반환됩니다.
