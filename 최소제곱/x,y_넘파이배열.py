import numpy as np
# 넘파이: 수학 연산과 분석을 하게해주는 라이브러리
# 공부한 시간과 점수를 각각 x,y라는 이름의 넘파이 배열을 만듭니다.
x= np.array([2,4,6,8])
y= np.array([81,93,91,97])
print(x,y)

#최소제곱근 공식으로 기울기a의 값과 y절편 b의 값을 구해보자
    #mean() : 평균구하는 넘파이함수 # mx변수에는 x원소의 편균값을 넣음
mx = np.mean(x)
my = np.mean(y)    
print(mx,my)

# 최소제곱근의 공식중 "분모값" = "x"의 각 원소와 x의 평균값들의 차를 제곱하라" 명령어 만들기
# divisor변수를 만들어 구현
divisor = sum([(i-mx)**2 for i in x])
print(divisor)
# 최소제곱근의 공식중 "분자값"= x와 y의 편차를 곱해서 합한 값을 구함
# diviedend 변수에 분자값 저장
def top(x, mx, y, my):
    d =0
    for i in range(len(x)):
        d += (x[i]-mx)*(y[i]-my)
    return d
dividend =top (x, mx, y, my)   
print(dividend)

#기울기 a
a = dividend/divisor
print(a)
#y절편 b
b= my - (mx*a)
print(b)


# 선형회귀하는이유?: '연속된 숫자'가 있을때 eg)공부시간x(독립변수)dp eogks 성적을 예측하는 데이터가 있다고 가정할때, 그 그래프의 예측값을 찾고자할때 선형회귀분석을하는데 여기에   기울기와 y절편을 구하기위해서(=예측선을 그리기위해) 바로 알 수 없기 때문에 최소제곱법을 이용하여 예측

# 예측선을 긋는다. 연속된 숫자가 있을때 예측하고싶어서 선형회귀를 한다.
#                 기울기와 y절편을 구하기위해서 최소제곱법을 사용
