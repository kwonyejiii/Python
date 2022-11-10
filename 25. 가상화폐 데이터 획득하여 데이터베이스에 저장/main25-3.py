import pandas as pd # 데이터베이스 읽을 때 사용할 라이브러리
import sqlite3

# 데이터베이스 연결하고 데이터 가져오기
db_path = r"C:\Python\25. 가상화폐 데이터 획득하여 데이터베이스에 저장\coin.db"
con = sqlite3.connect(db_path, isolation_level=None)

readed_df = pd.read_sql("SELECT * FROM 'BTC'", con, index_col = 'index')

print(readed_df)

#  =>
#  - DB에 저장된 비트코인 데이터

# - 23시 58분까지 저장되었다. ?? 해당 시간 미만으로 나오는 듯

# - 200개 데이터 저장

