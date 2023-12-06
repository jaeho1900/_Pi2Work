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

# 데이터 검색 방법=====
close = df['종가']
close['2020']
close['2021-08']
close['2020':'2021']

# 그래프 그리기=====
# 그래프1
close['2020':'2021'].plot(figsize=(15,7), color='red').grid()

# 그래프2
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

fig  # 그래프가 저장되어 있어서 호출하면 그래프를 반환

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

# # 배당금 데이터=====
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

# # 대시보드=====
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


# 사례 연습
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

# 최고가, 최저가 연습
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





