# =====================
# Pandas
# =====================

# --------------------
# 데이터 생성
# --------------------

# >>> 판다스 고유의 데이터 타입

# 1) Series: label로 이뤄진 1차원 배열 구조 --> 행단위 처리
#   - 생성: 직접 리스트, 넘파이배열(numpy.array), 딕셔너리(dict)로 생성
#   - 자동으로 인덱스 축 생성(index, value 확인 가능)
#   - DataFrame의 열을 검색하면 Series 타입으로 리턴

# 2) DataFrame: 2차원 배열 구조 --> 열단위 처리

import numpy as np
import pandas as pd

# >>> Series

# Series 생성
ar = pd.Series([1, 2, 3, -4, 5], index=['a', 'b', 'c', 'd', 'e'])
ar = pd.Series(np.array([1, 2, 3, -4, 5]))
pydic = {"서울": 100, "부산": 200, "광주": 300, "세종": 400}
ar = pd.Series(pydic)

# 추가된 인덱스에 miss match된 값은 NaN(Not a Number) 생성
pydic = {"서울": 100, "부산": 200, "광주": 300}
ar = pd.Series(pydic)

_ix_name = ['서울', '광주', '인천', '세종']
ar1 = pd.Series(pydic, index=_ix_name)
ar1

# 정보 확인
ar.index
ar.values  # 복수형(s)철자 주의!!
ar.dtype
ar.dtypes
type(ar)

# Series 이름 지정
ar.name = "대한민국 광역시"
ar

# 특정 인덱스 변경
ar = ar.rename(index={'부산':'충주'})
ar

# 전체 인덱스 변경
ar.index = ['a', 'b', 'c']
ar

# 자료 추가
ar[10] = 100   # 정수인덱스로는 추가할 수 없다(인덱스범위를 벗어남)
ar['k'] = 100  # 라벨인덱스로 원소 추가

# 자료 삭제
del ar['k']

# Series 연산
ar = pd.Series([1, 2, 3, 4, 5])
ar * 2
ar ** 2

# 비교 연산
ar = pd.Series(['a', 'b', 'c', 'd', 'e']) 
ar[ar > 'b']

# >>> DataFrame

# 파일로부터 생성
filepath = 'dataset/data.csv'
pd.read_csv(filepath, na_values='NA', encoding='utf8') # NA값이 'NA'라는 스트링값으로 저장된 경우

# 파일로 저장
data.to_csv('result.csv', header=True, index=True, encoding='utf8')

# 중첩 리스트로 생성
pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], index=['a', 'b'], columns=['a', 'b', 'c', 'd', 'e'])
pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], ['a', 'b'])  # index 생략가능
pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], index=list('ab'))

# 넘파이 함수로 생성
pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
pd.DataFrame(np.arange(1, 10).reshape(3, 3))

# 딕셔너리로 생성
raw_data = {'food':['melon', 'melon', 'apple', 'apple', 'apple', 'peach'],
            'year':[2018, 2019, 2018, 2019, 2020, 2018],
            'quantity':[490, 512, 478, 325, 290, 800]}
df = pd.DataFrame(raw_data)

# 인덱스로 생성
pd.DataFrame(df, columns=['year', 'food', 'quantity'])
pd.DataFrame(df, index=[0, 1, 3])

# 특정 범위로 생성
x = {'selectFood': df2['food'][:-1]}
pd.DataFrame(x)

# 추가된 인덱스에 miss match된 값은 NaN(Not a Number) 생성
pd.DataFrame(raw_data, columns=['quantity', 'year', 'rank', 'food'])

# NaN 값 대체
df2 = pd.DataFrame(raw_data, columns = ['quantity', 'year', 'food', 'Name'])
df2

df2.fillna(100)   # 원본을 변화시키지는 않음
df2.fillna('kor')

# 조건을 이용한 컬럼 추가 생성
df2['addcol'] = df2.food == 'apple'
df2

# 컬럼 삭제
del df2['addcol']

# 행과 열 바꾸기(Transpose)
df2.T

# 기존 컬럼을 인덱스로 변경: drop은 인덱스로 지정된 컬럼의 삭제 여부, append는 기존 인덱스를 데이터프레임의 컬럼으로 추가 여부
df2.set_index('year', drop = True, append = False, inplace = False)

# 새로운 정수형 인덱스 설정: drop는 기존 인덱스를 삭제할지 컬럼에 추가할지 결정
df2.reset_index(drop = False, inplace = False)

# >>> 데이터프레임의 열 자료형 변경: astype

# 변경하고자 하는 열의 이름을 딕셔너리 키와 값으로 전달
df = df.astype({'A':int32, 'B':float32, 'C':str})        # error 판다스에는 int32자료형이 없음
df = df.astype({'A':np.int32, 'B':np.float32, 'C':str})  # 넘파이 자료형 적용
df = df.astype({'A':int, 'B':float, 'C':str})            # 파이썬 자료형 적용

# 특정 열의 자료형 변경
df['E'] = df['E'].astype('float64')

# >>> 정보 확인
df2.values
type(df2)         # DataFrame
type(df2.values)  # numpy.ndarray(넘파이 다차원배열)
df2.index
df2.columns
df2.ndim
df2.size
df2.shape

# >>> to_frame() : 시리즈를 데이터베이스로 변환하는 함수
ar = pd.Series(['a', 'b', 'c', 'd', 'e']) 
test = ar.to_frame()
test

# >>> 변수의 데이터프레임 여부 확인
isinstance(ar, pd.DataFrame)
isinstance(test, pd.DataFrame)

# >>> View

# 슬라이싱한 데이터프레임은 뷰일 뿐이다
v = pd.DataFrame(np.arange(1,16).reshape(3,5), index=list('abc'), columns=list('ABCDE'))
v1 = v.loc['a':,'D':]
v1

# 뷰의 일부 값을 바꾸면 원본에 반영됨
v1.loc['b','D'] = 900
v1
v
np.may_share_memory(v, v1)

# 열을 전부 바꾸면 해당 열은 원본으로 부터 독립됨
v1['E'] = 400
v1
v
np.may_share_memory(v, v1)

# 뷰의 일부 값을 바꾸면 독립된 열을 제외하곤 계속하여 원본에 영향을 줌
v1.loc['b','D'] = 500
v1.loc['b','E'] = 500
v1
v
np.may_share_memory(v, v1)


# --------------------
# 인덱싱 & 슬라이싱
# --------------------

# Series 색인
pydic = {"서울": 100, "부산": 200, "광주": 300, "세종": 400}
ar = pd.Series(pydic)

ar['서울']
ar['부산':]
ar['부산':'세종']  # 라벨로 슬라이싱(마지막도 포함!!)
ar[-1]
ar[2:]
ar[1:3]

# >>> 헷갈리는 DataFrame 색인(열기준)
df = pd.DataFrame(np.arange(1, 31).reshape(5, 6))

df[4, 4]  # error (넘파이 배열 인덱싱 안됨 !!)
df[0]     # 데이터프레임은 열기준 색인이 기본
df[5]
df[3][4]  # df[열][행] 개념 !!
df[4][4]

df1 = pd.DataFrame(np.arange(1, 31).reshape(5, 6), index=list('abcde'), columns=list('ABCDEF'))

df1[0]  # error
df1.A
df1['A']
df1[['A','E']]  # 다중 열 색인
df1['D']['b']   # df[열][행] 개념 !!

# >>> 판다스 인덱서
raw_data = {'food':['melon', 'melon', 'apple', 'apple', 'apple', 'peach'],
            'year':[2018, 2019, 2018, 2019, 2020, 2018],
            'quantity':[490, 512, 478, 325, 290, 800]}
df1 = pd.DataFrame(raw_data)

# loc: 라벨형
df1.loc[3]
df1.loc[:]
df1.loc[[:]]   # error
df1.loc[1, 5]  # error
df1.loc[[1, 5]]
df1.loc[[1, 5], :]
df1.loc[[1, 5], ['quantity', 'year', 'food']]
df1.loc[2:4, 'food':'quantity']  # 마지막 지정 범위도 반환

# iloc: 정수형
df1.iloc[:, 2]     # Series 반환
df1.iloc[:, [2]]   # DataFrame 반환
df1.iloc[:, 1:]
df1.iloc[:, [1:]]  # error
df1.iloc[:, [0, 2, 1]]
