import pandas as pd
import numpy as np

# Read
df = pd.read_excel("통합자료보고서용.xlsx",
                   index_col = 0,
                   header = 1)
df.info()
df.columns
len(df.columns)

df2 = df[['item'] + list(df.columns[5:65])]
df2 = df2.set_index('item')

arrays = [[x[0:2] for x in list(df.columns[5:65])], list(df.columns[5:65])]
df2.columns = pd.MultiIndex.from_arrays(arrays, names=('year', 'month'))

df2.head()
df2.index.unique()
df2.index.nunique()

df2 = df2.replace(np.nan, 0)
df2 = df2.astype('int')

df3 = df2.groupby(df2.index).sum()
df3.shape
df3.index

result = df3.loc[['원격감시', '캡슐커피'], ['24']].T
result = result.droplevel(0, axis=0)

# graph
import matplotlib.pyplot as plt
plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

plt.plot(result, label=['원격감시', '캡슐커피'])
plt.xticks(rotation=90, ha='left')
plt.legend()
plt.show()
# plt.savefig ("FIGURE.png")
