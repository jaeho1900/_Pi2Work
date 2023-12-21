# =====================
# Numpy
# =====================

# --------------------
# 배열 생성 및 주요 함수
# --------------------

import numpy as np

# >>> 1차원 배열 생성
np.array([1, 2, 3, 4, 5])

# >>> 2차원 배열 생성
arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(arr1)  # 넘파이배열에서는 , 가 생략됨

# >>> 정보 확인
arr1.shape  # 배열 형태: (3, 4) 큰방 3개에 각 방마다 4개씩 들어있다
len(arr1)   # 길이(큰방의 갯수)
arr1.size   # 원소 갯수
arr1.ndim   # 차원 확인

# >>> 3차원 배열 생성
a = np.array([[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]],
             [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])
a.shape

b = np.arange(24).reshape(2, 3, 4)  # (깊이, 행, 열)
b.shape

# >>> 특수 배열
np.zeros((3, 4))   # 모든 요소를 0으로
np.ones((3, 4))    # 모든 요소를 1로
np.eye(4)          # 단위행렬: 대각선은 1, 나머지는 0

# >>> 빈배열: 초기화가 안된 빈배열 생성(그래서 속도가 빠름)
z = np.empty([3, 3], dtype=float)
z
z.dtype

z1 = np.empty(z, dtype=int)       # error
z1 = np.empty_like(z, dtype=int)  # z와 동일한 형태의 초기화안된 배열 생성
z1.dtype

# >>> arange() 함수: 파이썬의 range
np.arange(10)
np.arange(1, 20, 2)
np.arange(1, 10, 0.5)  # 간격이 0.5이면 10-0.5(간격)까지로 범위가 변경되어 9.5도 출력!!

# >>> reshape() 함수: 배열 구조 변경
ar = np.arange(12).reshape(3, 4)

# reshape(-1, n[정수]): 열 기준으로 변경(요소보다 배열을 중시)
ar.reshape(-1, 1)  # (12, 1) 원소의 갯수를 모르거나 변동일때 유용
ar.reshape(-1, 2)  # ( 6, 2)

# reshape(n[정수, -1]): 행 기준으로 변경
ar.reshape(2, -1)  # (2, 6)
ar.reshape(4, -1)  # (4, 3)

# reshape(-1) : 행 기준으로 1차원 배열로 변경
ar.reshape(-1)     # (12), (12,), (1, -1), (1, 12)

# >>> 파이썬 append()
a = []
a.append([1, 2])
a.append([3, 4])
a  # [[1, 2], [3, 4]]: 2차원 배열로 추가

# >>> 넘파이 append(axis=0,1)
a = np.array([])
a = np.append(a, [1, 2])
a = np.append(a, [3, 4])
a  # array([1., 2., 3., 4.]): 1차원 배열로 추가

artest = np.ones((5, 5), int)
artest
artest = np.append(artest, np.array([[3, 4, 5, 6, 7]]), axis=0)  # axis옵션 주의 !!
artest

arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
arr1
addcol = np.zeros((2, 1))
addcol
np.append(arr1, addcol, axis=1)

# >>> View vs Copy()

# View: 넘파이에서 배열의 인덱싱/슬라이싱 결과는 View(원본 참조)
ar30 = np.arange(1, 31).reshape(5, 6)
a = ar30[-1][2:-1]
a[-1] = 0            # a 는 view
ar30                 # 슬라이싱한 a 사본을 변경했는데 ar30의 값이 변경됨 !!

# 넘파이의 may_share_memory()사용하여 메모리 공유 여부를 확인
# 뷰에 새로운 원소가 추가되면 원본에서 독립하여 분리됨 !!
np.may_share_memory(ar30, a)

# Copy: 넘파이에서 배열 결과를 복사하고 싶다면 copy()메서드를 사용
a = np.arange(10)
a1 = a[:5].copy()
a1
a1[:2] = 100
a1
a


# --------------------
# 인덱싱 & 슬라이싱
# --------------------

import numpy as np

ar30 = np.arange(1, 31).reshape(5, 6)
print(ar30)

# >>> 파이썬 공통 방식([][]) 인덱싱
ar30[0]
ar30[2]
ar30[-1]
ar30[-1:]      # [-1:] 은 -1부터 시작해서 정방향으로 가는 것이 아님 !!(역방향 아님)
ar30[-3:]
ar30[4][4]
ar30[1][1:]
ar30[:3][1:3]  # []+[] 결과는 다중 슬라이싱과 다름(행렬개념이 아니다) !!

# >>> 넘파이 인덱싱: 빠르다
ar30[1, 1:]
ar30[2,]    # 1차원 반환
ar30[2:3]   # 2차원 반환
ar30[:, 1:-1]
ar30[:, 3:]
ar30[:3, 1:3]  # 다중 슬라이싱(행렬개념)

# >>> 넘파이 슬라이싱 [스타트행:라스트행:스텝]
ar30[::2]
ar30[::3]
ar30[:3:3]
ar30[1::2]  # 시작도 포함 !!
ar30[-1::-1]
ar30[-1:-6:-2]

# >>> 팬시 색인: 배열(리스트)을 색인에 사용, 기존(다차원) 배열의 형태를 유지하며 반환
# 팬시 색인은 메모리 공유를 하지 않는다(뷰가 아님)
ar30[[0]]      # array([[1, 2, 3, 4, 5, 6]])
ar30[[0, -1]]  # array([[1, 2, 3, 4, 5, 6], [25, 26, 27, 28, 29, 30]])

# >>> 넘파이 ix_함수를 이용한 팬시 색인: 지정된 인덱스 값을 반환하여 직관적임
ar30[np.ix_([2,3],[2,3])]

# >>> 3차원 배열 인덱싱과 슬라이싱

# 3차원 배열 인덱싱
a = np.arange(27).reshape(3, 3, 3)
a
a[0]
a[0, 2]
a[0, 2, 2]

# 3차원 배열 슬라이싱
a[-1, -1, :2]


# --------------------
# 행렬 계산
# --------------------

import numpy as np

ar1 = np.eye(2)
ar2 = np.array([[3, 4], [5, 6]])

# >>> 일반곱셈: 같은 위치의 요소끼리만 수식 적용
ar1 * ar2

# >>> 행렬의 곱셈
np.dot(ar1, ar2)

# >>> Broadcasting 확장: 스칼라값, 한쪽배열크기1, 동일차원, 동일축길이인 경우에 적용

# 스칼라(상수)값은 넘파이 내부에서 np.array([3,3,3,3,3])로 확장되어 계산
a = np.array([1, 2, 3, 4, 5])
a + 3

# 열 갯수가 같으면 행으로 자동 확장되어 계산
a = np.ones((4, 4))
b = np.arange(4)
a + b

# 상대 배열 형상에 맞춰 각각 열과 행을 확장 후 계산됨
a = np.arange(5).reshape(5, 1)
b = np.arange(3)
a + b

# 비교연산(==, !=, >, <, >=, <=)
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [1, 5, 2]])
c = np.array([7, 8, 9])
d = np.array([7, 8])
e = np.array([1, 2, 3, 4])

a == b
a == c  # c가 브로드케스팅됨
b == c
b != c
b >= c


# --------------------
# 넘파이 자료형
# --------------------
# i  integer(int8 은 -128~127)
# u  unsigned integer(-부호가 없는 즉 0을 포함한 양수만, uint8 은 0~255, -1은 255를 -2는 254를 대체)
# f  single precision float
# d  double precision float
# b  bool
# D  complex(실수와 허수로 구성된 복소수)
# S  string
# U  unicode

import numpy as np

# >>> 넘파이는 모든 요소를 동일한 타입으로 처리 !!
arr = np.array([1, 2, 3, 'a', 'b', 'c'])
arr[0]        # '1'
type(arr[0])  # 숫자와 문자가 혼재되어 있으면 모두 문자 타입으로 통일

# >>> 자료형 이해
ar1 = np.array([1, 2, 3, 4, 255, 256, -1], dtype=np.uint8)  # 넘치면 0부터 다시 순환, -는 뒤부터 순환
ar1

ar1 = np.array([True, False])
ar1.dtype

# >>> 자료형 지정
np.array([1, 2, 3, 4, 5], dtype=np.int64)
np.arange(10, dtype=np.uint8)
np.arange(10, dtype='uint8')
np.arange(10, dtype='u1')   # u 뒤의 숫자는 바이트(8비트) 의미: 1x8
np.arange(10, dtype='<u1')  # <리틀엔디언은 디폴트값

# 직접 타입 지정
np.float32([1, 2, 4])

# int_ : int32 약칭으로 int 가 아님 주의!!
x = np.int_([1, 2, 4])    # int32 약칭
x.dtype

x = np.float_([1, 2, 4])  # float64 약칭
x.dtype

# >>> dtype: 자료형 확인
ar = np.array([1, 2, 3.5, 4, 5])
ar.dtype

# str: 자료형의 문자형 확인
x = np.dtype('float64')
x       # dtype('float64')
x.type  # numpy.float64
x.str   # '<f8': < 리틀엔디언저장방식 float 8 x 8,  참고.> 빅엔디언저장방식(중요한 것을 먼저 저장)

# issubdtype: 자료형을 확인하여 True/False 반환
ar = np.arange(10, dtype=np.float32)
np.issubdtype(ar.dtype, np.integer)
np.issubdtype(ar.dtype, np.float64)
np.issubdtype(ar.dtype, np.floating)

# >>> astype: 데이터 자료형 변환
ar = ar.astype(np.float64)
ar.dtype

ar = ar.astype(int)
ar.dtype


# --------------------
# 실전 코드
# --------------------

# 문제) 2차원 배열과 3차원 배열을 각각 arange()로 생성한 후 각 요소들의 값을 for문으로 출력하시오?
import numpy as np

a = np.arange(1, 26).reshape(5, 5)
for x_ in range(0, 5):
    for y_ in range(0, 5):
        print(a[x_, y_], end='\t')
    print()

b = np.arange(1, 61).reshape(3, 4, 5)
for n_ in range(0, 3):
    for x_ in range(0, 4):
        for y_ in range(0, 5):
            print(b[n_, x_, y_], end='\t')
        print()
    print()
