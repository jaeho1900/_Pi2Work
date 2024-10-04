# =====================
# 웹 스크래핑 이해하기
# =====================

# 우리가 웹 브라우저의 주소창에 어떤 URL을 입력한 다음 키보드 [Enter]키를 누르면,
# 웹 브라우저는 해당 웹 사이트를 운영하는 서버에 요청(Requests)을 보냅니다.
# 그러면 웹 서버는 이 요청을 받고, 요청된 자원에 대한 응답(Response)을 HTML 파일의 형태로 보내줍니다.
# 웹 브라우저는 이렇게 서버로부터 받은 HTML 파일을 해석하고 처리해 시각적으로 웹 페이지를 표시합니다. 

# BeautifulSoup는 HTML과 XML 파일을 파싱(parsing)하기 위한 파이썬 라이브러리로,
# 주로 정적 웹페이지에서 효과적으로 데이터를 추출할 수 있습니다.

# Selenium은 웹 브라우저를 자동으로 조작할 수 있는 도구로, 마치 우리가 웹 브라우저를 열어서 마우스를
# 움직여 주소창을 클릭한 다음 키보드로 URL을 입력하는 것과 같은 행동을 파이썬으로 자동화할 수 있습니다.
# 그렇기 때문에 동적 웹 페이지에서 스크립트가 생성하는 모든 동적 내용을 포착할 수 있습니다.


# =====================
# 웹 요청 라이브러리(requests)
# =====================

# Requests는 브라우저 대신 웹 서버에 요청을 보내고 응답을 받는 작업을 한다.

# Requests는 웹 서버에 요청을 보낼 때 어떤 요청을 하느냐에 따라 각기 다른 메서드를 사용한다.
# 서버에서 데이터를 가져오기 위한 요청을 할 때 사용하는 GET 메서드,
# 서버에 데이터를 생성하기 위한 요청을 할 때는 POST,
# 데이터를 수정할 때는 PUT,
# 서버의 특정 리소스를 삭제할 때는 DELETE를 사용한다.

# (참고) 웹 서버로부터 받은 응답에는 어떤 정보들이 포함되어 있을까요?
# GET 방식으로 요청했을 때 웹 서버로부터 받는 응답에는 웹 페이지의 HTML 문서 외에도 다양한 정보들이
# 포함되어 있습니다. 요청의 성공 또는 실패 여부를 나타내는 응답 상태 코드(Status Code),
# 웹 페이지의 HTML 본문이 담겨있는 응답 본문(Response Body), 콘텐츠 유형, 인코딩, 서버 정보 등이
# 포함된 헤더(Headers), 쿠키(Cookies) 정보, 서버가 요청을 받고 응답을 완료하는 데 걸린 시간을
# 나타내는 응답 시간(Response Time) 등이 있습니다.
# 
# User Agent: 우리가 브라우저에서 웹 페이지를 접속하면 웹 서버로 요청을 보낸다고 배웠습니다.
# 이 요청에는 요청을 보낸 브라우저의 고유한 식별 정보를 담은 User Agent가 포함되어 있습니다.
# User Agent에는 크롬, 엣지와 같은 웹 브라우저의 이름과 버전 번호, 그리고 윈도우나 맥과 같은
# 운영 시스템 종류와 버전 정보가 포함되어 있습니다. 모바일에서 접속하는 경우에는 스마트폰이나
# 태블릿과 같은 기기의 종류가 포함되기도 합니다. 이외에도 여러 정보가 담겨 있는데, 이를 바탕으로
# 웹 서버는 사용자 운영 시스템과 브라우저에 최적화된 컨텐츠를 제공하거나, 브라우저가 지원하지 않는
# 기능을 웹 페이지에서 사용하지 않도록 조정할 수 있습니다.

# 파이썬에서 requests 라이브러리로 웹 스크래핑을 하면, 기본적으로 User Agent 정보가 기본적인 값으로
# 설정됩니다. 이 값은 python-requests라는 라이브러리 이름, 라이브러리 버전 번호, 파이썬 버전 번호 등이
# 포함된 requests의 기본 식별자이기 때문에, 웹 서버에서는 파이썬 또는 자동화된 도구에서 접속한 것으로
# 판단할 수 있습니다.

# Request로 HTML 문서를 가져올 때 발생하는 여러 에러 중 하나로 웹 서버에서 사람이 브라우저로 직접
# 접속하는 것이 아니라고 판단하면 접근을 차단시켜서 데이터를 가져오지 못하게 하는 경우가 있습니다. 
# 이러한 문제를 해결하는 방법으로, requests로 요청을 보낼 때 User Agent를 지정해주면 서버에서는
# 브라우저에서 접근하는 것으로 인식하게 됩니다.
# 자신이 사용하는 특정 브라우저의 User Agent 정보를 확인해서 코드에 넣어주면 됩니다. User Agent를
# 확인하는 방법은 다음과 같습니다.
# User Agent를 확인하는 방법은 방문자의 User-Agent 정보를 보여주는 서비스를 제공하는 다양한 온라인
# 웹사이트를 이용하는 것입니다. 구글에 User Agent 또는 User Agent String을 검색하여 아래의 사이트로
# 접속합니다.
# https://www.whatismybrowser.com/detect/what-is-my-user-agent/
# https://www.useragentstring.com/
# https://www.whatsmyua.info

import requests

url = 'http://www.google.com'

# headers 지정
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

# headers 옵션을 설정하여 get()함수 실행
response = requests.get(url, headers=headers) 
response.raise_for_status()

# >>> 기본 사용법 -----

import requests

# requests.get()으로 웹페이지 가져오기
url = 'http://www.google.com'
response = requests.get(url)

# 응답코드 확인하기
print(response.status_code) 

# 결과값
200

# 응답 코드는 세 자리의 숫자로 이루어져있는데, 숫자의 범위에 따라 응답 상태가 다르다고 생각하면 됩니다.
# 100대의 숫자(100~199)는 임시 응답을 가리킵니다.
# 200대의 숫자(200-299)는 요청이 성공적으로 수락되었고 처리되었음을 나타냅니다.
# 300대의 숫자(300-399)는 요청된 자료가 다른 위치로 옮겨졌다는 것을 의미합니다.
# 400대의 숫자(400-499)는 요청에 오류가 있어서 서버가 요청을 처리할 수 없다는 것을 의미합니다.
# 500대의 숫자(500-599)는 요청에는 문제가 없었지만 서버의 오류로 요청을 처리하지 못했음을 의미합니다.

# raise_for_status() 함수는 마치 if문을 사용한 것처럼 정상적으로 HTML 파일을 가져왔을 때는 문제 없이
# 코드가 진행되고, 에러가 났을 때는 코드를 진행하지 않고 오류를 표시하며 실행을 종료합니다.

# >>> 응용1. 스크래핑한 내용을 리스트나 딕셔너리로 정리한 후, 데이터프레임으로 변환 -----

import requests
from bs4 import BeautifulSoup as bs
import urllib3
import re

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = 'http://pythonscraping.com/pages/page1.html'
res = requests.get(url, verify=False).text
soup = bs(res, 'lxml')
rows = soup.select('div > ul > li')
etfs = {}
for row in rows:
    try:
        etf_name = re.findall(r'^(.*) \(NYSE', row.text)
        etf_market = re.findall(r'\((.*)\|', row.text)
        etf_ticker = re.findall(r'NYSE Arca\|(.*)\)', row.text)
        if (len(etf_ticker) > 0) & (len(etf_market) > 0) & (len(etf_name) > 0):
            # 리스트를 원소로 갖는 딕셔너리를 생성
            etfs[etf_ticker[0]] = [etf_market[0], etf_name[0]]
    except AttributeError as err:
        pass

# 딕셔너리를 데이터프레임으로 변환
df = pd.DataFrame(etfs)

# >>> 응용2. JSON 포맷 데이터를 가져오기 -----

import requests
import pandas as pd

url = 'http://api.nobelprize.org/v1/prize.json'
res = requests.get(url).text
df = pd.read_json(res).fillna(False)
print(df)

# dict 로 데이터구조 파악하여 원하는 자료 추출
print(df['prizes'][0])
print(df['prizes'][0].keys())

print(df['prizes'][0]['laureates'][0])
print(df['prizes'][0]['laureates'][0].keys())

novel2021_prize_chemistry = pd.json_normalize(df['prizes'][0]['laureates'])
print(novel2021_prize_chemistry)

# >>> 응용3. XML 포맷 데이터를 가져오기 -----

import requests
import xml.etree.ElementTree as ET
import pandas as pd
import numpy as np
import seaborn as sns

url = "https://www.w3schools.com/xml/cd_catalog.xml"
res = requests.get(url).text
xtree = ET.fromstring(res)
print(xtree)

# 노드들을 dict 로 저장
rows = []
for node in xtree:
    n_title = node.find("TITLE").text
    n_artist = node.find("ARTIST").text
    n_country = node.find("COUNTRY").text
    n_company = node.find("COMPANY").text
    n_price = node.find("PRICE").text
    n_year = node.find("YEAR").text

    rows.append({"title": n_title,
                 "artist": n_artist,
                 "country": n_country,
                 "company": n_company,
                 "price": n_price,
                 "year": n_year})

# 데이터프레임 만들기
columns = ["title", "artist", "country", "company", "price", "year"]
catalog_cd_df = pd.DataFrame(rows, columns=columns)
catalog_cd_df.head(10)

# >>> 응용4. 그림이미지를 저장하기 -----

import requests
from bs4 import BeautifulSoup as bs

url = 'https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway'
res = requests.get(url, verify=False).text
soup = bs(res, 'lxml')

target_image = soup.find(name='img',
                         attrs={'alt': 'Seoul-Metro-2004-20070722.jpg'})
target_image_src = target_image.get('src')
target_image_res = requests.get('http:' + target_image_src, verify=False)

outfile_path_name = 'metro_image.jpg'
with open(outfile_path_name, 'wb') as out_file:
    out_file.write(target_image_res.content)
    print('이미지파일로 저장되었습니다.')


# =====================
# 웹 요청 라이브러리(urllib)
# =====================

# >>> urllib.request.urlopen() -----

# urllib.request.urlopen(url, data=None, timeout, cafile=None,
#                        capath=None, cadefault=False, context=None)
# data: Post 요청 옵션, context: SSL 연결 옵션
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import urllib3
import ssl

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://pythonscraping.com/pages/page1.html'
res = urlopen(url, context=ctx).read()
soup = bs(res, 'html.parser')
print(soup)

# >>> 에러 처리 -----

# URLError:  서버 못 찾음, URL 오류, 서버 다운
# HTTPError: 없는 페이지(태그) 호출
# AttributeError: 객체에 없는 속성 호출

from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        res = urlopen(url).read()
        bs = BeautifulSoup(res, 'html.parser')
        return bs.title.text
    except URLError as e:
        print("The server could not be found!", e, sep='\n')
        return None
    except HTTPError as e:
        print("The server returned an HTTP error!", e, sep='\n')
        return None
    except AttributeError as e:
        print("The server returned an None!", e, sep='\n')
        return None


# title = getTitle('http://www.pythonscraping.com/pages/page1.html')
# title = getTitle('https://pythonscrapingthisurldoesnotexist.com')
title = getTitle('http://www.pythonscraping.com/pages/warandpeace.html')

if title is None:
    print('Title could not be found.')
else:
    print(title)


# =====================
# 웹 요청 라이브러리(urllib)
# =====================

# >>> html 의 <table>태그로 작성된 표 읽기 -----

tables = pd.read_html('./trainingdata/html/first.html', encoding='utf-8')
tables[0]  # 첫번째 표(복수의 표는 데이터프레임 리스트로 읽어옴)


# =====================
# bs4
# =====================

# BeautifulSoup()으로 BeautifulSoup 클래스의 객체를 생성합니다. 이 클래스는 HTML 파일을 파싱하고
# 파싱된 데이터를 탐색하고 수정하는 데 사용합니다.

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}

data = requests.get('https://www.google.com', headers=headers)
data.raise_for_status()

# HTML 데이터를 로컬 파일로 저장
with open('downloaded_page.html', 'w', encoding='utf-8') as file:
    file.write(data.text)

# 저장된 HTML 파일을 열어 파싱해 BeautifulSoup 객체를 생성
with open('downloaded_page.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')
soup


# ----------
# find 메서드
# ----------

# find 함수는 태그를 이용하여 조건에 부합하는 태그(이름(name), 속성(attribute), 속성값(value))를 찾아서
# 결과를 추출합니다.

# find()나 find_all()은 지정된 조건과 일치하는 태그와 그 태그 안에 포함된 모든 하위 요소들을 함께 
# 반환합니다.
# find_all()에만 설정할 수 있는 옵션으로, 반환할 결과의 최대 개수를 지정해주는 limit이 있습니다. 

# soup.find('태그명')                          태그명에 해당하는 첫번째 태그 추출
# soup.find(속성='속성값')	                   속성='속성값'과 일치하는 첫번째 태그 추출
# soup.find(attrs={'속성':'속성값'})           속성='속성값'과 일치하는 첫번째 태그 추출
# soup.find('태그명', 속성='속성값')            태그명과 일치하면서 속성='속성값'과도 일치하는 첫번째 태그 추출
# soup.find('태그명', attrs={'속성':'속성값'})	태그명과 일치하면서 속성='속성값'과도 일치하는 첫번째 태그 추출

# 태그명이 p인 모든 태그 추출
soup.find_all('p') 

# 태그의 id 속성이 clothes인 첫 번째 태그 추출
soup.find(id='clothes')

# 태그명이 p인 첫 번째 태그 추출
soup.find_all('p', limit=1)

# 경로를 지정해주고 싶을 경우에는 soup.find('p').find('span')와 같이 find()를 중첩해서 사용합니다.
# 첫 번째 p 태그의 하위 태그 중 첫 번째 span 태그 추출
soup.find('p').find('span')

# find_all()도 이와 같은 중첩 방식을 사용할 수 있는데, find_all()의 경우에는 반환되는 결괏값이 리스트형태이기 때문에 인덱싱으로 몇 번째 태그의 하위 태그를 찾을 것인지를 지정해야합니다.
# 첫 번째 p 태그의 하위 태그 중 첫 번째 span 태그 추출
soup.find_all('p')[0].find_all('span')[0]

# 실제 웹 페이지에서 사용자에게 보여지는 텍스트만 가져오고 싶을 때는 어떻게 하면 될까요? 이런 경우 .get_text()를 뒤에 붙여주면 태그의 텍스트만 가지고 올 수 있습니다. 이렇게 가져오는 텍스트에는 공백도 포함됩니다.
# span 태그 중 클래스가 menu인 첫 태그에서 텍스트 추출
soup.find('span', class_='menu').get_text()

# span 태그 중 클래스가 menu인 첫 태그에서 텍스트 추출
soup.find_all('span', class_='menu')[0].get_text()


# ----------
# select 메서드
# ----------

# select 함수는의 CSS 선택자(HTML 문서에서 스타일을 적용할 요소를 지정하는 방법)를 사용해 태그를
# 찾습니다.

# soup.select('태그명')                    태그명에 해당하는 모든 태그 추출
# soup.select('.클래스 속성 값')           클래스 속성값이 일치하는 모든 태그 추출
# soup.select('#아이디 속성 값')           아이디의 속성값이 일치하는 모든 태그 추출
# soup.select('상위태그명 > 하위태그명')	상위태그에 포함된 태그들 중 하위태그명이 일치하는 모든 태그 추출(자식 관계)
# soup.select('상위태그명 공백 하위태그명')	상위태그에 포함된 태그들 중 하위태그명이 일치하는 모든 태그 추출(자손 관계)
# soup.select('조건1, 조건2')	           태그명, 속성값 등 나열된 조건들 중 하나라도 일치하는 모든 태그 추출
# soup.select('태그명. 클래스 속성 값')	    태그명과 클래스 속성값이 모두 일치하는 모든 태그 추출
# soup.select('태그명[속성명="속성 값"]')   태그명과 속성명=속성값(아이디와 클래스 외 다른 속성)이 모두 일치하는 모든 태그 추출

# <body>
#  <h1> 장바구니
#        <p class="name" id="clothes" title="라운드티"> 라운드티 
#          <span class="number"> 25 </span>
#  <span class="price"> 29000 </span>
#  <span class="menu"> 의류</span>
#  <a href="http://www.naver.com"> 바로가기 </a>
#  </p>
#  <p class="name" id="watch" title="시계"> 시계 
#          <span class="number"> 28 </span>
#  <span class="price"> 32000 </span>
#  <span class="menu"> 액세서리 </span>
#  <a href="http://www.facebook.com"> 바로가기 </a>
#  </p>
#  </h1>
#  </body>

# 태그 이름으로 특정 
soup.select('body')

# 아이디 속성 값으로 특정 
soup.select('#watch')

# 자식 관계로 특정 : p태그 아래에 span 태그 중 클래스 속성 값이 menu인 것을 불러옵니다.
soup.select('p > .menu')

# 자손 관계로 특정 : 손자관계(공백)
soup.select('h1 .menu')

# select 함수도 find 함수처럼 get_text()를 사용해 텍스트 부분만 추출할 수 있습니다.
# h1태그의 자손 중 클래스 속성 값이 menu인 태그의 텍스트 추출
soup.select_one('h1 .menu').get_text()

# h1태그의 자손 중 클래스 속성 값이 menu인 태그의 텍스트 추출
soup.select('h1 .menu')[0].get_text()


# ----------
# 그외 탐색 방법
# ----------

# 특정 태그에 직접 접근해서 데이터를 추출하는 방법도 있습니다. 'soup.태그명'으로 태그에 접근할 수 있기 문법이 매우 간단합니다. 첫 번째 태그만 가져옵니다.
# soup.태그명                태그명에 해당하는 첫 번째 태그 추출
# soup.태그명.get('속성명')   태그명에 해당하는 첫 번째 태그의 속성값을 반환
# soup.태그명['속성명']       태그명에 해당하는 첫 번째 태그의 속성값을 반환
# soup.태그명.attrs          태그명에 해당하는 첫 번째 태그의 모든 속성 정보를 딕셔너리로 반환
# soup.상위태그명.하위태그명  상위태그명에 해당하는 첫 번째 태그의 하위태그 중 하위태그명과 일치하는 첫 번째 태그 추출(자식 관계)

# 첫 번째 a태그를 추출
soup.a

# 속성명을 지정하는 방식은 soup.태그명['속성명']와 soup.태그명.get('속성명'), 이렇게 두 가지 방법이 있는데, soup.태그명['속성명'] 방식을 사용할 경우에는 해당 속성이 존재하지 않으면 에러가 발생해 코드 실행이 멈추게 됩니다. get() 함수를 사용해 속성명을 지정하는 방식은 지정한 속성이 존재하지 않으면 None을 반환하기 때문에 코드 실행이 중단되지 않아 안전하게 코드를 실행할 수 있습니다.
# 첫 번째 a태그의 href 속성값을 반환
soup.a.get('href')

# 첫 번째 a태그의 속성 정보를 추출
soup.a.attrs

# 첫 번째 h1태그의 자식 태그 중 첫 번째 p태그 추출
soup.h1.p

# 첫 번째 h1태그의 자식 태그 중 첫 번째 p태그의 자식태그 중 첫 번째 span 태그 추출
soup.h1.p.span

# p태그의 title 속성값 추출
soup.p['title']

# 첫 번째 p 태그의 텍스트 추출
soup.p.get_text()


# ----------
# 부모태그 및 앞뒤의 형제태그로 추출하기
# ----------

# >>> 부모태그로 이동할 때는 find_parent()와 find_parents()를 사용 -----

# find_parent()는 바로 위 직계 부모를 찾는 함수이고 find_parents()는 직계 부모를 넘어 조상들까지
# 반환하는 함수입니다.

# 첫 번째 a태그의 부모태그를 추출
soup.a.find_parent()

# 첫 번째 a태그의 모든 조상태그를 리스트로 추출
soup.a.find_parents()

# >>> 형제 태그로 이동하는 방법 -----

# 형제 태그로 이동하는 방법으로는 find_next_sibling()함수와 find_previous_sibling()이 있습니다.
# 이름에서도 알 수 있듯 find_next_sibling()은 지정한 태그의 다음 형제 태그로 이동하는 것이고
# find_previous_sibling()은 이전 형제 태그로 이동하는 것을 의미합니다.

# 첫 번째 span 태그의 다음에 있는 형제태그 추출
soup.span.find_next_sibling()

# 다음 형제태그 모두를 가져올 때는 .find_next_siblings()를 사용합니다.
# find_next_siblings()는 다음 형제태그 전체를 리스트로 반환합니다.

# 첫 번째 span 태그의 다음에 있는 모든 형제태그 추출
soup.span.find_next_siblings()

# find_next_sibling('태그명', '속성값')의 형태로 괄호 안에 원하는 특정 태그명이나 속성값을 넣어주면
# 다음에 있는 형제 태그 중에서 해당 태그명이나 속성값을 갖는 다음 형제를 찾을 수 있습니다.

# 첫 번째 span 태그의 다음에 있는 형제 태그 중 a 태그를 추출
soup.span.find_next_sibling('a')

# 첫 번째 span 태그의 다음에 있는 형제태그들 중 span 태그만 추출
soup.span.find_next_siblings('span')

# 첫 번째 a태그의 이전에 있는 모든 형제태그 추출
soup.a.find_previous_siblings()

# 첫 번째 a태그의 이전에 있는 형제태그 중 속성값이 number인 형제태그 추출
soup.a.find_previous_sibling('span', class_='number')

# 첫 번째 a태그의 이전에 있는 형제태그 중 속성값이 number인 형제태그의 텍스트만 추출
soup.a.find_previous_sibling('span', class_='number').get_text(strip=True)

# >>> 정리 -----

from bs4 import BeautifulSoup as bs
import re

file = "D:/DeskTop/ctiger/Dropbox/Goodjob/Pi/trainingdata/html/TestHtml.html"
f = open(file, 'r')
soup = bs(f.read())

# # 직접 태그 선택 -----
soup.title
soup.title.parent

# # select 로 태그 선택 -----
soup.select('h1')                         # 태그명과 일치하는 태그 선택
soup.select('#footer')                    # id 가 ~~인 태그 선택
soup.select('.gift')                      # class가 ~~인 태그 선택
soup.select('tbody > tr.gift')            # 직계자손 태그 선택
soup.select('tbody  tr.gift')             # 모든 자손 태그 선택
soup.select('#giftList td:nth-child(3)')  # :nth-child(n) n번째 태그 선택
soup.select('tr[class = "gift"]')         # class속성 값이 ~~인 tr 태그 선택
soup.select('tr[class != "gift"]')        # class속성 값이 ~~가 아닌 tr 태그 선택
soup.select('img[src ^= "./"]')           # src속성 시작값이 ~~인 img 태그 선택
soup.select('img[src $= "jpg"]')          # src속성 끝값이 ~~인 img 태그 선택
soup.select('img[src *= "file"]')         # src속성 값이 ~~를 포함한 img 태그 선택
soup.select('img[src ~= "file"]')         # src속성 값이 독립단어 ~~를 포함한 img 태그 선택
soup.select(('img[type="hidden"][data-value="userValue"]'))  # and조건 img 태그 선택

# # find 로 태그 선택: find(tag, {attribute}, text) -----
soup.findAll(['h1', 'h2', 'h3'])                   # 복수의 태그명 선택
soup.findAll('span', {'class': ['red', 'green']})  # 복수의 속성 선택
soup.findAll('span', text='the prince')            # 태그 사이의 텍스트로 선택
soup.findAll(lambda tag: len(tag.attrs) == 2)      # 속성이 2개인 태그 선택
soup.findAll(lambda tag: tag.text == 'Anna Pavlovna')  # 태그 사이의 텍스트로 선택
soup.findAll('img', {'src': re.compile(r"\.\/TestHtml_files\/img.*\.jpg")})

# # 태그에서 필요 정보를 추출 -----
tag = soup.select('tr')[1]

tag.parent.name              # 태그명

tag.text                     # 태그 사이 텍스트
tag.get_text(strip=True)     # 태그 사이(하위 태그 포함)의 유니코드문장(\n제거)으로 반환
tag.string                   # 태그 사이 순수문자만 반환하고 아니면 None 반환(b태그, \n, () 등)
list(tag.stripped_strings)   # 태그 사이 줄바꿈 등 제거한 문장을 리스트로 반환

tag['id']                    # 태그 속성값 없으면 에러 발생
tag.get('id')                # 태그 속성값 없으면 None 반환(에러 미발생), 여러 개면 리스트를 반환
tag.attrs['id']              # 태그 속성값
tag.attrs                    # 태그 속성 목록 {속성1:속성값1, 속성2:속성값2, ...}
tag.has_attr('id')           # 태그 속성값 존재 유무

# # 태그에서 불필요한 정보 제거(1) -----
html = """
        <body>김딩코의 데이터세상
            <p>Great<b>Big</b>스토리</p>
            <p>소문난 이야기</p>
            <p>개봉<b>박두</b></p>
        </body>
       """
soup = bs(html, 'html.parser')
print(soup)

import copy
test1 = soup.body                  # p태그 묶인 부분 가져오기
test2 = copy.deepcopy(soup.body)   # 깊은 복사

print(test1.p.extract())           # 지정 태그 잘라내기(하위태그 포함, 태그값반환)
print(test1)

print(test2.p.decompose())         # 지정 태그 잘라내기(하위태그 포함, None반환)
print(test2)

# # 태그에서 불필요한 정보 제거(2): 정규표현식 -----
import re
html = "<html><head>some header information</head> \
        <Body>it's start. \
        <script src='..'>some script</script> \
        <!-- some comments -->some \
        <p>body</p> contents.. \n \
        <a href='some link'>gogo</a> \
        그리고 다른 것들.. \
        <script>another</script> \
        </Body> \
        </html>"
soup = bs(html, 'html.parser')
print(soup)

# # <body></body>의 내용만 잘라내기
body = re.search('<body.*/body>', html, re.I | re.S)
print(type(body))
# <body로 시작하고 어떤 글자가(.) 없을 수도 여러개 있을수도 (*) 있고 그 이후에 </body>로 끝난다
# re.I(=re.IGNORECASE) 대소문자를 미구분 의미(Body, body)
# re.S(=re.DOTALL) 여러 줄에 걸쳐서 정규 표현식을 찾으라는 의미(.(dot)의 범위가 모든 문자(\n)를 포함하라는 의미)

if (body is None):
    print("No <body> in html")
    exit()
body = body.group()  # <class 're.Match'>를 <class 'str'>로 변환
print(type(body))
print(body)

# # <script>...</script> 삭제
body = re.sub('<script.*?>.*?</script>', '', body, 0, re.I | re.S)
# 0은 부합되는 모든 문자열을 삭제, 1을 적으면 첫번째 <script>만 삭제
print(body)

# # 공백 제거
nospace = re.sub('&nbsp;| |\t|\r|\n', '', body)
# &nbsp;나 스페이스, 탭(\t), 엔터(유닉스:\r, 윈도우즈:\n)를 삭제
print(nospace)

# # 활용 -----
lists = test1.find_all('p')
for idx in range(len(lists)):
    if lists[idx].b is not None:
        lists[idx].b.decompose()
    text = lists[idx].text
    print(f"{idx} 번째 list : {text}")

for i in soup.select('#gift1 > td'):
    print(i.string, i.text, sep="\n")

for img in soup.findAll('img'):
    print('image src : ', img['src'])

# 상속: children, parents, descendants, next_siblings
for child in soup.find('table', {'id': 'giftList'}).children:  # .parent(s)
    print('children--------')
    print(child.text, '\n')

print(soup.find('img', {'src': './TestHtml_files/img1.jpg'})
      .parent.previous_sibling.text)


# ----------
# 실전! BeautifulSoup을 이용해 뉴스 기사 크롤링하기
# ----------

# >>> newspaper3k 사용하기 -----

# 뉴스기사를 추출할 때는 조금 더 편리하게 가져올 수 있도록 도와주는newspaper3k라는 패키지가 있습니다. newspaper3k는 인터넷 기사의 url만 전달해주면, 이로부터 기사의 제목과 내용을 추출해주는 크롤링 패키지입니다. 
# conda install newspaper3k

from newspaper import Article

# 파싱할 뉴스 기사 URL 지정
url = 'https://v.daum.net/v/20230211141701492'

# 언어를 한국어로 설정하고 URL을 전달해 Article 클래스의 객체 생성
article = Article(url, language='ko')

# 지정된 웹 페이지를 다운로드
article.download()  # 이 과정은 인터넷에 접속해 해당 URL의 서버에 요청하고 응답을 받아 HTML 데이터를 가져오는 작업을 포함합니다.

# 다운로드한 웹 페이지를 분석하고 필요한 정보를 추출
article.parse()

# 기사 제목 출력
print('기사 제목 :',article.title)
print('')

# 기사 내용 출력 
print('기사 내용 :') 
print(article.text)


# =====================
# selenium
# =====================

# ----------
# Selenium 환경 설정
# ----------

# 웹 드라이버(Web Driver)를 다운로드합니다. 웹 드라이버를 다운로드하는 방법은 크게 3가지입니다.

# >>> 첫번째 -----

# 자동으로 웹 드라이버를 설치하고 업데이트를 관리 해주는 webdriver-manager라는 외부 패키지를 이용하는 것입니다. 셀레니움에 포함되어 있지 않은 외부 패키지이기 때문에 별도로 패키지를 설치해주어야 사용이 가능합니다.
# pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from webdriver_manager.chrome import ChromeDriverManager

# webdriver_manager를 사용하여 크롬 드라이버의 실행 경로 설정
# service 객체는 Selenium 4.0 이상에서 웹드라이버를 관리하는 새로운 방법 중 하나
service = Service(executable_path=ChromeDriverManager().install())
# 설정된 service를 사용하여 크롬 드라이버 인스턴스 생성
driver = ChromeDriver(service=service)

# 테스트하려는 웹사이트 열기
driver.get("http://www.example.com")

# 필요한 작업 수행 후 드라이버 종료
driver.quit()

# >>> 두번째 -----

# 최신 버전의 셀레니움에 포함되어 있는 Selenium Manager를 이용하는 방법입니다.
# Selenium Manager는 자동으로 웹드라이버를 관리하는 셀레니움의 공식 드라이버 관리자로,
# 셀레니움 버전 4.6부터는 각 셀레니움 릴리스에 Selenium Manager도 포함되어 제공됩니다.

from selenium import webdriver

# 웹드라이버 자동 관리를 통해 크롬 드라이버 사용
driver = webdriver.Chrome()

# >>> 세번째 -----

# 과거에 주로 사용하던 방식으로 드라이버 파일을 수동으로 다운로드한 후, 이 파일을 시스템의 PATH에
# 추가하거나, 스크립트에서 직접 경로를 지정하여 웹 드라이버가 브라우저를 제어할 수 있도록 설정하는 방법입니다.


# ----------
# XPath 이해하기
# ----------

# XPath란 웹 문서의 특정 요소나 속성에 접근하는 경로를 지정하는 언어입니다.

# <회사 이름="우리회사">
#   <본부 이름="A본부">
#     <팀 이름="1팀">
#       <직원 직급="부장" 사번"0100">정우성</직원>
#       <직원 직급="과장" 사번"0150">이지은</직원>
#       <직원 직급="대리" 사번"0200">차은우</직원>
#       <직원 직급="사원" 사번"0400">박은빈</직원>
#       <직원 직급="인턴" 사번"0500">박보영</직원>
#     </팀>
#     <팀 이름="2팀"/>
#     <팀 이름="3팀"/>
#     ...
#   </본부>
#   <본부 이름="B본부"/>
#   ...
# </회사>

# "차은우"는 "우리회사" 안의 "A본부" 안의 "1팀"에서 3번째에 위치하고 있습니다. 이를 XPath의 절대 경로로
# 나타내면, /회사/본부[1]/팀[1]/직원[3]로 표시할 수 있습니다.
# 사번을 이용해 "차은우"의 위치를 가리킬 수도 있을 것입니다. 이 구조에서 사번은 모두 고유한 번호이기
# 때문에 사번이 "0200"인 직원의 위치를 통해 "차은우"를 찾을 수 있습니다.
# XPath에는 //[@사번="0200"]으로 표현합니다. 여기서 //는 문서의 어떤 위치에서나 조건에 맞는 요소를
# 찾을 수 있다는 것을 의미하고, [@사번="0200"]는 사번 속성이 "0200"인 요소를 선택한다는 뜻입니다.


# ----------
# XPath 기본규칙
# ----------

# <html>
#     <head>
#         <title>업무자동화 공부하기</title>
#     </head>
#     <body>
#         <input type="text" value="아이디를 입력하세요.">
#         <input type="password">
#         <input type="button" value="로그인">
#         <a href="http://naver.com"> 네이버로 이동하기</a>
#         <div id="content">
#             <h1 id="title" class="about">웹스크래핑 알아보기</h1>
#             <p>Beautiful Soup을 공부해보자</p>
#         </div>
#     </body>
# </html>

# XPath 경로는 다음의 규칙으로 표시합니다.

# 1) 슬래시(/)는 한 단계 아래 요소(element)를 의미합니다.
# /html/body/div/h1

# 2) 슬래쉬 두 개(//)는 여러 단계를 생략하여 표시합니다. 이렇게 사용할 경우 하위 모든 요소에 대해 다 찾아보게 됩니다.
# //h1[@class='about']

# 3) 별표(*)는 요소의 이름과 상관없이 모든 요소에서 해당 속성을 갖고 있는 요소가 있는지를 찾습니다.
# //*[@id="title"]
# 이 경우, id가 title인 요소를 모든 문서에서 찾게 됩니다.


# ----------
# XPath 확인하기
# ----------

# 브라우저의 개발자 도구에서 XPath를 찾고자하는 HTML요소에서 마우스 오른쪽 클릭 후,
# 복사(Copy) → XPath 복사(Copy XPath) 또는, 전체 XPath 복사(Copy full XPath)를 클릭합니다.
# XPath 복사(Copy XPath)는 축약된 경로가 표시되고, 전체 XPath 복사(Copy full XPath)는 전체 경로를 다 표시합니다.


# ----------
# 웹 브라우저 제어하기
# ----------

# 셀레니움 매니저로 자동으로 웹 드라이버를 다운받아 크롬 브라우저를 시작하고 종료하는 예제 코드입니다.
from selenium import webdriver

# 웹드라이버 자동 관리를 통해 크롬 드라이버 객체 생성
driver = webdriver.Chrome()

# 웹 브라우저를 실행하여 지정한 url에 접속
driver.get("http://www.google.com")

# 브라우저 창의 크기를 너비 800픽셀, 높이 600픽셀로 설정
driver.set_window_size(800, 600)

# # 브라우저 창을 최대화
# driver.maximize_window()

# 작업 완료 후 브라우저 종료
driver.quit()

# 위의 두 가지 방법은 먼저 크롬 브라우저를 열고 나서 크기를 변경한다는 특징이 있는데, 그렇지 않고
# 브라우저를 열 때 창의 크기도 미리 설정한 값으로 열고 싶다면 크롬 옵션(ChromeOptions)을 사용해야 합니다. 크롬 옵션을 사용하면 브라우저 시작 시 창 크기나 다른 옵션을 설정할 수 있습니다. 다음은 크롬 옵션으로 브라우저 크기를 너비 800픽셀, 높이 600픽셀로 설정하는 예제 코드입니다.

from selenium import webdriver

# 옵션 설정을 위해 option 객체 생성
options = webdriver.ChromeOptions()

# 창 크기를 너비 800픽셀, 높이 600픽셀로 설정 
options.add_argument("window-size=800,600")

# # 전체 화면으로 실행
# options.add_argument("--start-fullscreen")

# 옵션을 적용하여 드라이버 객체 생성
driver = webdriver.Chrome(options=options)

driver.get("http://www.google.com")

driver.quit()


# ----------
# time.sleep() 함수
# ----------

# time.sleep() 함수는 파이썬의 time 모듈에 포함된 함수로, 프로그램 실행을 지정된 시간 동안 일시 중지할 수 있게 해줍니다. 이 함수는 주로 스크립트의 실행을 잠시 멈추게 하여, 네트워크 요청이 완료되기를 기다리거나 사용자 입력을 받기 전에 일시적으로 대기하는 등의 목적으로 사용됩니다. 
# 웹에서 데이터를 가져오거나 웹 작업을 자동화할 때 페이지가 완전히 로드되거나 특정 요소가 화면에 나타날 때까지 기다려야하는 경우가 많이 있는데, 이럴 때 time.sleep()을 사용하여 일정 시간을 기다린 다음 이후의 작업을 진행하도록 할 수 있습니다.

from selenium import webdriver
import time  # 시간 관련 함수를 사용하기 위해 time 모듈을 임포트

driver = webdriver.Chrome()
driver.get("http://www.google.com")

# 브라우저 창의 크기를 너비 800픽셀, 높이 600픽셀로 설정
driver.set_window_size(800, 600)

time.sleep(5)  # 5초 동안 대기

driver.quit()


# ----------
# 웹 페이지 내 요소 선택하기
# ----------

# 셀레니움에서도 특정 요소를 찾는 find_element와 find_elements 메서드를 제공하고 있습니다.

# find_element 메서드는 주어진 검색 기준(예: ID, 클래스 이름, 태그 이름 등)에 해당하는 첫 번째 요소를
# 반환합니다. 요소가 존재하지 않을 경우 NoSuchElementException 예외가 발생합니다. find_element를
# 사용할 때는 find_element(By.속성, "속성값")의 형태로 찾고자하는 기준 속성과 조건에 해당하는 속성값을
# 전달합니다
# By. 뒤에 찾고자하는 속성명을 넣고, 그 다음 인자로 요소의 식별값을 전달합니다.

# find_element 대신 find_elements 메서드를 사용하면 조건을 만족하는 모든 요소를 찾아 리스트로
# 반환합니다. 요소가 없는 경우에는 빈 리스트를 반환하기 때문에 find_element 메서드와 달리
# find_elements 메서드는 요소가 없어도 오류가 발생하지 않아 스크립트가 중단되지 않고 계속 실행될 수
# 있습니다.

# 속성	               방법                                                     	예시
# ID                  페이지 내 고유한 ID로 요소를 찾습니다.	                      find_element(By.ID, "login-form")
# CLASS_NAME	      CSS 클래스 이름으로 요소를 찾습니다.	                          find_element(By.CLASS_NAME, "navigation-menu")
# NAME	              요소의 name 속성으로 요소를 찾습니다.	                          find_element(By.NAME, "email")
# TAG_NAME	          태그 이름으로 요소를 찾습니다.	                              find_element(By.TAG_NAME, "a")
# LINK_TEXT	          a 태그 안의 링크 문자열이 전체 일치하는 요소를 찾습니다.	        find_element(By.LINK_TEXT, "Click Here")
# PARTIAL_LINK_TEXT	  a 태그 안의 링크 문자열이 부분적으로 일치하는 요소를 찾습니다.	find_element(By.PARTIAL_LINK_TEXT, "More Info")
# XPATH	              XPath 표현을 사용하여 요소를 찾습니다.	                      find_element(By.XPATH, "//div[@class='container']")
# CSS_SELECTOR	      CSS 선택자를 사용하여 요소를 찾습니다.                          find_element(By.CSS_SELECTOR, "button.submit")

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.google.com")

# class 이름이 "gb_d"인 첫번째 요소 찾기
driver.find_element(By.CLASS_NAME, "gb_d")

driver.quit()


# ----------
# 웹 페이지 로드하기
# ----------

# 셀레니움은 요소가 로드될 때까지 대기하는 명시적 대기(Explicit Wait)와 암시적 대기(Implicit Wait) 메커니즘이 있습니다.

# >>> 명시적 대기(Explicit Wait) -----

# 명시적 대기는 특정 요소가 특정 조건(예: 요소가 클릭 가능해짐, 요소의 로딩이 완료됨 등)을 충족할 때까지 대기하도록 설정합니다. 
# WebDriverWait 클래스와 expected_conditions 모듈을 함께 사용하여 구현되며, 특정 요소에 대한 대기 시간을 세밀하게 조절할 수 있습니다.

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# WebDriverWait 객체 생성 및 최대 대기 시간 설정
# until 메서드는 expected_conditions 모듈에서 제공하는 다양한 메서드 중 하나를 매개변수로 받아 해당 조건이 충족될 때까지 대기합니다. 조건이 충족되면 대기가 중단되고, 다음 코드 라인으로 넘어갑니다. 
# '메서드명' 부분에 조건을 정의할 메서드를 넣어주고, 웹 요소를 찾는 기준 속성과 값을 (By.속성, "값")의 형태로 전달합니다.

WebDriverWait(driver, 10).until(EC.메서드명((By.속성, "속성값")))

# 대기할 조건을 지정하는 주요 메서드는 다음과 같습니다.

# presence_of_element_located
# : 웹 페이지에 해당 요소가 존재하는지 확인할 때까지 대기합니다. HTML에 요소의 존재가 확인되어 다음의 작업으로 진행되더라도 해당 요소가 우리의 눈에는 보이지 않을 수도 있습니다. 요소가 HTML에는 존재하더라도 실제로 사용자에게 보이는지는 별개의 문제이며, CSS 스타일이나 JavaScript로 인해 보이지 않을 수도 있기 때문입니다.

# visibility_of_element_located
# : 해당 요소가 사용자에게 보이고, 실제로 클릭 가능하거나 상호작용 가능할 때까지 기다립니다.

# element_to_be_clickable
# : 해당 요소가 클릭 가능한 상태가 될 때까지 기다립니다. 클릭 가능한 상태란 요소가 화면에 보이고, 활성화되며, 클릭을 수신할 수 있는 상태일 때를 의미합니다.

# >>> 암시적 대기(Implicit Wait) -----

# 암시적 대기(implicit wait)는 셀레니움에서 웹 드라이버가 웹 요소를 찾을 수 없을 때, 지정된 시간 동안 자동으로 요소가 나타날 때까지 대기하도록 설정하는 방법입니다. 
# 요소가 지정된 시간 내에 발견되면 대기를 중단하고 실행을 계속하며, 요소가 발견되지 않으면 예외를 발생시킵니다. 암시적 대기는 전역 설정으로, 한 번 암시적 대기를 설정하면 드라이버 세션이 종료될 때까지 적용됩니다. 또한 코드 내의 모든 요소 검색에 적용됩니다. 즉, 코드 전체에서 요소 검색에 대해서 모두 일관된 대기 시간이 적용됩니다.

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 최대 10초 동안 대기

# implicitly_wait(10)는 전체 코드 내에서 요소를 검색할 때마다 드라이버가 요소를 찾을 수 없을 때 최대 10초까지 기다리라는 명령입니다. 요소가 10초 내에 발견되면 즉시 다음 코드로 진행하며, 10초 동안 발견되지 않으면 NoSuchElementException 오류가 발생합니다.



# =====================
# 웹 요소와 상호작용하기
# =====================

# ----------
# 키보드 입력하기
# ----------

# >>> 1) 일반 텍스트 입력하기 -----

# send_keys() 메서드는 키보드 입력을 시뮬레이션하여 사용자가 직접 타이핑하는 것과 같은 효과를 낼 수 있습니다. send_keys()를 사용할 때는 먼저 find_element를 이용해 웹 페이지에서 텍스트를 입력할 텍스트 필드 요소를 찾은 다음, 요소에 send_keys() 메서드를 사용해 원하는 텍스트를 인자로 전달합니다.
# 셀레니움에서는 특수 키인 Enter를 사용하거나 마우스를 클릭하는 것 외에도 submit() 메서드를 사용해 서버로 제출할 수도 있습니다. 즉, 위의 코드에서 마지막에 input_element.submit()을 추가하면 검색이 실행됩니다.

# >>> 2) 특수 키 사용하기 -----

# 셀레니움에서는 Keys 클래스를 통해 특수 키(Special Keys) 입력도 지원하고 있습니다. 
# 특수 키를 입력할 때는 send_keys(Keys.키 값)과 같이 Keys 클래스에 정의된 키 값을 send_keys() 메서드와 함께 사용합니다.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")

# 검색어 입력 필드 찾기
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")

# 입력 필드의 내용 모두 지우기
input_element.clear()

# 텍스트 입력
input_element.send_keys("서울 날씨")

# Enter 키 사용하기
input_element.send_keys(Keys.ENTER)

# >>> 특수 키와 문자키를 조합하여 사용하는 조합 키(Combination Keys) 사용하기 -----

# 예를 들어, 조합 키 Ctrl+C로 텍스트를 복사하려고 한다면 send_keys(Keys.CONTROL, 'c')와 같이 사용할 수 있습니다.

# Keys클래스에 포함된 주요 키 값들은 다음과 같습니다.

# ALT: Alt 키
# BACKSPACE: 백스페이스 키
# CANCEL: Cancel 키
# CLEAR: Clear 키
# COMMAND: Command 키 (Mac)
# CONTROL: Ctrl 키
# DELETE: Delete 키
# DOWN: 아래쪽 화살표 키
# END: End 키
# ENTER: Enter 키
# INSERT: Insert 키
# LEFT: 왼쪽 화살표 키
# PAGE_DOWN: Page Down 키
# PAGE_UP: Page Up 키
# RIGHT: 오른쪽 화살표 키
# SHIFT: Shift 키
# SPACE: 스페이스 바
# TAB: Tab 키
# UP: 위쪽 화살표 키

# >>> 3) 콘솔에서 사용자의 입력 받기 -----

# input() 함수는 사용자가 Enter 키를 누를 때까지 프로그램의 실행을 일시 중지하고 사용자의 입력을 기다립니다. 사용자가 텍스트를 입력 후 Enter 키를 치면, 그 시점에 입력된 모든 텍스트가 문자열로 반환되고 프로그램은 다음 코드를 실행합니다.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.google.com")

search_query = input("검색할 단어를 입력하세요: ")

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys(search_query)

# Enter 키 사용하기
input_element.send_keys(Keys.ENTER)

# >>> 마우스 입력하기 -----

# 1) 기본 마우스 클릭
# 버튼, 링크, 체크박스 등 클릭할 요소의 성격과 관계 없이 click() 메서드를 사용하는 방식은 모두 동일합니다.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.google.com")

# 이미지 검색 페이지 버튼 찾기
element_to_click = driver.find_element(By.PARTIAL_LINK_TEXT, "이미지")

# 마우스 클릭 실행
element_to_click.click()

# >>> 2) 드래그 앤 드롭 -----

# ActionChains은 셀레니움 WebDriver에서 제공하는 유틸리티로, 사용자가 복잡한 마우스 및 키보드 상호작용을 연속적으로 체이닝(chain)하여 시퀀스를 만들 수 있도록 도와줍니다. 즉, 쉽게 말해 단순하게 클릭이나 입력을 개별적으로 한 번씩 하는 것을 넘어서, 여러 동작을 연속적으로 실행할 수 있게 해준다고 이해하면 됩니다.
# ActionChains로 여러 동작들을 연속적으로 실행하고자 할 경우, 필요한 동작들을 순서대로 ActionChains 객체에 전달하고 마지막에 동일하게 perform()으로 실행해주면 됩니다.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.google.com")

source = driver.find_element(By.PARTIAL_LINK_TEXT, "이미지")
target = driver.find_element(By.CLASS_NAME, "gLFyf")

# 드래그 앤 드롭 실행
actions = ActionChains(driver)
actions.drag_and_drop(source, target).perform()

# Enter 키 사용하기
target.send_keys(Keys.ENTER)

# >>> 3) 마우스 오버 -----

# 웹 페이지에서 마우스 오버는 특정 요소 위에 마우스 포인터를 위치시켜 그 요소의 마우스 오버 효과(예: 드롭다운 메뉴, 툴팁 표시)를 활성화하는 데 사용됩니다.
# 셀레니움에서 마우스 오버 작업은 주로 ActionChains 클래스의 move_to_element() 메서드를 사용해 동작시킵니다.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("http://www.google.com")

# 마우스 오버 대상 요소
hover_element = driver.find_element(By.CLASS_NAME, "XDyW0e")

# 마우스 오버 실행
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()


# ----------
# 기타 웹 페이지 제어 기법
# ----------

# >>> 페이지 스크롤 -----

# 스크롤을 구현할 때는 주로 자바스크립트(JavaScript)의 window.scrollTo() 함수나 scrollIntoView() 메서드를 사용합니다. window.scrollTo() 함수는 좌표를 이용해 페이지의 특정 위치로 스크롤하는 방식이고, scrollIntoView() 메서드는 웹 페이지의 특정 요소를 이용해 해당 요소의 위치로 스크롤을 조정하는 방식으로 작동됩니다. 이러한 자바스크립트 코드를 실행하기 위해서는 셀레니움의 execute_script() 메서드를 사용해야합니다.

# 자바스크립트의 window.scrollTo() 함수를 이용하면 페이지를 특정 위치로 스크롤할 수 있습니다. 이 함수는 주어진 좌표에 따라 위치를 조정하기 때문에 x좌표와 y좌표를 순서대로 인자로 전달해야합니다.

# x 좌표: 수평 축에서의 스크롤 위치를 나타냅니다. 0은 가장 왼쪽을 의미합니다.
# y 좌표: 수직 축에서의 스크롤 위치를 나타냅니다. 0은 가장 위를 의미합니다.

# 페이지의 가장 마지막으로 이동하고자할 때는 y 값의 절대 좌표 대신 document.body.scrollHeight를 사용할 수 있습니다.
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.naver.com")

# 페이지 최하단으로 스크롤
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

특정 요소로 이동하고자 할때는 위치 계산이 필요 없는 scrollIntoView()를 주로 사용하며, window.scrollTo() 함수는 특정 좌표를 알고 있을 때나 페이지를 맨 위나 멘 마지막으로 이동시킬 때, 또는 반복문을 사용해 y좌표를 일정하게 증가시키면서 스크롤을 점진적으로 내리고자 할 때 주로 사용합니다.

scrollIntoView()

driver.execute_script("arguments[0].scrollIntoView();", element)

behavior: 스크롤 동작을 지정합니다. "auto" (기본값)는 즉각적인 스크롤을, "smooth"는 부드러운 스크롤을 수행합니다.
block: 요소가 브라우저 창에 보여질 수직 방향의 위치를 지정합니다. "start", "center", "end", "nearest(기본값)" 중 선택할 수 있습니다.
inline: 요소가 브라우저 창에 보여질 수평 방향의 위치를 지정합니다. "start", "center", "end", "nearest(기본값)" 중 선택할 수 있습니다.

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.naver.com")

# 페이지에서 "증시" 코너의 "증시" 아이콘 요소 찾기
element = driver.find_element(By.PARTIAL_LINK_TEXT, "증시")

# 해당 요소가 화면 중앙으로 오도록 부드럽게 스크롤 조정driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'});", element)


# ----------
# 브라우저 창 전환하기
# ----------

# 웹 페이지에서 특정 요소를 클릭하여 다른 페이지로 이동할 때 기존의 브라우저 창이 아닌 새로운 탭이나 창이 열리는 경우가 많습니다. 또는 특정 사이트에서 로그인을 하거나 결제 등의 작업을 실행할 때 그 기능이 별도의 탭이나 창에서 처리되는 경우들도 있습니다

# 새로운 창으로 전환하기 위해서는 먼저 driver.window_handles로 모든 window handle을 리스트로 가져옵니다. 이렇게 가져온 리스트로 현재 브라우저 세션에 열려 있는 모든 탭과 팝업 창을 식별하고, 그 중 전환하고자 하는 탭이나 창을 선택하여 switch_to.window()로 창 전환을 실행합니다. 다음은 모든 창의 리스트를 가져온 다음 두 번째 창(일반적으로 새 팝업 창)으로 전환하고 다시 기존에 작업하던 창(첫 번째 창)으로 돌아오는 코드입니다.

# 현재 모든 창 핸들을 리스트로 가져오기
window_handles = driver.window_handles

# 두 번째 창(일반적으로 새 팝업 창)으로 전환하기
driver.switch_to.window(window_handles[1])

# 첫 번째 창으로 다시 전환하기
driver.switch_to.window(window_handles[0])

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.naver.com")

# "부동산" 아이콘 클릭하기
xpath = '//*[@id="shortcutArea"]/ul/li[7]/a/span[1]'
real_estate = driver.find_element(By.XPATH, xpath)
real_estate.click()

# 새로운 탭이 완전히 열리도록 2초 대기
time.sleep(2)

# 새로 열린 탭으로 전환
window_handles = driver.window_handles
driver.switch_to.window(window_handles[1])  # 두 번째 창으로 전환

# 현재 창의 페이지 url과 제목 출력
print("현재 URL:", driver.current_url)
print("현재 페이지 제목:", driver.title)


# ----------
# 이미지로 저장하기
# ----------

# 필요에 따라 셀레니움으로 웹 페이지 전체나 특정 웹 요소들의 스크린샷을 이미지로 저장할 수 있습니다. 전체 페이지의 스크린샷은 save_screenshot()메서드로, 특정 요소에 대한 스크린샷은 screenshot() 메서드를 사용합니다. 웹 페이지의 스크린샷을 캡처할 때는 먼저 웹 페이지가 완전히 로드되었는지 확인해야 합니다. 

# >>> 전체 페이지 스크린샷 -----

# 전체 페이지 스크린샷 캡처는 주로 save_screenshot() 메서드를 사용합니다. save_screenshot() 메서드는 driver.save_screenshot('파일명')과 같이 WebDriver 객체에 직접 호출되며, 저장할 파일 이름을 문자열로 받아 그 이름으로 전체 페이지의 스크린샷을 저장합니다.

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.save_screenshot('full_page_screenshot.png')
driver.quit()

# >>> 특정 요소의 스크린샷 -----

# 특정 웹 요소만 캡처하고 싶은 경우, Selenium 4 이상에서는 screenshot() 메서드를 사용할 수 있습니다. screenshot() 메서드는 웹 요소 객체에 대해 호출되며, 마찬가지로 파일 이름을 문자열로 받아 해당 요소의 스크린샷을 저장합니다.

# 이번에는 구글에 접속하여 검색어 입력 필드 상단의 구글 메인 로고만 캡쳐하여 저장해보겠습니다.

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/img")
element.screenshot('element_screenshot.png')
driver.quit()


# ----------
# 헤드리스(Headless) 모드
# ----------

# 헤드리스 웹 브라우저는 GUI(그래픽 사용자 인터페이스)가 없는 웹 브라우저입니다. 다시 말해 화면에 아무것도 보이지 않고 내부적으로만 작동하는 웹 브라우저입니다.
# 크롬 브라우저를 헤드리스 모드로 실행하려면, 웹 브라우저의 구성 옵션을 설정하는 Options 클래스를 사용합니다.
# add_argument 메서드를 사용하지 않고 chrome_options.headless = True로 헤드리스 모드를 True로 설정할 수도 있습니다.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 옵션 객체 생성
chrome_options = Options()
chrome_options.add_argument("--headless")  # 헤드리스 모드 활성화

# 설정된 옵션을 포함하여 웹 드라이버 인스턴스 생성
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.google.com")
print(driver.title)

driver.quit()





# # 기본 사용법 -----
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(executable_path=r"D:\DeskTop\ctiger\Dropbox\Goodjob\Pi\util\chromedriver.exe",
                          chrome_options=options)
url = r"file:\D:\DeskTop\ctiger\Dropbox\Goodjob\Pi\trainingdata\html\TestHtml.html"
driver.get(url)
time.sleep(1)
html = driver.page_source

soup = bs(html, 'lxml')
print(soup.prettify())

time.sleep(1)
driver.quit()

# # selector 로 태그 선택 -----
# 웹페이지 '검사' > 'Copy' > 'Copy selector' 복사
# soup.select() 사용방법 참조

driver.find_element_by_css_selector('#footer')

# # Xpath 로 태그 선택 -----
# 웹페이지 '검사' > 'Copy' > 'Copy XPath' 복사
# //         탐색 시작
# 태그명
# @          속성
# []         속성지정, n번째 노드선택
# /          직계자속
# *          모든 요소
# //a[@href='http://google.com']   href 속성에 http://google.com 속성값을 가진 모든 a 태그 선택
# //div[@*]                        속성이 하나라도 있는 div 태그 선택
# //input[value>=50]               value 가 50 이상인 input 태그 선택
# //input[value>=50]/@value        선택된 태그의 값만 가지고 오려면
# //div/*[4]                       4번째에 있는 자식 태그를 선택

driver.find_element_by_xpath('//h1[text() = "War and Peace"]')  # 태그사이의 전체 문자로 선택
driver.find_element_by_xpath('//*[contains(text(), "War")]')    # 태그사이의 일부 문자로 선택
driver.find_element_by_xpath('//*[contains(@src, "img")]').get_attribute('src')  # 속성값 추출
driver.find_element_by_xpath('//table')
driver.find_element_by_xpath('//table[@id]/tbody')
driver.find_element_by_xpath('//*[@id="gift1"]/td[3]')

# # Action -----
a = driver.find_element_by_css_selector('#footer')

driver.current_url             # 현재url 추출
a.text                         # 태그에 담긴 텍스트 추출
a.get_attribute('id')          # 태그의 속성값 추출

a.send_keys('text')            # 텍스트 입력
a.send_keys(Keys.RETURN)       # 특수키 입력
a.submit()                     # 폼양식 제출
a.clear()                      # 폼양식 지우기
a.click()                      # 요소 클릭(재사용 안됨)
# a 태그에 링크가 있으면 <a href='http://test.test'> click() 으로 실행 가능
# 링크가 아닌 자바스크립트가 있으면 <a href = '#', onclick = 명령어>
driver.find_element_by_xpath("//button").send_keys(Keys.ENTER)
# 또는 자바스크립트로 처리
element = driver.find_element_by_xpath("//button")
driver.execute_script("arguments[0].click();", element)

a.screenshot('캡쳐.png')       # 태그주변 캡처 저장

driver.set_window_size(1920, 1080)
driver.maximize_window()
driver.minimize_window()
driver.implicitly_wait(3)      # 최대 대기(초)
driver.forward()
driver.back()
driver.save_screenshot('file_name.png')  # 자바스크립트(화면 하단 끝으로 이동)
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
driver.close()                 # 해당 드라이버 종료
driver.quit()                  # 모든 드라이버 종료

# # ActionChains (연속 실행) -----
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

menu = driver.find_element_by_css_selector('.nav')
hidden_submenu = driver.find_element_by_css_selector('.nav #submenu1')

ActionChains(driver).move_to_element(menu).click(hidden_submenu).perform()
ActionChains(driver).key_down(Keys.CONTROL).send_keys('v') \
    .key_up(Keys.CONTROL).perform()  # Ctrl+V

# 검색창을 찾아서 '아이스크림'을 입력한 후 Enter를 입력하고 체인을 실행
search_box = driver.find_element_by_id('headerSearchKeyword')
actions = webdriver.ActionChains(driver).send_keys_to_element(search_box, '아이스크림').send_keys(Keys.ENTER)
actions.perform()

# # 동작 함수
# click_and_hold(on_element=None)	인자로 주어진 요소를 왼쪽 클릭하고 누르고 있는다.
# release(on_element=None)	        마우스를 주어진 요소에서 뗀다.
# # click(on_element=None)         	인자로 주어진 요소를 왼쪽 클릭한다.
# double_click(on_element=None)	    인자로 주어진 요소를 왼쪽 더블클릭한다.
# context_click(on_element=None)	인자로 주어진 요소를 오른쪽 클릭한다.
# drag_and_drop(source, target)	                            source 요소에서 왼쪽 클릭한채로 이동한 뒤 놓는다.
# drag_and_drop_by_offset(source, xoffset, yoffset)	        위와 비슷하지만 offset만큼 이동하여 마우스를 놓는다.
# # move_to_element(to_element)	                            마우스를 해당 요소의 중간 위치로 이동한다.
# move_to_element_with_offset(to_element, xoffset, yoffset)	마우스를 해당 요소에서 offset만큼 이동한다.

# # send_keys_to_element(element, *keys_to_send)	키보드 입력을 주어진 요소에 보낸다.
# # send_keys(*keys_to_send)	                    키보드 입력을 현재 focused된 요소에 보낸다.
# key_down(value, element=None)	                    value로 주어진 키를 누르고 떼지 않는다.
# key_up(value, element=None)	                    value로 주어진 키를 뗀다.
# pause(seconds)	                                주어진 시간(초)만큼 입력을 중지한다.

# perform()	         이미 쌓여 있는(stored) 모든 행동을 수행한다.
# reset_actions()	 이미 쌓여 있는(stored) 모든 행동을 취소한다.

# # 인자
# on_element         해당 인자가 주어지지 않으면 현재 마우스 위치를 기준으로 한다.
# element            해당 인자가 주어지지 않으면 현재 선택된 요소를 기준으로 한다.
# key_down, key_up   Ctrl 등의 키를 누를 때 쓰면 된다

# # 팝업창 이동 -----
driver.get('http://comp.fnguide.com')
time.sleep(3)

selector = "#topChart01"
driver.find_element_by_css_selector(selector).click()
print(driver.window_handles)

# 팝업 창이 한 개인 경우
driver.switch_to_window(driver.window_handles[1])
driver.close()

# 팝업 창이 여러 개인 경우
# main = driver.window_handles
# for handle in main:
#     if handle != main[0]:
#         driver.switch_to_window(handle)
#         driver.close()

driver.switch_to_window(driver.window_handles[0])
print(driver.window_handles)
driver.quit()

# # 윈도우 이동 -----
driver.switch_to_window("windowName")
driver.switch_to.window(driver.window_handles[0])

# # 프레임 이동 -----
driver.switch_to_frame("frameName")
driver.switch_to_default_content()     # 기본 프레임으로 이동

# # 경고창 이동 -----
driver.switch_to.alert()                         # 경고창으로 이동
print(driver.switch_to.alert.text)               # 경고창 text 얻기
assert "alert창" in driver.switch_to.alert.text  # 경고창 text 얻기
driver.switch_to.alert.accept()                  # '확인' 클릭
driver.switch_to.alert.dismiss()                 # '취소' 클릭
driver.switch_to.alert.send_keys('내용')         # '내용' 전송

# # Headless -----
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")  # 혹은 --disable-gpu

options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) \
                     AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument("lang=ko_KR")

driver = webdriver.Chrome('chromedriver', chrome_options=options)
driver.get('https://www.google.com')

driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5];},});")
driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
driver.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype. \
                      getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} \
                      if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return \
                      getParameter(parameter);};")

driver.implicitly_wait(3)
driver.get_screenshot_as_file('headless_check.png')

driver.quit()

# # 윈도우 다운로드 다이얼로그 창 끄기 -----
options.add_experimental_option("prefs", {
                                "download.default_directory": r"C:\Users\Clover\Desktop",
                                "download.prompt_for_download": False,
                                "download.directory_upgrade": True,
                                "safebrowsing.enabled": True})


# =====================
# Tip
# =====================

# # 한글 검색어를 url 코드 형식으로 변환 -----
import urllib

keyword_input = '파이썬'
keyword = urllib.parse.quote(keyword_input)
print('파이썬 문자열을 URL 코드로 변환: ', keyword)

# # 맥에서 작성된 한글자료를 엑셀로 저장할 때 자모음이 분리되는 현상 방지 -----
import unicodedata
contents = unicodedata.normalize('NFC', tag.text)

# # 클립보드 -----
import pyperclip

pyperclip.copy('my_id')
text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = str(i) + ' : ' + lines[i]
text = '\n'.join(lines)

with open('clipboard.txt', 'w', encoding='utf8') as file:
    file.write(text)
