"""
_네이버뉴스검색
220426
"""

# # 네이버 검색어 스크랩 ==========

import urllib
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd

keyword_input = '블루에셋'
keyword_except = '스카이블루에셋'
start_date = '2021.04.01'
end_date = '2022.03.31'

sd = start_date.replace('.', '')
ed = end_date.replace('.', '')
keyword = urllib.parse.quote(keyword_input)
keyword2 = urllib.parse.quote(keyword_except)

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(executable_path=r'D:/2022/_Py/_common/chromedriver.exe', chrome_options=options)
url = f"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%22{keyword}%22+-%22 \
        {keyword2}%22&oquery=%22{keyword}%22&tqi=hDQsCdp0Jywssl88giGsssssshN-194891&nso=so%3Ar%2Cp%3A \
        from{sd}to{ed}%2Ca%3Aall&de={end_date}&ds={start_date}&mynews=0& \
        office_section_code=0&office_type=0&pd=3&photo=0&sort=0"
driver.get(url)
time.sleep(3)

# 변수정의 ----------
t_press = []
t_date = []
t_title = []
t_link = []
t_relatenews = []


# 페이지스크랩 ----------
def page_scrap():

    html = driver.page_source
    soup = bs(html, 'html.parser')

    # 메인뉴스
    for i in soup.select('div.info_group a.info.press'):
        t_press.append(i.text)
    for i in soup.select('div.info_group span.info'):
        if i.text[0:2] == '20':
            t_date.append(i.text)
    for i in soup.select('div.news_area > a'):
        t_title.append(i.text)
    for i in soup.select('div.news_area > a'):
        t_link.append(i.get('href'))

    # 서브뉴스
    for i in soup.select('cite.sub_txt.press'):
        t_press.append(i.text)
    for i in soup.select('span.sub_txt'):
        if i.text[0:2] == '20':
            t_date.append(i.text)
    for i in soup.select('span.sub_wrap > a'):
        t_title.append(i.text)
    for i in soup.select('span.sub_wrap > a'):
        t_link.append(i.get('href'))

    # 관련뉴스
    for i in soup.select('a.news_more'):
        t_relatenews.append('https://search.naver.com/search.naver' + i.get('href'))


# 페이지넘김 ----------
def page_scrap_click():
    while driver.find_element_by_css_selector('a.btn_next').get_attribute('aria-disabled') == 'false':
        page_scrap()
        driver.find_element_by_css_selector('a.btn_next').click()
        time.sleep(3)


# 실행 ----------
try:
    if driver.find_element_by_css_selector('a.btn_next').get_attribute('aria-disabled') == 'false':
        page_scrap_click()
        page_scrap()
    else:
        page_scrap()
except NoSuchElementException:
    print("해당 검색어에 대한 언론뉴스가 없습니다.")

# 관련뉴스 추가 ----------
if len(t_relatenews) > 0:
    for iurl in t_relatenews:
        url = iurl
        driver.get(url)
        time.sleep(3)
        page_scrap_click()
        page_scrap()

# 데이터프레임 저장 ----------
df = pd.DataFrame({'언론사명': t_press, '기사날짜': t_date, '제목': t_title, 'URL': t_link})
df.sort_values(by=['기사날짜', '언론사명'], ascending=True, inplace=True, ignore_index=True)
df.drop_duplicates(['기사날짜', '언론사명'], keep='first', inplace=True, ignore_index=True)
df.index = df.index + 1
with pd.ExcelWriter("C:/Users/Administrator/Desktop/{}.xlsx".format(keyword_input)) as writer:
    df.to_excel(writer)
time.sleep(1)
driver.close()


# # 판다스 분석 ==========

import pandas as pd
import datetime
import matplotlib.pyplot as plt

from matplotlib import rc
rc('font', family='malgun gothic')

# trend_df = pd.read_excel(
#             'c:/Users/Administrator/Desktop/에스원_동향.xlsx',
#             skiprows=6,
#             parse_dates = ['날짜'])

trend_df = pd.read_excel('c:/Users/Administrator/Desktop/에스원_동향.xlsx',
                         sheet_name='취합',
                         usecols='B:D',
                         parse_dates=['날짜'])

asset_df = pd.read_excel('c:/Users/Administrator/Desktop/에스원_동향.xlsx',
                         sheet_name='블루에셋',
                         usecols='B:E',
                         parse_dates=['기사날짜'])

scan_df = pd.read_excel('c:/Users/Administrator/Desktop/에스원_동향.xlsx',
                        sheet_name='블루스캔',
                        usecols='B:E',
                        parse_dates=['기사날짜'])

asset_count = asset_df['기사날짜'].value_counts(dropna=False)
scan_count = scan_df['기사날짜'].value_counts(dropna=False)
new_df = pd.merge(trend_df, asset_count, how='outer', left_on='날짜', right_index=True)
new_df = pd.merge(new_df, scan_count, how='outer', left_on='날짜', right_index=True)
new_df.columns = ['날짜', '블루스캔검색추이', '블루에셋검색추이', '블루에셋언론기사건수', '블루스캔언론기사건수']
new_df.fillna(0, inplace=True)

new_df.to_excel('c:/Users/Administrator/Desktop/에스원_동향2.xlsx',
                sheet_name='취합')

# # 시각화 ------------------
fig = plt.figure(figsize=(15, 10))
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

ax1.plot(new_df['날짜'], new_df['블루에셋검색추이'], color='blue')
ax1.set_ylabel('네이버 트랜드 추이(%)')
ax1.set_xlim(new_df['날짜'].min() - pd.Timedelta(days=5), new_df['날짜'].max() + pd.Timedelta(days=5))
ax1.set_ylim(0, 100)
ax1.grid(True)
ax1.set_title('블루에셋 네이버 검색추이')

ax2.plot(new_df['날짜'], new_df['블루스캔검색추이'], color='magenta')
ax2.set_xlim(new_df['날짜'].min() - pd.Timedelta(days=5), new_df['날짜'].max() + pd.Timedelta(days=5))
ax2.set_ylim(0, 100)
ax2.grid(True)
ax2.set_title('블루스캔 네이버 검색추이')

ax3.bar(new_df['날짜'], new_df['블루에셋언론기사건수'], color='blue')
ax3.set_ylabel('기사건수(개)')
ax3.set_xlim(new_df['날짜'].min() - pd.Timedelta(days=5), new_df['날짜'].max() + pd.Timedelta(days=5))
ax3.set_ylim(0, 30)
ax3.grid(True)
ax3.set_title('블루에셋 언론기사건수')

ax4.bar(new_df['날짜'], new_df['블루스캔언론기사건수'], color='magenta')
ax4.set_xlim(new_df['날짜'].min() - pd.Timedelta(days=5), new_df['날짜'].max() + pd.Timedelta(days=5))
ax4.set_ylim(0, 30)
ax4.grid(True)
ax4.set_title('블루스캔 언론기사건수')

plt.suptitle("'검색 트랜드'와 '언론 기사 건수' 상관성", fontsize=20)
plt.show()
