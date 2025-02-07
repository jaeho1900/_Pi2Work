import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# 데이터 입력
data = {
    '상품': ['A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 
             'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D', 'A', 'B', 'C', 'D'],             
    '정량': [54, 100, 91, 87, 44, 50, 56, 76, 66, 50, 58, 63, 
             66, 93, 64, 65, 58, 81, 48, 89, 69, 52, 99, 43],
    '정성': [67, 98, 37, 69, 55, 85, 73, 63, 31, 32, 27, 78, 
             36, 33, 40, 42, 67, 41, 29, 65, 37, 100, 88, 27],
    '평가월': [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 
             4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 차트 그리기
plt.figure(figsize=(10, 6))

# 각 상품에 대해 분산형 차트 추가
for product in df['상품'].unique():
    subset = df[df['상품'] == product]
    plt.scatter(subset['정량'], subset['정성'], label=product)

# 레이블 추가
for i in range(len(df)): # 행 개수만큼 순회
    row = df.iloc[i] # 한 행씩 꺼내기
    name = row['평가월'] # 이름이 저장된 열
    x = row['정량'] # x좌표가 저장된 열
    y = row['정성'] # y좌표가 저장된 열
    plt.text(x, y, name, size=20, va='center', ha='center')


# 차트 제목 및 축 레이블 설정
plt.title('정량 vs 정성')
plt.xlabel('정량')
plt.ylabel('정성')
plt.legend(title='상품')
plt.grid(True)

# 차트 표시
plt.show()
