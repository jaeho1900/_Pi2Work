import pandas as pd

xlcolumns = pd.read_excel("./ADP_ver01/데이터구조.xls",
                          engine='xlrd',
                          header=1,
                          usecols=[0, 1])

df = pd.read_csv("./ADP_ver01/mart_djy_03.txt",
                 header=None,
                 nrows=50,
                 encoding='cp949',
                 sep='|')

code_df = pd.read_csv("./ADP_ver01/표제부_시군구_코드_지명집.csv")

df.shape
df.columns = xlcolumns["컬럼 한글명"]
df.head()
df.tail(3)

df2 = pd.merge(df, code_df, how='left', left_on='시군구_코드', right_on='시군구_코드')

df2['Short_지명'].count()
df2['Short_지명'].unique()
df2['Short_지명'].nunique()

df2.columns
df2['주_용도_코드_명'].unique()
df2[(df2['주_용도_코드_명'].isin(['제2종근린생활시설', '업무시설', '노유자시설'])) & (df2['연면적(㎡)'] >= 10000)]['건물_명'].head(30)
df2[(df2['주_용도_코드_명'].isin(['제2종근린생활시설', '업무시설', '노유자시설'])) & (df2['연면적(㎡)'] >= 10000)].count()

df3 = df2[(df2['주_용도_코드_명'].isin(['제2종근린생활시설', '업무시설', '노유자시설'])) & (df2['연면적(㎡)'] >= 10000)]
df4 = df3['Short_지명'].value_counts().to_frame()
df4.sum()

# ============================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import platform
if platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic') 
elif platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic') 
elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        plt.rc('font', family='Malgun Gothic') 
plt.rcParams['axes.unicode_minus'] = False

data_draw_korea = pd.read_csv("./ADP_ver01/data_map_draw_korea.csv", index_col=0)

# 건축물 갯수 추가 ---
data_draw_korea = pd.merge(data_draw_korea, df4, how='left', left_on='shortName', right_index=True)
data_draw_korea['count'].size
# -------------------

# 위치(x,y) 잡고, 경계선을 그리고, 데이터를 배치하고, colormap 적용
BORDER_LINES = [
    [(3, 2), (5, 2), (5, 3), (9, 3), (9, 1)], # 인천
    [(2, 5), (3, 5), (3, 4), (8, 4), (8, 7), (7, 7), (7, 9), (4, 9), (4, 7), (1, 7)], # 서울
    [(1, 6), (1, 9), (3, 9), (3, 10), (8, 10), (8, 9),
     (9, 9), (9, 8), (10, 8), (10, 5), (9, 5), (9, 3)], # 경기도
    [(9, 12), (9, 10), (8, 10)], # 강원도
    [(10, 5), (11, 5), (11, 4), (12, 4), (12, 5), (13, 5),
     (13, 4), (14, 4), (14, 2)], # 충청남도
    [(11, 5), (12, 5), (12, 6), (15, 6), (15, 7), (13, 7),
     (13, 8), (11, 8), (11, 9), (10, 9), (10, 8)], # 충청북도
    [(14, 4), (15, 4), (15, 6)], # 대전시
    [(14, 7), (14, 9), (12, 9), (12, 10), (13, 10), (13, 13)], # 경상북도
    [(14, 8), (16, 8), (16, 10), (15, 10),
     (15, 11), (14, 11), (14, 12), (13, 12)], # 대구시
    [(15, 11), (16, 11), (16, 13)], # 울산시
    [(17, 1), (17, 3), (18, 3), (18, 6), (15, 6)], # 전라북도
    [(19, 2), (19, 4), (21, 4), (21, 3), (22, 3), (22, 2), (19, 2)], # 광주시
    [(18, 5), (20, 5), (20, 6)], # 전라남도
    [(16, 9), (18, 9), (18, 8), (19, 8), (19, 9), (20, 9), (20, 10)], # 부산시
]

gamma = 0.85 # 0.75  

blockedMap = data_draw_korea
targetData = 'count'

whitelabelmin = (max(blockedMap[targetData]) - min(blockedMap[targetData])) * 0.25 + min(blockedMap[targetData])

datalabel = targetData

vmin = min(blockedMap[targetData])
vmax = max(blockedMap[targetData])

mapdata = blockedMap.pivot(index='y', columns='x', values=targetData)
masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)

cmapname = 'Reds' # 'Blues' # 'Greens'

plt.figure(figsize=(8, 13))
plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, edgecolor='#aaaaaa', linewidth=0.7)

# 지역 이름 표시
for idx, row in blockedMap.iterrows():
    annocolor = 'white' if row[targetData] > whitelabelmin else 'black'
    
    # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다. (중구, 서구)
    if row['광역시도'].endswith('시') and not row['광역시도'].startswith('세종'):
        dispname = '{}\n{}'.format(row['광역시도'][:2], row['행정구역'][:-1])
        if len(row['행정구역']) <= 2:
            dispname += row['행정구역'][-1]
    else:
        dispname = row['행정구역'][:-1]

    # 서대문구, 서귀포시 같이 이름이 3자 이상인 경우에 작은 글자로 표시한다.
    if len(dispname.splitlines()[-1]) >= 3:
        fontsize, linespacing = 9.5, 1.5
    else:
        fontsize, linespacing = 11, 1.2

    plt.annotate(dispname, (row['x']+0.5, row['y']+0.5), weight='bold',
                 fontsize=fontsize, ha='center', va='center', color=annocolor,
                 linespacing=linespacing)
    
# 시도 경계 그린다.
for path in BORDER_LINES:
    ys, xs = zip(*path)
    plt.plot(xs, ys, c='black', lw=2)

plt.gca().invert_yaxis()
#plt.gca().set_aspect(1)

plt.axis('off')
    
cb = plt.colorbar(shrink=.1, aspect=10)
cb.set_label(datalabel)

plt.tight_layout()
plt.show()
