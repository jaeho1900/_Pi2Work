# # 파이썬 re 모듈의 다양한 함수 - match, findall, search

# findall vs match, search 함수는 반환하는 결과 값이 서로 다르다.
# ┌ findall : 처음부터 끝까지 일치하는 것 반복해서 --> 리스트로 반환.
# ├ search  : 처음부터 끝까지 일치하는 첫번째 것만 --> matchObject 객체로 결과를 반환.
# └ match   : 처음부분만 일치되는 것을 찾아서      --> matchObject 객체로 결과를 반환.

import re

rst_matchObj1 = re.findall('k2k', '2k2k2k2k2')
rst_matchObj2 = re.search('k2k', '2k2k2k2k2')
rst_matchObj3 = re.match('k2k', '2k2k2k2k2')

print("findall 검색 결과 : ", rst_matchObj1)
print("search 검색 결과 : ", rst_matchObj2)
print("match 검색 결과 : ", rst_matchObj3)







