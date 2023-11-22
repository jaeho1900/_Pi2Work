# >>> 판다스 고유 데이터타입
# Series: label로 이뤄진 1차원배열 자료구조
#  - 생성 방식: 딕셔너리(dict), 넘파이배열(numpy.array), 직접 리스트 입력
#  - 자동으로 인덱스 축 생성(index, value 둘다 확인 가능)
#  - DataFrame의 열을 검색하면 Series 타입으로 리턴 받음
# DataFrame: 2차원배열 자료구조
# 시리즈는 1차원배열이므로 행단위로 처리되고, 
# 데이터프레임은 2차원배열이므로 열단위로 처리됨

# >>> Series
import pandas as pd
import numpy as np

# 생성
ar1 = pd.Series([1, 2, 3, -4, 5])  # 대소문자주의 !! Series x
ar1
type(ar1)

ar2 = pd.Series(np.array([1, 2, 3, -4, 5]))
ar2
type(ar2)

# index, value 확인
ar2.index
ar2.values  # 복수형(s)철자 주의!!

# type 확인
ar2.dtype
ar2.dtypes

# 인덱스 속성으로 지정
ar = pd.Series([1, 2, 3, -4, 5], index=['a', 'b', 'c', 'd', 'e'])
ar

# 딕셔너리로 인덱스 지정
pydic = {"서울": 100, "부산": 200, "광주": 300, "세종": 400}
ar = pd.Series(pydic)
ar

# 시리즈 이름 지정
ar.name = "대한민국 광역시"
ar

# 인덱스 수정
ar.index = ['a', 'b', 'c', 'd']
ar

# 인덱스를 이용한 접근
ar["a"]
ar[-1]
ar[1:3]
ar[2:]
ar["c":]

# 조건을 이용한 접근: 조건은 값으로 비교
ar = pd.Series(['a', 'b', 'c', 'd', 'e'])
ar
# a 이상만 출력?
ar[ar > 'a']

# Series 연산
ar = pd.Series([1, 2, 3, 4, 5])

ar * 2
ar1 = ar ** 2
ar1

# 추가 인덱스 지정
pydic = {"서울": 100, "부산": 200, "광주": 300}
ar = pd.Series(pydic)

_ix_name = ['서울', '부산', '광주', '세종']
ar1 = pd.Series(pydic, index=_ix_name)
ar1  # 추가된 인덱스에 miss match된 값은 NaN(Not a Number) 

# Series에서 2차원배열을 생성하려면 error
ar1 = pd.Series(np.arange(1, 10, 2))
ar2 = pd.Series(np.arange(1, 31).reshape(5, 6))  # error

# >>> DataFrame
import pandas as pd
import numpy as np

# 중첩리스트로 생성
df = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
df

# 인덱스 지정
df1 = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], index=['a', 'b'])
df1 = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], ['a', 'b'])  # index 생략가능
df1

df2 = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], index=list('a', 'b'))  # error
df2 = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], index=list('ab'))
df2

# df생성시 행과 열의 레이블 지정
df = pd.DataFrame([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                  index=['aa', 'bb'], columns=['a', 'b', 'c', 'd', 'e'])
df

# values 속성
df.values
type(df)         # DataFrame
type(df.values)  # numpy.ndarray(넘파이 다차원배열)

# 행과 열의 속성 타입 확인
df.index
df.columns

# 차원, 사이즈, 형태도 넘파이처럼 출력
df.ndim
df.size
df.shape

# 넘파이 함수로 df 생성
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
df
df1 = pd.DataFrame(np.arange(1, 10).reshape(3, 3))
df1

# 헷갈리는 df 색인
ar = np.arange(1, 31).reshape(5, 6)
ar
ar[4, 4]

df = pd.DataFrame(ar)
df
df[4, 4]  # error
df[0]     # 데이터프레임은 열기준 색인이 기본
df[5]
df[0][0]  # df[열][행] 개념
df[4][4]
df[4][5]  # KeyError: 5
