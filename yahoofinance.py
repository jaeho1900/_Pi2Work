# 네이버 대체
from urllib import parse
from ast import literal_eval
import requests
import pandas as pd
import numpy as np

def get_sise(code, start_time, end_time, time_from='day') :
    get_param = {
    	'symbol':code,
	    'requestType':1,
	    'startTime':start_time,
	    'endTime':end_time,
	    'timeframe':time_from
    }
    get_param = parse.urlencode(get_param)
    url="https://api.finance.naver.com/siseJson.naver?%s"%(get_param)
    response = requests.get(url, verify=False)
    return literal_eval(response.text.strip())
    
data = get_sise('005930', '20200101', '20231130', 'day')
column = data[0]
df = pd.DataFrame(data=data, columns=column)
df.drop([0], inplace=True)
df = df.set_index(['날짜'])
df.index = pd.to_datetime(df.index)
df

# Yahoo Finance API 사용 =====
import yfinance as yf

# yfinance로 주가 데이터 받아오기 =====
# 티커를 요청하면 Open, High, Low, Close, Adj Close, Volume값을 리턴
data = yf.download(['AAPL','MU'],start = '2019-01-01')
data['Close']

# yfinance로 주가 외 데이터 받아오기(재무제표를 받아오기 위해선 yahoofinance 패키지를 사용) =====
# 주가 데이터를 받아올 때와 달리 변수 선언이 필요
aapl = yf.Ticker('AAPL')
aapl.dividends  # 배당내역
aapl.splits  # 주식분할
aapl.recommendations  # 애널리스트 평가

# 데이터 검색 방법 =====
close = df['종가']
close['2020']
close['2021-08']
close['2020':'2021']

# 그래프 그리기1 =====
close['2020':'2021'].plot(figsize=(15,7), color='red').grid()

# 그래프 그리기2 =====
import plotly.express as px
vol = df.거래량
px.line(x=vol.index, y=vol,
        template='plotly_dark',
        labels={'x':'날짜', 'y':'거래량'})

# 이중축 그래프
subset = df[['종가','거래량']]
subset.plot(figsize=(15,7))

subset['거래량'].plot(color='b', figsize=(15,7))
subset['종가'].plot(color='r',secondary_y=True)

import matplotlib.pyplot as plt
t = subset.index
y_left = subset.거래량
y_right = subset.종가

fig, ax1 = plt.subplots(figsize=(13,6))

ax1.plot(t, y_left, color='b')
ax1.set_ylabel('volume', color='b')
ax1.grid()

ax2 = ax1.twinx()
ax2.plot(t, y_right, color='r')
ax2.set_ylabel('close', color='r')

plt.show()

# 그래프가 저장되어 있어서 호출하면 그래프를 반환

# plotly 활용
import plotly.graph_objects as go
from plotly.subplots import make_subplots

subset = df[['종가','거래량']]
data_vol = go.Scatter(x=subset.index, y=subset['거래량'], name='Volume')
data_close = go.Scatter(x=subset.index, y=subset['종가'], name='Close')

fig = make_subplots(specs=[[{"secondary_y":True}]])
fig.add_trace(data_vol, secondary_y=False)
fig.add_trace(data_close, secondary_y=True)
fig.update_layout(template='plotly_dark')
fig.update_layout(title='Samsung Value')
fig.update_layout(width=1100, height=500)
fig.update_yaxes(title_text='거래량', secondary_y=False)
fig.update_yaxes(title_text='주가', secondary_y=True)
fig.show()

# 배당금 데이터 =====
import yfinance as yf
div = yf.Ticker('0').dividends  # 0 은 '리얼티인컴'이라는 회사임
div
div.plot(figsize=(12,6))  # 주식분할(1주->2주) 미반영(배당금은 50%로 줄어든것으로 보임, 총배당금은 동일)

data.index = data.index.strftime('%Y-%m-%d')  # 타임라인 인덱스 형태 변경
div['2018':].plot(kind='bar', figsize=(15,7))

# plotly로 그리기
import plotly.express as px
code = 'AAPL'
start = '2015'
end = '2020'
aapl = yf.Ticker(code).dividends[start:end]
x_line = aapl.index
y_line = aapl
fig = px.bar(x=x_line, y=y_line)
fig.update_layout(bargap=0.5)  # 바간격
fig.update_layout(width=1100, height=500)
fig.update_layout(template='plotly_dark')
fig.update_layout(title='애플주당배당금')
fig.update_yaxes(title_text='배당금')
fig.update_xaxes(title_text='날짜')

# 대시보드 =====
# 1.대시보드에 담고 싶은 데이터 종류들을 리스트에 입력한다
# 2.종목데이터를 딕셔너리에 순서대로 담는다
# 3.딕셔너리에 종목을 추가한다
# 4.대시보드(데이터프레임) 만든다
# 사용데이터는 ARCC(아레스캐피탈)이다

import pandas as pd
dash_list = ['종목코드','업종','보유주식수','국가']
dash_dic = {'삼성전자':['005930.KS','IT','100','한국']}
dash_dic['테슬라'] = ['TSLA','자동차','2','미국']
dash = pd.DataFrame(data=dash_dic, index=dash_list)
dash
dash.T

dash.loc['종목코드']
dash.iloc[0]

# 사례 연습 =====
import pandas as pd
import yfinance
dash_list = ['종목명','현재주가','전일주가','일일변동율(%)']  # 인덱스는 리스트 활용
code = 'ARCC'
arcc = yfinance.Ticker(code)['Close']
current_price = arcc.iloc[-1]
previous_price = arcc.iloc[-2]
oneday_change = (current_price - previous_price)/previous_price * 100
dash_data = {'ARCC':['아레스캐피탈',current_price,previous_price,oneday_change]}  # 데이터는 딕셔너리 활용
dash = pd.DataFrame(data=dash_data, index=dash_list)
dash
dash.T

# 최고가, 최저가 연습 =====
import pandas as pd
idx = ['회사이름','현재주가']
dict = {'MSFT':['마이크로소프트', 5000]}
df = pd.DataFrame(data=dict, index=idx)
dash = df.T
dash

ticker = 'MSFT'
ms_close = yfinance.Ticker(ticker).Close
ms_close

# 52주 최고 최저 추출: Rolling 함수
# 직전 252일치 중 최고값 계산, min_periods=1 옵션은 처음 2일은 1일치라고 계산해서 NaN 을 채움
# 주말, 휴일 등 실제 운영일로 계산하면 52주는 252일로 계산됨(또는 5*52=260 쓰기도 함)
high_52 = ms_close.rolling(252, min_periods=1).max()
now_52max = high_52.iloc[-1]  # 최근 일자의 52최고가
now_52max

low_52 = ms_close.rolling(252, min_periods=1).min()
now_52min = low_52.iloc[-1]  # 최근 일자의 52최저가
now_52min

dash['52주최고가'] = now_52max
dash['52주최저가'] = now_52min
dash.round(2)
dash.index.name = '종목코드'
dash.rename(cloumns={'회사이름':'종목명'},inplace=True)
dash = dash.reindex(cloumns=['종목명','현재주가','52주최저가','52주최고가'])
dash
dash.plot().grid()

new = dash.copy()
del new['종목명']
new

# 이동평균 만들기 =====
snp500 = yfinance.Ticker('^GSPC').Close
snp500.head(3)

ma_180 = snp500.rolling(180,min_periods=1).mean()
ma_60 = snp500.rolling(60,min_periods=1).mean()
ma_20 = snp500.rolling(20,min_periods=1).mean()

df_price = pd.DataFrame(snp500)
df_price['180MA'] = ma_180
df_price['60MA'] = ma_60
df_price['20MA'] = ma_20
df_price.tail()

df_price.plot(figsize=(15,7)).grid(axis='y')

import plotly.express as px
px.line(df_price)

# 종합 =====
tiker = '005930.KS'
company = '삼성전자'
idx = ['회사명','현재주가','전일자주가','일간변동율(%)',
       '연초주가','연초대비수익률(%)',
       '52주최고가','52주최저가',
       '180일 이동평균','60일 이동평균']
close = yfinance(ticker).Close
cur_price = close.iloc[-1]
previous_price = close.iloc[-1]
oneday_change = (cur_price-previous_price)/previous_price * 100
first_2020 = close['2020'].iloc[0]
ytd = (cur_price-first_2020)/first_2020 * 100
high52 = close.rolling(252).max().iloc[-1]
low52 = close.rolling(252).min().iloc[-1]
ma_180d = close.rolling(180).mean().iloc[-1]
ma_60d = close.rolling(60).mean().iloc[-1]
dic_data = {ticker:[company, cur_price,previous_price,oneday_change,first_2020,ytd,high52,low52,ma_180d,ma_60d]}
dash = pd.DataFrame(index=idx,data=dic_data).T

# PER 추가하기 =====
aapl_info = yf.Ticker('AAPL').info
aapl_info

aapl_info['sector']
aapl_info['priceToBook']
aapl_info['forwardPE']

dash['PER'] = aapl_info['forwardPE']
