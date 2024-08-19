import pandas as pd
import numpy as np

# ----- 데이터프레임 받기 -----

df = pd.read_csv("D:/mart_djy_03.txt",
                 header=None,
                #  nrows=300000,
                 encoding='cp949',
                 sep='|')

xlcol = pd.read_excel("./ADP_ver01/데이터구조.xls",
                      engine='xlrd',
                      header=1,
                      usecols=[0, 1])

df.columns = xlcol["컬럼 한글명"]
df.tail(1)

# ----- Address 전처리 -----

df2 = df['대지_위치'].to_frame()

# 결측치 확인
df2.isna().sum()

# 스페이스문자 요소 삭제
df2[df2['대지_위치'] == ' ']
df2['대지_위치'] = df2['대지_위치'].replace(' ', None)
df2.dropna(inplace=True)

# ----- next -----

df3 = pd.DataFrame(df2['대지_위치'].apply(lambda v: v.strip().split()[:2]).tolist(), columns=('광역시도', '행정구역'))

df2['대지_위치'].str.split().str[:2]

len(df2)


df4 = pd.concat([df3, df2], axis=1)



df4['광역시도'].isna().sum()

df3[df3['광역시도'].isna()]

df3['행정구역'].isna().sum()

df3['광역시도'].value_counts(dropna=False)

# ----- 표준 광역시도 생성 -----

# 표준 광역시도
std_광역시도 = """서울특별시 인천광역시 세종특별자치시 대전광역시 광주광역시 대구광역시 울산광역시 부산광역시
경기도 강원특별자치도 충청북도 충청남도 전북특별자치도 전라남도 경상북도 경상남도 제주특별자치도"""

std_area_df = pd.DataFrame([x for x in std_광역시도.split()], columns = ['표준광역시도'])

# ----- 표준광역시도와 사용자df의 광역시도 비교 -----

df3_tmp = pd.DataFrame(df3['광역시도'].unique(), columns=['광역시도'])
std_area_df.merge(df3_tmp, left_on=['표준광역시도'], right_on=['광역시도'], how='outer')

# ----- 표준광역시도 명칭으로 사용자 광역시도 명칭을 변경 -----

광역시도_aliases = """서울:서울특별시 서울시:서울특별시 세종:세종특별자치시 세종시:세종특별자치시
제주:제주특별자치도 제주도:제주특별자치도 강원:강원특별자치도 강원도:강원특별자치도 전북:전북특별자치도 전북북도:전북특별자치도
경기:경기도 경남:경상남도 경북:경상북도 전남:전라남도 충남:충청남도 충북:충청북도
광주:광주광역시 광주시:광주광역시 대구:대구광역시 대구시:대구광역시 대전:대전광역시 대전시:대전광역시
부산:부산광역시 부산시:부산광역시 울산:울산광역시 울산시:울산광역시 인천:인천광역시 인천시:인천광역시"""

광역시도_aliases = dict(aliasset.split(':') for aliasset in 광역시도_aliases.split())
df3['광역시도'] = df3['광역시도'].apply(lambda v: 광역시도_aliases.get(v, v))

# ----- 광역시도 + 행정구역 합치기 -----

df3['short_name'] = df3['행정구역'].apply(lambda x: x[:-1])

df3['short_name'].where(~(df3['광역시도'].str.contains('^강원', na=False) & df3['행정구역'].str.contains('^고성', na=False)), '강원고성')
df3['short_name'].where(~(df3['광역시도'].str.contains('^경상', na=False) & df3['행정구역'].str.contains('^고성', na=False)), '경남고성')

condition = df3['행정구역'].apply(lambda x: len(x) > 2)
df3['short_name'].where(~(df3['광역시도'].str.contains('^(?!세종).*시$', na=False) & condition), \
                        df3['광역시도'].str[:2] + df3['행정구역'].str[:-1])
df3['short_name'].where(~(df3['광역시도'].str.contains('^(?!세종).*시$', na=False) & ~condition), \
                        df3['광역시도'].str[:2] + df3['행정구역'].str[:])

# code_df = pd.read_csv("./ADP_ver01/지도_지명_코드집.csv")
