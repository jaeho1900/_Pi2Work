# =====================
# 데이터 분석
# =====================

# --------------------
# 사용자 정의 함수
# --------------------

# # 매개변수가 없는 사용자 정의 함수
def pair_gugudan():
    for x in range(2, 10, 2):
        for y in range(1, 10):
            print(x, 'x', y, '=', x * y, end='\t')
        print(end='\n')

pair_gugudan()

# # 매개변수가 있는 사용자 정의 함수
def show_list_element(ani):
    for i in ani:
        print(i)

animals = ['사자', '늑대', '호랑이']
show_list_element(animals)

# # 리턴값이 있는 사용자 정의 함수
def my_func_rtn(x, y):
    return x - y

result = my_func_rtn(5, 3)
my_func(result, 3)


# --------------------
# 내장 함수
# --------------------

# >>> dir(): 해당 객체가 가지고 있는 변수와 함수를 반환
# 객체의 속한 변수와 함수는 .을 찍어서 호출하여 사용함
dir([1, 2, 3])

dir([1, 2, 3]).clear()        

# >>> enumerate(): 순서있는 자료형(리스트, 튜플, 문자열 등)을 인자로 주면 인덱스와 값을 함께 반환
lst = ['lion', 'tiger', 'bear', 'hippo']

for i, lstName in enumerate(lst):
    print(i, lstName)

# >>> eval(): 입력받은 문자열을 통해서 함수나 클래스를 동적으로 실행
eval('3 + 4')  # 7

# >>> id(): 객체의 고유 주소값 반환
id(100)

# >>> filter(): 결과가 참인 값만 리스트를 생성하여 반환
def odd(x):
    return x % 2 != 0

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list(filter(odd, lst))





# 11. input() : 프롬프트에서 사용자 입력을 받음
a = input()
# 사용자 입력을 기다려서 받아 냄
a
type(a)

b = int(input("Enter the number: "))
# 사용자 입력을 기다려서 받아 냄
b
type(b)


# 12. isinstance(인스턴스, 클래스이름) : 해당 클래스의 인스턴스 여부를 True, False로 반환
class Test: pass


a = Test()
type(a)
isinstance(a, Test)

x = list([1, 2, 3, 4, 5])
x
type(x)
isinstance(x, list)

# 13. sum() : 리스트, 튜플의 모든 요소의 합 반환
lst = [1, 2, 3, 4, 5]
tup = 6, 7, 8, 9, 10
sum(lst)
sum(tup)

# 14. zip() : 동일개수의 자료형을 묶어서 리스트로 반환, 짝이 안 맞으면 맞는 만큼만 묶어서 리스트로 반환
a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd']
list(zip(a, b))

# 15. pow() : 제곱한 값을 반환
print(2**4)
pow(2, 4)


# 16. 람다식 : 함수를 생성하는 대신 람다식으로 바로 사용
def _odd(x):
    return x % 2 != 0  # % 나머지 연산자


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list(filter(_odd, lst))

list(filter(lambda x: x % 2, lst))  # 참을 반환
list(filter(lambda x: x % 2 != 0, lst))
list(filter(lambda x: x % 2 == 0, lst))

5 / 2
5 // 2  # 몫
5 % 2   # 나머지 (1 = 5 - ((5 // 2) * 2))
divmod(5, 2)
a, b = divmod(5, 2)
print("몫은", a, "나머지는", b)

0 % 2  # 0 거짓
1 % 2  # 1 참
2 % 2  # 0 거짓
3 % 2  # 1 참
4 % 2
5 % 2
6 % 2

# 17. print 포맷팅
print("우리", "나라")
print("우리" + "나라")                      # 붙여쓰기
print("우리" + "나라" + str(10000) + "세")  # +에서는 type 맞춰야 함

name = '홍길동'
age = 100
print("나의 나이는 %d입니다" % a)
print("나의 이름은 %s입니다" % "홍길동")
print("이름은 %s, 나이는 %d입니다" % (name, age))

# 18. ' '.join(map(str, tup_list)).. : tup_list의 각 요소를 문자로 (매핑)바꾸어 ' ' 사이의 구분자로 연결된 하나의 문자열로 반환
# map() 함수로 만들어진 요소들은 받아 줄 객체(리스트나 튜플 등)가 필요함
a = 20
b = "대학수학능력시험"
c = 21
d = 13
strSentence = a, '회', b, '만점자 총', c, '명, 재수생 만점자', d, '명 기록'
print(strSentence)
type(strSentence)  # 튜플

print(str(strSentence))  # str()함수로 변형하면 ()까지 문자열로 표시됨

print(a, '회', b, '만점자 총', c, '명, 재수생 만점자', d, '명 기록')
print(' '.join(map(str, strSentence)))  # map()함수는 원본을 유지하면서 새로 생성
print('/'.join(map(str, strSentence)))

# 19. f문자열
a = 20
b = "대학수학능력시험"
c = 21
d = 13
원하는결과 = '20회 대학수학능력시험 만점자 총 21명, 재수생 만점자 13명 기록'

result = str(a) + '회 ' + b + ' 만점자 총 ' + str(c) + '명, 재수생 만점자 ' + str(d) + '명 기록'
print(result)

result2 = f'{a}회 {b} 만점자 총 {c}명, 재수생 만점자 {d}명 기록'
print(result2)
type(result2)

listValue = ['인간', 100]
type(listValue)
print(f'{listValue[0]}은 이제 {listValue[1]}살 까지 살 수 있다')  # 리스트 활용하기

# print(f'{listValue[0]}은 이제 '{listValue[1]}'살 까지 살 수 있다')  # 홀따옴표 활용하기(에러)
print(f"{listValue[0]}은 이제 '{listValue[1]}'살 까지 살 수 있다")  # 홀따옴표 활용하기(외부를 쌍따옴표로 감싸기)

# f문자열 자릿수 옵션
strValue = 'KOREA'
print(f"나의 조국은 '{strValue}'입니다.")

print(f"나의 조국은 '{strValue:<15}'입니다.")
print(f"나의 조국은 '{strValue:>15}'입니다.")
print(f"나의 조국은 '{strValue:^15}'입니다.")  # 가운데 옵션 사용 중 양쪽 자릿수가 일치하지 않으면 왼쪽으로 치우쳐 처리
