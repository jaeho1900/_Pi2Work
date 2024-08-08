import pandas as pd
import matplotlib.pyplot as plt
import platform

from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')    

# 데이터 프레임 
df = pd.read_excel('C:/Users/Administrator/Desktop/■서비스센터 월간 보고서_5월.xlsx',
                   sheet_name='엣지공수데이터 5월',
                   index_col=0,
                   usecols='A:H,L,M')
print(df)

# 결측값 확인
print(df.isnull().sum())

# 기본 통계량
print(df.describe())

# 데이터 정제
df = df[df['구분'] != '출동대기']
df = df[df['서비스센터'].str.contains('서비스센터')]

df['일자'] = pd.to_datetime(df['작업일자'])
df['요일'] = df['일자'].dt.day_name()

df = df[~df['요일'].isin(['Saturday', 'Sunday'])]
df = df[~df['일자'].isin(['2024-05-01', '2024-05-06', '2024-05-15', '2024-05-31'])]


# >>> 시각화 분석 -----

# 요일별 작업시간과 이동시간
gdf = df.groupby('요일').agg({'작업시간(분)' : 'mean', '이동시간(분)': 'mean'})
gdf.index = [x[:3] for x in gdf.index]
weekday_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
gdf = gdf.reindex(weekday_order)
work_avg = gdf['작업시간(분)'].mean()
travel_avg = gdf['이동시간(분)'].mean()

plt.figure(figsize=(10, 5))
ax1 = plt.subplot(111)
ax1.plot(gdf.index, gdf, label=['작업시간', '이동시간'])
ax1.legend (loc='best')
ax1.set_ylabel('시간(분)', fontsize=10, color='black')
ax1.set_xlim(-0.1, 4.5)

ax2 = plt.subplot(111)
# ax2 = ax1.twinx()
ax2.hlines(work_avg, 0, 4, color='gray', linestyle='--', linewidth='1', label='평균작업시간')

ax3 = plt.subplot(111)
# ax3 = ax1.twinx()
ax3.hlines(travel_avg, 0, 4, color='gray', linestyle='--', linewidth='1', label='평균이동시간')
plt.show()





# 작업시간 분포
plt.hist(df['작업시간(분)'], bins=20)
plt.title('작업시간 분포')
plt.xlabel('작업시간(분)')
plt.ylabel('빈도수')
plt.show()

# 이동시간 분포
plt.hist(df['이동시간(분)'], bins=20)
plt.title('이동시간 분포')
plt.xlabel('이동시간(분)')
plt.ylabel('빈도수')
plt.show()

# 작업시간과 이동시간 분포
plt.figure(figsize=(10, 6))
plt.scatter(df["이동시간(분)"], df["작업시간(분)"])
plt.legend()
plt.xlabel("이동시간(분)")
plt.ylabel("작업시간(분)")
plt.show()

# # 이동시간이 길었던 작업들
# long_travel = df[df['이동시간(분)'] > df['이동시간(분)'].quantile(0.75)]
# print(long_travel)




# 생산성(작업생산성) 비율
df['생산성비율'] = round(df['작업시간(분)'] / (df['이동시간(분)'] + df['작업시간(분)']) * 100, 1)
print(df[['계약공간', '생산성비율']])






# 시간 분석
df.groupby('서비스센터')["작업시간(분)"].sum().plot(kind="bar")
df.groupby('작업일자')["작업시간(분)"].sum().plot(kind="bar")


# # scatter plot ----------
plt.scatter (x=df.x, y=df.y, s=20, c='r', alpha=0.5)
plt.scatter (x=df.x, y=df.y, s=df.z * 100, c='r', alpha=0.5) # 버블 차트(3변수)
df.plot (kind='scatter', x='x', y='y', s=200, c='r', alpha=0.5) # x, y 데이터에는 '열이름' 만 입력(df.열이름 x)
df.plot (kind='scatter', x='x', y='y', s=df.z * 100, c='r', alpha=0.5) # s 데이터에는 df.열이름

# # box plot ----------
plt.boxplot (df.y)
df.y.plot (kind='box', vert=False)

# # bar plot ----------
df.plot (kind='bar', color=['b', 'g', 'c'], stacked=True)
df.iloc [1].plot(kind='barh', color=['b', 'g', 'c'])
plt.bar ( np.arange (4), df.y, width=0.5, color='c', edgecolor="gray", linewidth=2, tick_label=[0, '갑', '을', '병'])
plt.barh ( np.arange (4), df.y, height=-0.6, align='edge', color='c', edgecolor="gray", linewidth=2,
tick_label=[0, '갑', '을', '병'])

# # pie plot ----------
df2 = pd.DataFrame ({'수입국': ['kO', 'JP', 'USA', 'kO', 'JP', 'USA', 'kO'],
'품명': ['banana', 'apple', 'mango', 'apple', 'apple', 'banana', 'apple']})
# 품명별 수입국 선적 횟수 비교 비율
df2['count'] = 1 # 카운트를 위한 임시 변수
df_py = df2.groupby (by='품명').sum()
df_py['count'].plot(kind='pie',
autopct='%.1f%%', # 퍼센트 표시
startangle=90, # 시작점(오른쪽 경계선이 3시 부터 반시계방향으로 증가 이동)
colors=['c', 'r', 'g'],
labels=['사과', '바나나', '망고'],
explode=[0, 0.2, 0], # 조각 띄어내기
wedgeprops={'width': 0.5, 'edgecolor': 'k', 'linewidth': 2} # 부채꼴 스타일
)
plt.pie (df_py['count'], autopct='%.1f%%', labels=['사과', '바나나', '망고'], startangle=90)
