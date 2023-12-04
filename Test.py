import yfinance as yf

# 삼성전자(005930.KS)의 주가 데이터 가져오기
ticker = "005930.KS"
stock_info = yf.Ticker(ticker)

# 기본 정보 조회
print(stock_info.info)

# 주가 데이터 가져오기 (날짜 범위 설정 가능)
historical_data = stock_info.history(period="1y")
print(historical_data)