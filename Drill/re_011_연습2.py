# 연습문제
# 아래의 정규식 패턴에 문제가 있는지 살펴보시오? 에러가 난다면 왜 에러가 나는지 말해보시오?
import re

text = 'my.name@localhost.com'

# pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w-.]+.com')  # '-'이 짝을 이루면 '범위'로 해석되어 bad character 에러 발생
pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w-]+.com')     # '-' 앞뒤의 짝을 깨서 해결
pattern = re.compile(r'[a-zA-Z0-9-.]+@[\w\-.]+.com')   # '-' 앞에 \ 추가해서 해결
rst_matchLst = re.findall(pattern, text)
print(rst_matchLst)
