# =====================
# 배열
# =====================

# --------------------
# 넘파이 자료형
# --------------------
# i  integer(int8 은 -128~127)
# u  unsigned integer(-부호가 없는 0을 포함한 양수만, uint8 은 0~255, -1은 255를 -2는 254로 대체)
# f  single precision float
# d  double precision float
# b  bool
# D  complex(실수와 허수로 구성된 복소수)
# S  string
# U  unicode

import numpy as np

# >>> 자료형 특징 -----

# 모든 요소를 동일한 타입으로 처리 !!
arr = np.array([1, 2, 3, 'a', 'b', 'c'])
type(arr[0])   # numpy.str_

# 넘치면 0부터 다시 순환, -는 뒤부터 순환
np.array([1, 2, 3, 255, 256, -2, -1], dtype=np.uint8)  # uint8(0~255)

# >>> 자료형 지정 -----

# 옵션에서 지정
np.array([1, 2, 3, 4, 5], dtype=np.int64)
np.arange(10, dtype=np.uint8)
np.arange(10, dtype='uint8')
np.arange(10, dtype='u1')   # u 뒤의 숫자는 바이트(8비트) 의미: 1x8
np.arange(10, dtype='<u1')  # <리틀엔디언은 디폴트값

# 직접 지정
np.int_([1, 2, 4])     # int32
np.float_([1, 2, 4])   # float64
np.float32([1, 2, 4])  # float32

# >>> 자료형 변환 -----

np.int_([1, 2, 4]).astype(int)
np.int_([1, 2, 4]).astype(np.float64)

# >>> 자료형 확인 -----

np.array([1, 2, 3.5, 4, 5]).dtype


# --------------------
# 배열 생성
# --------------------

import numpy as np

# >>> 배열 생성 -----

np.zeros((3, 4))               # 모든 요소를 0으로
np.ones((3, 4))                # 모든 요소를 1로
np.eye(4)                      # 단위행렬: 대각선은 1, 나머지는 0
np.empty([3, 3], dtype=float)  # 빈배열: 초기화가 안되어 속도가 빠른 배열
np.empty_like(A, dtype=int)    # A배열과 동일한 형상의 초기화가 안된 배열 생성

np.array([1, 2, 3, 4, 5])                                # 1차원
np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])  # 2차원
np.array([[[0, 1, 2], [4, 5, 6], [8, 9, 10]], [[2, 3, 4], [6, 7, 8], [10, 11, 12]]])  
np.arange(24).reshape(2, 3, 4)                           # 3차원 (깊이, 행, 열)

# np.arange(): 원소 생성 (파이썬의 range와 유사)
np.arange(10)
np.arange(1, 20, 2)
np.arange(1, 10, 0.5)  # 간격 0.5이면 9.5 까지 출력!!

# np.reshape(): 배열 형상 생성
arr = np.arange(12).reshape(3, 4)
print(arr)

# reshape(정수, -1): 행 기준(원솟수를 모르거나 가변적일 때 형상 중심으로 변경)
arr.reshape(-1)     # (12), (12,), (1, -1), (1, 12) 와 동일 결과
arr.reshape(1, -1)  # (1, ?)
arr.reshape(2, -1)  # (2, ?)
arr.reshape(4, -1)  # (4, ?)

# reshape(-1, 정수): 열 기준
arr.reshape(-1, 1)  # (?, 1)
arr.reshape(-1, 2)  # (?, 2)

# >>> 샘플링 데이터 생성 -----

# numpy.random.choice(a, size=None, replace=True, p=None)
# a: 배열 데이터 또는 정수이면 np.arange(정수) 명령으로 해석하여 데이터 생성
# size: 샘플 숫자(정수)
# replace: True이면 한번 선택한 데이터를 다시 선택 가능
# p: 배열, 각 데이터가 선택될 수 있는 확률

np.random.choice(10, 3, replace=False)
np.random.choice(3, 10, replace=True)

# np.random.rand(행, 열):           0부터 1사이의 균일 분포
# np.random.randn(행, 열):          표준 정규 분포
# np.random.randint(size=(행, 열)): 균일 분포의 정수 난수

np.random.rand(5)
np.random.rand(3, 5)
np.random.randn(5)
np.random.randn(3, 5)
np.random.randint(10, size=10)           # 0  ~ 10 사이 10개의 1차원 배열
np.random.randint(10, 20, size=10)       # 10 ~ 20 사이 10개의 1차원 배열
np.random.randint(10, 20, size=(3, 5))   # 10 ~ 20 사이 3x5의 2차원 배열

# >>> View vs Copy -----

# View: 넘파이 인덱싱|슬라이싱으로 생성(참조)된 복사본은 '원본에 영향'을 주므로 주의 !!
arr1 = np.arange(1, 31).reshape(5, 6)
arr2 = arr1[-1][2:-1]            # arr2 는 view
arr2[-1] = 10000                 # arr2 를 변경
print(arr1)                      # arr1 값도 변경 !!

# Copy: 원본과 분리된 복사본 생성
arr3 = np.arange(10)
arr4 = arr3[:5].copy()
arr4[-1] = 10000
print(arr3)

# 메모리 공유 여부 확인
np.may_share_memory(arr1, arr2)
np.may_share_memory(arr3, arr4)

# >>> 배열 정보 -----

arr.shape  # 배열 형상, (3, 4) 큰방 3개에 각 방마다 4개씩 들어있다
len(arr)   # 길이(큰방의 갯수)
arr.size   # 원소 갯수
arr.ndim   # 차원 확인


# --------------------
# 배열의 행, 열 추가
# --------------------

import numpy as np

# >>> np.append(): 모든 배열 원소를 풀어서 1차원 배열로 추가 -----

arr = np.array([1, 2])
arr = np.append(arr, [3, 4])
print(arr)         # [1 2 3 4]

# 파이썬의 append(): 2차원 배열로 추가
x = []
x.append([1, 2])
x.append([3, 4])
print(x)           # [[1, 2], [3, 4]]

# >>> np.append(axis=0): 배열 형상을 유지하며 마지막 행에 추가 -----

arr1 = np.ones((3, 5), int)
arr1 = np.append(arr1, np.array([[3, 4, 5, 6, 7]]), axis=0)
print(arr1)

# >>> np.append(axis=1): 배열 형상을 유지하며 마지막 열에 추가 -----

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.append(arr2, np.zeros((2, 1)), axis=1) 
print(arr2)


# --------------------
# 인덱싱 & 슬라이싱
# --------------------

import numpy as np
arr = np.arange(1, 31).reshape(5, 6)
print(arr)

# >>> 파이썬의 순차 인덱싱 [선][후] -----

arr[2]
arr[-3:]        # [-3:] 은 -3부터 시작해서 순방향으로 진행 !!(역방향 X)
arr[1][1:]
arr[:4][2:100]

# >>> 넘파이의 핀셑 인덱싱 [행, 열] -----

arr[1, 1:]
arr[2,]         # 1차원 반환
arr[2:3]        # 2차원 반환
arr[:, 1:-1]
arr[:, 3:]
arr[:4, 2:100]  # 다중 슬라이싱(행렬개념)

# >>> 넘파이 슬라이싱 [스타트행:라스트행:스텝] -----

arr[::3]
arr[:3:3]
arr[1::2]
arr[-1::]
arr[-1::-1]     # (-)스텝은 역방향 진행!!
arr[-1:-10:-2]

# >>> 팬시 인덱싱: '[정수]' 리스트를 인덱싱에 활용, 연속범위(:)는 사용 못함!! -----

# 팬시 인덱싱은 메모리 공유를 하지 않으모로 뷰가 아님
arr[[0]]              # array([[1, 2, 3, 4, 5, 6]])
arr[[0, -1]]          # array([[1, 2, 3, 4, 5, 6], [25, 26, 27, 28, 29, 30]])

# 동일 위치의 원소 추출 [(0,1), (2,4), (-1,3)] !!
arr[[0, 2, -1], [1, 4, 3]]          # array([2, 17, 28])

 # 행열의 곱(3x3)으로 원소 추출 [[0,[1,4,3]],[2,[1,4,3]],[-1,[1,4,3]]] !!
arr[np.ix_([0, 2, -1], [1, 4, 3])]  # array([[2, 4], [26, 28]])


# --------------------
# 행렬 계산
# --------------------

import numpy as np

# >>> 행렬의 곱셈 -----

arr1 = np.eye(2)
arr2 = np.array([[3, 4], [5, 6]])

np.dot(arr1, arr2)

# 일반 곱셈: 같은 위치의 요소끼리만 수식 적용
arr1 * arr2

# >>> Broadcasting -----

# 스칼라값은 상대 배열 형상으로 자동 확장
arr3 = np.array([1, 2, 3, 4, 5])
arr3 + 3

# 상대 배열 형상에 맞춰 각각 행과 열을 확장
arr4 = np.arange(3)
arr5 = np.arange(5).reshape(5, 1)
arr4 + arr5

# 열 갯수가 같으면 행으로 자동 확장
arr6 = np.eye(4)
arr7 = np.arange(4)
arr6 + arr7

# >>> 비교연산(==, !=, >, <, >=, <=) -----

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [1, 5, 2]])
c = np.array([7, 8, 9])
d = np.array([7, 8])
e = np.array([1, 2, 3, 4])

a == b
a == c  # c는 브로드케스팅
b == c
b != c
b >= c


# =====================
# 시리즈와 데이터프레임
# =====================

# 1) Series:    label + 1차원 배열 형상 --> 행단위 처리
# 2) DataFrame: label + 2차원 배열 형상 --> 열단위 처리


# --------------------
# 데이터 생성
# --------------------

import numpy as np
import pandas as pd

# >>> 데이터프레임 생성 -----

pd.Series(['a', 'b', 'c', 'd', 'e']).to_frame()
pd.DataFrame([[1, 2, 3, 4], [6, 7, 8, 9]], index=list('ab'), columns=['a', 'b', 'c', 'd'])
pd.DataFrame(np.arange(1, 10).reshape(3, 3))
df = pd.DataFrame({'food':['melon', 'melon', 'apple', 'apple'],
                   'year':[2018, 2019, 2018, 2019],
                   'quantity':[490, 512, 478, 325]})
pd.DataFrame(df, index=[0, 1], columns=['food', 'man', 'quantity'])  # miss match된 라벨의 원솟값은 NaN(Not a Number) 으로 채워짐

# >>> 자료형 변경 -----

# 변경하고자 하는 열명과 자료형을 딕셔너리의 키와 값으로 전달
df = df.astype({'food':str, 'year':int, 'quantity':float})            # 파이썬 자료형 적용
df = df.astype({'food':str, 'year':np.float32, 'quantity':np.int32})  # 넘파이 자료형 적용
df['quantity'] = df['quantity'].astype('float64')

# >>> label 지정 -----

# 라벨명 설정
df.index = ['a', 'b', 'c', 'd']
df.columns = ['food', 'year', 'quantity']
df.rename(index={'a': 'no_1', 'b': 'no_2'}, inplace=False)
df.rename(columns={'food': 'Fruit'}, inplace=False)

# 특정 열을 인덱스로 설정: drop은 지정된 열의 삭제 여부, append는 기존 인덱스의 삭제 여부
df.set_index('year', drop = True, append = False, inplace = False)

# 정수 인덱스로 초기화: drop는 기존 인덱스의 열 이동 여부
df.reset_index(drop=True, inplace=False)

# >>> label 정렬 -----

# 인덱스 기준
df.sort_index(ascending=False)           # 내림차순(False)

# 컬럼 기준
df.sort_values(by=['year', 'food'],      # 기준열
               ascending=True,           # 오름차순(True)
               na_position='first',      # 결측값 위치 'first'
               # ignore_index=True,      # 기존 인덱스 무시
               # inplace=True,           # 자체 저장
               )

# >>> 정보 확인 -----

df          # DataFrame
df.values   # numpy.ndarray(넘파이 다차원배열)
df.index
df.columns
df.size
df.shape
df.ndim
type(df.values)


# --------------------
# 데이터 조작
# --------------------

import numpy as np
import pandas as pd
df = pd.DataFrame({'food':['melon', 'melon', 'apple', 'apple'],
                   'year':[2018, 2019, 2018, 2019],
                   'quantity':[490, 512, 478, 325]},
                   index = list('abcd'))
print(df)

# >>> 열 추가

df['man'] = 10

# >>> 행 열 삭제 -----

df.drop(['a', 'b'], inplace=False)       # 행(axis=0), default
df.drop('man', axis=1, inplace=False)    # 열(axis=1)
del df['man']                            # 열 삭제, 즉시 적용 



## >>> 하단부분 복습 필요 지점



# >>> 중복값 확인, 삭제 -----

# 확인
df.duplicated()
df['city'].duplicated()

# 삭제
df.drop_duplicates()
df.drop_duplicates(subset=['city'], keep='last')

# >>> 결측값 확인, 삭제, 대체 -----

# 확인
df.info()
df.isnull().sum()

# dropna()
df.dropna(axis=0)                          # 결측값이 존재하는 모든 행 삭제
df.dropna(axis=1)                          # 결측값이 존재하는 모든 열 삭제
df.dropna(subset=['city', 'pop'], axis=0)  # 지정된 열에 결측값이 존재하는 행만 삭제
df.dropna(thresh=6, axis=1)                # thresh 옵션은 정상값이 지정 갯수 미만인 열 삭제

# fillna(): 원본을 변화시키지는 않음
mean_age = df.area.mean(axis=0)
df.area.fillna(mean_age)                                  # 평균값 대체
most_freq = df['pop'].value_counts(dropna=True).idxmax()  # value_counts(): S의 unique value로 그룹핑해서 count하는 함수(groupby()에선 그룹 중복으로 피함)
df['pop'].fillna(most_freq)                               # 최빈값 대체
df['pop'].fillna(method='ffill', inplace=False)           # 이웃값 대체('ffill', 'bfill')
df.fillna({'pop': most_freq, 'area': mean_age})           # 열별 대체

# 보간 대체(linear 선형보간, time 시간보간: 시간형 인덱스이어야 함)
df.interpolate(method='linear')

# S.where(), DF.where(): 조건이 true면 원래값 유지, false면 명시된 값 또는 NaN으로 대체
df.where(pd.notnull(df), df.mean(), axis='columns')
ndf['확인일시'].where(pd.notnull(ndf['확인일시']), ndf['delay'] + ndf['발생일시'])
ndf['건물'].where(ndf['대분류'] == '건물군', ndf['건물'].str.split('_').str[2])

# np.where(조건문, true 일때 값, false 일때 값)
np.where(pd.notnull(df['area']), df['call'], df['city'])

# >>> 데이터셋 합치기, 나누기 -----

# 병합
# 키: 열명(on, left_on, right_on), 인덱스(left_index, right_index), 방식: inner, outer, left, right
pd.merge(df, df2)                        # 공통 열 모두를 기준으로 교집합
pd.merge(df, df2, left_index=True, right_on='major')
pd.merge(df, df2, left_on=['year', 'city'], right_on=['date', 'city'], how='inner')

# 연결
pd.concat([df, df2])                     # 열기준(axis=0), 합집합(join='outer')
pd.concat([df, df2], ignore_index=True)  # 새로운 정수형 인덱스 설정, 기존 행 인덱스는 삭제
pd.concat([df, df2], axis=1)

# str.extract: 정규표현식으로 선택한 문자를 독립된 열로 분할
df.city.str.extract(r'(.*)_(.*)')

# str.split(slice)
df['city'].str.split('_').str[0]
df['city'].str.split('_').str[1]
df['city'].str.slice(2, 3)

# np.where(조건문, true 일때 값, false 일때 값)
np.where(df['area'] >= 50e3, "Big", "Small")

# >>> 행과 열 바꾸기(Transpose) -----

df2.T

# >>> View -----

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

ar[-1]
ar[2:]
ar[1:3]
ar['서울']
ar['부산':]
ar['부산':'세종']  # 라벨로 슬라이싱(마지막도 포함!!)

ar = pd.Series(['a', 'b', 'c', 'd', 'e'])
ar[ar > 'b']  # 비교 연산 활용

# >>> 헷갈리는 DataFrame 색인(열기준)
df = pd.DataFrame(np.arange(1, 31).reshape(5, 6))

df[4, 4]  # error (넘파이 배열 인덱싱 안됨 !!)
df[0]     # 데이터프레임은 [열]기준 색인이 기본
df[5]
df[3][4]  # df[열][행] 개념 !!
df[4][4]

df1 = pd.DataFrame(np.arange(1, 31).reshape(5, 6), index=list('abcde'), columns=list('ABCDEF'))

df1[0]  # error (라벨이 존재하면 라벨로 색인)
df1.A
df1['A']
df1[['A','E']]  # 팬시색인
df1['D']['b']   # df[열][행] 개념 !!

# >>> 불린 응용
df[df['area'].isnull()]
df[df['area'].notnull()]
df[(30e3 < df.area) & (df.area < 80e3)]
# isin(): 리스트 조건 만족 여부를 반환
df[df['year'].isin(['2011', '2013'])]
# str.contains(): 정규표현식으로 조건 만족 여부를 반환
df['city'].str.contains('S|j', na=False, regex=True)  # 결측값은 'False'로 반환
df[~df.city.str.contains('(S|j)', na=False)]          # 불포함(결측값이 있는 경우 'na=False')

# >>> 판다스 인덱서
raw_data = {'food':['melon', 'melon', 'apple', 'apple', 'apple', 'peach'],
            'year':[2018, 2019, 2018, 2019, 2020, 2018],
            'quantity':[490, 512, 478, 325, 290, 800]}
df1 = pd.DataFrame(raw_data)

# loc: 라벨형
df1.loc[3]     # Series 반환
df1.loc[[3]]   # DataFrame 반환
df1.loc[:]
df1.loc[[:]]   # error (팬시색인은 연속범위는 사용 못함)
df1.loc[1, 5]  # error
df1.loc[[1, 5]]
df1.loc[[1, 5], :]
df1.loc[[1, 5], ['quantity', 'year', 'food']]
df1.loc[2:4, 'food':'quantity']  # 마지막 지정 범위도 반환

# iloc: 정수형
df1.iloc[:, 2]     # Series 반환
df1.iloc[:, [2]]   # DataFrame 반환
df1.iloc[:, 1:]
df1.iloc[:, [1:]]  # error (팬시색인은 연속범위는 사용 못함)
df1.iloc[:, [0, 2, 1]]

# >>> 멀티 인덱스
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare', 'class', 'who', 'embark_town', 'alive']]

df.columns = pd.MultiIndex.from_arrays([['num','num','object','object','object','object'], list(df.columns)], names=("col1", "col2"))
mdf = df.set_index([('object','class'), ('object','who')], drop = True)
print(mdf)

# 멀티 레벨명 변경
mdf.rename_axis(['분류1', '분류2'], axis=1)
mdf.rename_axis(['선실', '남녀'], axis=0)

# 정렬
mdf.sort_index(level=0, axis=1, ascending=False)
mdf.sort_index(level=1, axis=1)

# 레벨수준 변경
mdf.reorder_levels(['col2', 'col1'], axis=1)
mdf.reorder_levels([1, 0], axis=0)

# 색인
print(mdf.loc['First'])

# >>> xs 인덱서

# 행: axis=0
mdf.xs('First')
mdf.xs('man', level=1, drop_level=False)
mdf.xs(('First', 'man'))
mdf.xs(('man', slice(None)), level=[1, 0])

# 열: axis=1
mdf.xs('object', axis=1)
mdf.xs('fare', level=1, axis=1)
mdf.xs(('num', 'age'), axis=1)
mdf.xs(('age', 'num'), level=[1, 0], axis=1)

# >>> 피벗테이블

# 행인덱스와 열인덱스의 조건을 만족하는 데이터가 2개 이상인 경우는 에러가 발생
# 피벗테이블은 열인덱스의 피라미드 밑에서부터 columns->values->aggfunc 순으로 쌓임
df.columns = [j for i,j in df.columns]
pd.pivot_table(df,                       # 피벗할 데이터프레임
               index=['class', 'who'],   # 행위치에 들어갈 열
               columns='alive',          # 열 위체에 들어갈 열
               values=['age', 'fare'],   # 데이터로 사용할 열
               aggfunc=['max', 'mean'],  # 데이터 집계함수
               # aggfunc={'age': 'max', 'fare': 'mean'},
               fill_value=0,            # NaN 채우기
               margins=True,            # 행별,열별 합계
               margins_name='계')


# --------------------
# 전처리
# --------------------

# >>> 데이터 형식 변경
df['area'].replace(np.nan, 0).astype('int64')                      # 형 변환
df['pop'].str.replace(',', '').replace(np.nan, 0).astype('int64')  # 천단위 콤마 삭제
df['area'].apply(lambda x: format(x, ','))                         # 천단위 콤마 추가
df['area'].apply(lambda x: '{:.2f}'.format(x))                     # 소수점 자리수 변경

# >>> 정규화(Normalization): 변수별 범위차이로 인한 상대적 크기 차이 해소, 데이터를 [0~1|-1~1]으로 변경

# 통계정보
# include 옵션: 문자형 데이터의 원소수, 카테고리값갯수, 최빈값, 최빈값사용빈도수 추가
df.describe(include='all')

# 상대적 크기 차이 해소: 열데이터에서 열최솟값을 뺀 값을 분자로 하고, 열최댓값-열최솟값을 분모로 산출(0~1)
min_x = df['area'] - df['area'].min()
min_max = df['area'].max() - df['area'].min()
df['area_normalization'] = min_x / min_max
df['area_normalization'].describe()

# >>> 카테고리화

# 확인
df['year'].unique()   # 카테고리값 구성원 배열
df['year'].nunique()  # 카테고리값 갯수
df['year'].value_counts()                       # 카테고리값별 자료수(NaN 생략)
df['year'].value_counts(dropna=False).idxmax()  # 카테고리값별 자료수(NaN 포함)
df['area'].value_counts(bins=[0, 50000, 100000], sort=False)  # 구간별 자료수

# pd.cut(): 수치형 열(변수)을 동일한 길이(경계값 기준 등)으로 분할
# np.histogram(): 도수(각 구간에 있는 원소수)와 도수분포구간을 구함
count, bin_divcityers = np.histogram(df['home'], bins=3)
bin_labels = ['소형', '중형', '대형']
df['home_bin'] = pd.cut(x=df['home'],         # 데이터 배열
                        bins=bin_divcityers,  # 경계 값 리스트
                        labels=bin_labels,    # bin 라벨
                        include_lowest=True)  # 최하 경계값 포함
df['home_bin'].value_counts()
import seaborn as sns
sns.displot(df, x='home', hue='home_bin', element='step')
df.groupby('home_bin')['home'].mean()

# pd.qcut(): 수치형 열(변수)을 동일한 갯수로 분할
df['home_cnt'] = pd.qcut(df['home'], 3, labels=['Q1', 'Q2', 'Q3'])  # 3개 구간
df['home_cnt'].value_counts()
sns.displot(df, x='home', hue='home_cnt', element='step')
df.groupby('home_cnt')['home'].mean()

# 더미 열 생성: 분할 라벨별 열 생성(속하면1, 속하지 않으면0)
pd.get_dummies(df['home_cnt'])


# --------------------
# 배열 함수
# --------------------

# >>> S.map -> value -> S
df['city'].map(lambda x: print(x, '\n-- 작업 --\n'))
df['city'].map({'A_Busan': 'Pusan', 'B_Kwangju': 'Gwangju', np.nan: 'None'})
df['pop'].map('city people is {}'.format, na_action=None)
df['pop'].map('city people is {}'.format, na_action='ignore')

# >>> S.apply -> value -> S
df['city'].apply(lambda x: print(x, '\n-- 작업 --\n'))
df['area'].apply(lambda x: 'Giant' if x >= 8e4 else 'Big' if x >= 5e4 else 'Small')

# >>> DF.applymap -> value -> DF
df.applymap(lambda x: print(x, '\n-- 작업 --\n'))

# >>> DF.apply -> column, row -> S, DF
df.apply(lambda x: print(x, '\n-- 작업 --\n'))

# >>> DF.pipe -> DataFrame -> scalar, S, DF
df.pipe(lambda x: print(x, '\n-- 작업 --\n'))
df.pipe(lambda x: x.dropna(axis=0)).pipe(lambda x: x.sum())


# --------------------
# groupby() 집계
# --------------------
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.DataFrame(data=np.arange(20).reshape(4, 5),
                  columns=['c1', 'c2', 'c3', 'c4', 'c5'],
                  index=['r1', 'r2', 'r3', 'r4'])

# >>> 딕셔너리로 그룹핑 기준 생성

# 행 라벨기준 그룹 합산
mapping_dict_row = {'r1': 'row_g1',
                    'r2': 'row_g1',
                    'r3': 'row_g2',
                    'r4': 'row_g2'}

df.groupby(mapping_dict_row).sum()  # 그룹핑 후 집계함수 적용
df.groupby(mapping_dict_row).sum().reset_index(drop=True)  # 그룹라벨 삭제

# 열 라벨기준 그룹 합산
mapping_dict_col = {'c1': 'col_g1',
                    'c2': 'col_g1',
                    'c3': 'col_g2',
                    'c4': 'col_g2',
                    'c5': 'col_g2'}

df.groupby(mapping_dict_col, axis=1).sum()
mdf.groupby(level='col1', axis=1).sum()  # 멀티인덱스 적용

# >>> 사용자함수로 그룹핑 기준 생성

def row_grp_func(x):
    if x == 'r1' or x == 'r2':
        row_group = 'row_g1'
    else:
        row_group = 'row_g2'
    return row_group

df.groupby(row_grp_func).sum()


# --------------------
# 기술통계량 집계
# --------------------
titanic = sns.load_dataset('titanic')
gdf = titanic.loc[:, ['survived', 'age', 'fare', 'class', 'who', 'embark_town']]
grouped = gdf.groupby(['who', 'class'])

# >>> key 기준으로 특정 그룹 데이터만 추출
grouped.get_group(('man', 'First'))

# >>> 기술통계량(연속형 변수) 함수
# [nan 포함]   size
# [nan 미포함] count, sum, min, max, mean, median, std, var, first, last 등

grouped['age'].mean()                         # Series
pd.DataFrame(grouped['age'].mean())           # DataFrame
grouped[['age','fare']].mean().reset_index()  # DataFrame(계층라벨모두 채움)
grouped[['age','fare']].mean().reset_index(drop=True)
grouped[['age','fare']].mean().reset_index().sort_values('fare', ascending=False)

# >>> 사용자정의 함수

def func(x):
    d = {}
    d['fare_mean'] = x['fare'].mean()
    d['fare_std'] = x['fare'].std()
    d['age_max'] = x['age'].max()
    d['age_min'] = x['age'].min()
    return pd.Series(d)

# apply(): 그룹핑된 개별 원소에 일대일 함수 매핑(그룹별 한 줄의 결과값으로 정리됨)
grouped.apply(func)

grouped.apply(lambda x: x.describe())
grouped.apply(lambda x: len(x) >= 200)

mdf.groupby(level=1, axis=1).apply('sum')

# 평균값 대체
grouped['age'].apply(lambda g: g.fillna(g.mean()))
# 최빈값 대체
grouped['embark_town'].apply(lambda g: g.fillna(g.value_counts().idxmax()))

# agg(): 숫자 타입의 Series(행/열)의 빠른 집계를 목적으로 하는 apply()의 특수 형태
grouped['age'].agg(['min', 'max'])
# 동일 열에 다수의 함수 매핑
grouped['age'].agg(['min', 'max'])
# 다수 열에 다수의 함수 매핑
grouped[['age', 'fare']].agg(['min', 'max'])
# 열별로 다른 함수 매핑
grouped.agg({'fare': ['min', 'max'], 'age': 'mean'})

# >>> transform(): 원래 인덱스와 원소를 유지하며 그룹별 연산결과만 채움
# apply()와 달리 매서드안에서는 열명을 사용할 수 없고, 연산 불가능한 열은 자동 필터링됨
grouped['age'].transform(np.mean)
ndf.groupby('경보명')['delay'].transform(lambda g: g.mean(numeric_only=False))  # 시간 등 숫자 이외의 평균값 적용 옵션

# >>> filter(): 조건을 충족하지 못하는 소그룹을 삭제
grouped.filter(lambda x: len(x) >= 200)

# >>> 그룹별 반복 작업하기
for key, group in grouped:
    print('* key : ', key)
    print(group.head())


# --------------------
# 시계열
# --------------------

# >>> 시계열 객체 변환

# 문자열을 Timestamp 로 변환
# %Y(2020), %y(20), %m(01~12), %d(01~31)
# %H(01~23), %I(01~12), %M(01~59), %S(00~61)
# %w(0일~6토), %U(일요일기준누적주), %W(월요일기준누적주)
# %B(Jauary), %b(Jan), %A(Sunday), %a(Sun)
tsp = pd.to_datetime(['180101', '180104', '191210'], format='%y%m%d')

# Timestamp 를 Period 로 변환
# D, B, W, W-MON, M, MS, Q, QS, A, AS, H, T, S
tsp.to_period(freq='A')
tsp.to_period(freq='M')
tsp.to_period(freq='D')

# >>> 시계열 배열 생성

# Timestamp 배열
pd.date_range(start='2019-01-01',   # 날짜 범위의 시작
              end=None,             # 날짜 범위의 끝
              periods=4,            # 생성할 Timestamp의 개수
              freq='3MS',           # 시간 간격 (MS: 월의 시작일)
              tz='Asia/Seoul')      # 시간대(timezone)

# Period 배열
pd.period_range(start='2019-01-01',  # 날짜 범위의 시작
                end=None,            # 날짜 범위의 끝
                periods=3,           # 생성할 Period 개수
                freq='H')            # 기간의 길이 (H: 시간)

# resample(): 등간격 시간 조정
# 업-샘플링은 시간 간격이 좁아지면서 빈 데이터 원소에 Nan 이 추가되므로 채워야 함(ffill, bfill)
# 다운-샘플링은 시간 간격이 넓어지므로 기간의 대표값을 구해야 함
tdf = pd.DataFrame(np.random.randn(100), columns=['value'],
                   index=pd.date_range('2018-1-1', periods=100, freq='D'))
tdf['value'].tail(20)
tdf['value'].resample('10H').ffill()
tdf['value'].resample('M').first()
# ohlc(): 기간의 시고저종(open, high, low, close)을 구함
tdf['value'].resample('W').ohlc()

# >>> 시계열 집계

# resample(): 등간격 기간별 데이터 집계
tdf['value'].resample('6M').sum()
tdf['value'].resample('6M').sum().cumsum()
tdf['value'].resample('6M').max()
tdf['value'].resample('6M').min()
tdf['value'].resample('6M').mean()
tdf['value'].resample('6M').median()
tdf['value'].resample('6M').first()
tdf['value'].resample('6M').last()
tdf['value'].resample('6M').var().fillna(0)
np.sqrt(tdf['value'].resample('6M').var())  # 표준편차

# 선형적 기간 집계
tdf['value'].resample('M').count()

# 순환적 기간 집계 (시간, 요일 등 반복개념)
tdf.index.day_name().value_counts()
tdf.index.day.value_counts().sort_index()

# >>> dt 활용

# 날짜 데이터 분리
pd.DataFrame(tdf.index)[0].dt.date              # YYYY-MM-DD(문자)
pd.DataFrame(tdf.index)[0].dt.year              # 연(4자리숫자)
pd.DataFrame(tdf.index)[0].dt.month             # 월(숫자)
pd.DataFrame(tdf.index)[0].dt.month_name()      # 월(문자)
pd.DataFrame(tdf.index)[0].dt.day               # 일(숫자)
pd.DataFrame(tdf.index)[0].dt.time              # HH:MM:SS(문자)
pd.DataFrame(tdf.index)[0].dt.hour              # 시(숫자)
pd.DataFrame(tdf.index)[0].dt.minute            # 분(숫자)
pd.DataFrame(tdf.index)[0].dt.second            # 초(숫자)
pd.DataFrame(tdf.index)[0].dt.quarter           # 분기(숫자)
pd.DataFrame(tdf.index)[0].dt.day_name()        # 요일이름(문자)
pd.DataFrame(tdf.index)[0].dt.weekday           # 요일숫자(0-월, 1-화) (=dayofweek)
pd.DataFrame(tdf.index)[0].dt.weekofyear        # 연 기준 몇주째(숫자) (=week)
pd.DataFrame(tdf.index)[0].dt.dayofyear         # 연 기준 몇일째(숫자)
pd.DataFrame(tdf.index)[0].dt.days_in_month     # 월 일수(숫자) (=daysinmonth)
pd.DataFrame(tdf.index)[0].dt.is_leap_year      # 윤년 여부

# Period 객체로 만들어서 '년, 년-월' 분리
pd.DataFrame(tdf.index)[0].dt.to_period(freq='A')
pd.DataFrame(tdf.index)[0].dt.to_period(freq='M')

# 문자열 변환
pd.DataFrame(tdf.index)[0].dt.strftime("%Y년 %m월 %d일")

# >>> 시계열 인덱싱
tdf['2018']
tdf['2018-03-28':'2018-04-05']
tdf.loc['2018-03':]

# >>> 시간대 설정
ts_seoul = pd.DataFrame(tdf.index)[0][0].tz_localize('Asia/Seoul')
ts_UTC = ts_seoul.tz_convert('UTC')


# --------------------
# 파일 입출력
# --------------------

# >>> csv

# 읽기
df_csv = pd.read_csv("./stats.csv",
                     # index_col=0,          # 행 인덱스가 되는 열 지정(None..)
                     # header=0,             # 열명으로 사용할 행 지정(None..)
                     # usecols=[0,3,6,8],    # 불러올 columns
                     # nrows=6,              # 불러올 rows
                     # skiprows=[1,3],       # 처음 몇 줄을 skip할지 설정
                     # skipfooter=5,         # 마지막 몇 줄을 skip할지 설정
                     # na_values='NA',       # NA값이 'NA'라는 스트링값으로 저장된 경우
                     # encoding='CP949',     # 한글인코딩: 조합형유니코드UTF8, 완성형웹EUC-KR, 완성형윈도우CP949
                     # sep=",",              # txt파일은 "\t"
                     )

# 쓰기
df.to_csv("./sample.csv",
          # columns = ['날짜', '국적', '계'],  # 저장할 열 지정
          # index = False,                     # 행 인덱스 삭제
          # header = False,                    # 열명 삭제
          # encoding = 'utf-8',
          )

# >>> excel

# 읽기
df_xl = pd.read_excel('./stats.xlsx',
                      # sheet_major='prod',
                      # index_col="A",       # 행 인덱스가 되는 열 지정(숫자, 열명, None..)
                      # usecols='B:D, H, j',
                      )

# 쓰기
pd.DataFrame(df_csv, index=range(1, len(df_csv) + 1), columns=['column_name']) \
    .to_excel('./sample.xlsx ')

df.to_excel("./sample.xlsx")

# 복수의 excel sheet에 저장
with pd.ExcelWriter('./sample_multi_sheet.xlsx') as writer:
    df.to_excel(writer, sheet_major='1sheet')
    df2.to_excel(writer, sheet_major='2sheet')

# 기존 excel 파일에 저장
import openpyxl
book = openpyxl.load_workbook('./present.xlsx')
writer = pd.ExcelWriter('./present.xlsx', engine='openpyxl')
writer.book = book
df.to_excel(writer, sheet_major='1sheet')
df2.to_excel(writer, sheet_major='2sheet')
writer.save()
writer.close()

# excel: protected files
import win32com.client
import pandas as pd
import os
xl = win32com.client.Dispatch("Excel.Application")
# xl.Visible = False
filename = './excel_pass.xlsx'
PW = '1'
wb = xl.Workbooks.Open(os.path.abspath(filename), Password=PW)
ws = wb.Sheets(1)
content = ws.Range('A1:G313').Value
# content = xlws.Range(xlws.Cells(1,1), xlws.Cells(313,7)).Value
df = pd.DataFrame(list(content))
xl.Quit()


# --------------------
# IPython 환경 설정
# --------------------

# 옵션 확인: pd.get_option('~~')
# 옵션 설정: pd.set_option('~~')
# 옵션 초기화: pd.reset_option('~~')
pd.set_option('display.max_rows', None)                  # 행 개수
pd.set_option('display.max_columns', 10)                 # 열 개수
pd.set_option('display.max_colwidth', 20)                # 열 너비
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드로 조정한 열 너비
