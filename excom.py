import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

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
# df = df.fillna(0)
df.info()
df.columns
df.head()

pv_df = pd.pivot_table(df,                       # 피벗할 데이터프레임
                       index=['item', '리커링'],   # 행구분에 들어갈 열
                       aggfunc=['sum', 'count'],  # 적용할 함수
                       # aggfunc={'age': 'max', 'fare': 'mean'},
                       fill_value=0,            # NaN 채우기
                       margins=True,            # 행별,열별 합계
                       margins_name='계')
pv_df.xs('리커링', level=1)

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


import pandas as pd
import numpy as np

arrays = [['t','t','t','s'], [1, 1, 2, 2], ['red', 'blue', 'red', 'blue']]
pd.MultiIndex.from_arrays(arrays, names=('vol', 'number', 'color'))
data = np.random.randn(4, 4)
df = pd.DataFrame(data, columns=arrays)
print(df)

df.xs('blue', level=2, axis=1).sum(axis=1)
