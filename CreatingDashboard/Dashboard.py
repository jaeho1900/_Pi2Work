import streamlit as st
import requests
import pandas as pd
from lightweight_charts.widgets import StreamlitChart

if "symbols_list" not in st.session_state:
    st.session_state.symbols_list = None
    
st.set_page_config(
    layout = 'wide',
    page_title = 'Crypto Dashboard'
)

st.markdown(
    """
    <style>
        footer {display: none}
        [data-testid="stHeader"] {display: none}
    </style>
    """, unsafe_allow_html = True
)

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

api_key = 'YOUR TAAPI.IO API KEY'
        
title_col, emp_col, btc_col, eth_col, xmr_col, sol_col, xrp_col = st.columns([1,0.2,1,1,1,1,1])

with title_col:
    st.markdown('<p class="dashboard_title">Crypto<br>Dashboard</p>', unsafe_allow_html = True)

with btc_col:
    with st.container():
        btc_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=BTC/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="btc_text">BTC / USDT<br></p><p class="price_details">{btc_price}</p>', unsafe_allow_html = True)

with eth_col:
    with st.container():
        eth_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=ETH/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="eth_text">ETH / USDT<br></p><p class="price_details">{eth_price}</p>', unsafe_allow_html = True)

with xmr_col:
    with st.container():
        xmr_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XMR/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xmr_text">XMR / USDT<br></p><p class="price_details">{xmr_price}</p>', unsafe_allow_html = True)

with sol_col:
    with st.container():
        sol_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=SOL/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="sol_text">SOL / USDT<br></p><p class="price_details">{sol_price}</p>', unsafe_allow_html = True)

with xrp_col:
    with st.container():
        xrp_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XRP/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xrp_text">XRP / USDT<br></p><p class="price_details">{xrp_price}</p>', unsafe_allow_html = True)

params_col, chart_col, data_col = st.columns([0.5,1.2,0.6])

with params_col:
    
    with st.form(key = 'params_form'):
        
        st.markdown(f'<p class="params_text">CHART DATA PARAMETERS', unsafe_allow_html = True)
        
        st.divider()
        
        exchanges = ['binance', 'bitstamp', 'binancefutures', 'whitebit', 'bybit', 'gatetio', 'coinbase', 'binanceus', 'kraken']
        exchange = st.selectbox('Exchange', exchanges, key = 'exchange_selectbox')
        
        if st.session_state.symbols_list == None:
            symbols = []
            for i in exchanges:
                symbols_list = requests.get(f'https://api.taapi.io/exchange-symbols?secret={api_key}&exchange={i}').json()
                symbols.extend(symbols_list)
            symbol = st.selectbox('Symbol', symbols, key = 'symbol_selectbox')
            st.session_state.symbols_list = symbols
        else:
            symbol = st.selectbox('Symbol', st.session_state.symbols_list, key = 'symbol_selectbox')
        
        interval_col, period_col = st.columns(2)
        with interval_col:
            interval = st.selectbox('Interval', ['1m', '5m', '15m', '30m', '1h', '2h', '4h', '12h', '1d'], key = 'interval_selectbox')
        with period_col:
            period = st.number_input('Period', min_value = 10, max_value = 500, value = 365, step = 1, key = 'period_no_input')
        
        st.markdown('')
        update_chart = st.form_submit_button('Update chart')
        st.markdown('')
        
        if update_chart:
            url = f'https://api.taapi.io/candles?secret={api_key}&exchange={exchange}&symbol={symbol}&interval={interval}&period={period}&results=max'
            hist_json = requests.get(url).json()
            hist_df = pd.DataFrame(hist_json).drop('timestampHuman', axis = 1).rename(columns = {'timestamp':'time'})
            hist_df.time = pd.to_datetime(hist_df.time, unit = 's')

            with chart_col:

                with st.container():        
                    chart = StreamlitChart(height = 450, width = 650)
                    chart.grid(vert_enabled = True, horz_enabled = True)

                    chart.layout(background_color='#131722', font_family='Trebuchet MS', font_size = 16)

                    chart.candle_style(up_color='#2962ff', down_color='#e91e63',
                                       border_up_color='#2962ffcb', border_down_color='#e91e63cb',
                                       wick_up_color='#2962ffcb', wick_down_color='#e91e63cb')

                    chart.volume_config(up_color='#2962ffcb', down_color='#e91e63cb')
                    chart.legend(visible = True, font_family = 'Trebuchet MS', ohlc = True, percent = True)

                    chart.set(hist_df)
                    chart.load()
                    
            with data_col:
                    st.dataframe(hist_df, height = 470)