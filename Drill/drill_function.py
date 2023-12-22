# =====================
# Function
# =====================

# --------------------
# 사용자 정의 함수
# --------------------

# >>> 매개변수가 없는 사용자 정의 함수
def pair_gugudan():
    for x in range(2, 10, 2):
        for y in range(1, 10):
            print(x, 'x', y, '=', x * y, end='\t')
        print(end='\n')

pair_gugudan()

# >>> 매개변수가 있는 사용자 정의 함수
def show_list_element(ani):
    for i in ani:
        print(i)

animals = ['Tiger', 'Wolf', 'Lion']
show_list_element(animals)

# >>> 리턴값이 있는 사용자 정의 함수
def my_func_rtn(x, y):
    return x - y

my_func_rtn(5, 3)

# >>> 작성 사례

# [퀴즈] 거스름돈 계산
# Q) 사용자의 거스름돈을 동전으로 계산해줄때 각 동전이 몇 개 필요한지 출력하시오
# Q1) 거스름돈은 사용자 입력으로 처리
# Q2) 1원 동전 단위까지 처리한다. 안할 경우는 예외처리하거나 절삭 처리
# Q3) 각 동전이 몇 개 필요한지 출력
# Q4) 총 동전이 몇 개 필요한지 출력
# A) 계산할 거스름돈을 입려해주세요: 1780
# 총 필요한 동전의 갯수는: 9개
# 500원: 3개, 100원: 2개, 50원: 1개, 10원: 3개, 1원: 0개

def _test():
    # ------------------------------------------------
    # 사용자 입력(거스름존) 및 정수 처리
    m = int(input("계산할 거스름돈을 입려해주세요:"))

    # 변수 선언 및 초기화
    money = m
    cnt = 0
    cnts = []

    # 각각의 동전을 리스트로 선언
    lst = [500, 100, 50, 10, 1]

    # 반복하면서 각 동전 카운트 및 총 동전 카운트 저장
    for i in lst:
        cnts.append(money // i)
        cnt += money // i
        money %= i

    # 출력
    print("총 필요한 동전의 갯수는: {0}개".format(cnt))
    print("500원: {0}개, 100원: {1}개, 50원: {2}개, 10원: {3}개, 1원: {4}개"
          .format(cnts[0], cnts[1], cnts[2], cnts[3], cnts[4]))
    # ------------------------------------------------

_test()

# [퀴즈] 앞뒤가 똑같은 문자열인지 비교?

def _test2():
    # ------------------------------
    # 사용자 입력 및 예외처리
    while (True):
        a = input("문자를 입력하세요")
        if a == '':
            print("뭐라도 입력하세요")
            continue
        else:
            break

    # 사용자가 입력한 문자열을 거꾸로 저장
    b = ''.join(reversed(a))

    # 비교
    if a == b:
        print("앞뒤가 똑같은 문자열입니다 ^_^")
    else:
        print("앞뒤가 다른 문자열입니다 ㅠ.ㅠ")
    # ------------------------------

_test2()


# --------------------
# 람다식
# --------------------

# >>> iterable 자료형에 적용
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]

list(filter(lambda x: x % 2, lst))  # filter(): 참인 결과 값만 반환
list(filter(lambda x: x % 2 != 0, lst))
list(filter(lambda x: x % 2 == 0, lst))

# >>> 함수의 인자에 적용
def my_strip(x):
    return x.strip()

a = ' UD001 - lion, UD002 - tiger , UD003 - hippo '
b = a.split(',')

c = list(map(my_strip, b))
c.sort(key=lambda x: x[8])  # 9번째 글자 기준 오름차순 정렬
print(c)


# --------------------
# 내장 함수
# --------------------

# >>> zip(): 동일 개수의 자료형을 묶어서 리스트로 반환(짝이 안 맞으면 맞는 만큼만 적용)
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd']
list(zip(a, b))

# >>> enumerate(): 리스트, 튜플, 문자열을 인자로 주면 인덱스와 값을 함께 반환
lst = ['lion', 'tiger', 'bear', 'hippo']

for i, lstName in enumerate(lst):
    print(i, lstName)

# >>> map(): iterable 객체 요소를 하나씩 지정 함수로 보냄, 결과값은 담을 그릇(리스트나 튜플) 필요
x = [1, 2, 3, 4, 5]
list(map(float, x))
tuple(map(lambda x: x**3, x))

# >>> filter(): 참인 결과 값만 리스트로 반환
def odd(x):
    return x % 2 != 0

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list(filter(odd, lst))

# >>> eval(): 입력 받은 문자열을 함수나 클래스에서 동적 실행
eval('3 + 4')  # 7

# >>> dir(): 해당 객체가 가지고 있는 변수와 함수를 반환
# 객체의 속한 메서드는 객체 뒤에서 .으로 호출하여 사용
dir([1, 2, 3])
dir([1, 2, 3]).clear()

# >>> id(): 객체의 고유 주소값 반환
id(100)

# >>> isinstance(인스턴스, 클래스명): 해당 클래스의 인스턴스 여부를 boolean 반환
x = list([1, 2, 3, 4, 5])
type(x)
isinstance(x, list)


# --------------------
# iterable 메서드
# --------------------

# >>> List Comprehention
lst = ['lion', 'tiger', 'hippo']
[i.upper() for i in lst]

# >>> Add
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

# >>> Delete
lst = ['li', 'Co', 'Ni', 'Mn', 'Al', 'Mg']

lst.pop(-1)       # pop(index): 해당 인덱스의 값을 빼면서 뺀 값을 보여줌
lst.pop()         # 인덱스가 없으면 마지막 원소에 적용
lst.remove('Mn')  # Remove(value): index 불가!!
del lst[-1]
lst.clear()

# >>> Sort
lst = 'I am a bright Man'.split()

sorted(lst)              # 원본보존 및 결과반환
lst.sort()               # 원본변경(오름차순)
lst.sort(reverse=True)   # 내림차순
lst.sort(key=len)        # 요소의 길이를 기준 정렬
lst.sort(key=str.lower)  # 알파벳 기준 정렬

# >>> Reverse
lst = [4, 5, 1, 3, 2, 6]

reversed(lst)  # 원본보존 및 결과반환
lst.reverse()  # 원본변경

# >>> Count
lst = [4, 5, 1, 3, 2, 6, 1, 3, 1, 7]
lst.count(1)


# --------------------
# String
# --------------------

# >>> Print
print("우리", "나라")                        # 띄어쓰기
print("우리" + "나라")                       # 붙여쓰기
print("우리" + "나라" + str(10000) + "세")   # + 에서는 자료형 맞춰야 함
print("그는 \"J\"에게 말했다. \'가지마!\'")   # 문장 안에서 ', " 사용( \ 백슬래시)

print("23년 승률은 %d%% 입니다." % 100)      # 퍼센트 시는 2번 써 준다
print("%5.3f" % 3.141592)                   # 소수점 찍기
print("'%d년은 %s년 입니다." % (24, "갑진"))

print("{money}원 짜리는 {cnt}개 입니다." .format(money=500, cnt=2))

lst = [20, '시험', 21]
strValue = lst[1]
print(f'{lst[0]}회 {lst[1]} 만점자 총 {lst[2]}명')
print(f"'{lst[0]}'회 {lst[1]} 만점자 총 '{lst[2]}'명")  # 홀따옴표 활용하기(외부를 쌍따옴표로 감싸기)
print(f"나의 조국은 '{strValue}'입니다.")
print(f"나의 조국은 '{strValue:<15}'입니다.")
print(f"나의 조국은 '{strValue:>15}'입니다.")
print(f"나의 조국은 '{strValue:^15}'입니다.")           # 가운데정렬의 중간이 맞지 않으면 왼쪽으로 치우침

# >>> Find
test = "Welcome to Korea"

test.find("Z")              #  찾는 문자없으면 -1
test.index("Z")              # error

test.find("K")              # 11 (이하 index 매서드 동일)
test.find("K") - len(test)  # -5
test.find("e")              # 앞에서 부터 첫번째 것
test.rfind("e")             # 뒤어세 부터 첫번째 것

# >>> Replace
test = "Welcome to Korea"

test.replace('K', 'C')
test[:-5] + 'C' + test[-4:]

# >>> strip(), lstrip(), rstrip()
test = "   Welcome to Korea   "
test.strip()
test.lstrip()
test.rstrip()

# >>> lower(), upper(), capitalize()
test = "Welcome to Korea"
print(test.lower())
print(test.upper())
print(test.capitalize())  # 문장의 시작 단어만 대문자

# >>> join(): 연결자
strSentence = 20, '회 ', '시험', ' 만점자 총 ', 21, '명'
type(strSentence)  # 튜플

print(str(strSentence))  # 이슈: str()함수로 변형하면 ()까지 표시됨

print(''.join(map(str, strSentence)))
print('/'.join(reversed(list(map(str, strSentence)))))

# >>> 워드클라우드: 딕셔너리 키 정렬
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
