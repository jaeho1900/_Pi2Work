# >>> 넘파이 indexing, slicing
a = np.arange(9)
a[4:8]
a[5:-1]
a[1:3:2]  # 시작도 포함 !!
a[3:8:2]

b = np.arange(1, 10).reshape(3, 3)
b[0]
b[1]
b[2]
b[0][1]
b[2][2]
b[0:1]
b[0:2]
b[0:3]
b[0:-1]
b[:, 1:]
b[:1, :2]
b[1:2, 1:2]

c = np.arange(1, 26).reshape(5, 5)
c[::2, ::2]
c[:3, 1:3]
c[:3][1:3]  # []+[]는 결과가 다름(행열개념이 아니다) !!

d = np.arange(1, 10).reshape(3, 3)
d[2, 1]    # 인덱싱
d[1:2]     # 슬라이싱
d[:-1]
d[:-1, :]  # 다중 슬라이싱
d[:-1, :2]
d[1:, :-1]

# >>> View vs Copy
# 넘파이에서 배열의 인덱싱/슬라이싱 결과는 뷰(View)로 원본을 변경한다
# 넘파이에서 배열 결과를 복사하고 싶다면 copy()메서드를 사용한다
a = np.arange(10)
a1 = a[:5]
a1
a1[:2] = 100
a

a = np.arange(10)
a1 = a[:5].copy()
a1
a1[:2] = 100
a
a1

# >>> 3D array
# 3차원 배열 생성
import numpy as np
a = np.array([[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]],
             [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]])
a = np.arange(24).reshape(2, 3, 4)  # (깊이, 행, 열)
a.shape

# 3차원 배열 인덱싱
a = np.arange(27).reshape(3, 3, 3)
a
a[0]
a[0, 2]
a[0, 2, 2]

# 3차원 배열 슬라이싱
a[-1, -1, :2]

# 문제) 2차원 배열과 3차원 배열을 각각 arange()로 생성한 후 각 요소들의
#      값을 for문으로 출력하시오? 2차원배열은(1~25), 3차원요소수는 60개
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

# >>> 넘파이 Append() axis=0,1
# 파이썬
a = []
a.append([1, 2])
a.append([3, 4])
a  # [[1, 2], [3, 4]]: 2차원 배열로 추가

# 넘파이
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

# >>> empty: 초기화가 안된 빈배열 생성(그래서 속도가 빠름)
a = np.empty([3, 3])
a.dtype

z = np.empty([3, 3], dtype=int)
z
z.shape
z1 = np.empty(z, dtype=int)       # error
z1 = np.empty_like(z, dtype=int)  # z와 동일한 형태의 초기화안된 배열 생성

ar = np.ones((5, 5), dtype=int)  # 1로 초기화된 배열 생성
ar1 = np.zeros((5, 5), int)      # 0으로 초기화된 배열 생성
