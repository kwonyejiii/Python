import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from currency_converter import CurrencyConverter


def get_exchange_rate(target1, target2):
    URL = f"https://kr.investing.com/currencies/{target1}-{target2}"
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url=URL)
    price = driver.find_element_by_css_selector(
        "#__next > div > div > div > div.grid.gap-4.tablet\:gap-6.grid-cols-4.tablet\:grid-cols-8.desktop\:grid-cols-12.grid-container--fixed-desktop.general-layout_main__3tg3t > main > div > div.instrument-header_instrument-header__1SRl8.mb-5.bg-background-surface.tablet\:grid.tablet\:grid-cols-2 > div:nth-child(2) > div.instrument-price_instrument-price__3uw25.flex.items-end.flex-wrap.font-bold > span"
    )
    print(f"{target1}/{target2}환율 정보{price.text}")
    driver.close()


cc = CurrencyConverter()
print(f"지원하는 통화{cc.currencies}")  # 지원 되는 통화 목록 확인

a = input("어떤 화폐를 알고싶나요?")
b = input("어떤 통화로 바꿀까요?")
a = a.lower()  # 사이트에 전달해주는 값이 소문자일때만 정상 적으로 값을 불러오기떄문에 입력받은값 소문자 전환
b = b.lower()
get_exchange_rate(f"{a}", f"{b}")