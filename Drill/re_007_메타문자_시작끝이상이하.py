
import re

# [1] : 주어진 텍스트내에서 영문자가 3개 또는 5개로 구성된거 다 찾기?
text1 = "(Question) kor 단어는 검색되지만 korea 또는 korean 에는 매칭이 안되는 패턴? a ab abc abcd abcde abcdef"
pattern1 = re.compile(r'\b[a-zA-Z]{3}\b|\b[a-zA-Z]{5}\b')
rst_matchLst1 = re.findall(pattern1, text1)
print("[1] : ", rst_matchLst1)


# [2] : 영어 단어만 검색하려면?
text2 = "Question : kor1 단어는 검색되지만 korea 또는 korean 에는 매칭이 안되는 패턴? a ab abc abcd abcde abcdef"
pattern2 = re.compile(r'[a-zA-Z]+')
rst_matchLst2 = re.findall(pattern2, text2)
print("[2] : ", rst_matchLst2)


# [3] : 변수의 처음과 끝을 표시
text3 = "Question15412478abcdef"
pattern3 = re.compile(r'^[a-zA-Z0-9]+$')  # 처음부터 끝까지
rst_matchLst3 = re.findall(pattern3, text3)
print("[2] : ", rst_matchLst3)


# [4] : {이상,이하}
text4 = "Question : kor 단어는 검색되지만 korea 또는 korean 에는 매칭이 안되는 패턴? a ab abc abcd abcde abcdef"
pattern4 = re.compile(r'\b[a-zA-Z]{3,}\b')    # 3이상
pattern4 = re.compile(r'\b[a-zA-Z]{2,4}\b')   # 2이상 4이하
pattern4 = re.compile(r'\b[a-zA-Z]{2, 4}\b')  # 오작동 {}안의 띄어쓰기 주의!!
rst_matchLst4 = re.findall(pattern4, text4)
print("[4] : ", rst_matchLst4)


# [5] : caaaat 에서 (문자사이에 포함된)aaaa만 매칭시키고 싶다면?
text5 = "ccccaaaabbbb"
pattern5 = re.compile(r'\Baaaa\B')
rst_matchLst5 = re.findall(pattern5, text5)
print("[5] : ", rst_matchLst5)


# [6] : 대소문자무시옵션 및 옵션적용(컴파일할때)단계
# JupyterNotebook 에는 매치되지만, evernote, notebook, onenote 등에는 매치되지 않는 정규식은?
text6 = "JupyterNotebook"
pattern6 = re.compile(r'(?i)\Bnote\B')             # inline방식
pattern6 = re.compile(r'\Bnote\B', re.IGNORECASE)  # 컴파일할때 세번째 옵션을 적용
rst_matchLst6 = re.findall(pattern6, text6)        # 패턴을 변수로 사용할때 IGNORECASE 는 에러 발생
print("[6] : ", rst_matchLst6)


# [7] : [ ] 안의 문자는 OR의 의미
# 아래 텍스트에서 'Notebook'이 들어간(포함된) 단어(문자열)를 모두 매치하려면?
text7 = '''
jupyternotebook, evernote, notebook, onenote, notebook1, 21세기notebook, jupyter-notebook,
jupyter_notebook, jupyter~notebook, jupyter@notebook, jupyter1notebook
'''
# pattern7 = re.compile(r'[a-zA-Z]*notebook\w*')
# pattern7 = re.compile(r'\w*[-@]*notebook\w*')   # [-@] 도 괜찮으나 어떤게 또 있을지 모르므로 약간의 수정 필요.
pattern7 = re.compile(r'\w*[^\w\s]*notebook\w*')  # [ ] 안의 ^ 는 부정의 의미.
rst_matchLst7 = re.findall(pattern7, text7)
print("[7] : ", rst_matchLst7)


# [8] : [^ab] 용법은 [^a^b], [^(ab)]을 의미
text8 = "abc-def-ab123-456"
pattern8 = re.compile(r'[^ab]')    # ###############(1) : 이것과 같음 --> [^a^b], [^(ab)]
# pattern8 = re.compile(r'[^a^b)]')
# pattern8 = re.compile(r'[^(ab)]')
# pattern8 = re.compile(r'^ab')    # ###############(2) : [ ] 빼면 결과가 완전 달라짐. ab로 시작하는 걸 찾음.
rst_matchLst8 = re.findall(pattern8, text8)
print("[8] : ", rst_matchLst8)
