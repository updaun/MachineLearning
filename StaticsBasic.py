import numpy as np
from scipy import stats

# 무작위 난수 출력시 같은 무작위 수를 제작 (통제 가능 제한적 공간)
np. random.seed(0)

# 0부터 100까지 10000개의 무작위 데이터 생성
data_A = np.random.randint(0, 100, 10000)
# 분포를 이룰 무작위 데이터 생성
data_B = np.random.normal(size = 100)

# 평균값 출력
mean = np.mean(data_A)
mean_b = np.mean(data_B)
# 중앙값 출력
median = np.median(data_A)
median_b = np.median(data_B)
# 최빈값 출력
mode = stats.mode(data_A)
mode_b = stats.mode(data_B)

# data_A
print("평균값 : ", mean.round(2))
print("중앙값 : ", median)
print("최빈값 : {} ( {} )".format(mode[0][0], mode[1][0]) )
print()
# data_B
print("평균값 : ", mean_b.round(2))
print("중앙값 : ", median_b)
print("최빈값 : {} ( {} )".format(mode_b[0][0], mode_b[1][0]) )
print()

# numpy의 var(), std() 활용하여 분산, 표준편차 출력
data_A_var = np.var(data_A)
data_A_std = np.std(data_A)

# 분산은 값이 너무 커서 비교가 쉽지 않다.
print("분산 : ", data_A_var.round(2))
print("표준편차 : ", data_A_std.round(2))