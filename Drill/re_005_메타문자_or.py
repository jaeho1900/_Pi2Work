# # 메타 문자(Meta Character) 사용법

import re

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
