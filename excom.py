import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import sys

# data prepare
df = pd.read_excel("C:/Users/Administrator/Desktop/exCom/통합자료보고서용_2311_2406.xlsx",
                   sheet_name = '통합(금액)',
                   index_col = 0,
                   header = 1)
df['site'] = df['wbs'].map(lambda a: a[a.rfind('-')+1:len(a)])
df = df.loc[:, ['category', 'item', 'LG/Open', '리커링', 'site', '23-11', '23-12', '24-01',
       '24-02', '24-03', '24-04', '24-05', '24-06']]
df = df.fillna(0)

df_outParking = df[df['category'] != 'Parking']


def count_nonzero(column):
    return np.count_nonzero(column > 0)


xsum = df[['23-11', '23-12', '24-01', '24-02', '24-03', '24-04', '24-05', '24-06']].sum()
xcount = df.loc[:, ['23-11', '23-12', '24-01', '24-02', '24-03', '24-04', '24-05', '24-06']].apply(count_nonzero)
print(xsum, xcount, sep="\n\n")

ysum = df_outParking[['23-11', '23-12', '24-01', '24-02', '24-03', '24-04', '24-05', '24-06']].sum()
ycount = df_outParking.loc[:, ['23-11', '23-12', '24-01', '24-02', '24-03', '24-04', '24-05', '24-06']].apply(count_nonzero)
print(ysum, ycount, sep="\n\n")

# graph
if sys.platform in ['win32', 'win64']:
    rc('font', family='malgun gothic')
elif sys.platform == 'darwin':
    rc('font', 'Gothic')
else:
    print('Check your OS system')
    rc('axes', unicode_minus=False) 

plt.plot(xsum, label='기간별 금액')
plt.plot (xcount, label='기간별 유효사이트수')
plt.plot (ysum, label='기간별 금액')
plt.plot (ycount, label='기간별 유효사이트수')
plt.show()

df[['23-11', '23-12', '24-01', '24-02', '24-03', '24-04', '24-05', '24-06']].groupby(df.category).sum()
df[['23-11', '23-12', '24-01', '24-02', '24-03', '24-04', '24-05', '24-06']].groupby(df.category).count()