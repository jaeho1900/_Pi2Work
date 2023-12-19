# # 다양한 패턴의 홈페이지(웹사이트) 주소 URL을 매치시키는 정규식 패턴을 작성하시오?

import re

text = '우리의 홈페이지 회사소개 페이지 주소는 http://yourcompany.com/search?a=111&b=222 입니다.'

pattern = re.compile(r'http[s]*://[a-zA-Z0-9-_]*[.]*[\w-]+[.]+[\w.-/~?&=%]+')
rst_matchLst = re.findall(pattern, text)
print(''.join(rst_matchLst))
