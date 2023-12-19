# 주요함수 사용법: 거스름돈 계산(1)
# Q) 사용자의 거스름돈을 동전으로 계산해줄때 각 동전이 몇 개 필요한지 출력하시오
# Q1) 거스름돈은 사용자 입력으로 처리
# Q2) 1원 동전 단위까지 처리한다. 안할 경우는 예외처리하거나 절삭 처리
# Q3) 각 동전이 몇 개 필요한지 출력
# Q4) 총 동전이 몇 개 필요한지 출력
# A) 계산할 거스름돈을 입려해주세요: 1780
# 총 필요한 동전의 갯수는: 9개
# 500원: 3개, 100원: 2개, 50원: 1개, 10원: 3개, 1원: 0개


def _test():
    # jaeho------------------------------------------------
    x = int(input("계산할 거스름돈을 입려해주세요:"))

    k500, x = divmod(x, 500)
    k100, x = divmod(x, 100)
    k50, x = divmod(x, 50)
    k10, x = divmod(x, 10)
    k1, x = divmod(x, 1)

    print("총 필요한 동전의 갯수는: %d개" % (k500 + k100 + k50 + k10 + k1))
    print("500원: %d개, 100원: %d개, 50원: %d개, 10원: %d개, 1원: %d개" % (k500, k100, k50, k10, k1))
    # ------------------------------------------------


_test()


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

# -----------------
# 문자열 함수
# -----------------

# ', " 동시에 쓰기
# \(백슬래시) 사용
test1 = "그는 나에게 말했다. \"거기 가지마!\""
test2 = '그는 나에게 말했다. \'거기 가지마!\''

# """ 3개
test = """
동해물과 백두산이 마르고 닿도록
하느님이 보우하사 우리나라 만세
"""
test
print(test)

# 문자열 바꾸기
test = "Welcome to Korea"
test[-5] = 'C'  # error
test = test[:-5] + 'C' + test[-4:]

# 문자열 포멧
test = "%d 년은 %s 년 입니다." % (2023, "계묘년")
test

# 퍼센트 표시는 2번 써 준다
test = "올 해 승률은 %d%% 입니다." % 100
test

# 소수점 찍기
print("%5.3f" % 3.141592)

# format 함수 사용시 이름 지정하기
print("{money}원 짜리는 {cnt}개 입니다.".format(money=500, cnt=2))

# find: 위치 알림
test = "Welcome to Korea"
test.find("K")              # 11
test.find("K") - len(test)  # -5
test.find("Z")              # -1 없는 문자를 찾아도 -1 반환
test.find("e")     # 앞에서 부터 첫번째
test.rfind("e")    # 뒤어세 부터 첫번째

# index: 위치 알림
test = "Welcome to Korea"
test.index("K")
test.index("Z")            # 없는 문자 찾으면 error 반환
test.index("e")    # 앞에서 부터 첫번째
test.rindex("e")   # 뒤어세 부터 첫번째

# lower, upper, capitalize
test = "Welcome to Korea"
print(test.lower())
print(test.upper())
print(test.capitalize())  # 문장의 맨앞단어만 대문자

# strip, lstrip, rstrip
test = "   Welcome to Korea   "
test.strip()
test.lstrip()
test.rstrip()

# replace
test = "Welcome to Korea"
test.replace('K', 'C')

# 주소
a = "Korea"
b = "Korea"
c = "Korea"
id("Korea")  # 모두 같은 값을 지닌 주소를 가리킴
id(a)
id(b)
id(c)

a = "Corea"
id(a)

# reverse(), reversed() : 요소들의 순서를 뒤집기
a = [9, 2, 8, 5, 7]
a.reverse()                 # 원본을 변경함
print(a)

print(list(reversed(a)))    # 원본 변경없이 새로운 리스트 생성

# join : 연결자
test = "seoul"
'*'.join(test)
'*'.join(reversed(test))


# [퀴즈]앞뒤가 똑같은 문자열인지 비교하는 함수
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
    b = ''.join(reversed(a))      # 새로 생성된 리스트를 문자열로 묶음

    # 비교
    if a == b:
        print("앞뒤가 똑같은 문자열입니다 ^_^")
    else:
        print("앞뒤가 다른 문자열입니다 ㅠ.ㅠ")
    # ------------------------------


_test2()

# sort: 원본변형, sorted: 원본보존
a = 'I am a ion Man'
b = a.split()
sorted(b)
b.sort()              # 오름차순
b.sort(reverse=True)  # 내림차순

# 딕셔너리 키 정렬
str1 = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
 when an unknown printer took a galley of type and scrambled it to make a type
 specimen book. It has survived not only five centuries, but also the leap into
 electronic typesetting, remaining essentially unchanged. It was popularised in
 the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
 and more recently with desktop publishing software like Aldus PageMaker including
 versions of Lorem Ipsum."""
str1.count('text')

str2 = str1.split()
cnts = dict()

for i in str2:
    if i not in cnts:
        cnts[i] = 1
    else:
        cnts[i] += 1

print(cnts)

cnts1 = sorted(cnts.items())  # 키 값으로 딕셔너리 정렬되어 리스트!!로 반환

for k, v in dict(cnts1).items():  # 리스트를 딕셔너리로 변환
    print(k, '\t', v)

# 람다 사용하여 정렬하기 !!
# 람다식: 한 줄의 함수식(람다선언 인자 : 함수식)

# 람다식 예제1
a = 'd e s i g n w o r l a'
b = a.split()
print(b)

b.sort(key=len)
print(b)  # 길이가 정렬 기준으로 바뀌지 않음

b.sort(key=lambda x: x[0])  # key 조건을 람다로 수정
print(b)

b.sort(key=lambda x: x[0], reverse=True)
print(b)

# 람다식 예제2
a = 'UD001 - lion, UD002 - tiger, UD003 - hippo'
b = a.split(',')


def my_strip(x):
    return x.strip()


b = list(map(my_strip, a.split(',')))
b.sort(key=lambda x: x[8])
