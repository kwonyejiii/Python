#  원하는 날짜들의 비트코인 분봉정보 읽어와 저장하기 / 중복 데이터 제거하여 새로운 DB로 만들기

# - 'BTC' 에 원하는 정보를 모두 저장한 뒤

# - SELECT DISTINCT * FROM 'BTC' 를 사용해서 중복정보 제외하고 읽어와

# - 'BTC_NEW' 에 저장한다.

import pyupbit
import sqlite3
import datetime

def date_range(start, end):
    start = datetime.datetime.strptime(start, "%Y-%m-%d")
    start = start + datetime.timedelta(days=1)
    end = datetime.datetime.strptime(end, "%Y-%m-%d")
    end = end + datetime.timedelta(days=1) 
    dates = [(start + datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range((end-start).days+1)]
    return dates

dates = date_range("2021-11-30", "2021-12-01")

print(dates)

for day in reversed(dates):
    myDay = day + ' 00:00'
    print(myDay)

    ticker = 'KRW-BTC'
    interval = 'minute1'
    to = myDay
    count = 1440 
    price_now = pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

    print(price_now)

    db_path = r"C:\Python\25. 가상화폐 데이터 획득하여 데이터베이스에 저장\coin.db"

    con = sqlite3.connect(db_path, isolation_level=None)
    price_now.to_sql('BTC', con, if_exists='append')  

    con.close