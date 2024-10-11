import matplotlib.pyplot as plt
import pandas as pd

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

y = [200000, 230000, 350000, 550000]

plt.figure(figsize=(3,4), dpi=80)
plt.boxplot(y)
plt.title('Box plot', fontsize=14, color='black', loc='center')
plt.xticks(ticks=[1], labels=['price per 3.3㎡'])
