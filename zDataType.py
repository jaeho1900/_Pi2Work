# =====================
# iterable 함수
# =====================

name = ['merona', 'gugucon', 'bibibig']
price = [500, 1000, 600, 700]
lst = ['lion', 'tiger', 'hippo']
nlst = [0, 1, 2, 3, 4, 5]

# zip 함수 : 두 개 이상의 iterable객체를 인자로 받아서 같은 위치에 있는 요소들끼리 묶어 튜플로 반환(총길이는 가장 짧은 객체의 길이를 따름) -----
list(zip(name, price))

# Comprehention : 파이썬에서 for문을 사용하여 iterable 객체를 생성 -----
[v*2 for k, v in zip(name, price)]
[i.upper() for i in lst]

{k:v*2 for k, v in zip(name, price) if v < 1000}
{k:v/2 for k, v in zip(name, price) if k != 'merona'}

# enumerate 함수 : iterable객체의 각 요소의 인덱스와 요소를 튜플로 반환 -----
[(i, x) for i, x in enumerate(lst) if 'o' in x]
[(i, x) for i, x in enumerate(filter(lambda x: x % 2 == 0, nlst))]

# filter(함수, iterable객체) : 결과가 True인 값만 반환 -----
list(filter(lambda x: x % 2, nlst))        # [1, 3, 5]
list(filter(lambda x: x % 2 != 0, nlst))   # [1, 3, 5]

# map(함수, iterable객체) : iterable객체의 각 요소에 함수를 적용, 결과값은 담을 그릇(리스트나 튜플) 필요 -----
list(map(lambda x: x % 2, nlst))           # [0, 1, 0, 1, 0, 1]
list(map(lambda x: x % 2 != 0, nlst))      # [False, True, False, True, False, True]


# =====================
# List 매서드 : 원본 변경
# =====================

# >>> Count, Find -----

lst = [None, 'lily', 'Man', 'Mn', 'Alarm', 'Mg', 'Mn']

# len() : 전체 요소의 갯수 (NaN 포함) -----
len(lst)

# count() : 검색 요소의 갯수 -----
lst.count('Mn')

# index() : 검색 요소와 일치하는 첫번째 인덱스를 반환 -----
lst.index('Mn')

# >>> Access : 리스트의 인덱싱과 슬라이싱 -----

# 인덱싱        : 변수명[인덱스번호]
# 슬라이싱(구간) : 변수명[start:end:step]
lst[3]
lst[3::2]
lst[3, 4]  # error, integers or slices 만 허용

# >>> 참조 -----

'Man' in lst
'Man' not in lst

# >>> Add -----

lst1 = [1, 2, 3]; lst2 = [1, 2, 3]; lst3 = [1, 2, 3]
lst4 = ('lion', 'tiger', 'hippo')

# insert(삽입위치인덱스, 값) : 지정된 인덱스 위치에 요소를 삽입
lst1.insert(0, [10, 20])       # [[10, 20], 1, 2, 3]
lst1.insert(-1, 100)           # [[10, 20], 1, 2, 100, 3]          -2번째 추가
lst1.insert(len(lst1), 'end')  # [[10, 20], 1, 2, 100, 3, 'end']   -1번째 추가

# append() : 리스트의 끝에 요소를 추가
lst2.append(4)         # [1, 2, 3, 4]
lst2.append([5, 6])    # [1, 2, 3, 4, [5, 6]]

# extend() : 리스트의 끝에 iterable 요소를 하나씩 꺼내어 추가
# lst3.extend(4)       # error: iterable 자료형만 입력 가능
lst3.extend([4])       # [1, 2, 3, 4]
lst3.extend([5, 6])    # [1, 2, 3, 4, 5, 6]
lst3.extend([[5, 6]])  # [1, 2, 3, 4, 5, 6, [5, 6]]

# + 연산자
lst1 + ['cow']
lst1 + list(lst2)      # 튜플은 리스트로 변환 후 작업

# >>> Delete -----

lst = ['li', 'Co', 'Ni', 'Mn', 'Al', 'Mg', 'Mn']

# remove(value) : 검색된 첫번째 항목을 삭제
lst.remove('Mn')

# pop(index) : 지정된 인덱스의 항목을 반환하며 삭제
lst.pop()      # 인덱스가 없으면 마지막 원소에 적용
lst.pop(-1)

# del 함수
del lst[-1]

# clear() : 리스트 비우기
lst.clear()


# =====================
# Dictionary
# =====================

# >>> Make  : key는 문자형이어야 함 -----

# dict() 함수
name = ['merona', 'gugucon', 'bibibig']
price = [500, 1000, 600]

dict(zip(name, price))
dict(korea = name, japan = 'tokyo')

# 일반 방법
aa = {1: 'one', 2: [1, 2, 3], '인사': '방가'}
bb = {'korea':'seoul', 'japan':'tokyo'}

# >>> Access : 순서가 없기때문에 인덱싱이나 슬라이싱을 사용할 수 없음 -----

aa.keys()
aa.values()
aa.items()

# get() : key를 검색해서 요소를 가져오며, 찾는게 없을 경우 default 값을 반환 -----
# Series.get(key, default=None)      # Series에서는 key로 행의 레이블(index)을 받는다
# DataFrame.get(key, default=None)   # DataFrame에서는 key로 열의 레이블(columns)을 받는다
aa['gender']             # 검색 key가 없으면 KeyError, 프로세스 중단
aa.get('gender')         # 검색 key가 없으면 None, 다음 프로세스 진행
aa.get('gender', 'man')  # 검색 key가 없을때 지정값 반환

# >>> Replace -----

aa[1] = 'bye'

# >>> Add -----

aa[6] = 'six'
aa.update(bb)

# >>> Delete -----

del aa['인사']
aa.pop(2)
aa.clear()


# =====================
# String
# =====================

# >>> 문자열 포맷팅 -----

# separate(사이 구분자)
s1 = "First str"
s2 = "Second str"
print(s1, s2, sep='\n그리고\t')  # \t tap, \n 줄바꿈

# end(끝 구분자)
print("First str", end='\t끝\n')    # \t tap, \n 줄바꿈
print("Second str")

# str concatenation : + , -----
print("우리", "나라")                        # 띄어쓰기
print("우리" + "나라")                       # 붙여쓰기
print("우리" + "나라" + str(10000) + "세")   # + 에서는 자료형 맞춰야 함
print("그는 \"J\"에게 말했다. \'가지마!\'")   # 문장 안에서 ', " 사용( \ 백슬래시)

# C 언어 % 포맷팅: %s(문자열), %d(정수), %f(부동소수점) -----
print("23년 승률은 %d%% 입니다." % 100)      # 퍼센트는 2번 써 준다
print("%5.3f" % 3.1415)                     # 소수점 자릿수
print("'%d년은 %s년 입니다." % (24, "갑진"))
print('%s의 투자비중은 %-15.3f%%입니다.' % ('갑진년', 3.1415))              # 좌정렬 및 자릿수 맞춤, 반올림
print('%s의 투자비중은 % 15.3f%%입니다.' % ('갑진년', 3.1415))              # 우정렬 및 자릿수 맞춤, 반올림
print('%s의 투자비중은 %015.3f%%입니다.' % ('갑진년', 3.1415), end='\n\n')  # 우정렬 및 0채움, 반올림

# str.format() 메서드 : {지정변수명또는인덱스번호:[빈공간채울문자][정렬방향<^>][+양수부호][공간수][,][.소수자릿수]} -----
a = 'america dream'; b = 3.1415
print('value is {{ {} }}'.format('%d' % b))
print('{}의 투자비중은 {}%입니다.'.format(a[8:13], '%15.2f' % b))
print('{name}의 투자비중은 {money}%입니다.'.format(name=a[8:13], money='%15.2f' % b))
print('{0}의 투자비중은 {1:<15.2f}%입니다.'.format('K씨', -1000.5))   # 좌정렬
print('{}의 투자비중은 {:^15.2f}%입니다.'.format('K씨', -1000.5))     # 가운데정렬
print('{}의 투자비중은 {:>15.2f}%입니다.'.format('K씨', -1000.5))     # 우정렬
print('{}의 투자비중은 {:0>15.2f}%입니다.'.format('K씨', -1000.5))    # 공백채우기
print('{}의 투자비중은 {:,.2f}%입니다.'.format('K씨', -1000.5))       # 천단위콤마표시
print('{1:+15,} 과 {0:+15,} 사이'.format(50000, -50000))             # 양수부호

lst = ["apple", "banana", "cherry"]
print("I like {} and {}.".format(lst[0], lst[2]))

dct = {'name': 'Alice', 'age': 30}
print("My name is {dct[name]} and I am {dct[age]} years old.".format(dct=dct))
print("My name is {name} and I am {age} years old.".format(**dct))  # 딕셔너리명 앞에 기호 ** 을 붙여 딕셔너리를 언패킹하는 방식

# f-strings (python 3.6 이후) -----
name = 'Matin'
lst = [20, '시험평균', 90.567]

print(f"5 곱하기 4는 {5 * 4}!")

print(f"{name}의 '{lst[0]}'회 {lst[1]}은 '{lst[2]}'점")  # 홀따옴표 활용하기(외부를 쌍따옴표로 감싸기)
print(f'평균은 {{ {int(lst[2])} }}')                     # {} 출력을 위해서는 두번씩 써주기

print(f"금년도 '{lst[1]:<15}'입니다.")
print(f"금년도 '{lst[1]:^15}'입니다.")         # 가운데정렬 중 글자수가 맞지 않으면 왼쪽으로 치우침
print(f"금년도 '{lst[1]:>15}'입니다.")

print(f'평균은 {lst[2]:*<+15,.2f}%입니다.')
print(f'평균은 {lst[2]:*^+15,.2f}%입니다.')
print(f'평균은 {lst[2]:*>+15,.2f}%입니다.')

dct = {'name': 'Alice', 'age': 30}
print(f"My name is {dct['name']} and I am {dct['age']} years old.")

# >>> 문자열 자리 간격 양식 -----

txt = "Welcome to Korea"
txt.ljust(50, '-')   # 총길이 50, 왼쪽정렬, 지정문자 채움
txt.rjust(50, ' ')   # 총길이 50, 오른쪽정렬, 공백 채움

# >>> 문자열 검색 -----

txt = "Welcome to Korea, King"

# len() : 전체 문자열 길이 -----
len(txt)

# str.count(substr, start, end) : 검색문자 갯수 -----
txt.count('e', 5)

# str.find(substr, start, end) : 검색문자의 첫번째 위치 인덱스 -----
txt.find("K", 15)          # 검색된 문장의 첫번째 인덱스 위치값 반환
txt.find("Z")              # 검색문자 없으면 -1 반환

# 오른쪽부터 처음 검색된 인덱스 위치값
txt.rfind("e")

# 모든 원소의 인덱스 위치 반환
[i for i, x in enumerate(txt) if x == 'e']

# 다른 데이터유형에서는 index가 사용
txt.index("K", 15)         # 검색된 문장의 첫번째 인덱스 위치값 반환
txt.index("Z")             # 검색문자 없으면 error

# str.startswith(prefix, start, end) 문자열의 시작 또는 끝 부분 일치 여부를 # boolean 반환 -----
# str.endswith(suffix, start, end)
txt.startswith('Wel')
txt.endswith('Kin', -4, -1)

# >>> Replace, Split, Join -----

txt = 'asiana air com'

# str.replace(old, new, count) : 교체 -----
print(txt.replace('a', 'A'))     # 해당 문자 전부 교체
print(txt.replace('a', 'A', 1))

# str.split(sep=None, maxsplit=-1) : 분리 -----
print(txt.split(' ', maxsplit=1))

# str.join(iterable) : 지정문자를 끼워넣기 -----
print('@'.join(txt))

# >>> 공백 또는 검색문자 삭제 -----

txt = "   Welcome to Korea   "
txt.strip()
txt.lstrip()
txt.rstrip()
txt.strip().strip('Wel')

# >>> 대소문자 변환 -----

txt = "Welcome to Korea"
print(txt.lower())
print(txt.upper())
print(txt.capitalize())

# >>> 워드클라우드: 딕셔너리 key 정렬 -----

txt = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
 when an unknown printer took a galley of type and scrambled it to make a type
 specimen book. It has survived not only five centuries, but also the leap into
 electronic typesetting, remaining essentially unchanged. It was popularised in
 the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,
 and more recently with desktop publishing software like Aldus PageMaker including
 versions of Lorem Ipsum."""

split_txt = txt.split()

cnts = dict()
for i in split_txt:
    if i not in cnts:
        cnts[i] = 1
    else:
        cnts[i] += 1

print(cnts)


# --------------------
# 정규표현식 (Regular Expression)
# --------------------

# Character classes -----
# .	                   하나의 문자(개행문자 \n을 제외한 모든 문자)
# \d	               숫자 한 자리, [0-9]와 동일
# \D	               숫자가 아닌 문자 한 자리
# \w	               문자 한 자리, 알파벳+한글+숫자+언더스코어( _ ) 중 하나의 문자. [a-zA-Z0-9_]와 동일
# \W	               알파벳+숫자+언더스코어( _ )가 아닌 문자 한 자리
# \s	               공백이나 탭 한 자리
# \S	               공백이나 탭이 아닌 문자 한 자리
# [abc]                괄호 안의 문자들 중 하나와 일치; a 또는 b 또는 c
# [^ab]                ^뒤에 있는 괄호안의 문자들 제외; [^a^b], [^(ab)]와 같음
# [a-c]	               -앞부터 뒤까지의 문자들; a 또는 b 또는 c
# [0-9]                숫자
# [a-zA-Z]             영어
# [ㄱ-ㅎ|ㅏ-ㅣ|가-힣]   한글

# Anchors -----
# ^	        문자열의 시작 패턴
# $	        문자열의 끝 패턴
# \b        단어경계(\w 와 \W 사이의 경계)
# \B        철자경계(\w와 \w 사이)

# Quantifiers & Alternation -----
# *	        앞문자가 0 or more
# +	        앞문자가 1 or more
# ?	        앞문자가 0 or 1
# {n}       앞문자가 n번 반복
# {n,}      앞문자가 n번 이상
# {n,m}     앞문자가 최소 n번이상 최대 m번 이하(붙여쓰기에 주의!!)
# a+?    	가능한한 적게 맞추기(1 if 1 or more)
# a{2,}?	가능한한 적게 맞추기(2 if 2 or more)
# ab|cd	    ab 또는 cd (순서 중요)

# Groups -----
# (abc)	      특정부분만 capturing group #1 (자동으로 그룹번호 생성)
# \1	      그룹1 표현식을 복사
# (?:abc)	  그룹에 ?:를 앞에 붙여주면, 검색결과에는 반영되나 그룹번호는 미지정

# Lookaround -----
# A(?=B)	  positive lookahead, A와 B 를 모두 충족하는 검색문자를 찾아서 A를 반환
# A(?!B)	  negative lookahead, A를 충족하는 문자 중 A와 B를 모두 충족하는 문자는 제외하고 반환
# (?<=B)A	  positive lookbehind, A와 B 를 모두 충족하는 검색문자를 찾아서 A를 반환
# (?<!B)A	  negative lookbehind, A를 충족하는 문자 중 A와 B를 모두 충족하는 문자는 제외하고 반환

# \ 사용법 -----

# '\문자열' 은 --> 짝수로만 인식
"\superman"        # \2개
"\\superman"       # \2개
"\\\superman"      # \4개
"\\\\\superman"    # \6개

# r'\문자열' 은 --> 2배수로 인식
r"\superman"        # \2개
r"\\superman"       # \4개
r"\\\superman"      # \6개

# 파이썬 엔진은 --> '\문자열', r'\문자열'에서 산정된 '\' 개수를 --> 50% 만 인식
print("\superman")    # \1개 -> \2개 -> \1개
print("\\superman")   # \2개 -> \2개 -> \1개
print(r"\\superman")  # \2개 -> \4개 -> \2개 (직관적임)

# ChatGPT 정규식 요청 프롬프트 -----

# #명령어#
# 너는 지금부터 Regex 생성기로 행동해.
# 주어진 단어를 추출하는 Regex를 작성할 것.
# 단어의 패턴을 이해하고 최대한 비슷한 구조의 다양한 단어를 추출하는 Regex로 작성해 줘.
# Regex의 동작 설명이나 예제는 작성하지 말고, Regex만 답변해.
# #단어#
# 850101-1234567
# 920305-2345678


# --------------------
# re 모듈
# --------------------

# re메서드        검색범위                           성공반환값     실패반환값
# re.match()      문자열 처음부분만                   객체 1개       None
# re.search()     문자열 처음부터 일치하는 첫번째 것   객체 1개       None
# re.findall()    문자열 처음부터 일치하는 모든 것     리스트         빈 리스트
# re.finditer()   문자열 처음부터 일치하는 모든 것     순환객체       None

# re.compile()    패턴을 컴파일(컴퓨터가 이해할 수 있는 형태로 변환)하여 정규식 객체로 반환
# re.sub()        문자열에서 패턴과 일치하는 모든 부분을 다른 문자열로 대체
# re.split()      문자열에서 패턴과 일치하면 패턴을 기준으로 리스트로 나눔

# match() 또는 search()에 적용 -----
# start():    매칭된 문자열의 시작 위치 반환
# end():      매칭된 문자열의 끝 위치 반환
# span():     매칭된 문자열의 (시작, 끝) 위치 튜플 반환
# groups():   소괄호로 패턴을 묶어서 검색
# group():    그룹핑된 그룹별로 반환

# flags : 컴파일된 패턴에서는 사용 불가 -----
# 패턴에 (?옵션)을 직접 입력(인라인 방식)
# re.I        (?i)   대소문자 불문
# re.S        (?s)   . 에 개행문자(\n) 포함
# re.M        (?m)   ^ $ 를 행별로 적용
# re.I|re.M   (?im)  복합 사용

import re

txt = '''홍길동 010-1234-5671
         이순신 010-3333-9632
         김유신 010.9999.5417
         강감찬 010 111  2222'''

# >>> re.search() : 처음부터 검색하여 패턴 일치 문자열을 하나 반환 -----

pattern = re.compile(r'(\w+)\s+(\d{3}).(\d{3,4}).+(?:\d{4})$', re.I|re.M)
# pattern = re.compile(r'(?im)(\w+)\s+(\d{3}).(\d{3,4}).+(?:\d{4})$')
result = re.search(pattern, txt)
print(result)

# 매칭객체의 위치값 -----
print(result.span())
print(result.start())
print(result.end())

# 매칭객체의 그룹값 -----
print(result.groups())  # groups() : 그룹번호가 배정된 모든 그룹값을 튜플로 반환
print(result.group())   # group()  : 매칭된 전체 문자열
print(result.group(0))  # group(0) : 매칭된 전체 문자열
print(result.group(1))  # group(1) : 매칭된 1번째 그룹의 문자열
# print(result.group(4))  # error : 그룹번호 미등록(?:)

print(pattern.sub('\\1 : \\2 - \\3 - ****', txt))
print(pattern.sub(r'\1 : \2 - \3 - ****', txt))
print(pattern.sub(r'\g<1> : \g<2> - \g<3> - ****', txt))

# >>> re.findall() : 패턴 일치되는 모든 문자열을 리스트로 반환 -----

pattern = re.compile(r'\w+\s+\d{3}[-_. ]+\d{3,4}[-_.\s]+\d{4}')
result = re.findall(pattern, txt)
print(result)
print('\n'.join(result))

# >>> re.finditer() : 패턴 일치되는 모든 문자열을 순환객체로 반환 -----

result = re.finditer('010', txt)
for iter in result:
    print(iter.start())

# >>> re.sub(pattern, replacement, string, count) : 대체 -----

print(re.sub(r'\d{4}[\n ]', '.xxxx.', txt, 2))
print(re.sub(pattern=r'\d{4}[\n ]', repl='xxxx', string=txt, count=2))

# >>> re.split(pattern, string, count) : 나누기 -----

print(re.split(r'\d{4}[\n ]', txt, 1))
print(re.split('ab', 'abaabca', 2))

# >>> Lookaround -----

txt = '10월 26일 코로나 감염자 20명 비감염자 100명'
pattern = r'\d+(?!명)'
print(re.findall(pattern, txt))

# 후방탐색(look-behind)에서는 변동범위를 사용할 수 없다.(갯수 고정 필요)
txt = '"https://www.naver.com" 또는 "http://youtube.com"'
# pattern = r'(?<=https?://)[\w.]+'  # error
pattern = r'(?<=https://)[\w.]+|(?<=http://)[\w.]+'
print(re.findall(pattern, txt))

# >>> [-] 범위 -----

text = 'my.name@localhost.com'
# pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w-.]+.com')  # '-'이 짝을 이루면 '범위'로 해석되어 bad character 에러 발생
pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w-]+.com')     # '-' 앞뒤의 짝을 깨서 해결
pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w\-.]+.com')   # '-' 앞에 \ 추가해서 해결
rst_findLst = re.findall(pattern, text)
print(rst_findLst)


# =====================
# Array
# =====================

# --------------------
# 배열 생성
# --------------------

import numpy as np

# >>> 일반 방식 -----

# np.arange(): 원소값 생성 (파이썬의 range와 유사)
np.arange(10)          # 0 ~ 9
np.arange(1, 20, 2)    # 1 ~ 19, 간격 2
np.arange(1, 10, 0.5)  # 1 ~ 9.5, 간격 0.5

# np.reshape([깊이,] 행, 열): 형상 생성
np.arange(12).reshape(3, 4)
np.arange(24).reshape(2, 3, 4)

# >>> 랜덤 방식 -----

# np.random.rand(행, 열):           0부터 1사이의 균일 분포
# np.random.randn(행, 열):          표준 정규 분포
# np.random.randint(size=(행, 열)): 균일 분포의 정수 난수
# np.random.choice(a, size=None, replace=True)
# a        데이터 범위, 1차원 배열 또는 정수(arange(정수)로 해석)
# size     샘플 생성 갯수(정수)
# replace  중복 허용 여부

np.random.rand(5)
np.random.rand(3, 5)

np.random.randn(5)
np.random.randn(3, 5)

np.random.randint(10, size=10)           # 0  ~ 10 사이 10개의 1차원 배열
np.random.randint(10, 20, size=10)       # 10 ~ 20 사이 10개의 1차원 배열
np.random.randint(10, 20, size=(3, 5))   # 10 ~ 20 사이 3x5의 2차원 배열

np.random.choice(10, 5, replace=True)
np.random.choice(10, 5, replace=False)

# >>> 행 또는 열에 집중한 배열 생성(원솟수를 모르거나 가변적일 때 유용) -----

arr= np.arange(12).reshape(3, 4)

# reshape(정수, -1): 행 기준
arr.reshape(-1)     # (12), (12,), (1, -1), (1, 12) 와 동일 결과
arr.reshape(1, -1)  # (1, ?)
arr.reshape(2, -1)  # (2, ?)
arr.reshape(3, -1)  # (2, ?)
arr.reshape(4, -1)  # (4, ?)

# reshape(-1, 정수): 열 기준
arr.reshape(-1, 1)  # (?, 1)
arr.reshape(-1, 2)  # (?, 2)


# --------------------
# 배열 정보, 자료형 변경
# --------------------

import numpy as np
arr = np.arange(1, 31).reshape(5, 6)
print(arr)

arr.ndim   # 차원 확인
arr.shape  # 배열 형상, (5, 6) 큰방 5개에 각 방마다 원소가 6개씩 들어있다
arr.size   # 배열의 원소 갯수
arr.dtype  # 자료형 확인
len(arr)   # 큰방의 갯수

# 자료형 변경 -----
arr.astype(int)
arr.astype(np.float32)


# --------------------
# 배열의 인덱싱과 슬라이싱
# --------------------

import numpy as np
arr = np.arange(1, 31).reshape(5, 6)
print(arr)

# 인덱싱 : 변수명[인덱스번호]
# 슬라이싱(구간) : 변수명[start:end:step]

# 순차 방식 [전][후] -----
arr[2]
arr[-3::2]
arr[-1::-1]     # 마이너스 스텝은 역방향 진행!!
arr[1][1:]
arr[:4][2:100]  # 작업 순서의 개념([전][후])

# 핀셑 방식 [행,열] -----
arr[1, 1:]
arr[2,]         # 1차원 반환
arr[2:3]        # 2차원 반환
arr[:, 1:-1]
arr[:4, 2:100:2]

# >>> 팬시 방식 [[선택적 추출]] -----
# 팬시 인덱싱은 메모리 공유를 하지 않으므로 뷰가 아님

# 지정 행렬만 추출 : 대괄호[]사용하며 연속범위(:)는 사용불가
arr[[0]]
arr[[0, -1]]

# 교차 위치의 원소값 추출
arr[[0, 2, -1], [1, 4, 3]]          # [(0,1), (2,4), (-1,3)] !!

 # 행렬 곱셈으로 다차원 원소값 추출
arr[np.ix_([0, 2, -1], [1, 4, 3])]  # [[0,[1,4,3]],[2,[1,4,3]],[-1,[1,4,3]]] !!

# >>> View vs Copy -----

# View: 넘파이 인덱싱, 슬라이싱으로 참조된 복사본은 '원본에 영향'을 주므로 주의 !!
arr1 = np.arange(1, 31).reshape(5, 6)
arr2 = arr1[-1][2:-1]            # arr2 는 view
arr2[-1] = 10000                 # arr2 를 변경
print(arr1)                      # arr1(원본)도 변경 !!

# Copy: 원본과 분리된 복사본 생성
arr3 = np.arange(10)
arr4 = arr3[:5].copy()
arr4[-1] = 10000
print(arr3)

# 메모리 공유 여부 확인
np.may_share_memory(arr1, arr2)
np.may_share_memory(arr3, arr4)


# --------------------
# 배열의 병합
# --------------------

import numpy as np

# np.append(): 배열의 모든 원소로 1차원 배열을 생성 -----
arr = np.array([[1, 2], [10, -1]])
arr = np.append(arr, [3, 4])
print(arr)         # [1 2 10 -1 3 4]

# np.append(axis=0): 행 삽입 -----
arr1 = np.ones((3, 5), int)
arr1 = np.append(arr1, np.array([[3, 4, 5, 6, 7]]), axis=0)
print(arr1)

# np.append(axis=1): 열 삽입 -----
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.append(arr2, np.zeros((2, 1)), axis=1)
print(arr2)


# --------------------
# 배열 연산
# --------------------

import numpy as np

# >>> 행렬의 곱 -----

arr1 = np.array([[2, 1], [0, 2]])
arr2 = np.array([[3, 4], [5, 6]])
np.dot(arr1, arr2)

# 일반 곱셈: 같은 위치의 요소끼리만 수식 적용 -----
arr1 * arr2

# >>> Broadcasting -----

# 스칼라값은 상대 배열 형상으로 확장 -----
arr3 = np.array([1, 2, 3, 4, 5])
arr3 + 3

# 상대 배열 형상에 맞춰 행과 열을 확장 -----
arr4 = np.arange(3)
arr5 = np.arange(5).reshape(5, 1)
arr4 + arr5

# >>> 비교연산(==, !=, >, <, >=, <=) -----

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [1, 5, 2]])
c = np.array([7, 8, 9])
d = np.array([7, 8])
e = np.array([1, 2, 3, 4])

a == b
a == c  # c는 브로드케스팅
b == c
b != c
b >= c


# =====================
# 데이터프레임
# =====================

# 1) Series:    label + 1차원 배열 형상
# 2) DataFrame: label + 2차원 배열 형상


# --------------------
# 데이터프레임 생성
# --------------------

import pandas as pd
import numpy as np

pd.Series(['a', 'b', 'c', 'd', 'e']).to_frame()

pd.DataFrame(np.arange(1, 10).reshape(3, 3))

pd.DataFrame([[1, 2, 3, 4], [6, 7, 8, 9]], index = ['m', 'n'], columns = list('abcd'))

df = pd.DataFrame({'food':['melon', 'melon', 'apple', 'apple'],
              'year':[2018, 2019, 2018, 2019],
              'quantity':[490, 512, 478, 325]})

# 기존 데이터프레임에서 지정된 행렬로 새로운 데이터프레임 생성(miss match된 행렬은 NaN(Not a Number) 으로 채워짐)
pd.DataFrame(df, index=[2, 3, 4], columns=['food', 'man', 'quantity'])


# --------------------
# 라벨 관리
# --------------------

# 일괄 라벨 생성 또는 덮어쓰기
df.index = ['a', 'b', 'c', 'd']
df.columns = ['food', 'year', 'quantity']

# 부분 라벨 변경
df.rename(index={'a': 'no_1', 'b': 'no_2'}, inplace=False)
df.rename(columns={'food': 'Fruit'}, inplace=False)

# 컬럼명으로 인덱스 설정 : drop은 컬럼의 잔존 여부
df_s = df.set_index('year', drop = False, inplace = False)
df_s.loc[2018]

# 다중 인덱스 설정
df_m = df.set_index(['food', 'year'])
df_m.loc['apple', 2018]

# 정수 인덱스로 설정 : drop는 기존 인덱스의 열 이동 여부
df.reset_index(drop = False, inplace = False)

# 인덱스 정렬
df.sort_index(ascending=False, inplace = False)

# 인덱스 라벨명 설정
df.index.name = 'No.'
df.columns.name = 'multi1'


# --------------------
# 데이터 분석 전처리
# --------------------

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare', 'class', 'who', 'embark_town', 'alive']]
df.fare = df.fare * 1000
df

# >>> 정보 확인 -----

df.info()                   # 종합정보
df.shape                    # 형상 (행, 렬)
df.index                    # 인덱스명
df.columns                  # 컬럼명
df.dtypes                   # 자료형
df.isna().sum()             # 결측값
df.describe(include='all')  # 통계정보(옵션 all은 문자형자료의 원솟수, 카테고리수, 최빈값, 최빈값사용빈도수 제공)

# >>> 자료형 변경 -----

import numpy as np
df.dtypes                   # 자료형
df.isna().sum()             # 결측값

# 형 변경을 위해서는 Nan, 문자, 수치간 변경제약사항 처리 필요
df['age'].replace(np.nan, 0).astype('int')
df.replace(np.nan, 0).astype({'who':str, 'age':int})

df['fare'] = df['fare'].apply(lambda x: format(x, ','))              # 천단위 콤마 추가 (object로 자동 형변경)
df['fare'] = df['fare'].str.replace(',', '').astype('float32')       # 천단위 콤마 삭제 (자동형변경 안됨)
df['fare'].astype('float32').apply(lambda x: '{:,.2f}'.format(x))    # 소수점 자릿수 변경

# >>> 컬럼 추가 -----

df['man'] = 10  # 동일원소로 일괄 추가

# >>> 인덱스 또는 컬럼 삭제 -----

# 인덱스 (axis=0)
df.drop([1, 6, 2], inplace=False)   # 다수의 인덱스 삭제, 범위(:) 지정불가
df.drop(df.index[1:4])              # 하나 또는 범위(:)를 지정, 다수 인덱스 사용불가
df.drop(df.index[[1, 4]])           # 다수의 인덱스 삭제, 범위(:) 지정불가

# 컬럼 (axis=1)
df.drop(['who', 'man'], axis=1, inplace=False)  # 다수의 컬럼 삭제, 범위(:) 지정불가
df.drop(df.columns[3:], axis=1)                 # 하나 또는 범위(:)를 지정, 다수 컬럼 사용불가
df.drop(df.columns[[1, 4, 3]], axis=1)          # 다수의 컬럼 삭제, 범위(:) 지정불가

# 컬럼 1개 삭제 : 즉시 적용
del df['man']









# >>> 중복값 처리 -----

# 중복값 확인
df.duplicated()
df['class'].duplicated()

# 중복값 삭제
df.drop_duplicates()
df.drop_duplicates(subset=['class'], keep='last')

# >>> 결측값 처리 -----

# 결측값 확인
df.isna().sum()  # df.isnull().sum() 동일

# 결측값 삭제
df.dropna(axis=0)                          # 결측값이 존재하는 행 삭제
df.dropna(axis=1)                          # 결측값이 존재하는 열 삭제
df.dropna(subset=['age', 'fare'], axis=0)  # 검색된 열에 결측값이 존재하는 행 삭제
df.dropna(subset=[888, 889, 890], axis=1)  # 검색된 행에 결측값이 존재하는 열 삭제
df.dropna(thresh=3, axis=0)                # thresh 옵션은 정상값이 지정된 갯수 미만인 행 또는 열 삭제

# 0으로 대체
df['age'].fillna(0)

# 열별 대체
df.fillna({'embark_town': 'most', 'age': 'mean'})

# 평균값 대체
mean_age = df.age.mean(axis=0)
df.age.fillna(mean_age)

# 최빈값 대체
most_freq = df['age'].value_counts(dropna=True).idxmax()  # value_counts(): 시리즈의 유일값을 그룹핑하여 count하는 함수
df['age'].fillna(most_freq)

# 이웃값 대체('ffill', 'bfill')
df['age'].fillna(method='ffill', inplace=False)

# 보간 대체(linear 선형보간, time 시간보간: 시간형 인덱스이어야 함)
df.age.interpolate(method='linear')

# S.where(), DF.where(): 조건이 true면 원래값 유지, false면 명시된 값 또는 NaN으로 대체
df['age'].where(df['alive'] == 'yes', df['fare'] + 10, axis=0)

# np.where(조건문, true 일때 값, false 일때 값) 대체  --> 카테고리 범주 활용 가능
np.where(pd.notnull(df['age']), df['age'], df['fare'] + 10)
np.where(df['age'] > 30, "Big", "Small")

# >>> 카테고리화 -----

# 컬럼 자료 확인
df['class'].unique()                             # 카테고리값 구성원 배열
df['class'].nunique()                            # 카테고리값 갯수
df['class'].value_counts()                       # 카테고리값별 자료수(NaN 생략)
df['class'].value_counts(dropna=False).idxmax()  # 카테고리값별 자료수(NaN 포함) 최빈값

# 구간별 임의 기준 분할
df['fare'].describe()
df['fare'].value_counts(bins=[0, 7, 14, 31, 520], sort=False)

# 구간별 동일 갯수 분할
df['fare_cnt'] = pd.qcut(df['fare'], 3, labels=['Q1', 'Q2', 'Q3'])
df['fare_cnt'].value_counts()
df.groupby('fare_cnt')['fare'].mean()

import seaborn as sns
sns.displot(df, x='fare', hue='fare_cnt', element='step')

# 구간별 동일 길이 분할
count, bin_divcityers = np.histogram(df['fare'], bins=3)  # np.histogram(): 도수분포함수
bin_labels = ['low', 'middle', 'high']
df['fare_bin'] = pd.cut(x=df['fare'],         # 데이터 배열
                        bins=bin_divcityers,  # 경계 값 리스트
                        labels=bin_labels,    # bin 라벨
                        include_lowest=True)  # 최하 경계값 포함

bin_divcityers
df['fare_bin'].value_counts()
df.groupby('fare_bin')['fare'].mean()

import seaborn as sns
sns.displot(df, x='fare', hue='fare_bin', element='step')

# 더미 열 생성 (속하면1, 속하지 않으면0)
pd.get_dummies(df['fare_cnt'])
pd.get_dummies(df['fare_bin'])

# >>> 정규화(Normalization) -----

# 상대적 크기 차이 해소: 열데이터에서 열최솟값을 뺀 값을 분자로 하고, 열최댓값-열최솟값을 분모로 산출(0~1)
min_x = df['fare'] - df['fare'].min()
min_max = df['fare'].max() - df['fare'].min()
df['fare_normalization'] = min_x / min_max
df['fare_normalization'].describe()

# >>> 인덱스라벨로 정렬 -----

df.sort_index(ascending=False)           # 내림차순(False)

# >>> 컬럼별 조건으로 정렬 -----

df.sort_values(by=['class', 'who'],      # 기준열
               ascending=[True, False],  # 오름차순(True)
               na_position='first',      # 결측값 위치 'first'
               # ignore_index=True,      # 기존 인덱스 무시
               # inplace=True,           # 자체 저장
               )

# >>> 데이터프레임 합치기, 형상 바꾸기 -----

df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'all', 'foo'],
                    'value': [1, 2, 3, 5]}, index=[2018, 2019, 2020, 2021])
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'foo', 'sel'],
                    'value': [6, 3, 2, 5],
                    'year': [1999, 2021, 2018, 2019]})

# 연결
pd.concat([df1, df2])                     # 행기준(axis=0), 합집합(join='outer')
pd.concat([df1, df2], axis=1)
pd.concat([df1, df2], ignore_index=True)  # 새로운 정수 인덱스 설정

# 병합
# key  : 열명(on, left_on, right_on) 또는 인덱스(left_index, right_index)
# 방식: inner, outer, left, right
df1.merge(df2)                                     # 공통된 기준으로 교집합으로 병합 (예제에선 value)
df1.merge(df2, left_index=True, right_on='year')
df1.merge(df2, left_on=['lkey'], right_on=['rkey'], how='inner')  # 병합되는 데이터프레임은 중복 가능
df1.merge(df2, left_on=['lkey'], right_on=['rkey'], how='outer')  # 양쪽 df에서 NaN 발생 가능
df1.merge(df2, left_on=['lkey'], right_on=['rkey'], how='left')   # 오른쪽 df에서 NaN 발생 가능
df1.merge(df2, left_on=['lkey'], right_on=['rkey'], how='right')  # 왼쪽 df에서 NaN 발생 가능

# 행과 열 바꾸기(Transpose)
df1.T


# --------------------
# 데이터프레임 인덱싱 & 슬라이싱
# --------------------

import pandas as pd
import numpy as np

dct = {'food':['melon', 'melon', 'apple', 'apple', np.nan, 'peach'],
        'year':[2018, 2019, 2018, 2019, 2020, 2018],
        'total':[np.nan, 512, 478, 325, 290, 800]}
df = pd.DataFrame(dct)

# >>> 인덱싱(열기준) -----

df.food                # 데이터프레임은 [열]기준 !!
df['total'][3]         # 순차인덱싱 [전][후] !!
df[['food', 'total']]  # 팬시인덱싱 [리스트]
df['total', '3']       # error, 핀셑인덱싱[행,렬] 불가 !! ---> 판다스 인덱서로 대체
df[0]                  # error, 컬럼라벨이 존재하면 정수인덱싱 불가 !! ---> 판다스 인덱서로 대체

df[df['food'].isna()]  # 불린 응용
df[df['food'].notna()]
df[(400 < df.total) & (df.total < 700)]
df[df['food'].isin(['melon', 'peach'])]

# >>> 판다스 인덱서 -----

# loc[행,열]: 라벨형
df.loc[3]                    # Series 반환
df.loc[1:3]                  # 마지막 범위 포함 !!
df.loc[1, 'total']
df.loc[2:4, 'food':'total']  # 연속범위 가능

df.loc[[3]]                  # DataFrame 반환
df.loc[[1, 5]]               # 리스트색인은 연속범위 불가
df.loc[[1, 5], :]
df.loc[[1, 5], ['total', 'year']]

# iloc[행,열]: 정수형
df.iloc[:, 2]                # Series 반환
df.iloc[:, :1]               # 마지막 정수범위 미포함 !!
df.iloc[:, [2]]              # DataFrame 반환
df.iloc[:, [0, 2, 1]]

# >>> View -----

df = pd.DataFrame(np.arange(1,16).reshape(3,5), index=list('abc'), columns=list('ABCDE'))

view = df.loc['a':,'D':]         # 슬라이싱한 데이터프레임은 뷰일 뿐이다
view.loc['b','D'] = 900          # 뷰의 일부 값을 바꾸면 원본도 바뀜 !!
print(df, view, sep='\n\n')

view['E'] = 400                  # 뷰의 열을 전부 바꾸면 "해당 열"은 원본에서 독립
print(df, view, sep='\n\n')

view.loc['c','D'] = 500          # 뷰의 일부 값을 바꾸면 독립된 열을 제외하곤 원본에 영향을 줌
view.loc['c','E'] = 500
print(df, view, sep='\n\n')


# --------------------
# 데이터프레임 메서드
# --------------------

# >>> map(), apply() 메서드 -----

def summation(x):
    return x + 100

df1 = pd.DataFrame({"salary":[200,300,400,500], "bonus":[100,200,300,400], "incentive":[80,20,1000,50]})
df2 = pd.DataFrame({"salary":['200원','300원','400원','500원'], "bonus":['100원','200원','300원','400원']})
series1 = pd.Series(index = ["철수","영호","민수"], data = ["빨간공","파란공","노란공"])
series2 = pd.Series(index = ["파란공","노란공","빨간공"], data = ["2만원","3만원","4만원"])

# '원소별'로 메서드 적용 : 시리즈
df1["salary"].map(summation)
df1["salary"].apply(summation)

# '원소별'로 메서드 적용 : 데이터프레임
df2.map(lambda x : x[:3])    # 모든 요소 값에서 3글자 추출('원' 삭제)

# '행별 또는 열별'로 메서드 적용
df2.apply(lambda x : x[:3])  # 1열의 3개요소와 2열의 3개요소를 반환

df1.apply(lambda x: [x[x > 200].sum(), len(x[x > 200])])   # 열별로 조건을 만족하는 요소의 합과 갯수 반환
df1.apply(lambda x: pd.Series([x[x > 200].sum(), len(x[x > 200])], index=['sum', 'count']))

# >>> DF.pipe() 메서드 -----

df2.pipe(lambda x: x.dropna(axis=0)).pipe(lambda x: x.sum())


# --------------------
# groupby()
# --------------------

import pandas as pd
import numpy as np
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['survived', 'age', 'fare', 'class', 'who', 'embark_town']]
print(df)

# >>> DataFrameGroupBy 객체 생성 -----

# df.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, observed=False, dropna=True)
#  by : 그룹화할 내용(함수, 축, 리스트 등등)
#  axis : 그룹화를 적용할 축
#  level : 멀티 인덱스의 경우 레벨을 지정
#  as_index : 그룹화할 내용을 인덱스로 할지 여부(False이면 기존 인덱스가 유지)
#  sort : 그룹key를 정렬할지 여부
#  group_keys : apply메서드 사용시 결과에따라 그룹화 대상인 열이 인덱스와 중복(group key)이 될 수 있음(group_keys=False로 인덱스를 기본값으로 지정)
#  observed : Categorical로 그룹화 할 경우 Categorical 그룹퍼에 의해 관찰된 값만 표시할 지 여부
#  dropna : 결측값을 계산에서 제외할지 여부

# 라벨명으로 그룹핑
df.groupby('class').sum()
df.groupby(['who', 'class']).sum()

# 행인덱스를 기준으로 새로운 행 그룹핑
mapping_dct_row = {0: 'row_g1',
                   2: 'row_g1',
                   4: 'row_g2'}

df[['age', 'fare']].groupby(mapping_dct_row).sum()

# 컬럼라벨을 기준으로 새로운 열 그룹핑
mapping_dct_col = {'survived': 'num1',
                   'age': 'num2',
                   'fare': 'num2'}

df.groupby(mapping_dct_col, axis=1).sum()

# >>> 그룹 인덱싱 -----

gdf = df.groupby(['who', 'class'])
gdf.get_group(('man', 'First'))

# filter 메서드 : 조건을 충족하는 데이터만 추출
gdf.filter(lambda x: len(x) >= 200)

# 그룹별 데이터 확인
for key, group in gdf:
    print('* key : ', key)
    print(group.head())

# >>> 기술통계량 연산 메서드 -----

# [nan 포함]   size
# [nan 미포함] count, sum, min, max, mean, median, std, var, first, last 등

gdf['age'].mean()                         # Series

pd.DataFrame(gdf['age'].mean())           # DataFrame

gdf[['age']].mean().reset_index()         # 인덱스를 열로 이동(계층 라벨이 모두 채워짐)
gdf[['age','fare']].mean().reset_index().sort_values('fare', ascending=False)   # 순서정렬까지 한번에

# >>> agg 메서드 : 빠른 수치 연산을 목적으로 하는 apply()의 특수 형태로 MultiColumns 형태로 반환 -----

gdf['age'].agg(['min', 'max'])                    # 단일 열에 다수의 함수를 매핑
gdf[['age', 'fare']].agg(['min', 'max'])          # 다수 열에 다수의 함수를 매핑(멀티컬럼으로 결과 반환)
gdf.agg({'fare': ['min', 'max'], 'age': 'mean'})  # 각 열별로 각각의 함수 매핑

# >>> apply 메서드 : 그룹별 & 열별로 함수 매핑 -----

def func(x):
    d = {}
    d['fare_mean'] = x['fare'].mean()
    d['fare_std'] = x['fare'].std()
    d['age_max'] = x['age'].max()
    d['age_min'] = x['age'].min()
    return pd.Series(d)

df[(df['who'] == 'woman') & (df['class'] == 'Third')]

gdf.apply(func)
gdf.apply(lambda x: x.describe())
gdf.apply(lambda x: len(x) >= 90)

gdf['age'].apply(lambda x: x.fillna(x.mean()))                           # 평균값 대체
gdf['embark_town'].apply(lambda x: x.fillna(x.value_counts().idxmax()))  # 최빈값 대체

# >>> transform 메서드 : 원본 데이터프레임 형상을 유지하며 결과만을 개별 원소값으로 대체 -----

gdf['age'].transform(np.mean)


# --------------------
# 멀티인덱스 그룹화
# --------------------

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare', 'class', 'who', 'embark_town', 'alive']]

# >>> 멀티 라벨 -----

# 멀티 라벨 설정
df.columns = pd.MultiIndex.from_arrays([['num','num','object','object','object','object'], list(df.columns)], names=("col1", "col2"))
mdf = df.set_index([('object','class'), ('object','who')], drop = True)
print(mdf)

# 멀티 라벨명 변경
mdf.rename_axis(['분류1', '분류2'], axis=1)    # 컬럼라벨구분 변경
mdf.rename_axis(['선실등급', '성별'], axis=0)  # 인덱스라벨구분 변경

# 멀티 라벨 수준 변경
mdf.reorder_levels(['col2', 'col1'], axis=1)
mdf.reorder_levels([1, 0], axis=0)

# 멀티 라벨 정렬
mdf.sort_index(level=0, axis=1, ascending=False)
mdf.sort_index(level=1, axis=1)

# 멀티 라벨 groupby() 합산
mdf.groupby(level='col1', axis=1).sum()
mdf.groupby(level=1, axis=0).apply('sum')

# 멀티 라벨 삭제
mdf.droplevel(1, axis=0)   # (level, axis=0)

# >>> 멀티 인덱스 행 or 열 삭제 -----

# 멀티인덱스 행 삭제
mdf.drop(['woman'], axis = 0, level = 1, inplace = False)
mdf.drop(mdf.index[1], axis = 0, inplace = False)

# 멀티인덱스 열 삭제
mdf.drop(['fare'], axis = 1, level = 1, inplace = False)
mdf.drop(mdf.columns[1], axis = 1, inplace = False)

# >>> xs 인덱서 -----

# 행: axis=0
mdf.xs('First')
mdf.xs('man', level=1, drop_level=True)
mdf.xs('man', level=1, drop_level=False)
mdf.xs(('man', slice(None)), level=[1, 0])
mdf.xs(('First', 'man'))

# 열: axis=1
mdf.xs('object', axis=1)
mdf.xs('fare', level=1, axis=1)
mdf.xs(('num', 'age'), axis=1)
mdf.xs(('num', 'age'), axis=1).to_frame()
mdf.xs(('age', 'num'), level=[1, 0], axis=1)


# --------------------
# 피벗테이블 그룹화
# --------------------

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare', 'class', 'who', 'embark_town', 'alive']]

# >>> 피벗테이블 생성 -----

# 피벗테이블은 컬럼의 피라미드 밑에서부터 columns->values->aggfunc 순으로 쌓임
# 인덱스와 컬럼의 조건을 만족하는 데이터가 2개 이상인 경우는 에러가 발생
pv_df = pd.pivot_table(df,                       # 피벗할 데이터프레임
                       index=['class', 'who'],   # 행구분에 들어갈 열
                       columns='alive',          # 열구분에 들어갈 열
                       values=['age', 'fare'],   # 데이터로 사용할 열
                       aggfunc=['max', 'mean'],  # 적용할 함수
                       # aggfunc={'age': 'max', 'fare': 'mean'},
                       fill_value=0,            # NaN 채우기
                       margins=True,            # 행별,열별 합계
                       margins_name='계')
print(pv_df)

# >>> xs 인덱서 -----

# 행: axis=0
pv_df.xs('First')
pv_df.xs('man', level=1, drop_level=True)
pv_df.xs('man', level=1, drop_level=False)
pv_df.xs(('man', slice(None)), level=[1, 0])
pv_df.xs(('First', 'man'))

# 열: axis=1
pv_df.xs('max', axis=1)
pv_df.xs('fare', level=1, axis=1)
pv_df.xs(('max', 'age'), axis=1)
pv_df.xs(('max', 'age', 'yes'), axis=1)
pv_df.xs(('max', 'age', 'yes'), axis=1).to_frame()
pv_df.xs(('age', 'mean'), level=[1, 0], axis=1)


# --------------------
# str 메서드
# --------------------

import pandas as pd
df = pd.DataFrame({'city':['seoul_junggu', 'masan', 'jinju', 'wooljin'],
                   'year':[2018, 2019, 2018, 2019],
                   'quantity':[490, 512, 478, 325]})

# str.contains(): 정규표현식으로 조건 만족 여부를 반환
df['city'].str.contains('S|j', na=False, regex=True)  # 결측값은 'False'로 반환
df[~df.city.str.contains('(S|j)', na=False)]          # 불포함(결측값이 있는 경우 'na=False')

# 정규표현식으로 선택한 문자를 독립된 열로 분할
df.city.str.extract(r'(.*)_(.*)')

# str.split() : 옵션에 expand=True를 넣으면 데이터프레임으로 반환
df['city'].str.split('_').str[0]
df['city'].str.split('_').str[1]

df['city'].str.split('_').str.get(0)
df['city'].str.split('_').str[0].get(0)

# str.slice()
df['city'].str.slice(2, 3)


# --------------------
# 시계열
# --------------------

# >>> Timestamp 생성 -----

# %Y(2020), %y(20), %m(01~12), %d(01~31)
# %H(01~23), %I(01~12), %M(01~59), %S(00~61)
# %w(0일~6토), %U(일요일기준누적주), %W(월요일기준누적주)
# %B(Jauary), %b(Jan), %A(Sunday), %a(Sun)

pd.date_range(start='2019-01-01',   # 날짜 범위의 시작
              end=None,             # 날짜 범위의 끝
              periods=4,            # 생성할 Timestamp의 개수
              freq='3MS',           # 시간 간격 (MS: 월의 시작일)
              tz='Asia/Seoul')      # 시간대(timezone)

# 텍스트를 Timestamp로 변환
tsp = pd.to_datetime(['200101', '220104', '241210'], format='%y%m%d')

# >>> Period 생성 -----

pd.period_range(start='2019-01-01',  # 날짜 범위의 시작
                end=None,            # 날짜 범위의 끝
                periods=3,           # 생성할 Period 개수
                freq='H')            # 기간의 길이 (H: 시간)

# Timestamp 를 Period 객체로 변환(D, B, W, W-MON, M, MS, Q, QS, A, AS, H, T, S)
tsp.to_period(freq='A')
tsp.to_period(freq='M')
tsp.to_period(freq='D')

# >>> 등간격 시간 조정 -----

tdf = pd.DataFrame(np.random.randn(100), columns=['value'],
                   index=pd.date_range('2018-1-1', periods=100, freq='D'))

# 업-샘플링은 시간 간격이 좁아지면서 빈 데이터 원소에 Nan 이 추가되므로 채워야 함(ffill, bfill)
tdf['value'].resample('10H').ffill()

# 다운-샘플링은 시간 간격이 넓어지므로 기간의 대표값을 구해야 함
tdf['value'].resample('M').first()

# >>> 기간의 시고저종(open, high, low, close) -----

tdf['value'].resample('W').ohlc()
tdf.head(7)

# >>> 기간 집계 함수 -----

# resample(): 등간격 데이터 집계
tdf['value'].resample('6M').sum()
tdf['value'].resample('6M').sum().cumsum()
tdf['value'].resample('6M').max()
tdf['value'].resample('6M').min()
tdf['value'].resample('6M').mean()
tdf['value'].resample('6M').median()
tdf['value'].resample('6M').first()
tdf['value'].resample('6M').last()
tdf['value'].resample('6M').var().fillna(0)
np.sqrt(tdf['value'].resample('6M').var())  # 표준편차

# 선형 기간 집계
tdf['value'].resample('M').count()

# 순환 기간 집계 (시간, 요일 등 반복개념)
tdf.index.day_name().value_counts()
tdf.index.day.value_counts().sort_index()

# >>> dt 활용 -----

# 날짜 데이터 분리
pd.DataFrame(tdf.index)[0].dt.date              # YYYY-MM-DD(문자)
pd.DataFrame(tdf.index)[0].dt.year              # 연(4자리숫자)
pd.DataFrame(tdf.index)[0].dt.month             # 월(숫자)
pd.DataFrame(tdf.index)[0].dt.month_name()      # 월(문자)
pd.DataFrame(tdf.index)[0].dt.day               # 일(숫자)
pd.DataFrame(tdf.index)[0].dt.time              # HH:MM:SS(문자)
pd.DataFrame(tdf.index)[0].dt.hour              # 시(숫자)
pd.DataFrame(tdf.index)[0].dt.minute            # 분(숫자)
pd.DataFrame(tdf.index)[0].dt.second            # 초(숫자)
pd.DataFrame(tdf.index)[0].dt.quarter           # 분기(숫자)
pd.DataFrame(tdf.index)[0].dt.day_name()        # 요일이름(문자)
pd.DataFrame(tdf.index)[0].dt.weekday           # 요일숫자(0-월, 1-화) (=dayofweek)
pd.DataFrame(tdf.index)[0][0].isocalendar()[1]  # 연 기준 몇주째(숫자)
pd.DataFrame(tdf.index)[0].dt.dayofyear         # 연 기준 몇일째(숫자)
pd.DataFrame(tdf.index)[0].dt.days_in_month     # 월 일수(숫자) (=daysinmonth)
pd.DataFrame(tdf.index)[0].dt.is_leap_year      # 윤년 여부

# Period 객체로 만들어서 '년, 년-월' 분리
pd.DataFrame(tdf.index)[0].dt.to_period(freq='A')
pd.DataFrame(tdf.index)[0].dt.to_period(freq='M')

# 문자열 변환
pd.DataFrame(tdf.index)[0].dt.strftime("%Y년 %m월 %d일")

# >>> 시계열 인덱싱 -----

tdf['2018-03-28':'2018-04-05']
tdf.loc['2018']
tdf.loc['2018-03':]

# >>> 시간대 설정 -----

ts_seoul = pd.DataFrame(tdf.index)[0][0].tz_localize('Asia/Seoul')
ts_UTC = ts_seoul.tz_convert('UTC')


# --------------------
# 파일 입출력
# --------------------

# >>> csv -----

# 읽기
df_csv = pd.read_csv("./stats.csv",
                     # index_col=0,          # 행 인덱스가 되는 열 지정(None..)
                     # header=0,             # 열명으로 사용할 행 지정(None..)
                     # usecols=[0,3,6,8],    # 불러올 columns
                     # nrows=6,              # 불러올 rows
                     # skiprows=[1,3],       # 처음 몇 줄을 skip할지 설정
                     # skipfooter=5,         # 마지막 몇 줄을 skip할지 설정
                     # na_values='NA',       # NA값이 'NA'라는 스트링값으로 저장된 경우
                     # encoding='CP949',     # 한글인코딩: 조합형유니코드UTF8, 완성형웹EUC-KR, 완성형윈도우CP949
                     # sep=",",              # txt파일은 "\t"
                     )

# 쓰기
df.to_csv("./sample.csv",
          # columns = ['날짜', '국적', '계'],  # 저장할 열 지정
          # index = False,                     # 행 인덱스 삭제
          # header = False,                    # 열명 삭제
          # encoding = 'utf-8',
          )

# >>> excel -----

# 읽기
df_xl = pd.read_excel('./stats.xlsx',
                      # sheet_major='prod',
                      # index_col="A",       # 행 인덱스가 되는 열 지정(숫자, 열명, None..)
                      # usecols='B:D, H, j',
                      )

# 쓰기
pd.DataFrame(df_csv, index=range(1, len(df_csv) + 1), columns=['column_name']) \
    .to_excel('./sample.xlsx ')

df.to_excel("./sample.xlsx")

# 복수의 excel sheet에 저장
with pd.ExcelWriter('./sample_multi_sheet.xlsx') as writer:
    df.to_excel(writer, sheet_major='1sheet')
    df2.to_excel(writer, sheet_major='2sheet')

# 기존 excel 파일에 저장
import openpyxl
book = openpyxl.load_workbook('./present.xlsx')
writer = pd.ExcelWriter('./present.xlsx', engine='openpyxl')
writer.book = book
df.to_excel(writer, sheet_major='1sheet')
df2.to_excel(writer, sheet_major='2sheet')
writer.save()
writer.close()

# excel: protected files
import win32com.client
import pandas as pd
import os
xl = win32com.client.Dispatch("Excel.Application")
# xl.Visible = False
filename = './excel_pass.xlsx'
PW = '1'
wb = xl.Workbooks.Open(os.path.abspath(filename), Password=PW)
ws = wb.Sheets(1)
content = ws.Range('A1:G313').Value
# content = xlws.Range(xlws.Cells(1,1), xlws.Cells(313,7)).Value
df = pd.DataFrame(list(content))
xl.Quit()


# =====================
# IPython 환경 설정
# =====================

# 옵션 확인: pd.get_option('~~')
# 옵션 설정: pd.set_option('~~')
# 옵션 초기화: pd.reset_option('~~')
pd.set_option('display.max_rows', None)                  # 행 개수
pd.set_option('display.max_columns', 10)                 # 열 개수
pd.set_option('display.max_colwidth', 20)                # 열 너비
pd.set_option('display.unicode.east_asian_width', True)  # 유니코드로 조정한 열 너비
