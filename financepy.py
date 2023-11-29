"""
# #  함수 업그레이드 변경 
import pandas_datareader, import pandas_datareader.data as pdr --> import yfinance as yf
pdr.get_data_yahoo('종목코드') --> yf.download('종목코드')  # 야후종목
"""
from urllib import parse
from ast import literal_eval
import requests

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
    
get_sise('005930', '20210601', '20210605', 'day')


# =======================
import yfinance as yf

samsung = yf.download('005930.KS')
close = samsung['Close']
close['2019']
close['2019-08']
close['2019':'2020']
close['2019':'2020'].plot(figsize=(15,7), color='red').grid()

import plotly.express as px
vol = samsung.Volume
px.line(x=vol.index, y=vol)



