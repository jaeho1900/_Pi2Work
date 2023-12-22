# =====================
# re
# =====================

# --------------------
# 검색
# --------------------
import re

sentence1 = "I am a korean."
sentence2 = "Korean boy"
sentence3 = "korean boy"
sentence4 = "korea vs korean의 차이는?"

# 검색 패턴 컴파일
pattern = "kor"
sp = re.compile(pattern)

# re.Match object 객체로 매칭 결과 반환
print(sp.match(sentence1))
print(sp.match(sentence2))
print(sp.match(sentence3))
print(sp.match(sentence4))

# re.Match object 객체로부터 매칭된 값만을 원한다면 group() 메서드를 사용
print(sp.match(sentence3).group())


# # group 메서드와 인덱스를 사용하여 각 그룹별 문자열 반환하기
text = "상품구매와 관련한 사항은 010-1234-4567 번호로 문의주세요!"

# 검색 패턴: 전화번호
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
