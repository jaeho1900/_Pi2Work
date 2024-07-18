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
df.columns

# selected data
df2 = df[['item'] + list(df.columns[5:29])]
df2.set_index('item', inplace=True)

# 데이터프레임의 열별 0이 아닌 값들의 합계와 갯수 구하기
df2.groupby(df2.index).sum()
df2.groupby(df2.index).apply(lambda x: x[x != 0].sum())
df2.groupby(df2.index).apply(lambda x: x[x != 0].count())


def hap(x):
    return x[x != 0].sum()

def su(x):
    return x[x != 0].count()



df = df.loc[:, ['category', 'item', 'LG/Open', '리커링', '23-11', '23-12', '24-01',
       '24-02', '24-03', '24-04', '24-05', '24-06']]

df_outParking = df[df['category'] != 'Parking']

xsum = df[['23-11', '23-12', '24-01', '24-02', '24-03', '24-04', '24-05', '24-06']].sum()
ysum = df_outParking[['23-11', '23-12', '24-01', '24-02', '24-03', '24-04', '24-05', '24-06']].sum()

plt.plot(xsum, label='기간별 금액')
plt.plot (ysum, label='기간별 금액')
