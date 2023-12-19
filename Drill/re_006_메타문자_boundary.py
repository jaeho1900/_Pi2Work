# # 정규식 사용시 많이 헤갈리는 특수문자 \b, \B

# b의 사전적의미 : 경계를 의미하는 border, boundary
# 즉, 각 단어의 경계 지점 == \w( [A-Za-z0-9_] )와 그 외의 문자사이의 경계에 대응
# 경계의 '위치'를 가리킨다. 그래서 패턴이 일치해도 매칭되는 길이는 0이다.
# r 선언을 해주고 한다. --> 안그러면 결과가 예상하고 다르게 나올 수 있다.

import re

# [1]
# 각각의 결과를 예상하시오?
rst_list1 = re.findall(r'\b', 'Welcome to Seoul.')
rst_list2 = re.findall(r'\B', 'Welcome to Seoul.')

# [ 복습 ]
# \b : 단어(문자)의 경계를 의미 --> 즉, 단어(문자)의 앞(시작) 또는 끝을 의미.
# \B : \b(단어문자의 경계)가 아닌 곳을 의미 --> 즉, 비단어문자의 경계를 의미.

# (문제 1) \b의 결과는?    6__개  ^Welcome^
# (문제 2) \B의 결과는?   12__개   W^e^l^c^o^m^e

# 출력
print("rst_list1 : ", rst_list1)
print("rst_list1 갯수 : ", len(rst_list1), "개")
print("--------------------------------------------------")
print("rst_list2 : ", rst_list2)
print("rst_list2 갯수 : ", len(rst_list2), "개")
print("--------------------------------------------------")


# [2]
print(re.findall(r'\B', 'Every single Koean should be wearing a mask when...'))
print(len(re.findall(r'\B', 'Every single Koean should be wearing a mask when...')))  # __34__개
print(len(re.findall(r'\b', 'Every single Koean should be wearing a mask when...')))  # __18__개


# [3]
print(re.findall(r'\B', '나는 대한민국의 20대 청년입니다.'))
print(len(re.findall(r'\B', '나는 대한민국의 20대 청년입니다.')))  # __12__개
print(len(re.findall(r'\b', '나는 대한민국의 20대 청년입니다.')))  # __8__개

print(re.findall(r'\b청년\b', '나는 대한민국의 20대(청년)입니다.'))


# # \b와 \B를 이용한 문자열 검색 패턴 이해

# (1) 메타문자 쓰임새 알기    (2) \b, \B 정확히 이해하고 써먹기

import re

# 1. [ ] : 대괄호는 문자 패턴의 집합을 의미
# [abc] ---> a 또는 b 또는 c 또는 의 의미로써 3개(a, b, c) 문자중 하나가 있으면 매칭된다.
# [a-zA-Z] ---> 마이너스(-) 기호를 사용하여 범위를 지정해 줄 수 있다. a 부터 z 까지중 하나가 있다면 매칭.

# (Question) kor 단어는 매칭이 되지만, korea 또는 korean 단어에는 매칭이 안되는 패턴을 만드시오?
text1 = "(Question) kor 단어는 매칭이 되지만, Korea 또는 korean 단어에는 매칭이 안되는 패턴을 만드시오?"
pattern1 = re.compile(r'[a-zA-Z]')  # o, k, o, r, k, o, r, k, o, r
rst_matchLst1 = re.findall(pattern1, text1)
print("[1] : ", rst_matchLst1)

# 2. 숫자
text2 = "(Question) kor 단어는 매칭이 되지만, Korea 또는 korean 단어에는 매칭이 안되는 패턴을 만드시오? 123, 456, 789"
pattern2 = re.compile(r'[0-9]')  # 숫자
rst_matchLst2 = re.findall(pattern2, text2)
print("[2] : ", rst_matchLst2)

# 3.  . : 모든 문자(공백문자, 기호 포함)에 매칭
text3 = "(Question) kor 단어는 매칭이 되지만, Korea 또는 korean 단어에는 매칭이 안되는 패턴을 만드시오?"
pattern3 = re.compile(r'.{3}')
rst_matchLst3 = re.findall(pattern3, text3)
print("[3] : ", rst_matchLst3)

# 4.  + : 1개 이상
# 주어진 텍스트에서 영단어를 검색하고자 한다면?
text4 = "(Question) kor 단어는 매칭이 되지만, Korea 또는 korean 단어에는 매칭이 안되는 패턴을 만드시오?"
pattern4 = re.compile(r'[a-zA-Z]+')  
rst_matchLst4 = re.findall(pattern4, text4)
print("[4] : ", rst_matchLst4)

# 5.  * : 0개 이상
text5 = "(Question) kor 단어는 매칭이 되지만, Korea 또는 korean 단어에는 매칭이 안되는 패턴을 만드시오?"
pattern5 = re.compile(r'[a-zA-Z]*')  
rst_matchLst5 = re.findall(pattern5, text5)
print("[5] : ", rst_matchLst5)

# 6. 검색패턴의 순서가 중요!!
# 주어진 텍스트에서 korea, korean 단어들만 검색하시오?
# 주어진 텍스트에서 kor, korea, korean 단어들만 검색하시오?
text6 = "(Question) kor 단어는 매칭이 되지만, korea 또는 korean 단어에는 매칭이 안되는 패턴을 만드시오?"
pattern6 = re.compile(r'korean|korea|kor')
rst_matchLst6 = re.findall(pattern6, text6)
print("[6] : ", rst_matchLst6)

# 7. 
# 주어진 텍스트에서 kor 단어만 검색하시오?
text7 = "(Question) kor 단어는 매칭이 되지만, korea 또는 korean 단어에는 매칭이 안되는 패턴을 만드시오? ork rko okr"
pattern7 = re.compile(r'[kor]{3}')
rst_matchLst7 = re.findall(pattern7, text7)
print("[7] : ", rst_matchLst7)


import re

# [1]
text1 = "(Question) kor 단어는 매칭되지만 korea 또는 korean 에는 매칭이 안되는 패턴?"
pattern1 = re.compile(r'\bkor\b')
rst_matchLst1 = re.findall(pattern1, text1)
print("[1] : ", rst_matchLst1)

# [2]
text2 = "(Question) kor 단어는 매칭되지만 korea 또는 korean 에는 매칭이 안되는 매칭 패턴은?"
pattern2 = re.compile(r'\b매칭\w*\b')  # 매칭되지만, 매칭이, 매칭
rst_matchLst2 = re.findall(pattern2, text2)
print("[2] : ", rst_matchLst2)
