"""
# #  함수 업그레이드 변경 
import pandas_datareader, import pandas_datareader.data as pdr --> import yfinance as yf
pdr.get_data_yahoo('종목코드') --> yf.download('종목코드')  # 야후종목
import yfinance as yf
samsung = yf.download('005930.KS')
"""

from urllib import parse
from ast import literal_eval
import requests
import pandas as pd
import numpy as np
import matplotlib

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
close = df['종가']
close['2020']
close['2021-08']
close['2020':'2021']
close['2020':'2021'].plot(figsize=(15,7), color='red').grid()

import plotly.express as px
vol = df.거래량
px.line(x=vol.index, y=vol)
