import numpy as np
import pandas as pd

# raw_data 생성
raw_data = {
    'food':['apple', 'pear', 'peach', 'banana', 'orange', 'watermelon'],
    'month':[1, 2, 3, 4, 5, 6],
    'quantity':[55, 32, 59, 87, 24, 49]
    }
df = pd.DataFrame(raw_data)
df

# 무작위 data 입력(실습용)
raw_data = {'food':['melon', 'melon', 'apple', 'apple', 'apple', 'peach'],
            'year':[2018, 2019, 2018, 2019, 2020, 2018],
            'quantity':[490, 512, 478, 325, 290, 800]}
df = pd.DataFrame(raw_data)
df

# 컬럼 인덱스의 순서를 변경
df1 = pd.DataFrame(raw_data, columns=['year', 'food', 'quantity'])
df1

# 행 인덱스의 순서를 변경
df1 = pd.DataFrame(raw_data, index=list('abcdef'))
df1

# 컬럼 순서를 변경하면서 컬럼 하나를 추가 : rank에 값이 없으면 NaN으로 표시
df1 = pd.DataFrame(raw_data, columns=['quantity', 'year', 'rank', 'food'])
df1

# index, column 정보 확인
df1
df1.index
df1.columns

# >>> 특정한 행과 열의 값을 출력
# 행 : loc (별도의 인덱서를 사용)
df1.loc[3]

# 1, 5 행만 출력?
df1.loc[1]
df1.loc[1, 5]  # error
df1.loc[[:]]   # error
df1.loc[:]
df1.loc[[1, 5]]
df1.loc[[1, 5], :]
df1.loc[[1, 5], ['quantity', 'year', 'food']]

# 열 : 컬럼명 사용
df1.year

# 열 : iloc
df1.iloc[:, 3]
df1.iloc[:, 1:]
df1.iloc[:, [ 1:]]  # error
df1.iloc[:, [3]]
df1.iloc[:, [0, 3, 1]]

# >>> NaN 채우기
df1
df1.fillna(100)   # 원본을 변화시키지는 않음
df1.fillna('kor')

# >>> 조건을 이용한 True, False 입력
df1['addcol'] = df1.food == 'peach'
df1

# 컬럼 삭제
del df1['addcol']

# 행과 열 바꾸기(Transpose)
data = {
    'Seoul':{2018:1, 2019:2, 2020:1},
    'Busan':{2018:3, 2019:1, 2020:4},
}
df2 = pd.DataFrame(data=data)
df2

df2.T

# 특정 범위만 df 로 생성
df3 = pd.DataFrame(data, index=[2019, 2020])

x = {'Seoul': df2['Seoul'][:-1]}
pd.DataFrame(x)

# >>> 종합실습
import numpy as np
import pandas as pd

# >>> 시리즈
ar = pd.Series([1,2,3,4,5], dtype='object')  # 판다스에서는 보통 문자열을 object로 표현한다 
ar
ar.dtype
ar.dtypes
type(ar)  
ar.values
ar.index
ar = pd.Series([1,2,3,4,5], index=list('abcde'))
ar.index
ar.ndim
ar.size
ar.shape
ar[1]    # 정수 인덱스로 색인
ar['b']  # 인덱스 라벨로 색인
ar[:]    # 정수로 슬라이싱
ar[1:3]
ar[:-1]
ar['b':'d']  # 인덱스 라벨로 슬라이싱(마지막도 포함 주의!!)
ar = pd.Series([1,2,3,4,5])
ar
ar.index = list('abcde')
ar
ar = ar.rename(index={'e':'z'})
ar[100] = 100  # 정수인덱스로는 추가할 수 없다 !! (인덱스범위를 벗어남)
ar['z'] = 100  # 원소 추가
del ar['z']    # 원소 삭제

# 뷰: 같은 메모리 공유(원본에 영향)
arview = ar['b':'d']
# 넘파이의 may_share_memory()사용하여 메모리 공유 여부를 확인 가능
np.may_share_memory(ar, arview)
# 뷰에 새로운 원소를 추가하면 원본에 적용 안됨 !!
# 뷰가 새로게 원본으로 부터 독립하게 됨 !!
arview
arview['f'] = 100  
arview
ar
np.may_share_memory(ar, arview)

# 배열 복사
arcopy = ar['b':'d'].copy()
np.may_share_memory(ar, arcopy)

# to_frame() : 시리즈를 데이터베이스로 변환하는 함수
type(ar)
test = ar.to_frame()
type(test)
test.ndim

# 변수의 데이터프레임 여부 확인
isinstance(ar, pd.DataFrame)
isinstance(test, pd.DataFrame)

# >>> 데이터프레임
import numpy as np
import pandas as pd

# 2차원 데이터프레임 생성 방법
a = pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
a1 = pd.DataFrame(np.arange(1,16).reshape(3,5))
a2 = pd.DataFrame({'float':[4.0],'int':[9],'str':['korea']})

# 행렬의 레이블 지정
_df = pd.DataFrame(np.arange(1,16).reshape(3,5), index=list('abc'), columns=list('ABCDE'))
_df
_df.size
_df.ndim
_df.shape
_df.values
_df.index
_df.columns
type(_df)
_df.dtypes

# 데이터프레임 색인 : 열 기준 !!
_df
_df[0]    # error
_df['A']
_df['a']  # error
_df[['A','B']]  # 다중 열 색인

# 데이터프레임 행 색인 : loc
_df.loc['a']
_df.loc['a', :]

# 데이터프레임의 행과 열 색인 : 레이블 정보로 색인
_df['D']['b']
_df['D', 'b']
_df.loc['b':'c', 'A':'C']  # 마지막 지정 범위도 반환

# 슬라이싱한 데이터프레임은 뷰일 뿐이다
r = pd.DataFrame(np.arange(1,16).reshape(3,5), index=list('abc'), columns=list('ABCDE'))
r1 = r.loc['a':,'D':]
r1
r1.loc['b','D'] = 900
r
np.may_share_memory(r,r1)
r1['E'] = 400  # 열을 전부 바꾸면 원본에 영향을 주지 않음
r1
r
np.may_share_memory(r,r1)
r1.loc['b','D'] = 1000  # 일부 값만 바꾸면 다시 원본에 영향을 줌
r
np.may_share_memory(r,r1)

# 정수 인덱스로 색인 : iloc
_df = pd.DataFrame(np.arange(1,16).reshape(3,5), index=list('abc'), columns=list('ABCDE'))
_df.iloc[0]

# 뷰  
_df
_dfview = _df.iloc[:,:-1]
_dfview
np.may_share_memory(_df,_dfview)

# >>> 데이터프레임 생성의 다양한 예

# 필요 정보(data, index, column)로 생성
_data = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
_index = list('abc')
_column = list('ABCDE')
_df = pd.DataFrame(data=_data, index=_index, columns=_column)
_df

# 시리즈로 생성
_dfseries = pd.DataFrame({'A':pd.Series([1,2,3,4], dtype='int'),
                          'B':pd.Series([5,6,7,8], dtype='float')})
_dfseries

# 리스트로 생성
_dflist = pd.DataFrame({'점수':[99,90,88,70], '학점':['A+','A','B+','C']})
_dflist

# 데이터프레임의 열 자료형 변경: astype
# 변경하고자 하는 열의 이름을 딕셔너리 키와 값으로 전달
_df
_df.dtypes
_df = _df.astype({'A':int32, 'B':float32, 'C':str})        # error 판다스에는 int32자료형이 없음
_df = _df.astype({'A':np.int32, 'B':np.float32, 'C':str})  # 넘파이 자료형 적용
_df = _df.astype({'A':int, 'B':float, 'C':str})            # 파이썬 자료형 적용
_df.dtypes
_df

# 특정 열의 자료형 변경
_df['E'] = _df['E'].astype('float64')

# >>> 다차원 배열의 색인
ar = np.arange(1,26).reshape(5,5)
ar
# 정수 인덱스 색인 : 하나의 스칼라값 반환
ar[0]        # array([1, 2, 3, 4, 5])
ar[0, -1]    # 5

# 팬시 색인: 배열(리스트)을 색인에 사용, 기존(다차원) 배열의 형태를 유지하며 반환
# 팬시 색인은 메모리 공유를 하지 않는다(뷰가 아님)
ar[[0]]      # array([[1, 2, 3, 4, 5]]) : 팬시 색인
ar[[0, -1]]  # array([[ 1,  2,  3,  4,  5], [21, 22, 23, 24, 25]])

# 문제. ar 배열에서 13,14,18,19 를 색인하시오
temp = ar[[2,3]]
ar1 = temp[:, 2:4]
ar1

# 넘파이 ix_함수를 이용한 팬시 색인 : 직관적 반환
ar
ar[np.ix_([2,3],[2,3])]  # 지정된 인덱스 값을 반환

import pandas as pd
import numpy as np

# 파일에서 호출
filepath = 'dataset/data.csv'
df = pd.read_csv(filepath, na_values='NA', encoding='utf8') # NA값이 'NA'라는 스트링값으로 저장된 경우

data.to_csv('result.csv', header=True, index=True, encoding='utf8')

# 시리즈로 직접 생성
pd.Series({'idx1':'value', 'idx2':'value'}, name='class1')

# 데이터프레임으로 직접 생성
dataset = np.array([['kor', 70], ['math', 80]])
df = pd.DataFrame(dataset, columns=['class', 'score'])
df = pd.DataFrame(data=[['kor', 70], ['math', 80]], columns=['class','score'])
df = pd.DataFrame({'class': ['kor', 'math'], 'score': [70, 80]})
df

df.index
list(df.index)

# 인덱스 변경
df.index = ['A', 'B']
df

# 기존 컬럼을 인덱스로 변경: 키는 '문자형'으로 입력, drop은 인덱스로 지정한 컬럼을 데이터프레임에서 삭제여부, append는 기존 인덱스를 데이터프레임의 컬럼으로 추가여부, inplace는 원본데이터를 변경여부
df.set_index('class', drop = True, append = False, inplace = True)
df

# drop는 기존인덱스를 삭제할지 컬럼에 추가할지 결정
df.reset_index(drop = False, inplace = True)
df
