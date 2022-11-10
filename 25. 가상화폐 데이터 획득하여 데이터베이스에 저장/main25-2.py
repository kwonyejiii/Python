#비트코인 데이터베이스 읽어와서 저장

from itertools import count
import pyupbit
import sqlite3

# 가져 올 가상화폐 데이터
ticker = 'KRW-BTC'	# 비트코인
interval = 'minute1'	# 1분 단위
to = '2021-12-02 12:20'	# 12월 02일 11시 20분 까지
# 이전 200개의 데이터

# 가상화폐 데이터 가져오기
count = 200
price_now = pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

# 데이터베이스 연결, 데이터 저장하기
db_path = r"C:\Python\25. 가상화폐 데이터 획득하여 데이터베이스에 저장\coin.db"
con = sqlite3.connect(db_path, isolation_level=None)
price_now.to_sql('BTC', con, if_exists='append') 

# 데이터베이스 연결 종료
con.close

