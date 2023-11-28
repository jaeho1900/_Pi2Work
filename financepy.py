"""
# #  함수 업그레이드 변경 
import pandas_datareader, import pandas_datareader.data as pdr --> import yfinance as yf
pdr.get_data_yahoo('종목코드') --> yf.download('종목코드')  # 야후종목
"""

import yfinance as yf
yf.download('005930.KS')
yf.download("AAPL")



from datetime import datetime as dt
import pytz
import streamlit as st
import yfinance as yf

tz = pytz.timezone("America/New_York")
start = tz.localize(dt(2013,1,1))
end = tz.localize(dt.today())

tickers = "MA,V,AMZN,JPM,BA".split(",")
df = yf.download(tickers,start, end, auto_adjust=True)['Close']

st.table(df.head())
