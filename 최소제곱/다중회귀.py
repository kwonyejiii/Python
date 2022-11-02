import numpy as np
import matplotlib.pyplot as plt #그래프

#공부시간 x와 성적 y의 넘파이 배열을 만듬
x1 = np.array([2,4,6,8])
x2 = np.array([0,4,2,3])
y = np.array([81,93,91,97])

# 데이터의 분포를 그래프로 나타냄
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter3D(x1,x2,y)
plt.show()

# 기울기 a의 값과 절편 b의 값을 초기화
a1 = 0
a2 = 0
b = 0
# 학습률을 정함 (값 바꿔보기!)-> print에 학습률도 넣기
lr = 0.01
# 몇 번 반복될지 설정 (값 바꿔보기!)
epochs = 2001
# x 값이 총 몇 개인지 셈
n = len(x1)

# '경사하강법' 시작

for i in range(epochs):    #에포크 수만큼
    y_pred = a1*x1 +a2*x2 +b     # 예측값 구하는 식
    error = y- y_pred   # 실제 값과 비교한 오차를 error로 놓습니다.

    a1_diff = (2/n) * sum(-x1 *(error))   #오차함수를 a로 편미분한 값
    a2_diff = (2/n) * sum(-x2 *(error))
    b_diff = (2/n) * sum(-(error))      #오차함수를 b로 편미분한 값

    a1 = a1 - lr* a1_diff  #학습률을 곱해 기존의 a값을 업데이트 (오차값줄이기)
    a2 = a2 - lr* a2_diff
    b = b - lr* b_diff

    if i % 100 == 0: # 100번 반복될 때마다 현재의 a값, b값을 출력합니다.
        print("epoch = %.f, 기울기1 = %.04f, 기울기2 = %.04f, 절편 = %.04f" % (i, a1,a2, b))

# 실제 점수와 예측된 점수를 출력
print("실제 점수: ", y)
print("예측 점수: ", y_pred)