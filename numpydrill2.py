# --------------------
# # 넘파이 자료형
# --------------------
# i  integer(int8 은 -128~127)
# u  unsigned integer(-부호가 없는 즉 0을 포함한 양수만, uint8 은 0~255, -1은 255를 -2는 254를 대체)
# f  single precision float
# d  double precision float
# b  bool
# D  complex(실수와 허수로 구성된 복소수)
# S  string
# U  unicode

# >>> 자료형 이해
import numpy as np
ar1 = np.array([1, 2, 3, 4, 255, 256, -1], dtype=np.uint8)  # 넘치면 0부터 다시 순환, -는 뒤부터 순환
ar1

ar1 = np.array([True, False])
ar1.dtype

# >>> 자료형 지정
ar2 = np.array([1, 2, 3, 4, 5], dtype=np.int64)
ar2.dtype

ar3 = np.arange(10, dtype=np.uint8)
ar3 = np.arange(10, dtype='uint8')
ar3 = np.arange(10, dtype='<u1')  # <리틀엔디언은 디폴트값
ar3 = np.arange(10, dtype='u1')  # u 뒤의 숫자는 바이트(8비트) 의미: 1x8
ar3.dtype

# 직접 타입 지정
x = np.float32([1, 2, 4])
x.dtype

# int_ vs int: int32 약칭으로 int 가 아님 주의!!
a = np.int([1, 2, 4])   # Error
a = np.int_([1, 2, 4])  # int32 약칭
a.dtype

x = np.float_([1, 2, 4])  # float64 약칭
x.dtype

# >>> dtype: 자료형 확인
ar = np.array([1, 2, 3.5, 4, 5])
ar
ar.dtype

# str: 자료형의 문자형 확인
x = np.dtype('float64')
x       # dtype('float64')
x.type  # numpy.float64
x.str   # '<f8': < 리틀엔디언저장방식 float 8 x 8,  참고.> 빅엔디언저장방식(중요한 것을 먼저 저장)

# issubdtype: 자료형을 확인하여 True/False 반환
import numpy as np
ar = np.arange(10, dtype=np.float32)
ar

np.issubdtype(ar.dtype, np.integer)  # ar 의 타입이 정수형인가? False
np.issubdtype(ar.dtype, np.floating)
np.issubdtype(ar.dtype, np.float64)

# >>> astype: 데이터 자료형 변환
ar = ar.astype(np.float64)
ar.dtype
ar = ar.astype(int)
ar.dtype

# >>> View: 원본의 일부 또는 전체를 참조(메모리 상의 실제값이 아님)
import numpy as np
ar30 = np.arange(1, 31).reshape(5, 6)
ar30

a = ar30[-1][2:-1]  # a 사본값(?)을 변경했는데 원본값이 변경됨 !!
a[-1] = 0            # a 는 view 개념
ar30

# >>> [][]방법으로 인덱싱: 파이썬 공통 방식
ar30[0]
ar30[2]
ar30[-1]
ar30[4][4]
ar30[1][1:]

# >>> 넘파이 고유의 인덱싱 방식: 빠르다
ar30[1, 1:]

# >>> 행기준 인덱싱
ar = np.arange(10)
ar

ar[4:7]
ar[:]

# 범위로 지정된 요소값 변경
ar[4:7] = 0
ar

# 2차원 배열에서는: 1차원 배열과는 달리 좌우로 행, 열 분리
import numpy as np
ar5x5 = np.arange(1, 26).reshape(5, 5)
ar5x5

# 3행(16~20) 인덱스만 출력?
ar5x5[3, :]  # 3행의 모든 값
ar5x5[3,]    # ar[:] = ar
print(ar5x5[3, :])

# 24를 출력?
ar5x5[4, 3]

# 17, 18, 19를 출력?
ar5x5[3, 1:4]

# 2행만 출력?
ar5x5[-3]
ar5x5[2]
ar5x5[2, :]
ar5x5[2,]    # 1차원반환: array([11, 12, 13, 14, 15])
ar5x5[2:3]   # 2차원반환: array([[11, 12, 13, 14, 15]])
ar5x5[2:3].ndim

# 2~4행을 출력?
ar5x5[2:5]
ar5x5[2:]

# >>> 열기준 인덱싱
import numpy as np
ar5x5 = np.arange(1, 26).reshape(5, 5)
ar5x5

# 각 행의 2열값만 출력?
ar5x5[:, 2]

# 0~2열만 출력?
ar5x5[:, :3]

# 가운데열만 출력?
ar5x5[:, 1:-1]
ar5x5[:, 3:]

# 2,3,4,7,8,9 값을 0으로 채우기?
ar5x5[:2, 1:4] = 0

# 짝수행만 출력?
import numpy as np
ar30 = np.arange(1, 31).reshape(5, 6)
ar30

for i in range(ar30.shape[0]):
    if i % 2 == 0:
        print(ar30[i])

# 짝수열만 출력?
for i in range(ar30.shape[0]):
    for j in range(ar30.shape[1]):
        if j % 2 == 0:
            print(ar30[i, j], end=' ')
    print()

# >>> 넘파이 [스타트행:라스트행:스텝] 출력?
ar30[::2]
ar30[::3]
ar30[:3:3]
ar30[1::2]
ar30[-1::-1]
ar30[-1:-6:-2]
