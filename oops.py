import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

y = [200000, 230000, 350000, 550000]
median = np.median(y)

plt.figure(figsize=(3,4), dpi=80)
plt.boxplot(y)
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])
plt.text(1.1, median, f'Median: {median:,.0f}', verticalalignment='center')
plt.title('Box plot', fontsize=14, color='black', loc='center')
plt.xticks(ticks=[1], labels=['price per 3.3㎡'])


# >>> Matplotlib의 축눈금 숫자 서식 바꾸기 -----

# plt.gca().get_yticks()을 이용하여 현재 눈금정보가져와서 포멧팅 함수로 형식변환 후 
# set_yticklabels에 넘김
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:,.0f}'.format(x) for x in current_values])
