# 평균제곱오차 = 손실함수
# 경사하강법 = 옵티마이저

import numpy as np
import matplotlib.pyplot as plt #그래프

#텐션플로의 케라스 API에서 필요한 함수들을 불러옴
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

#공부시간 x와 성적 y의 넘파이 배열을 만듬
x = np.array([2,4,6,8])
y = np.array([81,93,91,97])

model = Sequential()

# 출력값, 입력변수, 분석방법에 맞게끔 모델을 설정
model.add(Dense(1, input_dim=1, activation='linear'))

# 오차 수정을 위해 경사하강법(sgd)을, 오차의 정도를 판단하기 위해
# 평균 제곱 오차(mse)를 사용
model.compile(optimizer='sgd', loss='mse')

# 오차를 최소화하는 과정을 2000번 반복
model.fit(x,y,epochs=2000)

# 데이터의 분포를 그래프로 나타냄
plt.scatter(x,y)
plt.plot(x, model.predict(x), 'r')      #예측 결과를 그래프로 나타냄
plt.show()
# 기울기 a의 값과 절편 b의 값을 초기화
a = 0
b = 0

# 임의의 시간을 집어넣어 점수를 예측하는 모델을 테스트해 보겠습니다.
hour = 7
prediction = model.predict([hour])
print("%.f시간을 공부할 경우의 예상 점수는 %.02f점 입니다." % (hour, prediction))