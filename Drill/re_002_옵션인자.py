# 파이썬 re 모듈의 옵션 인자
import re

# # re.I:대소문자 무시

# [1] 1번째인자: pattern, 2번째인자: string(text), 3번째인자: 옵션
rst_matchObj1 = re.match('kor', 'Korea', re.I)
print("[1] : ", rst_matchObj1)
print("----------------------------------------------------")

# [2] : 인라인 방식'(?옵션)'형식으로 패턴에 옵션을 직접 지정
rst_matchObj2 = re.match('(?i)kor', 'Korea')
print("[2] : ", rst_matchObj2)
print("----------------------------------------------------")


# # re.S: 마침표(.)와 개행문자(\n)가 일치하는 것으로 결정할지를 결정

import re

# [1]
rst_matchObj0 = re.findall('k.', 'kr k k\n ks')            # kr, k_, ks
rst_matchObj1 = re.findall('k.', 'kr k k\n ks', re.S)      # kr, k_, k\n, ks

# [2]
rst_matchObj2 = re.findall('(?s)k.', 'kr k k\n ks')


# 출력
print("[0] : ", rst_matchObj0)
print("--------------------------------------------")
print("[1] : ", rst_matchObj1)
print("--------------------------------------------")
print("[2] : ", rst_matchObj2)
