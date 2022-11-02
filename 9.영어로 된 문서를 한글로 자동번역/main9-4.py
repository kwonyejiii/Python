<<<<<<< HEAD

from distutils.file_util import write_file
from os import linesep
import googletrans


translator = googletrans.Translator()

read_file_path = r"9.영어로 된 문서를 한글로 자동번역/영어파일.txt"
write_file_path = r"9.영어로 된 문서를 한글로 자동번역/한글파일.txt"

with open(read_file_path, 'r') as f:
    readLines = f.readlines()
    
for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    with open(write_file_path, 'a', encoding='utf-8') as f:    #추가 모드('a')로 열고
        f.write(result1.text + '\n')

# f = open("foo.txt", 'w')
# f.write("Life is too short, you need python")
# f.close()
# 파일을 열면 위와 같이 항상 close해 주는 것이 좋다. 하지만 이렇게 파일을 열고 닫는 것을 자동으로 처리할 수 있다면 편리하지 않을까? 파이썬의 with문이 바로 이런 역할을 해준다. 다음 예는 with문을 사용해서 위 예제를 다시 작성한 모습이다.

# with open("foo.txt", "w") as f:
#     f.write("Life is too short, you need python")
=======

from distutils.file_util import write_file
from os import linesep
import googletrans


translator = googletrans.Translator()

read_file_path = r"9.영어로 된 문서를 한글로 자동번역/영어파일.txt"
write_file_path = r"9.영어로 된 문서를 한글로 자동번역/한글파일.txt"

with open(read_file_path, 'r') as f:
    readLines = f.readlines()
    
for lines in readLines:
    result1 = translator.translate(lines, dest='ko')
    print(result1.text)
    with open(write_file_path, 'a', encoding='utf-8') as f:    #추가 모드('a')로 열고
        f.write(result1.text + '\n')

# f = open("foo.txt", 'w')
# f.write("Life is too short, you need python")
# f.close()
# 파일을 열면 위와 같이 항상 close해 주는 것이 좋다. 하지만 이렇게 파일을 열고 닫는 것을 자동으로 처리할 수 있다면 편리하지 않을까? 파이썬의 with문이 바로 이런 역할을 해준다. 다음 예는 with문을 사용해서 위 예제를 다시 작성한 모습이다.

# with open("foo.txt", "w") as f:
#     f.write("Life is too short, you need python")
>>>>>>> 46be12439aef1acc1b128cc53dc407bca81bab44
# 위와 같이 with문을 사용하면 with 블록을 벗어나는 순간 열린 파일 객체 f가 자동으로 close되어 편리하다.