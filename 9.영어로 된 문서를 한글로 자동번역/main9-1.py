<<<<<<< HEAD
# 영어로 된 문서를 한글로 자동변역

from unittest import result
import googletrans

translator = googletrans.Translator()

str1 ="행복하세요"
result1 =translator.translate(str1, dest='en', src='auto')
print(f"행복하세요=>{result1.text}")

str2 ="I am happy"
result2 = translator.translate(str2, dest='ko', src='en')
=======
# 영어로 된 문서를 한글로 자동변역

from unittest import result
import googletrans

translator = googletrans.Translator()

str1 ="행복하세요"
result1 =translator.translate(str1, dest='en', src='auto')
print(f"행복하세요=>{result1.text}")

str2 ="I am happy"
result2 = translator.translate(str2, dest='ko', src='en')
>>>>>>> 46be12439aef1acc1b128cc53dc407bca81bab44
print(f"I am happy => {result2.text}")