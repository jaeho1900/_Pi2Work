"""
_알람 데이터 분석
"""

import pandas as pd
import numpy as np
import copy
import re

odf = pd.read_excel('c:/Users/Administrator/Desktop/RMS2022.xlsx')
df = copy.deepcopy(odf)
df.shape[0]
# 관측치 25,167개

# # data shower ----------

# # 당일 중복 알람 삭제
df['tmp발생일자'] = df['발생일시'].str[0:10]
df = df.drop_duplicates(subset=['경보명', 'tmp발생일자'])
df.shape[0]
# 잔여관측치 17,034개

# # 점검조 작업 및 테스트 알람 삭제
df = df[~df.확인자.str.contains('점검조|테스트', na=False)]
df = df[~df.처리자.str.contains('점검조|테스트', na=False)]
df.shape[0]
# 잔여관측치 16,382개

# # 통신 불량 알람 삭제
df = df[~df.경보명.str.contains('통신단절|Disconnect|Timeout|원격관제모듈|SID', na=False)]
df.shape[0]
# 잔여관측치 15,240개

# # 전처리 ----------

# # 형변환
df['발생일시'] = pd.to_datetime(df['발생일시'], format='%Y/%m/%d %H:%M:%S')
df['확인일시'] = pd.to_datetime(df['확인일시'], format='%Y/%m/%d %H:%M:%S')

# # 대분류 추가
df['대분류'] = np.where(
    df.고객군.str.contains('GS리테일'), 'GS수퍼',
    np.where(df.고객군.str.contains('H&M'), 'H&M', '건물군'))

# # 컬럼분리
df.columns
ndf = copy.deepcopy(df[['대분류', '건물', '경보명', '발생일시', '확인일시']])

# # 결측값 대체
# 확인
ndf.isnull().sum()
ndf[ndf['확인일시'].isnull()]

# 해당 경보의 딜레이(확인소요) 평균시간으로 대체
ndf['delay'] = ndf['확인일시'] - ndf['발생일시']
ndf['delay'] = ndf.groupby('경보명')['delay'].transform(lambda g: g.mean(numeric_only=False))
ndf['확인일시'] = ndf['확인일시'].where(pd.notnull(ndf['확인일시']), ndf['delay'] + ndf['발생일시'])
ndf.shape[0]
# 잔여관측치 15,240개

# # 경보 분류 추가
ndf.reset_index(drop=True, inplace=True)

for i in range(len(ndf)):
    if re.search('화재', ndf.loc[i, '경보명']):
        ndf.loc[i, '경보구분'] = 'fire'
    elif re.search('고수위|저수위|펌프|LOW|정화조|누수감지기', ndf.loc[i, '경보명']):
        ndf.loc[i, '경보구분'] = 'water'
    elif re.search('발전기|누전경보기|ALT|ACB|CTTS', ndf.loc[i, '경보명']):
        ndf.loc[i, '경보구분'] = 'power'
    else:
        ndf.loc[i, '경보구분'] = 'etc'

# # 건물 구분 추가
ndf['명칭'] = ndf['건물'].where(ndf['대분류'] == '건물군', "GS수퍼_" + ndf['건물'].str.split('_').str[2])
ndf['설비구분'] = ndf['경보명'].str.split('_').str[2].str.replace(r'\d', "", regex=True)

ndf.info()
ndf[ndf['설비구분'].isnull()]
ndf[ndf['설비구분'] == '부스터펌프']

a = ndf['설비구분'].value_counts(dropna=False)

ndf.head()



bysite = ndf.groupby(['대분류', '명칭'])['경보구분'].count().sort_values(ascending=False)
byfacility = ndf.groupby(['대분류', '설비구분'])['경보구분'].count().sort_values(ascending=False)


# ----------
# 질의응답
# ----------

# # 1. 사업장별 평균 알람수는 -----
bysite.loc['GS수퍼'].sum() / bysite.loc['GS수퍼'].count()  # 13638 / 302 = 45
bysite.loc['건물군'].sum() / bysite.loc['건물군'].count()  # 1602 / 140 = 11

# # 2. Top5 사업장은 -----
bysite.loc['GS수퍼'].head()  # max 동두천 227
bysite.loc['건물군'].head()  # max 연암대 76

# # 3. Top5 설비는 -----
byfacility.loc['GS수퍼'].head()  # max 수산냉장고 1343
byfacility.loc['건물군'].head()  # max 화재수신기 298



# # 4. 알람별 시계열 분석(요일, 일, 주, 월, 영업일) -----
ndf2.groupby('대분류')['경보명'].resample('D').count()
ndf2.groupby('대분류')['경보명'].resample('B').count()
ndf2.groupby('대분류')['경보명'].resample('W').count()
ndf2.groupby('대분류')['경보명'].resample('M').count()

week_count = ndf2.index.weekday.value_counts().sort_index()
hour_count = ndf2.index.hour.value_counts().sort_index()

# # 5. 확인지연 알람현황(지연설비, 지연평균시간 시계열 분석) -----



# 시각화
from matplotlib import rc
rc('font', family='malgun gothic')
rc('axes', unicode_minus=False)

day_count.plot(kind='area')
month_count.plot(kind='bar')
week_count.plot(kind='bar', xlabel='Mon(0) ~ Sun(6)')
hour_count.plot(kind='bar')
import calplot
calplot.calplot(day_count, cmap='YlGn')

import seaborn as sns
ndf2['week'] = ndf2.index.day_name()
ndf2['hour'] = ndf2.index.hour
ndf_week_hour = ndf2.groupby(['week', 'hour']).size()
ndf_table = ndf_week_hour.rename_axis(['Weekday', 'Hour']).unstack('Weekday')
days = ['Monday', 'Tuesday', 'Wednesday', 'Tuesday', 'Friday', 'Saturday', 'Sunday']
ndf_table_sort = ndf_table.reindex(columns=days).sort_index(ascending=False)
sns.heatmap(ndf_table_sort, cmap='YlGn')

# 일별 시계열 분해
from statsmodels.tsa.seasonal import seasonal_decompose
ts = ndf2['경보명'].resample('D').count()
result = seasonal_decompose(ts, model='Additive')
result.plot()
