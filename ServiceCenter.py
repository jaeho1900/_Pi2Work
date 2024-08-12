import pandas as pd
import matplotlib.pyplot as plt

import platform
if platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic')
elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

# >>> 데이터 프레임 -----

df = pd.read_excel('./ADP_ver01/서비스센터 월간 보고서_5월.xlsx',
                   sheet_name='엣지공수데이터 5월',
                   usecols='C:H,L,M')
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
df = df[~df['일자'].isin(pd.to_datetime(['2024-05-01', '2024-05-06', '2024-05-15', '2024-05-31']))]

df.columns
# ['구분', 'WBS', '서비스센터', '작업일자', 'Patrol인원',
# '계약공간', '작업시간(분)', '이동시간(분)', '일자', '요일']

# >>> [가설1] 작업건별 출동인원수? -----

gdf1 = df.groupby(['계약공간', '작업일자']).agg({'Patrol인원' : 'count'})
gdf1 = gdf1.groupby('Patrol인원').agg({'Patrol인원' : 'count'})

plt.figure(figsize=(5, 5))
gdf1.plot(kind='bar', legend='')
plt.ylabel('출동건수', fontsize=10, color='black')
plt.xlabel('작업조원수', fontsize=10, color='black')
plt.xticks(rotation=0, ha='center')
plt.show()

gdf1['Patrol인원'].plot(kind = 'pie',
                        autopct = '%.1f%%', # 퍼센트 표시
                        startangle = 60, # 시작점(오른쪽 경계선이 3시 부터 반시계방향으로 증가 이동)
                        colors=['g', 'c', 'r'],
                        labels=['1명', '2명', '3명'],
                        explode=[0, 0, 0.2], # 조각 띄어내기
                        wedgeprops={'width': 0.5, 'edgecolor': 'gray', 'linewidth': 1}, # 부채꼴 스타일
                        ylabel='')
plt.show()

# >>> [가설2] 이동시간 과다? -----

gdf2 = df.groupby(['계약공간', '작업일자']).agg({'이동시간(분)' : 'mean'})
long_travel = gdf2['이동시간(분)'].quantile(0.90)

plt.hist(gdf2['이동시간(분)'], bins=20, color='c')
plt.xlabel('이동시간(분)')
plt.ylabel('빈도수(건)')
plt.vlines(long_travel, 125, 0, color='gray', linestyle='--', linewidth=1)
plt.show()

# 이동시간이 길었던 작업들
long_travel_10 = gdf2[gdf2['이동시간(분)'] > gdf2['이동시간(분)'].quantile(0.90)]
print(long_travel_10)  # 지연상위 10% : 64건 추출

# >>> [가설3] 작업시간에 따른 이동시간 생산성? -----

gdf3 = df.groupby(['계약공간', '작업일자']).agg({'작업시간(분)' : 'mean', '이동시간(분)' : 'mean'})
gdf3['생산성비율'] = round(gdf3['작업시간(분)'] / (gdf3['이동시간(분)'] + gdf3['작업시간(분)']) * 100, 1)
nor_Activity = gdf3[gdf3['생산성비율'] >= 30]
low_Activity = gdf3[gdf3['생산성비율'] < 30]

plt.figure(figsize=(6, 5))
plt.scatter(nor_Activity['이동시간(분)'], nor_Activity['작업시간(분)'])
plt.scatter(low_Activity['이동시간(분)'], low_Activity['작업시간(분)'], color='r')
plt.xlabel("이동시간(분)")
plt.ylabel("작업시간(분)")
plt.show()

# >>> [가설4] 요일별 작업시간과 이동시간 -----

gdf4 = df.groupby('요일').agg({'작업시간(분)' : 'mean', '이동시간(분)': 'mean'})
gdf4.index = [x[:3] for x in gdf4.index]
weekday_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
gdf4 = gdf4.reindex(weekday_order)
work_avg = gdf4['작업시간(분)'].mean()
travel_avg = gdf4['이동시간(분)'].mean()
print("작업시간평균(분): ", work_avg)     # 123.5
print("이동시간평균(분): ", travel_avg)   # 73.7

plt.figure(figsize=(6, 5))
plt.plot(gdf4.index, gdf4, label=['작업시간', '이동시간'], marker='o')
plt.hlines(work_avg, 0, 4, color='gray', linestyle='--', linewidth=1)
plt.hlines(travel_avg, 0, 4, color='gray', linestyle='--', linewidth=1)
plt.legend (loc='center left')
plt.ylabel('시간(분)', fontsize=10, color='black')
plt.show()
