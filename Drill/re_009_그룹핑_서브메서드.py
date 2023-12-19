# # 이름과 전화번호가 들어있는 텍스트에서 전화번호가 맞는지 검증하여 출력하시오?

text = '''홍길동 010-1234-5671
이순신 010-3333-9632
강감찬 010_2222_4122
김유신 010.9999.541a
을지문덕 010-1191-2222'''

# [1] : 문자열함수로 해결
import re
rst1 = []
# 텍스트 내 각 개행(\n) 단위로 한줄씩 a 배열리스트로 저장
a = text.split('\n')
# a 리스트내 요소를 반복을 돌면서 띄어쓰기 단위로 쪼개서 b 배열리스트로 저장
for oneline in a:
    b = oneline.split(' ')
    rst2 = []
    for item in b:
        if len(item) == 13:
            if item[:3].isdigit() and item[4:8].isdigit() and item[-4:].isdigit():
                item = item[:3] + "-" + item[4:8] + "-" + "****"
                rst2.append(b[0] + ":" + item)
            else:
                rst2.append(b[0] + ":이 회원의 전화번호에는 숫자가 아닌 것이 있음.")
    rst1.append("".join(rst2))
print('\n'.join(rst1))  # 리스트를 문자열로 변환


# [2] : 정규식으로 해결
text = '''홍길동 010-1234-5671
이순신 010-3333-9632
강감찬 010_2222_4122
김유신 010.9999.541a
을지문덕 010-1191-2222'''

import re
# 조건에 맞는 패턴 컴파일
pattern = re.compile(r'^\w+\s+\d{3}.\d{3,4}.\d{4}$', re.M)  # re.M: 멀티라인 옵션을 컴파일단계에서 적용
rst_matchLst = re.findall(pattern, text)
print(rst_matchLst)


# [3] : 전화번호 구분자 -->  '-'   ' '   '.'   '_'
text = '''홍길동 010-1234-5671
이순신 010-3333-9632
강감찬 010_2222_4122
김유신 010.9999.5417
을지문덕 010 111    2222'''

import re
pattern = re.compile(r'^\w+\s+\d{3}[- ._]\d{3,4}[-\s._]+\d{4}$', re.M)
rst_matchLst = re.findall(pattern, text)
print('\n'.join(rst_matchLst))


# [4] : (그룹핑) --> 매치가 된 1차결과값에서 그룹핑된 2차결과값을 재매치 --> 튜플로 출력
pattern = re.compile(r'^(\w+)\s+\d{3}[-\s._]+\d{3,4}[-\s._]+\d{4}$', re.M)
rst_matchLst = re.findall(pattern, text)
print(rst_matchLst)


# [5] : 그룹핑된 문자열을 sub메서드를 사용해서 다른 문자열로 바꾸기
pattern = re.compile(r'^(\w+)\s+(\d{3})[-\s._]+(\d{3,4})[-\s._]+(\d{4})$', re.M)
print(pattern.sub(r'\g<1> : \g<2> - \g<3> - ****', text))  # 그룹은 1 부터 시작 주의!!
print(pattern.sub(r'\1 : \2 - \3 - ****', text))           # \g<1> 대신 \1 사용 가능
print(pattern.sub('\\1 : \\2 - \\3 - ****', text))         # \g<1> 대신 \1 사용 가능
print(re.sub(pattern, '***', text))
print(re.sub('^(\w+)', '***', text))
print(re.sub(r'(?m)^(\w+)', '***', text))  # (?m) : 멀티라인옵션


# [6] : re.sub() 메서드에서 치환 카운트 사용
print(re.sub(pattern=r'aaa', repl='bbb', count=3, string='aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa'))
print(re.sub(r'aaa', 'xxx', 'aaa aaa aaa aaa aaa aaa aaa aaa aaa aaa', 9))  # 변수명을 미사용할때는 카운트를 맨마지막에
