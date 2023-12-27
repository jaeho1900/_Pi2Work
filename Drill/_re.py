# =====================
# re
# =====================

# --------------------
# 매칭 함수
# --------------------
# re.findall: 문장 내 일치하는 모든 것   --> 리스트로 반환
# re.search : 문장 중 일치하는 첫번째 것 --> 객체로 반환
# re.match  : 문장 첫부분이 일치하는 것  --> 객체로 반환

import re

# >>> 옵션

# re.I 대소문자 불문
# re.S 메타문자(.)에서 개행문자(\n) 포함
# re.M 메타문자(^$)를 전체문장이 아닌 각 라인에 적용

# 패턴 컴파일에서 옵션 지정
text = '''홍길동 010-1234-5671
이순신 010-3333-9632
김유신 010.9999.5417
강감찬 010 111  2222'''
pattern = re.compile(r'\w+\s+\d{3}[-_. ]+\d{3,4}[-_.\s]+\d{4}', re.M)
rst_match = re.findall(pattern, text)
print('\n'.join(rst_match))

# 매칭함수(pattern, text, 옵션)에서 옵션 지정
re.findall('k.', 'k5r k k\n Ks', re.I)
re.findall('k.', 'k5r k k\n Ks', re.S)
re.findall('k.', 'k5r k k\n Ks', re.M)

re.findall('(?i)k.', 'k5r k k\n Ks')  # 패턴에 (?옵션)을 직접 입력(인라인 방식)
re.findall('(?s)k.', 'k5r k k\n Ks')
re.findall('(?m)k.', 'k5r k k\n Ks')


# --------------------
# 그룹핑 및 치환
# --------------------

import re
text = '홍길동 010-1234-5671'

# 컴파일의 sub() 그룹핑
pattern = re.compile(r'^(\w+)\s+(\d{3}).(\d{3,4}).+(\d{4})$', re.M)
print(pattern.sub(r'\g<1> : \g<2> - \g<3> - ****', text))
print(pattern.sub(r'\1 : \2 - \3 - ****', text))
print(pattern.sub('\\1 : \\2 - \\3 - ****', text))

# 매칭객체의 group() 그룹핑
rst_match = re.search(pattern, text)
print(rst_match.group(0))  # group(0) : 매칭된 전체 문자열 결과값
print(rst_match.group(1))  # group(1) : 매칭된 1번째 그룹의 문자열 결과값
print(rst_match.group(4))  # group(4) : 매칭된 4번째 그룹의 문자열 결과값

# re.sub(pattern, replacement, string, option) 치환
print(re.sub(pattern='aaa', repl='xxx', string='aa aaa aaaa aaaaa', count=2))
print(re.sub('aaa', 'xxx', 'aa aaa aaaa aaaaa', 3))


# --------------------
# 메타 문자
# --------------------

# [ ]            문자 패턴의 집합
# [^ab]          부정, [^a^b], [^(ab)]와 같음
# [abc]          a 또는 b 또는 c
# [a-zA-Z]       (-)기호로 짝을 맞춰 범위를 지정
# [0-9]          숫자
# ^              시작
# $              끝
# .              문자(공백문자, 기호 포함) 1개
# *              0개 이상
# +              1개 이상
# {숫자}         숫자 만큼
# {숫자,}        숫자 이상
# {숫자1,숫자2}  숫자1 이상, 숫자2 이하 (숫자1,숫자2 모두 붙여쓰기에 주의!!)
# |         또는 (순서 중요!!)

# \d 숫자 1개                        \D
# \w 알파벳+한글+숫자+_               \W
# \s 공백+탭                         \S
# \b 단어경계(\w 와 \W 사이의 경계)   \B 철자경계(\w와 \w 사이)

# >>> \ 사용 방법!!
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


# --------------------
# 사례
# --------------------

import re

# >>> [-] 사용법
text = 'my.name@localhost.com'
# pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w-.]+.com')  # '-'이 짝을 이루면 '범위'로 해석되어 bad character 에러 발생
pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w-]+.com')     # '-' 앞뒤의 짝을 깨서 해결
pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w\-.]+.com')   # '-' 앞에 \ 추가해서 해결
rst_matchLst = re.findall(pattern, text)
print(rst_matchLst)

# >>> | 사용법
text = "kor 단어는 매칭이 되지만, korea 또는 korean 단어에는 매칭이 안되는 패턴"
pattern = re.compile(r'kor|korea|korean')  # kor을 먼저 쓰면 kor만 3개 찾음
pattern = re.compile(r'korean|korea|kor')
print(re.findall(pattern, text))

# >>> \b 사용법
print("\\b 개수: ", len(re.findall(r'\b', 'Welcome to Seoul.')))
print("\\B 개수: ", len(re.findall(r'\B', 'Welcome to Seoul.')))
print(re.findall(r'\bkor\w+\b', "kor 는 비매칭 korea 또는 korean 와는 매칭"))

# >>> 웹페이지 URL 정규식
text = '웹주소는 http://yourcompany.com/search?a=111&b=222 이다.'
pattern = re.compile(r'http[s]*://[a-zA-Z0-9-_]*[.]*[\w-]+[.]+[\w.-/~?&=%]+')
rst_matchLst = re.findall(pattern, text)
print(''.join(rst_matchLst))  # 리스트에서 문자열만 추출

# >>> 정규식과 문자열 함수 대비
# Q) Notebook 이 포함된 단어를 모두 찾아라
text = '''
jupyternotebook, evernote, notebook, onenote, notebook1, 21세기notebook, jupyter-notebook,
jupyter_notebook, jupyter@notebook
'''

# A1) 정규식
pattern = re.compile(r'\w*[-@]*notebook\w*')
print(', '.join(re.findall(pattern, text)))

# A2) 문자열 함수
a = text.split()
rst_lists = []
for i in a:
    if 'notebook' in i:
        rst_lists.append(i)

print(rst_lists)

print([i for i in a if 'notebook' in i])
