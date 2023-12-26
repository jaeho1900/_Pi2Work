# =====================
# re
# =====================

# --------------------
# 매칭 함수
# --------------------
# - findall : 처음부터 끝까지 일치하는 것 반복해서 --> 리스트로 반환
# - search  : 처음부터 끝까지 일치하는 첫번째 것만 --> matchObject 객체로 반환
# - match   : 처음부분만 일치되는 것을 찾아서      --> matchObject 객체로 반환

# re.I 대소문자 불문
# re.S 메타문자(.)에 개행문자(\n) 포함
# re.M 메타문자(^$)를 전체문장이 아닌 각 라인에 적용

import re
text = '''홍길동 010-1234-5671
이순신 010-3333-9632
강감찬 010_2222_4122
김유신 010.9999.5417
을지문덕 010 111    2222'''

# [1] 컴파일 방식
pattern1 = re.compile(r'^\w+\s+\d{3}.\d{3,4}.\d{4}$', re.M)                       # 정규식
pattern2 = re.compile(r'^\w+\s+\d{3}[-_. ]\d{3,4}[-_.\s]+\d{4}$', re.M)           # 전화번호 구분자(- _ . 공백)
pattern3 = re.compile(r'^(\w+)\s+(\d{3})[-_. ]+(\d{3,4})[-_.\s]+(\d{4})$', re.M)  # (그룹핑)

rst_match1 = re.findall(pattern1, text)
rst_match2 = re.findall(pattern2, text)
rst_match3 = re.findall(pattern3, text)

print('\n'.join(rst_match1), end='\n\n')
print('\n'.join(rst_match2), end='\n\n')
print(rst_match3)

# [2] 직접 방식(1번째인자: pattern, 2번째인자: string(text), 3번째인자: 옵션)
re.match('kor', 'Korea', re.I)
re.findall('k.', 'k5r k k\n ks', re.S)
re.findall('k.', 'k5r k k\n ks', re.M)

# [3] 인라인 방식: '(?옵션)'을 패턴에 직접 입력
re.match('(?i)kor', 'Korea')
re.findall('(?s)k.', 'k5r k k\n ks')
re.findall('(?m)k.', 'k5r k k\n ks')

# >>> group(): 매칭된 결과값만 반환
rst_match4 = re.search(pattern3, text)
print(rst_match4.group(0))  # group(0) : 매칭된 전체 문자열 결과값
print(rst_match4.group(1))  # group(1) : 매칭된 1번째 그룹의 문자열 결과값
print(rst_match4.group(4))  # group(4) : 매칭된 4번째 그룹의 문자열 결과값

# >>> sub() 를 사용한 그룹핑
print(pattern3.sub(r'\g<1> : \g<2> - \g<3> - ****', text))  # 그룹은 1 부터 시작 주의!!
print(pattern3.sub(r'\1 : \2 - \3 - ****', text))           # \g<1> 대신 \1 사용 가능
print(pattern3.sub('\\1 : \\2 - \\3 - ****', text))         

# >>> re.sub(pattern, replacement, string)로 문자열 대체
print(re.sub(pattern=r'aaa', repl='xxx', count=3, string='aaa aaa aaa aaa'))  # count 옵션
print(re.sub(r'aaa', 'xxx', 'aaa aaa aaa aaa', 3))  # 변수명을 미사용할때는 카운트를 맨마지막에 입력


# --------------------
# 정규식 특수문자와 메타문자
# --------------------

import re

# >>> 메타문자

# [1]
# (Question) "숫자 3개," 구성의 패턴을 모두 찾으려면?
# 단, 콤마가 없는 경우도 모두 찾는다.

text1 = "돈을 0~9 숫자로 표현할 때는 숫자 3자리 마다 콤마(,)를 찍어줍니다. " \
        "예를들면 123,456,789 이렇게 말입니다."
# pattern1 = re.compile(r'\d')
# pattern1 = re.compile(r'\d\d\d')
# pattern1 = re.compile(r'\d{3}')
# pattern1 = re.compile(r'\d{3},')
# pattern1 = re.compile(r'\d{3}|\d{3},')  # "3자리숫자"를 먼저 찾기때문에 "3자리숫자,"를 못찾음
pattern1 = re.compile(r'\d{3},|\d{3}')    # "3자리숫자,"를 먼저 찾기때문에 결과가 달라짐
rst_matchLst1 = re.findall(pattern1, text1)
print("[1] : ", rst_matchLst1)


# [2]
# 메타 문자 --> | , 2개 이상의 선택시 사용.
text2 = "red box, blue box, yellow box, green box, black box, white box"
pattern2 = re.compile(r'red|yellow|white')  # red, yellow 모두 찾는다면?
rst_matchLst2 = re.findall(pattern2, text2)
print("[2] : ", rst_matchLst2)


# [3]
# 여러 개 결과를 출력하려면? --> findall() 사용!
text3 = "123, 456, 789"
pattern3 = re.compile(r'[0-9]')
rst_matchLst3 = re.findall(pattern3, text3)
print("[3] : ", rst_matchLst3)

cnt = 0
for i in rst_matchLst3:
    if cnt == 0:
        print("[3] : ", i, end='\t')  # end='\t'옵션으로 결과값을 가로로 출력
    else:
        print(i, end='\t')
    cnt += 1
print()


# >>> \d 숫자 하나, \D 숫자가 아닌 것(철자) 
print("\\d: ", re.findall(r'\d', 'Korea 20대_청년이여 힘내라~'))
print("\\D: ", re.findall(r'\D', 'Korea 20대_청년이여 힘내라~'))

# >>> \w word(알파벳+숫자+_), \W 비문(철)자
print("\\w: ", re.findall(r'\w', 'Korea 20대_청년이여 힘내라~'))
print("\\W: ", re.findall(r'\W', 'Korea 20대_청년이여 힘내라~'))

# >>> \s : space(공백+탭), \S 비공백문(철)자
print("\\s: ", re.findall(r'\s', 'Korea 20대_청년이여 힘내라~'))
print("\\S: ", re.findall(r'\S', 'Korea 20대_청년이여 힘내라~'))

# >>> \b : 단어의 경계(문장 앞뒤와 공백의 앞뒤), \B 비단어문자의 경계(철자사이(K와o 사이 등))
print("\\b: ", re.findall(r'\b', 'Korea 20대_청년이여 힘내라~'))
print("\\B: ", re.findall(r'\B', 'Korea 20대_청년이여 힘내라~'))
print("\\b: ", re.search(r'class\b', 'the classified no class at all'))
print("\\B: ", re.search(r'class\B', 'the classified no class at all'))

# >>> \ (backslash)

# '\'문자열 날 것은 --> 짝수로만 인식
"\superman"        # \2개
"\\superman"       # \2개
"\\\superman"      # \4개
"\\\\superman"     # \4개
"\\\\\superman"    # \6개

# r은 '\'문자열을 --> 더블로 인식
r"\superman"        # \2개
r"\\superman"       # \4개
r"\\\superman"      # \6개
r"\\\\superman"     # \8개
r"\\\\\superman"    # \10개

# 파이썬 엔진(print문 등)에선 뒤에 오는 '\' 갯수를 --> 반으로 인식
print("\superman")    # \2개 -> \1개
print("\\superman")   # \2개 -> \1개
print(r"\superman")   # \2개 -> \1개

# \\superman
print("\\\superman")   # \4개 -> \2개
print("\\\\superman")  # \4개 -> \2개
print(r"\\superman")   # \4개 -> \2개

# 예시1
text1 = '\superman'             # text3는 내부에 '\\superman'을 저장
pattern1 = re.compile('\\\\s')  # re.compile과정에서 반만 인식되며  '\\' 로 처리
pattern1 = re.compile(r'\\s')   # r이 붙으면 2배가 된 후('\\\\')된 후 re.compile과정에서 반만 인식되며 '\\' 로 처리
print("[3] : ", re.search(pattern1, text1))  
print("[3] : ", re.search(pattern1, text1).group())  

# 예시2
text = "정규식에서 \d는 숫자를 의미. 숫자란 123, 456 이런 것"

pattern2 = re.compile(r'\d')
rst_matchLst2 = re.findall(pattern2, text)
print("[2] : ", rst_matchLst2)  # ['1', '2', '3', '4', '5', '6']

pattern3 = re.compile(r'\\d')
rst_matchObj3 = re.findall(pattern3, text)
print("[3] : ", rst_matchObj3)  # ['\\d']


# --------------------
# Quiz
# --------------------

# 연습문제1
# 아래의 패턴 결과는 어떻게 나올지 예상해보시오? 그리고 숫자만 출력해보시오?
import re

text = "Welcome to Seoul 2020 Hi~."

pattern = re.compile(r'^\D*[0-9]')
rst_matchLst = re.findall(pattern, text)
print(rst_matchLst)

# 연습문제2
# 아래의 정규식 패턴에 문제가 있는지 살펴보시오? 에러가 난다면 왜 에러가 나는지 말해보시오?
import re

text = 'my.name@localhost.com'

# pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w-.]+.com')  # '-'이 짝을 이루면 '범위'로 해석되어 bad character 에러 발생
pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w-]+.com')     # '-' 앞뒤의 짝을 깨서 해결
pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w\-.]+.com')   # '-' 앞에 \ 추가해서 해결
rst_matchLst = re.findall(pattern, text)
print(rst_matchLst)

# 연습문제3
# 다양한 패턴의 홈페이지(웹사이트) 주소 URL을 매치시키는 정규식 패턴을 작성하시오?
import re

text = '우리의 홈페이지 회사소개 페이지 주소는 http://yourcompany.com/search?a=111&b=222 입니다.'

pattern = re.compile(r'http[s]*://[a-zA-Z0-9-_]*[.]*[\w-]+[.]+[\w.-/~?&=%]+')
rst_matchLst = re.findall(pattern, text)
print(''.join(rst_matchLst))
