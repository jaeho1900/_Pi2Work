# =====================
# --------------------
# >>> 


# =========================
# 웹 요청 라이브러리(requests)
# =========================

# # 기본 사용법 ----------
# 스크래핑한 내용을 리스트나 딕셔너리로 정리한 후, 데이터프레임으로 변환
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

# # JSON 포맷 데이터를 가져오기 ----------
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

# # XML 포맷 데이터를 가져오기 ----------
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

# # 그림이미지를 저장하기 ----------
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


# =========================
# 웹 요청 라이브러리(urllib)
# =========================

# # urllib.request.urlopen() ----------
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

# # 에러 처리 ----------
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


# =========================
# 웹 요청 라이브러리(urllib)
# =========================

# # html 의 <table>태그로 작성된 표 읽기 ----------
tables = pd.read_html('./trainingdata/html/first.html', encoding='utf-8')
tables[0]  # 첫번째 표(복수의 표는 데이터프레임 리스트로 읽어옴)

# =========================
# bs4
# =========================

from bs4 import BeautifulSoup as bs
import re

file = "D:/DeskTop/ctiger/Dropbox/Goodjob/Pi/trainingdata/html/TestHtml.html"
f = open(file, 'r')
soup = bs(f.read())

# # 직접 태그 선택 ----------
soup.title
soup.title.parent

# # select 로 태그 선택 ----------
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

# # find 로 태그 선택: find(tag, {attribute}, text) ----------
soup.findAll(['h1', 'h2', 'h3'])                   # 복수의 태그명 선택
soup.findAll('span', {'class': ['red', 'green']})  # 복수의 속성 선택
soup.findAll('span', text='the prince')            # 태그 사이의 텍스트로 선택
soup.findAll(lambda tag: len(tag.attrs) == 2)      # 속성이 2개인 태그 선택
soup.findAll(lambda tag: tag.text == 'Anna Pavlovna')  # 태그 사이의 텍스트로 선택
soup.findAll('img', {'src': re.compile(r"\.\/TestHtml_files\/img.*\.jpg")})

# # 태그에서 필요 정보를 추출 ----------
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

# # 태그에서 불필요한 정보 제거(1) ----------
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

# # 태그에서 불필요한 정보 제거(2): 정규표현식 ----------
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

# # 활용 ----------
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


# =========================
# selenium
# =========================

# # 기본 사용법 ----------
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

# # selector 로 태그 선택 ----------
# 웹페이지 '검사' > 'Copy' > 'Copy selector' 복사
# soup.select() 사용방법 참조

driver.find_element_by_css_selector('#footer')

# # Xpath 로 태그 선택 ----------
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

# # Action ----------
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

# # ActionChains (연속 실행) ----------
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

# # 팝업창 이동 ----------
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

# # 윈도우 이동 ----------
driver.switch_to_window("windowName")
driver.switch_to.window(driver.window_handles[0])

# # 프레임 이동 ----------
driver.switch_to_frame("frameName")
driver.switch_to_default_content()     # 기본 프레임으로 이동

# # 경고창 이동 ----------
driver.switch_to.alert()                         # 경고창으로 이동
print(driver.switch_to.alert.text)               # 경고창 text 얻기
assert "alert창" in driver.switch_to.alert.text  # 경고창 text 얻기
driver.switch_to.alert.accept()                  # '확인' 클릭
driver.switch_to.alert.dismiss()                 # '취소' 클릭
driver.switch_to.alert.send_keys('내용')         # '내용' 전송

# # Headless ----------
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

# # 윈도우 다운로드 다이얼로그 창 끄기 ----------
options.add_experimental_option("prefs", {
                                "download.default_directory": r"C:\Users\Clover\Desktop",
                                "download.prompt_for_download": False,
                                "download.directory_upgrade": True,
                                "safebrowsing.enabled": True})


# =========================
# Tip
# =========================

# # 한글 검색어를 url 코드 형식으로 변환 ----------
import urllib

keyword_input = '파이썬'
keyword = urllib.parse.quote(keyword_input)
print('파이썬 문자열을 URL 코드로 변환: ', keyword)

# # 맥에서 작성된 한글자료를 엑셀로 저장할 때 자모음이 분리되는 현상 방지 ----------
import unicodedata
contents = unicodedata.normalize('NFC', tag.text)

# # 클립보드 ----------
import pyperclip

pyperclip.copy('my_id')
text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = str(i) + ' : ' + lines[i]
text = '\n'.join(lines)

with open('clipboard.txt', 'w', encoding='utf8') as file:
    file.write(text)
