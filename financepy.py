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

# =======================
# 검색방법
close = df['종가']
close['2020']
close['2021-08']
close['2020':'2021']

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

# ===================
import yfinance as yf

div = yf.Ticker('0').dividends  # 0 은 '리얼티인컴'이라는 회사임
div
div.plot(figsize=(12,6))  # 주식분할 미반영

div['2018':].plot(kind='bar', figsize=(15,7))






# 타임라인 인덱스 형태 변경

data.index = data.index.strftime('%Y-%m-%d')

