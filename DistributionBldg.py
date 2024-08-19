import pandas as pd

# ----- 데이터프레임 받기 -----

df = pd.read_csv("D:/mart_djy_03.txt",
                 header=None,
                #  nrows=100000,
                 encoding='cp949',
                 sep='|')

xlcol = pd.read_excel("./ADP_ver01/데이터구조.xls",
                      engine='xlrd',
                      header=1,
                      usecols=[0, 1])

df.columns = xlcol["컬럼 한글명"]
df.tail(1)

# ----- 분석 데이터 추출 -----

df['주_용도_코드_명'].isna().sum()
df[df['주_용도_코드_명'].isna()]
df2 = df.drop(df[df['주_용도_코드_명'].isna()].index)

df2['주_용도_코드_명'].unique()

df3 = df2[(df2['주_용도_코드_명'].isin(['제2종근린생활시설', '업무시설', '노유자시설'])) \
          & (df2['연면적(㎡)'] >= 10000)]
df3.shape

# ----- 도식화 데이터 준비 -----

code_df = pd.read_csv("./ADP_ver01/표제부_시군구_코드_지명집.csv")

df3['시군구_코드'].isna().sum()
df3[df3['시군구_코드'].isna()]
df4 = df3.drop(df3[df3['시군구_코드'].isna()].index)

df5 = pd.merge(df4, code_df, how='left', left_on='시군구_코드', right_on='시군구_코드')
df6 = df5[['시군구_코드', 'Short_지명']].groupby('Short_지명').count()
df6 = df6.reset_index(drop=False)
print(df6)
