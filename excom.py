import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# # Hangul -----
# from matplotlib import rc
# rc('font', family='malgun gothic')
# rc('axes', unicode_minus=False) 
# # ------------

# Read
df = pd.read_excel("C:/Users/Administrator/Desktop/통합자료보고서용.xlsx",                    
                   sheet_name = '통합(금액)',
                   index_col = 0,
                   header = 1)
# df['site'] = df['wbs'].map(lambda a: a[a.rfind('-')+1:len(a)])
df.info()
df = df.fillna(0)
df.head()
df.columns

# selected data
df2 = df[['item'] + list(df.columns[5:29])]

df2.groupby('item').sum().head(2)
df2.groupby('item').count().head(2)


# # 피벗테이블은 열인덱스의 피라미드 밑에서부터 columns->values->aggfunc 순으로 쌓임
# pd.pivot_table(df,                       # 피벗할 데이터프레임
#                index=['class', 'who'],   # 행위치에 들어갈 열
#                columns='alive',          # 열 위체에 들어갈 열
#                values=['age', 'fare'],   # 데이터로 사용할 열
#                aggfunc=['max', 'mean'],  # 데이터 집계함수
#                # aggfunc={'age': 'max', 'fare': 'mean'},
#                fill_value=0,            # NaN 채우기
#                margins=True,            # 행별,열별 합계
#                margins_name='계')




df.columns[5:29].type

# =========================
# 데이터프레임의 B열과 G부터 L열까지의 열을 선택
selected_columns = df[['B'] + list(df.columns[6:12])]
# =========================


df = df.loc[:, ['category', 'item', 'LG/Open', '리커링', 'site', '23-11', '23-12', '24-01',
       '24-02', '24-03', '24-04', '24-05', '24-06']]

df_outParking = df[df['category'] != 'Parking']


def count_nonzero(column):
    return np.count_nonzero(column > 0)


xsum = df[['23-11', '23-12', '24-01', '24-02', '24-03', '24-04', '24-05', '24-06']].sum()
xcount = df.loc[:, ['23-11', '23-12', '24-01', '24-02', '24-03', '24-04', '24-05', '24-06']].apply(count_nonzero)
print(xsum, xcount, sep="\n\n")

ysum = df_outParking[['23-11', '23-12', '24-01', '24-02', '24-03', '24-04', '24-05', '24-06']].sum()
ycount = df_outParking.loc[:, ['23-11', '23-12', '24-01', '24-02', '24-03', '24-04', '24-05', '24-06']].apply(count_nonzero)
print(ysum, ycount, sep="\n\n")


plt.plot(xsum, label='기간별 금액')
plt.plot (xcount, label='기간별 유효사이트수')
plt.plot (ysum, label='기간별 금액')
plt.plot (ycount, label='기간별 유효사이트수')
plt.show()

df[['23-11', '23-12', '24-01', '24-02', '24-03', '24-04', '24-05', '24-06']].groupby(df.category).sum()
df[['23-11', '23-12', '24-01', '24-02', '24-03', '24-04', '24-05', '24-06']].groupby(df.category).count()