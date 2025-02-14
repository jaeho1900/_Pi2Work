import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("./salesactivity.csv",
    usecols=[0,3,4]
    )
# df_csv['작성일자'] = pd.to_datetime(df_csv['작성일자'], format="%Y-%m-%d")
df.info()
df.head()

# tree plot -----
import plotly.express as px
c1 = df.value_counts('Product').to_frame('count').reset_index()
fig = px.treemap(c1, path=['Product'],
    values='count',
    color='count', 
    color_continuous_scale='dense'
    )
fig.data[0].textinfo = 'label+text+value'
fig.layout.hovermode = False
fig.update_layout(coloraxis_showscale=False)
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()

# heatmap plot -----
# 1. 작성일자를 datetime 형식으로 변환
df['작성일자'] = pd.to_datetime(df['작성일자'])

# 2. 년월 컬럼 생성
df['년월'] = df['작성일자'].dt.to_period('M')

# 3. Product별, 년월별 집계
monthly_counts = df.groupby(['년월', 'Product']).size().unstack(fill_value=0)

# 4. 24년 1월부터 25년 2월까지의 데이터만 선택
start_date = pd.Period('2024-01')
end_date = pd.Period('2025-02')
monthly_counts = monthly_counts.loc[start_date:end_date]

# 5. Product별 총합계 계산 및 정렬
product_totals = monthly_counts.sum().sort_values(ascending=False)

# 6. 정렬된 순서대로 데이터 재정렬
monthly_counts = monthly_counts[product_totals.index]

# 7. Seaborn을 사용한 시각화
plt.figure(figsize=(15, 7))
sns.heatmap(monthly_counts.T[:14], cmap='YlOrRd', annot=True, fmt='d')
# plt.figure(figsize=(15, 16))
# sns.heatmap(monthly_counts.T, cmap='YlOrRd', annot=True, fmt='d')
plt.title('Product별 월간 발생 횟수 (2024년 1월 - 2025년 2월)')
plt.xlabel('년월')
plt.ylabel('Product')
plt.tight_layout()
plt.show()

# ■ groupby
# >> 같은 값을 한 그룹으로 묶어서 여러 가지 연산을 하는 함수.
# >> 기본 구조
# df.groupby(컬럼명, as_index = True).함수
# >> parameter
# as_index: 그룹으로 묶을 컬럼을 인덱스로 해서 시리즈형태로 출력(True), 데이터프레임으로 출력(False)
# >> 함수
# size() : 각 그룹의 전체 행의 개수
# count() : 각 그룹의 각 열에서 NaN이 아닌 데이터의 수
# nunique() : 행의 유니크한 개수
# sum : 합
# mean() : 평균
# max() : 최댓값
# min() : 최솟값
# std() : 표준편차
# var() : 분산
# apply(list) : 값들을 리스트 형태로 변환

# line plot -----
# '작성일자'를 datetime 형식으로 변환
df['작성일자'] = pd.to_datetime(df['작성일자'])

# 발생월을 기준으로 집계
df['발생월'] = df['작성일자'].dt.to_period('M').dt.to_timestamp()  # Period를 Timestamp로 변환
monthly_counts = df.groupby(['발생월', 'Product']).size().unstack(fill_value=0).reset_index()

print(monthly_counts)

# 발생월을 기준으로 시각화
plt.figure(figsize=(12, 6))
monthly_counts_long = monthly_counts.melt('발생월', var_name='Product', value_name='Count')
sns.lineplot(data=monthly_counts_long, x='발생월', y='Count', hue='Product', marker='o')
plt.title('2024년 1월부터 2025년 2월까지 제품별 월별 발생량')
plt.xlabel('발생월')
plt.ylabel('발생량')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

