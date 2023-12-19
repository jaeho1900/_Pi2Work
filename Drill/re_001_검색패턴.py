# # 파이썬 re 모듈을 이용한 검색

import re

pattern = "kor"
sentence1 = "I am a korean."
sentence2 = "korean boy"
sentence3 = "Korean boy"
sentence4 = "korea vs korean의 차이는?"

# [ 1 ] 검색 패턴을 컴파일
sp = re.compile(pattern)

# 매치결과는 matchObject 인스턴스 객체 반환
rst_matchObj_1 = sp.match(sentence1)
rst_matchObj_2 = sp.match(sentence2)
rst_matchObj_3 = sp.match(sentence3)
rst_matchObj_4 = sp.match(sentence4)

print("1번 문장의 패턴 매칭 결과는 : {} 입니다.".format(rst_matchObj_1))
print("2번 문장의 패턴 매칭 결과는 : {} 입니다.".format(rst_matchObj_2))
print("3번 문장의 패턴 매칭 결과는 : {} 입니다.".format(rst_matchObj_3))
print("4번 문장의 패턴 매칭 결과는 : {} 입니다.".format(rst_matchObj_4))

# matchObject 객체로부터 매칭된 값만을 원한다면 group() 메서드를 사용한다.

rst_matchObj_2 = sp.match(sentence2).group()

print("2번 문장의 패턴 매칭 값은 : {} 입니다.".format(rst_matchObj_2))


# # group 메서드와 인덱스를 사용하여 각 그룹별 문자열 반환하기

import re
text = "상품구매와 관련한 사항은 010-1234-4567 번호로 문의주세요!"

# 검색 패턴 매치 - 전화번호만 발췌
sp = re.compile(r"\d\d\d-\d\d\d\d-\d\d\d\d")

# 문자열 그룹핑
sp = re.compile(r"(\d\d\d)-(\d\d\d\d)-(\d\d\d\d)")
sp = re.compile(r"(\d+)-(\d+)-(\d+)")             # 숫자 자리수에 구애받지 않음
sp = re.compile(r"(\d+)[^\w](\d+)[^\w](\d+)")     # \w, \W: 단어 문자, 비 단어 문자
# + : 기호 앞에 표시된 문자가 연속적으로 1이상이 있는지를 검색 --> 1이상이면 Ok

rst_matchObj = sp.search(text)

# 출력
print(rst_matchObj)
print(rst_matchObj.group(0))  # group(0) : 매치된 전체 문자열
print(rst_matchObj.group(1))  # group(1) : 첫 번째 그룹에 해당하는 문자열 반환
print(rst_matchObj.group(2))  # group(2) : 두 번째 그룹에 해당하는 문자열 반환
print(rst_matchObj.group(3))  # group(3) : 세 번째 그룹에 해당하는 문자열 반환
