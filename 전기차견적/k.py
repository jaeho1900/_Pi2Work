import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.rand(3, 2))
df1.style.hide()   # 인덱스 숨기기
df1.style.hide([0], axis=1)  # 특정 행 또는 열 숨기기
df1.style.format("{:,.1f}")   # 자릿수 맞추기
df1.style.format("{:,.1f}")   # 자릿수 맞추기
df1.style.format("{:,.1f}").hide()  # 자릿수 맞추기 + 인덱스 감추기

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


# [판다스 팁]
# 1. 데이터프레임의 소수점 자리수 조절하여 표시하기
# pd.set_option('display.precision', 소수점자릿수)
# 2. 인덱스/칼럼 숨기기
# df.style.hide()
# df.style.hide(['E'], axis=1) 