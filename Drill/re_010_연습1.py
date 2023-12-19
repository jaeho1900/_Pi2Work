# 연습문제
# 아래의 패턴 결과는 어떻게 나올지 예상해보시오? 그리고 숫자만 출력해보시오?
import re

text = "Welcome to Seoul 2020 Hi~."

pattern = re.compile(r'^\D*[0-9]')
rst_matchLst = re.findall(pattern, text)
print(rst_matchLst)
