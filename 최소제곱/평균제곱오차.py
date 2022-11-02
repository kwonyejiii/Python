# <평균제곱오차> = 선의 오차 평가방법 = 오차의합/n (원소의 총 개수)
# 여러개의 입력을 처리하기 용이, 가설세우고 최소오차까지 수정해나가기
# 전 후 선의 각 오차를 계산하고 오차가작은쪽으로 바꾸는 알고리즘 필요
# 오차 =실제값(y) - 예측값(x를 식에 대입해서 나온 값)=>각오차값을 제곱해줌!(부호제거) : '평균제곱오차'

#구한 평균제곱오차보다 작은값을가지는 a,와b값을 찾으면됨
#(결론) '선형회귀': 임의의 직선을 그어 평균제곱오차를 구하고, 
#                   이 값을 작게 만들어주는 a,b값을 찾아가는 작업

import numpy as np
x= np.array([2,4,6,8])
y= np.array([81,93,91,97])
# fake_ : 가상의 기울기 a, y절편인 함수식 predict()정의
fake_a =3
fake_b = 76
def predict(x):
    return fake_a * x + fake_b

# 위 결과값이 들어가는 빈리스트 생성
predict_result =[]
#모든 x값을 predict()한번식대입해 예측값 리스트 채우는 코드 작성
for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("공부시간=%.f, 실제점수=%.f, 예측점수=%.f, " % (x[i], y[i] , predict(x[i])))

# 평균 제곱 오차 함수
n = len(x)
def mse(y, y_pred):
    return (1/n) * sum((y - y_pred)**2)
# 평균 제곱 오차 값을 출력합니다. 
print("평균 제곱 오차: " + str(mse(y,predict_result)))