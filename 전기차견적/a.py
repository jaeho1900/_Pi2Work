import streamlit as st

import pandas as pd

# 예제 DataFrame 생성
data = {'이름': ['홍길동', '김철수', '이영희'],
        '나이': [30, 25, 35],
        '성별': ['남', '남', '여']}
df = pd.DataFrame(data)

# iterrows() 함수를 사용하여 각 행 반복하기
for index, row in df.iterrows():
    print(index)
    # print(row['이름'])#, row['나이'], row['성별'])
    print(row['나이'])
    print('------')
