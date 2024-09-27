import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 데이터
data = pd.read_excel(r"c:\Users\Administrator\Desktop\123.xlsx",
                     header=None,
                     names=["x", "y"])

# 기울기 계산
data['slope'] = np.gradient(data['y'], data['x'])

# 기울기 변화량 계산
data['slope_change'] = np.abs(np.gradient(data['slope'], data['x']))

# 기울기 변화량이 가장 큰 지점 찾기
top_changes = data.nlargest(7, 'slope_change')

# 결과 출력
print(top_changes[['x', 'y', 'slope', 'slope_change']])

# 그래프 그리기
plt.figure(figsize=(12, 6))
plt.plot(data.x, data.y, 'b-', label='데이터')
plt.scatter(top_changes.x, top_changes.y, color='red', s=100, label='Top 5 변화 지점')
plt.title('선형 그래프와 기울기 변화가 큰 지점')
plt.show()
