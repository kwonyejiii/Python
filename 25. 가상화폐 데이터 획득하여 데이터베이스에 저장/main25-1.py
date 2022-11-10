import pyupbit

coin_lists = pyupbit.get_tickers(fiat='KRW')
print(coin_lists)

price_now = pyupbit.get_current_price(["KRW-BTC", "KRW-ETH"])
print(price_now)

# =>다양한 가상화폐 정보들과 마지막에 BTC, ETH 가격정보