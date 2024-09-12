import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r'C:\Users\Administrator\Desktop\customer.csv', encoding='CP949')

df['잠재고객'] = df[df.columns[0]].str.split('\t').str[0]
df['보유면수'] = df[df.columns[0]].str.split('\t').str[1]
df = df[['잠재고객', '보유면수']]
df['보유면수'] = df['보유면수'].astype(int)
df.info()

def assign_group(pages):
    if pages == 2:
        return '2'
    elif pages == 3:
        return '3'
    elif pages == 4:
        return '4'
    elif 5 <= pages <= 10:
        return '5-10'
    elif 11 <= pages <= 30:
        return '11-30'
    elif pages > 30:
        return '30+'
    else:
        return 'Other'

df['그룹'] = df['보유면수'].apply(assign_group)
gdf = df.groupby('그룹').describe()
gdf['no'] = [5,1,2,6,3,4]
gdf = gdf.sort_values(by='no', axis=0)
gdf = gdf.droplevel(0, axis=1)
gdf = gdf[['count', 'min', '50%','max']]
gdf

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

df.보유면수.plot(kind='hist', bins=5, density=True, histtype='step')
df.groupby('그룹').plot(kind='box')
