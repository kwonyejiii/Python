import numpy as np
import matplotlib.pyplot as plt #그래프

#공부시간 x와 성적 y의 넘파이 배열을 만듬
x = np.array([2,4,6,8])
y = np.array([81,93,91,97])

# 데이터의 분포를 그래프로 나타냄
plt.scatter(x,y)
plt.show()
# 기울기 a의 값과 절편 b의 값을 초기화
a = 0
b = 0
# 학습률을 정함 (값 바꿔보기!)-> print에 학습률도 넣기
lr = 0.003
# 몇 번 반복될지 설정 (값 바꿔보기!)
epochs = 2001
# x 값이 총 몇 개인지 셈
n = len(x)

# '경사하강법' 시작

for i in range(epochs):    #에포크 수만큼
    y_pred = a*x +b     # 예측값 구하는 식
    error = y- y_pred   # 실제 값과 비교한 오차를 error로 놓습니다.

    a_diff = (2/n) * sum(-x *(error))   #오차함수를 a로 편미분한 값
    b_diff = (2/n) * sum(-(error))      #오차함수를 b로 편미분한 값

    lr = 0.03          #학습률을 정함

    a = a - lr* a_diff  #학습률을 곱해 기존의 a값을 업데이트 (오차값줄이기)
    b = b - lr* b_diff

    if i % 100==0: # 100번 반복될 때마다 현재의 a값, b값을 출력합니다.
        print("학습률 = %.02f, epoch=%.f, 기울기 = %.04f, 절편 = %.04f" % (lr,i, a, b))

# 앞서 구한 최종 a값을 기울기, b 값을 y절편에 대입해 그래프를 그림
y_pred = a*x + b

#그래프 출력
plt.scatter(x,y)
plt.plot(x, y_pred,'r')
plt.show()