# ###############
# 데이터분석2
# ###############

# # list, tuple 은 다른 언어의 배열과 같은 개념이지만 파이썬에선 타입이 다른 구성원소도 묶어주고 인덱스도 부여됨

caseA = ('a')   # str
caseB = ('a',)  # tuple : 요소 1개의 튜플 만들때 주의!!

str = 'apple'

lststr = list(str)
tplstr = tuple(str)

lststr[0]   # 앞은  0부터 인덱스 시작
lststr[-1]  # 뒤는 -1부터 인덱스 시작

del lststr[2]
print(lststr)

len(str)  # length(길이)
max([1, 2, 3, 4, 5])
max(['app', 'banana', 'curcle', 'del', 'edit'])
min(['app', 'banana', 'curcle', 'del', 'edit'])
min([1, 2, 'app', 'banana', 'curcle', 'del', 'edit'])  # TypeError
min(['1', '2', 'app', 'banana', 'curcle', 'del', 'edit'])  # 숫자형 문자가 낮은 값을 가짐

print(lststr)
lststr = lststr + ['popcon', 'cidar']  # add
print(lststr)
lststr[-1] = 'pull'  # alteration
print(lststr)

newtpl = tplstr[1:] + (5, 6, 7)            # 튜플끼리 작업
tplstr = tuple(list(tplstr) + ['m', 'o'])  # 튜플+리스트 작업은 리스트로 만들어 작업 후 변환

# 주의!! 인덱스[-1:] 은 -1 부터 시작해서 왼쪽으로 가는 것이 아님,(오른쪽으로 감)
tup = 'a', 'b', 'c', 1, 2, 3
print(tup[-1:])
print(tup[-4:])
print(tup[-6:-3])  # 마이너스 인덱스의 구간 미자막은 자신을 포함
print(tup[0:3])    # 플러스 인덱스의 구간 마지막은 자신을 미포함

# upper() 메서드 : 몽땅 대문자로 변환
strTest = "i lOVE koRea."
print(strTest.upper())

# lower() 메서드 : 몽땅 소문자로 변환
print(strTest.lower())

# capitalize() 메서드 : 문자열의 첫요소는 대문자로 나머지는 소문자로 변환
print(strTest.capitalize())

# 리스트에는 upper() 등 메서드가 없다
lstTest = ['lion', 'tiger', 'hippo']
lstTest.upper()

for i in lstTest:
    print(i.upper(), end=' ~  ')  # 가로 출력

# List Comprehention
[i.upper() for i in lstTest]

# Append() : 리스트 추가 메서드
lstTest2 = []
for i in lstTest:
    lstTest2.append(i.upper())
print(lstTest2)

# Clear() 메서드
lstTest2.clear()
print(lstTest2)

# Extend() 메서드
a = [1, 2, 3]
b = ['a', 'b', 'c']
a.extend(b)
print(a)
print(a + b)

# Insert(넣을위치인덱스, 넣을값) 메서드
a.insert(2, 'kpop')   # 다른 메서드와 사용방법이 상이!!
a.insert(-2, 'jpop')  # -인덱스의 경우 -인덱스다음에 삽입됨!!

# Remove(원소값) 메서드, 주의 인덱스값 아님!!
print(a)
a.remove('kpop')  # 인덱스 적용 불가

# pop(index) 메서드: 리스트에서 인덱스의 값을 빼면서 뺀 값을 보여줌(확인시켜줌)
print(a)
a.pop(3)
a.pop(-1)
a.pop()  # 인덱스번호를 않쓰면 마지막원소에 적용
del a[-1]

# sort()
lst = [4, 5, 1, 3, 2, 6]
lst.sort()               # 오름차순
lst.sort(reverse=True)   # 내림차순
print(lst)

strTest = "I am a python programmer"
str1 = strTest.split()   # 문자열을 잘라서 리스트로 생성
str1.sort(key=len)        # 요소의 길이를 기준 정렬
str1.sort(key=str.lower)  # 알파벳 기준 정렬

# reverse() : 순서 뒤집기
lst.reverse()  # 내림차순 아님!!, 원자료의 순서를 뒤집는 것임
print(lst)

# count() 메서드: 목록의 특정 item 갯수 반환
lst = [4, 5, 1, 3, 2, 6, 1, 3, 1, 7]
lst.count(1)

# 딕셔너리 활용
cnts = dict()
for i in lst:
    if i not in cnts:
        cnts[i] = 1
    else:
        cnts[i] += 1
print(cnts)
print(cnts.keys())
print(cnts.values())
print(cnts.items())

for k, v in cnts.items():
    print(k, '숫자의 발생 빈도 수 ---->', v)

# map() 함수 : iterable 객체의 요소 하나하나를 특정 함수로 보내서 변환
# map() 함수로 생성된 요소들은 담아줄 그릇(리스트나 튜플 등)이 필요함
x = [1, 2, 3, 4, 5]
list(map(float, x))

tuple(map(pow, x))  # pow()함수는 매개변수가 2개가 필요하므로 에러 발생
tuple(map(pow, x, x))


def my_pow(x):
    return x**2


tuple(map(my_pow, x))

tuple(map(lambda x: x**3, x))

# (문제) 사용자가 입력한 6개의 정수를 입력 받아 중복되는 숫자를 제외하고 출력하시오?
# map()함수와 input()함수를 모두 사용하시오
# 여러 개의 정수 입력시 split()함수를 사용하시오
# 중복처리와 기본적인 예외처리를 프로그램 하시오

# ==========
# 개념

# 입력 받은 문자열을 공백 기준으로 분리
x = input('Please.. enter 6 numbers : ').split()

# 정수로 바꾸기(초보)
for i in range(len(x)):
    x[i] = int(x[i])

print(x)


# ==========
# 프로그래밍
def _test():
    # ---------------------------------------------
    rst = []  # 중복체크용 변수
    x = list(map(int, input('Please.. enter 6 numbers : ').split()))

    if len(x) != 6:
        print('숫자 6개를 입력해주세요. 스페이스바로 공백을 띄어주세요!', x)
        return  # 함수 종료 !!

    for i in range(len(x)):
        if x[i] not in rst:
            rst.append(x[i])

    return rst
    # ---------------------------------------------


_test()
