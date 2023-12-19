# # re 모듈을 이용한 정규식 특수문자와 메타문자의 사용법 및 의미 파악

import re

# \d : 숫자 하나
print("\\d: ", re.findall(r'\d', 'Korea 20대 청년이여 힘내라~'))

# \D : 숫자가 아닌 것, 문자를 의미
print("\\D: ", re.findall(r'\D', 'Korea 20대 청년이여 힘내라~'))

# \w : word, 알파벳+숫자+_ 를 의미.
print("\\w: ", re.findall(r'\w', 'Korea 20대 청년이여 힘내라~'))

# \W : 비문자를 의미.
print("\\W: ", re.findall(r'\W', 'Korea 20대 청년이여 힘내라~'))

# \s : space, 공백 문자나 탭 등을 의미.
print("\\s: ", re.findall(r'\s', 'Korea 20대 청년이여 힘내라~'))

# \S : 비공백문자를 의미.
print("\\S: ", re.findall(r'\S', 'Korea 20대 청년이여 힘내라~'))

# \b : 단어(문자)의 경계를 의미, 단어(문자)의 앞(시작) 또는 끝을 의미.
print("\\b: ", re.findall(r'\b', 'Korea 20대 청년이여 힘내라~'))

# \B : 비단어문자의 경계를 의미.
print("\\B: ", re.findall(r'\B', 'Korea 20대 청년이여 힘내라~'))


# # re 모듈을 이용한 정규식의 기초 - backslash

# 어떤 문자열(텍스트) 내용에서 \\superman 이라는 문자열을 검색하고자 한다면???

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

# 파이썬 엔진에선 뒤어 오는 '\' 갯수를 --> 반으로 인식
print("\superman")    # \2개 -> \1개
print("\\superman")   # \2개 -> \1개
print(r"\superman")   # \2개 -> \1개

# \\superman
print("\\\superman")   # \4개 -> \2개
print("\\\\superman")  # \4개 -> \2개
print(r"\\superman")   # \4개 -> \2개

import re

# [3]
text3 = '\superman'                          # text3는 내부에 '\\superman'을 저장
pattern3 = re.compile('\\\\superman')        # re.compile 내부에선 '\\\\' -> re.compile과정에서 '\\\\' -> '\\' 로 처리
pattern3 = re.compile(r'\\superman')         # r이 붙으면 2배로 처리('\\' -> '\\\\')된 후 re.compile과정에서 '\\\\' -> '\\' 로 처리
print("[3] : ", re.search(pattern3, text3))  

# [4]
text4 = "superman 단어 앞에다 백슬래시를 붙이면 \superman 이렇게 됩니다."
pattern4 = re.compile('\\\\superman')
rst4 = re.search(pattern4, text4)
print("[4] : ", rst4)

# [5]
text5 = "superman 단어 앞에다 백슬래시를 붙이면 \\\superman 이렇게 됩니다."
pattern5 = re.compile(r'\\\\s')
rst5 = re.search(pattern5, text5)
print("[5] : ", rst5)

# [6]
text6 = r"superman 단어 앞에다 백슬래시를 붙이면 \\superman 이렇게 됩니다."
pattern6 = re.compile(r'\\\\s')            # re.compile과정에서 반으로 줄어들므로 더블로 작성 주의
rst6 = re.search(pattern6, text6)
print("[6] : ", rst6)
print("[6] : ", rst6.group())


# # 문자열내에서 /d 자체를 검색하고자 할 때와 숫자를 검색할 때 주의점 비교

import re

# (Question) 다음중 에러가 나는 것은?
# '\s'     '\'     's\'
# SyntaxError : ............................................

# [1]
# 메타문자 --->  \  $  .   ^   +   *   ?   {  }  [  ]  (  )   |
# 첫번째 'a\\d'는 -->  정규식 엔진 내부에서 백슬래시(\)를 메타문자로 해석.
# 두번째 'a\\d'는 -->  인터프리터에 의해서 백슬래시(\)를 일반문자로 해석.
rst_matchObj1 = re.search('a\\d', 'a\\d')  # None
print("[1] : ", rst_matchObj1)

# Summary
# 패턴을 일치시키는 방법은?
# (1) 'a\\\\d'
# (2) r'a\\d'


# [2]
text2 = "정규식에서 \d는 숫자를 의미한다. 숫자란 123, 456, 789 이런걸 말한다."
pattern2 = re.compile(r'\d')
rst_matchLst2 = re.findall(pattern2, text2)
print("[2] : ", rst_matchLst2)

# [3] : 숫자가 아닌 \d 자체를 검색한다면? ( r선언을 하지 않는다면? )
text3 = "정규식에서 \d는 숫자를 의미한다. 숫자란 123, 456, 789 이런걸 말한다."
pattern3 = re.compile(r'\\d')
rst_matchObj3 = re.search(pattern3, text3)
print("[3] : ", rst_matchObj3)
