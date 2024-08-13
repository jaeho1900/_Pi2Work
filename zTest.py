import pandas as pd
import numpy as np

# 사용자 데이터 받기 -----------------------------------------------------------

df = pd.read_csv("./ADP_ver01/mart_djy_03.txt",
                 header=None,
                 nrows=50000,
                 encoding='cp949',
                 sep='|')

xlcol = pd.read_excel("./ADP_ver01/데이터구조.xls",
                      engine='xlrd',
                      header=1,
                      usecols=[0, 1])

# code_df = pd.read_csv("./ADP_ver01/지도_지명_코드집.csv")

df.columns = xlcol["컬럼 한글명"]
df.tail(3)
df.shape

# 주소가 입력된 컬럼
address_col = '도로명_대지_위치'

# -----------------------------------------------------------------------------

df[['광역시도', '행정구역']] = pd.DataFrame(df[address_col].apply(lambda v: v.strip().split()[:2]).tolist(),
                                           columns=('광역시도', '행정구역'))

df['광역시도'].isna().sum()
df['광역시도'].fillna("자료불명", inplace=True)

df['광역시도'].value_counts(dropna=False)
comp_df = pd.DataFrame(df['광역시도'].value_counts(dropna=False)).reset_index(drop=False)

# 표준광역시도 분포 현황
std_광역시도 = """서울특별시 인천광역시 세종특별자치시 대전광역시 광주광역시 대구광역시 울산광역시 부산광역시
경기도 강원특별자치도 충청북도 충청남도 전북특별자치도 전라남도 경상북도 경상남도 제주특별자치도"""

std_area_df = pd.DataFrame([x for x in std_광역시도.split()], columns = ['표준광역시도'])

std_area_df.merge(comp_df, left_on=['표준광역시도'], right_on=['광역시도'], how='outer')

# 광역시도_aliases = """서울:서울특별시 서울시:서울특별시 세종:세종특별자치시 세종시:세종특별자치시
# 제주:제주특별자치도 제주도:제주특별자치도 강원:강원특별자치도 강원도:강원특별자치도 전북:전북특별자치도 전북북도:전북특별자치도
# 경기:경기도 경남:경상남도 경북:경상북도 전남:전라남도 충남:충청남도 충북:충청북도
# 광주:광주광역시 광주시:광주광역시 대구:대구광역시 대구시:대구광역시 대전:대전광역시 대전시:대전광역시
# 부산:부산광역시 부산시:부산광역시 울산:울산광역시 울산시:울산광역시 인천:인천광역시 인천시:인천광역시"""

# 광역시도_aliases = dict(aliasset.split(':') for aliasset in 광역시도_aliases.split())
# df['광역시도'] = df['광역시도'].apply(lambda v: 광역시도_aliases.get(v, v))

# df['광역시도'].isna().sum()
# df[df['광역시도'].isna()]

# df['광역시도'].nunique()
# df['광역시도'].unique()

df['행정구역'].isna().sum()
df['행정구역'].fillna("자료불명", inplace=True)

df['disp_name'] = df['행정구역'].apply(lambda x: x[:-1])


def inputfunc(df):
    txt = ''
    if df['행정구역'].startswith('고성'):
        if df['광역시도'].startswith('강원'):
            txt = '강원고성'
        else:
            txt = '경남고성'
    elif (df['광역시도'].endswith('시')) & (~df['광역시도'].startswith('세종')):
        if len(df['행정구역'].str) > 2:
            txt = df['광역시도'].str[:2] + df['행정구역'].str[:-1]
        else:
            txt = df['광역시도'].str[:2] + df['행정구역'].str
    return txt


df['disp_name'] = df.apply(lambda x: inputfunc(x))


for idx, row in mapdf.iterrows():
    # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다(중구, 서구)
    if mapdf.loc[idx, '광역시도'] == None:
        continue
        if

    else:

mapdf['disp_name'].nunique()
mapdf['disp_name'].unique()


df2 = pd.concat([df, mapdf], axis=1)
df2.columns
df2[['대지_위치', '광역시도', '행정구역', 'disp_name']]


df2['주_용도_코드_명'].unique()
df2[(df2['주_용도_코드_명'].isin(['제2종근린생활시설', '업무시설', '노유자시설'])) & (df2['연면적(㎡)'] >= 10000)]['건물_명'].head(30)
df2[(df2['주_용도_코드_명'].isin(['제2종근린생활시설', '업무시설', '노유자시설'])) & (df2['연면적(㎡)'] >= 10000)].count()

df3 = df2[(df2['주_용도_코드_명'].isin(['제2종근린생활시설', '업무시설', '노유자시설'])) & (df2['연면적(㎡)'] >= 10000)]
df4 = df3['disp_name'].value_counts().to_frame()
df4.sum()


blockedMap = pd.read_csv("./ADP_ver01/data_map_draw_korea.csv", index_col=0)
targetData = 'count'

# -----------------------------------------------------------------------------

# >>> 한반도 카토그램 -----

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

gamma = 0.75

vmax = max(blockedMap[targetData])
vmin = min(blockedMap[targetData])
whitelabelmin = (vmax - vmin) * 0.25 + vmin

mapdata = blockedMap.pivot(index='y', columns='x', values=targetData)
masked_mapdata = np.ma.masked_where(np.isnan(mapdata), mapdata)

import matplotlib.pyplot as plt
import platform

if platform.system() == 'Windows': #윈도우
        plt.rc('font', family='Malgun Gothic')
elif platform.system() == 'Darwin': #맥
        plt.rc('font', family='AppleGothic')
elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
        plt.rc('font', family='Malgun Gothic')
plt.rcParams['axes.unicode_minus'] = False

cmapname = 'Greens' # 'Blues' 'Reds' 'Greens'

plt.figure(figsize=(8, 13))
plt.pcolor(masked_mapdata, vmin=vmin, vmax=vmax, cmap=cmapname, edgecolor='#aaaaaa', linewidth=0.5)

# 지역 이름 표시
for idx, row in blockedMap.iterrows():
    annocolor = 'white' if row[targetData] > whitelabelmin else 'black'

    # 광역시는 구 이름이 겹치는 경우가 많아서 시단위 이름도 같이 표시한다(중구, 서구)
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
    plt.plot(xs, ys, c='black', lw=4)

plt.gca().invert_yaxis()

plt.axis('off')

cb = plt.colorbar(shrink=.1, aspect=10)
cb.set_label(targetData)

plt.tight_layout()
plt.show()
