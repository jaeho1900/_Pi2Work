# =====================
# Numerical Python의 합성어
# =====================

# 호출
import numpy as np

# 버젼확인
np.__version__

# 1차원 배열 만들기
ar1 = np.array([1, 2, 3, 4, 5])
ar1

# 파이썬 리스트를 변수로 사용
lst = [6, 7, 8, 9, 10]
ar2 = np.array(lst)
ar2

# 다차원 배열
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
arr1.shape  # (3, 4) : 큰방 3개에 각 방마다 4개씩 들어있다

# 배열 출력
arr1
print(arr1)  # 넘파이배열에서는 , 가 생략됨

# 배열의 모양(형태) 확인
arr1.shape

# ndim : 차원만을 확인(shape로도 유추 가능)
arr1.ndim

# size : 원소의 갯수
arr1.size

# len : 길이(큰방의 갯수)
len(arr1)

# 넘파이는 모든 요소를 동일한 타입으로 처리 !!
arr2 = np.array([1, 2, 3, 'a', 'b', 'c'])
arr2[0]  # '1'
type(arr2[0])  # 숫자와 문자가 혼재되어 있으면 모두 문자 타입으로 통일

# 배열의 배열
import numpy as np
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
a[1, 0]
a[1, 2]
a[0, 1]

# 넘파이 객체로부터 직접 호출
a.shape
np.shape(a)

# reshape : 구조 변경
print(a)
# 2 x 6 shape change
a_new = a.reshape(2, 6)
a_new.shape

# zeros : 모든 요소를 0으로
arr = np.zeros((3, 4))
arr

# ones : 모든 요소를 1로
arr = np.ones((3, 4))
arr

# eye : 단위행렬(identity matrix) 대각선은 1, 나머지는 0
arr = np.eye(4)
arr

# dot : 행렬 곱셈
ar1 = np.eye(2)
ar2 = np.array([[3, 4], [5, 6]])
ar1
ar2

test = ar1 * ar2            # 같은 위치의 요소끼리만 수식 적용
test

ar1xar2 = np.dot(ar1, ar2)  # 행렬의 곱셈
ar1xar2

# arange : 원하는 숫자 범위, 간격을 지정
arr = np.arange(10)  # 파이썬의 range
arr

arr = np.arange(1, 20, 2)
arr

arr = np.arange(1, 10, 0.5)  # 간격이 0.5이면 10-0.5(간격)까지로 범위가 변경되어 9.5도 출력!!
arr

# arange + reshape 로 3x3 행렬 생성
arr = np.arange(9)
arr
arr_new = arr.reshape(3, 3)
arr_new

arr2 = np.arange(9).reshape(3, 3)  # 매서드 체인 활용
arr2

# -1 reshape(-1, n[정수]) : 행, 열 중 열을 기준으로 구조 변경(요소보다 배열을 중시)
import numpy as np
ar = np.arange(12).reshape(3, 4)
ar

ar1 = ar.reshape(-1, 1)  # (-1,1) == (12,1) 원소의 갯수를 모르거나 변동일때 유용
ar1

ar2 = ar.reshape(-1, 2)  # (-1,2) == (6,2)
ar2

# -1 reshape(n[정수, -1]) : 행, 열 중 행을 기준으로 구조 변경
import numpy as np
ar = np.arange(12)
ar3 = ar.reshape(2, -1)  # (2, 6)
ar3

ar4 = ar.reshape(4, -1)  # (4,3)
ar4

# -1 reshape(-1) : 행, 열 중 행을 기준으로한 1차원 배열 구조로 변경
import numpy as np
ar = np.arange(12)
ar5 = ar.reshape(-1)     # (12), (12,), (1, -1), (1, 12)
ar6 = ar.reshape(12)
ar7 = ar.reshape(12,)
ar8 = ar.reshape(1, -1)  # ?? 2차원배열
ar9 = ar.reshape(1, 12)  # ?? 2차원배열
print(ar, ar5, ar6, ar7, ar8, ar9, sep="\n")

ar.shape
ar.ndim
ar7.shape
ar7.ndim
ar8.shape
ar8.ndim
