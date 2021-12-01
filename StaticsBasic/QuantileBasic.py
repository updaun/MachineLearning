# 사분위수(Quantile) = 데이터의 구성을 전체적으로 살펴보고자 할 때 사용

mport pandas as pd
# 데이터 시각화 패키지
import matplotlib.pyplot as plt

store_a = pd.Series([20,21,23,22,26,28,35,35,41,42,43,45,44,45,46,47,47,46,47,58,58,59,60,56,57,57,80])
# store_b = pd.Series([5,6,11,13,15,16,20,20,21,23,22,27,27,30,30,32,36,37,37,40,40,43,44,45,51,54,70,600])
# B사의 '600' 데이터 삭제 : 이상치
store_b = pd.Series([5,6,11,13,15,16,20,20,21,23,22,27,27,30,30,32,36,37,37,40,40,43,44,45,51,54,70])

# quantile()를 활용해 사분위수값 출력
A_Q1 = store_a.quantile(0.25) ; print("1사분위 수 : ", A_Q1)
A_Q2 = store_a.quantile(0.50) ; print("2사분위 수(중앙값) : ", A_Q2)
A_Q3 = store_a.quantile(0.75) ; print("3사분위 수 : ", A_Q3)
A_Q4 = store_a.quantile(1) ; print("4사분위 수 : ", A_Q4,"\n")

B_Q1 = store_b.quantile(0.25) ; print("1사분위 수 : ", B_Q1)
B_Q2 = store_b.quantile(0.50) ; print("2사분위 수(중앙값) : ", B_Q2)
B_Q3 = store_b.quantile(0.75) ; print("3사분위 수 : ", B_Q3)
B_Q4 = store_b.quantile(1) ; print("4사분위 수 : ", B_Q4,"\n")

# boxplot() 활용

# plt.boxplot((store_a))
# plt.grid()
# plt.show()

# B사 데이터의 박스플롯

# plt.boxplot((store_b))
# plt.grid()
# plt.show()

# 이상치 제거 후, 분석결과 비교
plt.boxplot((store_a,store_b))
plt.grid()
plt.show()

# IQR = 이상치 탐색, 데이터 분포 등을 확인할 때 유용
# box_num = pd.Series([16,21,22,23,24,25,30])

# plt.boxplot(box_num)
# plt.grid()
# plt.show()

# IQR = Q3 - Q1
# print("IQR : ", IQR)
# STEP1 = IQR * 1.5
# print("STEP1 : ", STEP1)

# => IQR : 3.0
# => STEP1 : 4.5

# Lower_fence = Q1 - STEP1
# print(Lower_fence) 

# => 17.0

# Upper_fence = Q3 + STEP1
# print(Upper_fence)

# => 29.0