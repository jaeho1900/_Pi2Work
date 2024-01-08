# =====================
# Dictionary : 순서와 index 는 무의미, []는 키값을 나타낼 뿐
# =====================

aa = {1: 'one', 2: [1, 2, 3], '인사': '방가'}
bb = {'korea': 'seoul', 'japan': 'tokyo'}

# >>> access -----

list(aa.keys())
list(aa.values())

aa['인사']               # 키값이없으면 KeyError, 프로세스 중단
aa.get('인사')           # 키값이없으면 무반응, 다음 프로세스 진행
aa.get('gender', 'man')  # 키값이없을때 지정값 반환

# >>> update: 이어 붙이기 -----

aa[1] = 'bye'
aa[6] = 'six'
aa.update(bb)

# >>> delete -----

del aa['인사']
aa.clear()

# >>> 딕셔너리의 생성 -----

name = ['merona', 'gugucon', 'bibibig']
price = [500, 1000, 600]
{"메로나": 500, "구구콘": 1000}          # 일반 방법
dict(메로나=500, 구구콘=1000)            # 키가 문자열일 때 dict클래스에 담는 방법
dict(zip(name, price))                   # dict() + zip() 메소드
{k: v * 2 for k, v in zip(name, price)}  # 딕셔너리 컴프리헨션 방법: 연산 및 조건 식 가능
{k: v for k, v in zip(name, price) if v < 1000}


# =====================
# 배열
# =====================

# --------------------
# 넘파이 자료형
# --------------------
# i  integer          (int8 은 -128~127)
# u  unsigned integer (uint8 은 0~255, -부호없이 0과 양수만, -1은 255를 -2는 254로 대체)
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

# np.arange(): 원소값 생성 (파이썬의 range와 유사)
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

# numpy.random.choice(a, size=None, replace=True)
# a        배열 또는 정수이면 np.arange(정수) 명령으로 해석하여 데이터 생성
# size     샘플 숫자(정수)
# replace  True이면 한번 선택한 데이터를 다시 선택 가능

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

# 교차 위치의 원소값 반환
arr[[0, 2, -1], [1, 4, 3]]          # [(0,1), (2,4), (-1,3)] !!

 # 행렬 곱셈(3x3)으로 원소값 반환
arr[np.ix_([0, 2, -1], [1, 4, 3])]  # [[0,[1,4,3]],[2,[1,4,3]],[-1,[1,4,3]]] !!


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

# 스칼라값은 상대 배열 형상으로 확장
arr3 = np.array([1, 2, 3, 4, 5])
arr3 + 3

# 상대 배열 형상에 맞춰 행과 열을 확장
arr4 = np.arange(3)
arr5 = np.arange(5).reshape(5, 1)
arr4 + arr5

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
df.reset_index(drop=False, inplace=False)

# >>> label 정렬 -----

# 인덱스 기준
df.sort_index(ascending=False)           # 내림차순(False)

# 컬럼 기준
df.sort_values(by=['year', 'food'],      # 기준열
               ascending=[True, False],  # 오름차순(True)
               na_position='first',      # 결측값 위치 'first'
               # ignore_index=True,      # 기존 인덱스 무시
               # inplace=True,           # 자체 저장
               )

# >>> 정보 확인 -----

df          # DataFrame
df.values   # numpy.ndarray(넘파이 다차원배열)
df.size     # 원솟수
df.shape    # 형상
df.ndim     # 차원
df.index    # 인덱스명
df.columns  # 컬럼명
df.dtypes   # 자료형
df.info()
df.describe(include='all')  # 통계정보(include 옵션은 문자형 자료의 원솟수, 카테고리값갯수, 최빈값, 최빈값사용빈도수 추가)


# --------------------
# 멀티 라벨
# --------------------

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare', 'class', 'who', 'embark_town', 'alive']]

# >>> 멀티 라벨 -----

# 멀티 라벨 설정
df.columns = pd.MultiIndex.from_arrays([['num','num','object','object','object','object'], list(df.columns)], names=("col1", "col2"))
mdf = df.set_index([('object','class'), ('object','who')], drop = True)
print(mdf)

# 멀티 라벨명 변경
mdf.rename_axis(['분류1', '분류2'], axis=1)
mdf.rename_axis(['선실등급', '성별'], axis=0)

# 멀티 레벨 정렬
mdf.sort_index(level=0, axis=1, ascending=False)
mdf.sort_index(level=1, axis=1)

# 멀티 레벨 수준 변경
mdf.reorder_levels(['col2', 'col1'], axis=1)
mdf.reorder_levels([1, 0], axis=0)

# >>> xs 인덱서 -----

# 행: axis=0
mdf.xs('First')
mdf.xs('man', level=1, drop_level=False)
mdf.xs(('man', slice(None)), level=[1, 0])
mdf.xs(('First', 'man'))

# 열: axis=1
mdf.xs('object', axis=1)
mdf.xs('fare', level=1, axis=1)
mdf.xs(('num', 'age'), axis=1)
mdf.xs(('age', 'num'), level=[1, 0], axis=1)

# >>> 멀티 라벨 groupby() 집계 -----

mdf.groupby(level='col1', axis=1).sum()
mdf.groupby(level=1, axis=1).apply('sum')

# >>> 피벗테이블 -----

# 행인덱스와 열인덱스의 조건을 만족하는 데이터가 2개 이상인 경우는 에러가 발생
# 피벗테이블은 열인덱스의 피라미드 밑에서부터 columns->values->aggfunc 순으로 쌓임
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
# 인덱싱 & 슬라이싱
# --------------------

import pandas as pd
dict = {'food':['melon', 'melon', 'apple', 'apple', np.nan, 'peach'],
            'year':[2018, 2019, 2018, 2019, 2020, 2018],
            'total':[np.nan, 512, 478, 325, 290, 800]}
df = pd.DataFrame(dict)

# >>> 헷갈리는 DataFrame 색인(열기준) -----

df.food                # 데이터프레임은 [열]기준 !!
df[['food', 'total']]  # 팬시색인
df['total'][3]         # df[열][행] 개념 !!
df['total', '3']       # error, 넘파이 인덱싱 안됨 !!
df[0]                  # error, 컬럼라벨이 존재하면 정수인덱싱 불가 !!

# >>> 판다스 인덱서 -----

# loc[행,열]: 라벨형
df.loc[3]         # Series 반환
df.loc[1:3]       # 마지막 라벨범위 포함 !!
df.loc[1, 'total']
df.loc[2:4, 'food':'total']

df.loc[[3]]       # DataFrame 반환
df.loc[[1, 5]]
df.loc[[1, 5], :]
df.loc[[1, 5], ['total', 'year']]

# iloc[행,열]: 정수형
df.iloc[:, 2]     # Series 반환
df.iloc[:, :1]    # 마지막 정수범위 미포함 !!
df.iloc[:, [2]]   # DataFrame 반환
df.iloc[:, [0, 2, 1]]

# >>> 불린 응용 -----

df[df['food'].isnull()]
df[df['food'].notnull()]
df[(400 < df.total) & (df.total < 700)]
df[df['food'].isin(['melon', 'peach'])]  # isin(): 리스트 조건 만족 여부를 반환

# >>> View -----

df = pd.DataFrame(np.arange(1,16).reshape(3,5), index=list('abc'), columns=list('ABCDE'))

view = df.loc['a':,'D':]         # 슬라이싱한 데이터프레임은 뷰일 뿐이다
print(df, view, sep='\n\n')

view.loc['b','D'] = 900          # 뷰의 일부 값을 바꾸면 원본도 바뀜 !!
print(df, view, sep='\n\n')

view['E'] = 400                  # 뷰의 열을 전부 바꾸면 "해당 열"은 원본으로 부터 독립됨
print(df, view, sep='\n\n')

view.loc['c','D'] = 500         # 뷰의 일부 값을 바꾸면 독립된 열을 제외하곤 계속하여 원본에 영향을 줌
view.loc['c','E'] = 500
print(df, view, sep='\n\n')


# --------------------
# 데이터프레임 그룹 다루기
# --------------------

# >>> groupby() 집계 -----

import pandas as pd
import numpy as np
import seaborn as sns

df = pd.DataFrame(data=np.arange(20).reshape(4, 5),
                  columns=['c1', 'c2', 'c3', 'c4', 'c5'],
                  index=['r1', 'r2', 'r3', 'r4'])

# 행 기준 그룹 집계
mapping_dict_row = {'r1': 'row_g1',
                    'r2': 'row_g1',
                    'r3': 'row_g2',
                    'r4': 'row_g2'}

df.groupby(mapping_dict_row).sum()

# 열 기준 그룹 집계
mapping_dict_col = {'c1': 'col_g1',
                    'c2': 'col_g1',
                    'c3': 'col_g2',
                    'c4': 'col_g2',
                    'c5': 'col_g2'}

df.groupby(mapping_dict_col, axis=1).sum()

# 사용자함수로 그룹 집계
def row_grp_func(x):
    if x == 'r1' or x == 'r2':
        row_group = 'row_g1'
    else:
        row_group = 'row_g2'
    return row_group

df.groupby(row_grp_func).sum()

# >>> key 기준의 그룹 데이터 추출 -----

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['survived', 'age', 'fare', 'class', 'who', 'embark_town']]
gdf = df.groupby(['who', 'class'])

gdf.get_group(('man', 'First'))

# >>> 기술통계량(연속형 변수) 함수 -----

# [nan 포함]   size
# [nan 미포함] count, sum, min, max, mean, median, std, var, first, last 등

gdf['age'].mean()                         # Series
pd.DataFrame(gdf['age'].mean())           # DataFrame
gdf[['age']].mean().reset_index()         # 인덱스를 열로 이동(계층 라벨이 모두 채워짐)
gdf[['age','fare']].mean().reset_index().sort_values('fare', ascending=False)

# >>> apply(): 그룹핑된 개별 원소에 일대일 함수 매핑(그룹별 한 줄의 결과값으로 정리됨) -----

def func(x):
    d = {}
    d['fare_mean'] = x['fare'].mean()
    d['fare_std'] = x['fare'].std()
    d['age_max'] = x['age'].max()
    d['age_min'] = x['age'].min()
    return pd.Series(d)

gdf.apply(func)
gdf.apply(lambda x: x.describe())
gdf.apply(lambda x: len(x) >= 200)
gdf['age'].apply(lambda x: x.fillna(x.mean()))                           # 평균값 대체
gdf['embark_town'].apply(lambda x: x.fillna(x.value_counts().idxmax()))  # 최빈값 대체

# >>> agg(): 숫자 타입의 Series(행/열)의 빠른 집계를 목적으로 하는 apply()의 특수 형태 -----

gdf['age'].agg(['min', 'max'])                    # 동일 열에 다수의 함수 매핑
gdf[['age', 'fare']].agg(['min', 'max'])          # 다수 열에 다수의 함수 매핑
gdf.agg({'fare': ['min', 'max'], 'age': 'mean'})  # 열별로 다른 함수 매핑

# >>> transform(): 원래 인덱스를 유지하며 개별 원소에 그룹연산결과를 채움 -----

gdf['age'].transform(np.mean)

# >>> filter(): 조건을 충족하는 데이터만 추출 -----

gdf.filter(lambda x: len(x) >= 200)

# >>> 그룹별 반복 작업하기 -----

for key, group in gdf:
    print('* key : ', key)
    print(group.head())


# --------------------
# 행 열 함수
# --------------------

# >>> 행 열 함수 -----

def summation(x):
    return x+100

df1 = pd.DataFrame({"salary":[200,300,400,500], "bonus":[100,200,300,400], "incentive":[80,20,100,50]})
df2 = pd.DataFrame({"salary":['200원','300원','400원','500원'], "bonus":['100원','200원','300원','400원']})
series1 = pd.Series(index = ["철수","영호","민수"], data = ["빨간공", "파란공","노란공"])
series2 = pd.Series(index = ["빨간공", "파란공","노란공"], data = ["2만원", "3만원", "4만원"])

# S.map, S.apply: '원소별'로 함수를 적용
# 단, S.map 는 index를 활용하여 Series 간 mapping하는 경우에 유용
df1["salary"].map(summation)
df1["salary"].apply(summation)
series1.map(series2)

# DF.map:   '원소별'로 함수를 적용
# DF.apply: '행 또는 열별'로 함수를 적용
df2.map(lambda x : x[:3])    # 원소별 적용되어 '원'이 제거된 데이터 반환
df2.apply(lambda x : x[:3])  # 열별 적용되어 '3행'이 제거된 데이터 반환

# DF.pipe: '데이터프레임'에 함수를 적용
df.pipe(lambda x: x.dropna(axis=0)).pipe(lambda x: x.sum())


# --------------------
# 데이터 조작
# --------------------

import numpy as np
import pandas as pd
df = pd.DataFrame({'food':['melon', 'apple', 'banana', 'apple', 'melon'],
                   'year':[2018, 2019, 2018, 2017, 2018],
                   'quantity':[490, 512, 478, np.nan, 490]},
                   index = list('abcde'))
print(df)

# >>> 열 추가 -----

df['man'] = 10

# >>> 행 열 삭제 -----

df.drop(['a', 'b'], inplace=False)       # 행(axis=0), default
df.drop('man', axis=1, inplace=False)    # 열(axis=1)
del df['man']                            # 열 삭제, 즉시 적용

# >>> 중복값 확인, 삭제 -----

# 확인
df.duplicated()
df['food'].duplicated()

# 삭제
df.drop_duplicates()
df.drop_duplicates(subset=['food'], keep='last')

# >>> 결측값 확인, 삭제, 대체 -----

# 확인
df.isnull().sum()

# 삭제
df.dropna(axis=0)                               # 결측값이 존재하는 행 삭제
df.dropna(axis=1)                               # 결측값이 존재하는 열 삭제
df.dropna(subset=['food', 'quantity'], axis=0)  # 지정된 열에 결측값이 존재하는 행 삭제
df.dropna(subset=['a', 'd'], axis=1)            # 지정된 행에 결측값이 존재하는 열 삭제
df.dropna(thresh=3, axis=0)                     # thresh 옵션은 정상값이 지정된 갯수 미만인 행 또는 열 삭제

# 평균값 대체
mean_qtt = df.quantity.mean(axis=0)
df.quantity.fillna(mean_qtt)

# 최빈값 대체
most_freq = df['quantity'].value_counts(dropna=True).idxmax()  # value_counts(): 시리즈의 유일값을 그룹핑하여 count하는 함수
df['quantity'].fillna(most_freq)

# 이웃값 대체('ffill', 'bfill')
df['quantity'].fillna(method='ffill', inplace=False)

# 보간 대체(linear 선형보간, time 시간보간: 시간형 인덱스이어야 함)
df.interpolate(method='linear')

# 열별 대체
df.fillna({'year': most_freq, 'quantity': mean_qtt})

# S.where(), DF.where(): 조건이 true면 원래값 유지, false면 명시된 값 또는 NaN으로 대체
df['quantity'].where(df['year']<2018, df['year']+df['quantity'], axis=0)

# np.where(조건문, true 일때 값, false 일때 값) 대체
np.where(pd.notnull(df['quantity']), df['quantity'], df['year'])
np.where(df['year'] >= 2019, "Big", "Small")

# >>> 데이터셋 합치기, 나누기, 바꾸기 -----

df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'all', 'foo'],
                    'value': [1, 2, 3, 5]}, index=[2018, 2019, 2020, 2021])
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'foo', 'sel'],
                    'value': [6, 3, 2, 5],
                    'year': [1999, 2021, 2018, 2019]})

# 연결
pd.concat([df1, df2])                     # 열기준(axis=0), 합집합(join='outer')
pd.concat([df1, df2], ignore_index=True)  # 새로운 정수 인덱스 설정
pd.concat([df1, df2], axis=1)

# 병합
# 키  : 열명(on, left_on, right_on) 또는 인덱스(left_index, right_index)
# 방식: inner, outer, left, right
df1.merge(df2)                        # 공통 열 모두를 기준으로 교집합
df1.merge(df2, left_index=True, right_on='year')
df1.merge(df2, left_on=['lkey'], right_on=['rkey'], how='inner')

# 행과 열 바꾸기(Transpose)
df1.T

# >>> 데이터 양식 변경 -----

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare', 'class', 'who', 'embark_town', 'alive']]
df.fare = df.fare * 1000
print(df.info(), df.head(), sep='\n\n')

df['age'] = df['age'].replace(np.nan, 0).astype('int64')                           # 형 변환, Nan처리 필요
df['fare'] = df['fare'].apply(lambda x: format(x, ','))                            # 천단위 콤마 추가
df['fare'] = df['fare'].str.replace(',', '').replace(np.nan, 0).astype('float32')  # 천단위 콤마 삭제
df['fare'] = df['fare'].apply(lambda x: '{:.2f}'.format(x))                        # 소수점 자릿수 변경
df['fare'] = df['fare'].astype('float64')
df['class'] = df['class'].astype('str')

# >>> 정규화(Normalization) -----

# 통계 정보 확인
df.describe(include='all')  # include 옵션은 문자형 자료의 원솟수, 카테고리값갯수, 최빈값, 최빈값사용빈도수 추가

# 상대적 크기 차이 해소: 열데이터에서 열최솟값을 뺀 값을 분자로 하고, 열최댓값-열최솟값을 분모로 산출(0~1)
min_x = df['fare'] - df['fare'].min()
min_max = df['fare'].max() - df['fare'].min()
df['fare_normalization'] = min_x / min_max
df['fare_normalization'].describe()

# >>> 카테고리화 -----

# 컬럼 자료 확인
df['class'].unique()                             # 카테고리값 구성원 배열
df['class'].nunique()                            # 카테고리값 갯수
df['class'].value_counts()                       # 카테고리값별 자료수(NaN 생략)
df['class'].value_counts(dropna=False).idxmax()  # 카테고리값별 자료수(NaN 포함)

# 구간별 임의 기준 분할
df['fare'].describe()
df['fare'].value_counts(bins=[0, 100000, 200000, 300000], sort=False)

# 구간별 동일 갯수 분할
df['fare_cnt'] = pd.qcut(df['fare'], 3, labels=['Q1', 'Q2', 'Q3'])

df['fare_cnt'].value_counts()
df.groupby('fare_cnt')['fare'].mean()

import seaborn as sns
sns.displot(df, x='fare', hue='fare_cnt', element='step')

# 구간별 동일 길이 분할
count, bin_divcityers = np.histogram(df['fare'], bins=3)  # np.histogram(): 도수분포함수
bin_labels = ['low', 'middle', 'high']
df['fare_bin'] = pd.cut(x=df['fare'],         # 데이터 배열
                        bins=bin_divcityers,  # 경계 값 리스트
                        labels=bin_labels,    # bin 라벨
                        include_lowest=True)  # 최하 경계값 포함

bin_divcityers
df['fare_bin'].value_counts()
df.groupby('fare_bin')['fare'].mean()

import seaborn as sns
sns.displot(df, x='fare', hue='fare_bin', element='step')

# 더미 열 생성 (속하면1, 속하지 않으면0)
pd.get_dummies(df['fare_cnt'])
pd.get_dummies(df['fare_bin'])


# --------------------
# 시계열
# --------------------

# >>> Timestamp 생성 -----

# %Y(2020), %y(20), %m(01~12), %d(01~31)
# %H(01~23), %I(01~12), %M(01~59), %S(00~61)
# %w(0일~6토), %U(일요일기준누적주), %W(월요일기준누적주)
# %B(Jauary), %b(Jan), %A(Sunday), %a(Sun)

pd.date_range(start='2019-01-01',   # 날짜 범위의 시작
              end=None,             # 날짜 범위의 끝
              periods=4,            # 생성할 Timestamp의 개수
              freq='3MS',           # 시간 간격 (MS: 월의 시작일)
              tz='Asia/Seoul')      # 시간대(timezone)

# 텍스트를 Timestamp로 변환
tsp = pd.to_datetime(['200101', '220104', '241210'], format='%y%m%d')

# >>> Period 생성 -----

pd.period_range(start='2019-01-01',  # 날짜 범위의 시작
                end=None,            # 날짜 범위의 끝
                periods=3,           # 생성할 Period 개수
                freq='H')            # 기간의 길이 (H: 시간)

# Timestamp 를 Period 객체로 변환(D, B, W, W-MON, M, MS, Q, QS, A, AS, H, T, S)
tsp.to_period(freq='A')
tsp.to_period(freq='M')
tsp.to_period(freq='D')

# >>> 등간격 시간 조정 -----

tdf = pd.DataFrame(np.random.randn(100), columns=['value'],
                   index=pd.date_range('2018-1-1', periods=100, freq='D'))

# 업-샘플링은 시간 간격이 좁아지면서 빈 데이터 원소에 Nan 이 추가되므로 채워야 함(ffill, bfill)
tdf['value'].resample('10H').ffill()

# 다운-샘플링은 시간 간격이 넓어지므로 기간의 대표값을 구해야 함
tdf['value'].resample('M').first()

# >>> 기간의 시고저종(open, high, low, close) -----

tdf['value'].resample('W').ohlc()
tdf.head(7)

# >>> 기간 집계 함수 -----

# resample(): 등간격 데이터 집계
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

# 선형 기간 집계
tdf['value'].resample('M').count()

# 순환 기간 집계 (시간, 요일 등 반복개념)
tdf.index.day_name().value_counts()
tdf.index.day.value_counts().sort_index()

# >>> dt 활용 -----

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
pd.DataFrame(tdf.index)[0][0].isocalendar()[1]  # 연 기준 몇주째(숫자)
pd.DataFrame(tdf.index)[0].dt.dayofyear         # 연 기준 몇일째(숫자)
pd.DataFrame(tdf.index)[0].dt.days_in_month     # 월 일수(숫자) (=daysinmonth)
pd.DataFrame(tdf.index)[0].dt.is_leap_year      # 윤년 여부

# Period 객체로 만들어서 '년, 년-월' 분리
pd.DataFrame(tdf.index)[0].dt.to_period(freq='A')
pd.DataFrame(tdf.index)[0].dt.to_period(freq='M')

# 문자열 변환
pd.DataFrame(tdf.index)[0].dt.strftime("%Y년 %m월 %d일")

# >>> 시계열 인덱싱 -----

tdf['2018-03-28':'2018-04-05']
tdf.loc['2018']
tdf.loc['2018-03':]

# >>> 시간대 설정 -----

ts_seoul = pd.DataFrame(tdf.index)[0][0].tz_localize('Asia/Seoul')
ts_UTC = ts_seoul.tz_convert('UTC')


# --------------------
# 파일 입출력
# --------------------

# >>> csv -----

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

# >>> excel -----

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


# =====================
# String
# =====================

# >>> Print -----

# separate(프린트문 안에서의 구분자)
s1 = "First str"
s2 = "Second str"
print(s1, s2, sep='\n그리고\t')  # \t tap, \n 줄바꿈

# end(프린트문 끝부분에서의 구분자)
print("First str", end='\t')    # \t tap, \n 줄바꿈
print("Second str")

# str concatenation: + ,
print("우리", "나라")                        # 띄어쓰기
print("우리" + "나라")                       # 붙여쓰기
print("우리" + "나라" + str(10000) + "세")   # + 에서는 자료형 맞춰야 함
print("그는 \"J\"에게 말했다. \'가지마!\'")   # 문장 안에서 ', " 사용( \ 백슬래시)

# C 언어 % 타입: %s, %c, %d, %f, %%
print("23년 승률은 %d%% 입니다." % 100)      # 퍼센트 시는 2번 써 준다
print("%5.3f" % 3.141592)                   # 소수점 찍기
print("'%d년은 %s년 입니다." % (24, "갑진"))
print('%s의 투자비중은 %-15.2f%%입니다.' % (a[-6:-1], b))              # 좌정렬 및 자릿수 맞춤
print('%s의 투자비중은 % 15.2f%%입니다.' % (a[-6:-1], b))              # 우정렬 및 자릿수 맞춤
print('%s의 투자비중은 %015.2f%%입니다.' % (a[-6:-1], b), end='\n\n')  # 우정렬 및 0채움

# format 타입: {지정변수:[빈공간채울문자][정렬방향<>][+양수부호][공간수][,][.소수자릿수]}
print('value is {{ {} }}'.format('%d' % b))
print('{}의 투자비중은 {}%입니다.'.format(a[7:12], '%15.2f' % b))
print('{name}의 투자비중은 {money}%입니다.'.format(name=a[7:12], money='%15.2f' % b))
print('{0}의 투자비중은 {1:<15.2f}%입니다.'.format('K씨', -1000.5))   # 좌정렬
print('{}의 투자비중은 {:^15.2f}%입니다.'.format('K씨', -1000.5))     # 가운데정렬
print('{}의 투자비중은 {:>15.2f}%입니다.'.format('K씨', -1000.5))     # 우정렬
print('{}의 투자비중은 {:0>15.2f}%입니다.'.format('K씨', -1000.5))    # 공백채우기
print('{}의 투자비중은 {:,.2f}%입니다.'.format('K씨', -1000.5))       # 천단위콤마표시
print('{0:+15,} 과 {1:+15,} 사이'.format(50000, -50000))             # 양수부호

# f-string 타입(python 3.6 이후)
lst = [20, '시험', 21]
strValue = lst[1]

print(f'{lst[0]}회 {lst[1]} 만점자 총 {lst[2]}명')
print(f"'{lst[0]}'회 {lst[1]} 만점자 총 '{lst[2]}'명")  # 홀따옴표 활용하기(외부를 쌍따옴표로 감싸기)
print(f"나의 조국은 '{strValue}'입니다.")
print(f"나의 조국은 '{strValue:<15}'입니다.")
print(f"나의 조국은 '{strValue:>15}'입니다.")
print(f"나의 조국은 '{strValue:^15}'입니다.")           # 가운데정렬의 중간이 맞지 않으면 왼쪽으로 치우침
print(f'value is {{ {int(b)} }}')
print(f'{a[7:12]}의 투자비중은 {b:<15,.2f}%입니다.')
print(f'{a[7:12]}의 투자비중은 {b:^15,.2f}%입니다.')
print(f'{a[7:12]}의 투자비중은 {b:>15,.2f}%입니다.')

# >>> Count -----

test = "Welcome to Korea"

len(test)        # 문자열의길이, 리스트/튜플카운팅(NaN 포함)
test.count('e')  # 특정문자갯수, 리스트/튜플카운팅(NaN 제외)

# >>> 인덱스 위치값 -----

test.find("Z")              #  찾는 문자없으면 -1
test.index("Z")              # error

test.find("K")              # 11 (이하 index 매서드 동일)
test.find("K") - len(test)  # -5
test.find("e")              # 왼쪽부터 첫번째 인덱스 위치값
test.rfind("e")             # 오른쪽부터 첫번째 인덱스 위치값
[i for i, x in enumerate(test) if x == 'e']  # 모든 원소의 인덱스 위치 반환

# >>> 공백 제거 -----

test = "   Welcome to Korea   "
test.strip()
test.lstrip()
test.rstrip()

# >>> 대문자 양식 -----

test = "Welcome to Korea"
print(test.lower())
print(test.upper())
print(test.capitalize())  # 문장의 시작 단어만 대문자

# >>> 문자길이 양식 -----

test.ljust(50, '-')   # 총길이 50, 왼쪽정렬, 지정문자 채움
test.rjust(50, ' ')   # 총길이 50, 오른쪽정렬, 공백 채움

# >>> Replace, Split, Join -----

a = 'asiana air com'
b = a.replace(' ', '.')
a[7:10] + '@' + a[-3:]
c = b.split('.', maxsplit=1)
d = '@'.join(c)
print(d)

# >>> 워드클라우드: 딕셔너리 키 정렬 -----

str = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
 when an unknown printer took a galley of type and scrambled it to make a type
 specimen book. It has survived not only five centuries, but also the leap into
 electronic typesetting, remaining essentially unchanged. It was popularised in
 the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
 and more recently with desktop publishing software like Aldus PageMaker including
 versions of Lorem Ipsum."""

sltstr = str.split()

cnts = dict()
for i in sltstr:
    if i not in cnts:
        cnts[i] = 1
    else:
        cnts[i] += 1

print(cnts)

lstcnts = sorted(cnts.items())      # 키 값으로 정렬된 리스트!! 반환

for k, v in dict(lstcnts).items():  # 리스트를 딕셔너리로 변환하여 키와 값으로 분리하여 출력
    print(k, '\t', v)


# =====================
# re
# =====================

# --------------------
# 정규표현식
# --------------------

# abc                  문자열('abc')를 찾음
# [abc]                a 또는 b 또는 c
# [^ab]                부정, [^a^b], [^(ab)]와 같음
# [a-zA-Z]             (-)기호로 짝을 맞춰 범위를 지정
# [ㄱ-ㅎ|ㅏ-ㅣ|가-힣]   한글
# [0-9]                숫자
# ^                    시작
# $                    끝
# .                    문자(공백문자, 기호 포함) 1개
# * 	               0 or more
# +	                   1 or more
# ?	                   0 or 1
# {숫자}               숫자 만큼
# {숫자,}              숫자 이상
# {숫자1,숫자2}        숫자1 이상, 숫자2 이하 (숫자1,숫자2 모두 붙여쓰기에 주의!!)
# a+?    	           match as few as possible(1 if 1 or more)
# a{2,}?	           match as few as possible(2 if 2 or more)
# ab|cd	               match ab or cd (순서 중요!!)

# \d 숫자 1개                        \D
# \w 알파벳+한글+숫자+_               \W
# \s 공백+탭                         \S
# \b 단어경계(\w 와 \W 사이의 경계)   \B 철자경계(\w와 \w 사이)

# >>> \ 사용법!! -----
    
# '\문자열' 은 --> 짝수로만 인식
"\superman"        # \2개
"\\superman"       # \2개
"\\\superman"      # \4개
"\\\\\superman"    # \6개

# r'\문자열' 은 --> 2배수로 인식
r"\superman"        # \2개
r"\\superman"       # \4개
r"\\\superman"      # \6개

# 파이썬 엔진은 --> '\문자열', r'\문자열'에서 산정된 '\' 개수를 --> 50% 만 인식
print("\superman")    # \1개 -> \2개 -> \1개
print("\\superman")   # \2개 -> \2개 -> \1개
print(r"\\superman")  # \2개 -> \4개 -> \2개 (직관적임)


# --------------------
# 사용법
# --------------------

import re

# >>> re 모듈의 메소드 -----

# 종류          검색범위                         성공반환값     실패반환값
# re.match      문장 처음부분만                   객체 1개       None
# re.search     문장 처음부터 일치하는 첫번째 것   객체 1개       None
# re.findall    문장 처음부터 일치하는 모든 것     리스트         빈 리스트
# re.finditer   문장 처음부터 일치하는 모든 것     순환객체       None
# re.fullmatch  문장 일치                        객체 1개       None
# re.compile    정규식 반복 사용
# re.sub        패턴 대체

# >>> 옵션 -----

# re.I 대소문자 불문
# re.S 메타문자(.)에서 개행문자(\n) 포함
# re.M 메타문자(^$)를 전체문장이 아닌 각 라인에 적용

# >>> Groups & Lookaround -----

# (abc)	    capture group
# \1	    backreference to group #1(그룹1 표현식에서 캡쳐한 결과물을 복사)
# (?:abc)	non-capturing group(캡쳐그룹 해제)
# (?=abc)	positive lookahead, 조건 앞의 문자가 조건을 만족하는 경우 그것만 선택
# (?!abc)	negative lookahead, 조건 앞의 문자가 조건을 만족하는 경우 그것만 제외하고 선택
# (?<=abc)	positive lookbehind, 조건 뒤의 문자가 조건을 만족하는 경우 그것만 선택
# (?<!abc)	negative lookbehind, 조건 뒤의 문자가 조건을 만족하는 경우 그것만 제외하고 선택

# 패턴 컴파일에서 옵션 지정
text = '''홍길동 010-1234-5671
이순신 010-3333-9632
김유신 010.9999.5417
강감찬 010 111  2222'''
pattern = re.compile(r'\w+\s+\d{3}[-_. ]+\d{3,4}[-_.\s]+\d{4}', re.M)
rst_match = re.findall(pattern, text)
print('\n'.join(rst_match))

# 매칭함수(pattern, text, 옵션)에서 옵션 지정
re.findall('k.', 'k5r k k\n Ks', re.I)
re.findall('k.', 'k5r k k\n Ks', re.S)
re.findall('k.', 'k5r k k\n Ks', re.M)
result = re.finditer('010', text)
for iter in result:
    print(iter)

re.findall('(?i)k.', 'k5r k k\n Ks')  # 패턴에 (?옵션)을 직접 입력(인라인 방식)
re.findall('(?s)k.', 'k5r k k\n Ks')
re.findall('(?m)k.', 'k5r k k\n Ks')

# >>> 그룹핑 및 치환 -----

text = '홍길동 010-1234-5671'

# 컴파일의 sub() 그룹핑
pattern = re.compile(r'^(\w+)\s+(\d{3}).(\d{3,4}).+(\d{4})$', re.M)
print(pattern.sub(r'\g<1> : \g<2> - \g<3> - ****', text))
print(pattern.sub(r'\1 : \2 - \3 - ****', text))
print(pattern.sub('\\1 : \\2 - \\3 - ****', text))

# 매칭객체의 group() 그룹핑
rst_match = re.search(pattern, text)
print(rst_match.group(0))  # group(0) : 매칭된 전체 문자열 결과값
print(rst_match.group(1))  # group(1) : 매칭된 1번째 그룹의 문자열 결과값
print(rst_match.group(4))  # group(4) : 매칭된 4번째 그룹의 문자열 결과값

print(rst_match.start())      # start(): 매칭된 문자열의 시작 위치 반환
print(rst_match.end())        # end(): 매칭된 문자열의 끝 위치 반환
print(rst_match.span())       # span(): 매칭된 문자열의 (시작, 끝) 위치 튜플 반환

# re.sub(pattern, replacement, string, 치환횟수) 치환
print(re.sub(pattern='aaa', repl='xxx', string='aa aaa aaaa aaaaa', count=2))
print(re.sub('aaa', 'xxx', 'aa aaa aaaa aaaaa', 3))

# >>> [-] 사용법 -----

text = 'my.name@localhost.com'
# pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w-.]+.com')  # '-'이 짝을 이루면 '범위'로 해석되어 bad character 에러 발생
pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w-]+.com')     # '-' 앞뒤의 짝을 깨서 해결
pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w\-.]+.com')   # '-' 앞에 \ 추가해서 해결
rst_matchLst = re.findall(pattern, text)
print(rst_matchLst)

# >>> | 사용법 -----

text = "kor 단어는 매칭이 되지만, korea 또는 korean 단어에는 매칭이 안되는 패턴"
pattern = re.compile(r'kor|korea|korean')  # kor을 먼저 쓰면 kor만 3개 찾음
pattern = re.compile(r'korean|korea|kor')
print(re.findall(pattern, text))

# >>> \b 사용법 -----

print("\\b 개수: ", len(re.findall(r'\b', 'Welcome to Seoul.')))
print("\\B 개수: ", len(re.findall(r'\B', 'Welcome to Seoul.')))
print(re.findall(r'\bkor\w+\b', "kor 는 비매칭 korea 또는 korean 와는 매칭"))

# >>> 웹페이지 URL 정규식 -----

text = '웹주소는 http://yourcompany.com/search?a=111&b=222 이다.'
pattern = re.compile(r'http[s]*://[a-zA-Z0-9-_]*[.]*[\w-]+[.]+[\w.-/~?&=%]+')
rst_matchLst = re.findall(pattern, text)
print(''.join(rst_matchLst))  # 리스트에서 문자열만 추출

# >>> 한글만 추출 -----

text = "ㅋㅋㅋ ab 안녕하세요, do노력합ㅣ니다"

re.compile('[ㄱ-ㅎ]+').findall(text)  # 출력 ['ㅋㅋㅋ']
re.compile('[ㄱ-ㅎ|ㅏ-ㅣ]+').findall(text)  # 출력 ['ㅋㅋㅋ', 'ㅣ']
re.compile('[ㄱ-ㅎ|ㅏ-ㅣ|가-힣]+').findall(text)  # 출력 ['ㅋㅋㅋ', '안녕하세요', '노력합ㅣ니다']

txt = ("[[1월 20일]]| 부통령 = [[월터 먼데일]]| 전임 = 제럴드 포드| 전임대수 = 38| 후임 = 로널드 레이건|"
       "후임대수 = 40&lt;!--주지사--&gt;|국가2 = [[조지아주]]|명칭2 = [[주지사]]|대수2 = 76|취임일2 ="
       "[[1971년]] [[1월 12일]]|퇴임일2 = [[1975년]] [[1월 14일]]|부통령2 = 레스터 매독스|부통령명칭2 ="
       "[[분류:지미 카터 ]][[분류:1924년 출생]][[분류:1976년 미국 대통령 후보]][[분류:1980년 미국 대통령 후보]]")

p = re.compile('\[\[분류:(.*?)\]')
p.findall(txt)

p2 = re.compile('(?<=\[\[분류:)([ |0-9|ㄱ-ㅎ|ㅏ-ㅣ|가-힣]*?)(?=\]\])')
p2.findall(txt)

# >>> 정규식과 문자열 함수 대비 -----

# Q) Notebook 이 포함된 단어를 모두 찾아라
text = '''
jupyternotebook, evernote, notebook, onenote, notebook1, 21세기notebook, jupyter-notebook,
jupyter_notebook, jupyter@notebook
'''

# A1) 정규식
pattern = re.compile(r'\w*[-@]*notebook\w*')
print(', '.join(re.findall(pattern, text)))

# A2) 문자열 함수
a = text.split()
rst_lists = []
for i in a:
    if 'notebook' in i:
        rst_lists.append(i)

print(rst_lists)

print([i for i in a if 'notebook' in i])

# >>> str 메서드 응용 -----

# 정규표현식으로 선택한 문자를 독립된 열로 분할
df.city.str.extract(r'(.*)_(.*)')

# str.split(slice)
df['city'].str.split('_').str[0]
df['city'].str.split('_').str[1]
df['city'].str.slice(2, 3)

# str.contains(): 정규표현식으로 조건 만족 여부를 반환
df['city'].str.contains('S|j', na=False, regex=True)  # 결측값은 'False'로 반환
df[~df.city.str.contains('(S|j)', na=False)]          # 불포함(결측값이 있는 경우 'na=False')


# =====================
# iterable 메서드
# =====================

# >>> List Comprehention -----

lst = ['lion', 'tiger', 'hippo']
[i.upper() for i in lst]

# >>> Add -----

lst = [1, 2, 3]
lst2 = ('lion', 'tiger', 'hippo')

lst + ['cow']
lst + list(lst2)        # 튜플+리스트 병합은 리스트로 작업 후 튜플로 변환
lst.extend(list(lst2))

lst.append(4)       # [1, 2, 3, 4]
lst.append([5, 6])  # [1, 2, 3, 4, [5, 6]]

lst.extend(4)         # error: iterable 자료형만 입력 가능
lst.extend([4])       # [1, 2, 3, 4]
lst.extend([5, 6])    # [1, 2, 3, 4, 5, 6]
lst.extend([[5, 6]])  # [1, 2, 3, 4, [5, 6]]

lst.insert(0, [10, 20])    # 0번째(맨앞에) 추가, insert(위치인덱스, 값)
lst.insert(-1, 100)        # 마지막-1번째 추가
lst.insert(len(lst), 100)  # 마지막에 추가

# >>> Delete -----

lst = ['li', 'Co', 'Ni', 'Mn', 'Al', 'Mg']

lst.pop(-1)       # pop(index): 해당 인덱스의 값을 빼면서 뺀 값을 보여줌
lst.pop()         # 인덱스가 없으면 마지막 원소에 적용
lst.remove('Mn')  # Remove(value): index 불가!!
del lst[-1]
lst.clear()

# >>> Sort -----

lst = 'I am a bright Man'.split()

sorted(lst)              # 원본보존 및 결과반환
lst.sort()               # 원본변경(오름차순)
lst.sort(reverse=True)   # 내림차순
lst.sort(key=len)        # 요소의 길이를 기준 정렬
lst.sort(key=str.lower)  # 알파벳 기준 정렬

# >>> Reverse -----

lst = [4, 5, 1, 3, 2, 6]

reversed(lst)  # 원본보존 및 결과반환
lst.reverse()  # 원본변경

# >>> Count -----

lst = [4, 5, 1, 3, 2, 6, 1, 3, 1, 7]
lst.count(1)


# =====================
# 람다식
# =====================

# >>> iterable 자료형에 적용 -----

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list(filter(lambda x: x % 2, lst))  # filter(): 참인 결과 값만 반환
list(filter(lambda x: x % 2 != 0, lst))
list(filter(lambda x: x % 2 == 0, lst))

# >>> 함수의 인자에 적용 -----

def my_strip(x):
    return x.strip()

a = ' UD001 - lion, UD002 - tiger , UD003 - hippo '
b = a.split(',')

c = list(map(my_strip, b))
c.sort(key=lambda x: x[8])  # 9번째 글자 기준 오름차순 정렬
print(c)


# =====================
# IPython 환경 설정
# =====================

# 옵션 확인: pd.get_option('~~')
# 옵션 설정: pd.set_option('~~')
# 옵션 초기화: pd.reset_option('~~')
pd.set_option('display.max_rows', None)                  # 행 개수
pd.set_option('display.max_columns', 10)                 # 열 개수
pd.set_option('display.max_colwidth', 20)                # 열 너비
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드로 조정한 열 너비
