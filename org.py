import pandas as pd
import re

def second_space(text):
    match = re.match(r'(.+?\s.+?\s)', text)
    if match:
        return match.group(0).strip()
    else:
        return ''

df = pd.read_csv("C:/Users/Administrator/Desktop/mart_djy_03.txt",
                 header=None,
                 nrows=300,
                 encoding='cp949',
                 sep='|')

df.head(3)
df['숏도로명'] = df[6].map(second_space)

bgk_locs = pd.DataFrame(df[6].apply(lambda v: v.split()[:2]).tolist(),
                        columns=('d1', 'd2'))
bgk_locs.head()
bgk_locs['d1'].unique()

d1_aliases = """서울시:서울특별시 충남:충청남도 강원:강원도 경기:경기도 충북:충청북도 경남:경상남도 경북:경상북도
전남:전라남도 전북:전라북도 제주도:제주특별자치도 제주:제주특별자치도 대전시:대전광역시 대구시:대구광역시 인천시:인천광역시
광주시:광주광역시 울산시:울산광역시"""
d1_aliases = dict(aliasset.split(':') for aliasset in d1_aliases.split())
bgk_locs['d1'] = bgk_locs['d1'].apply(lambda v: d1_aliases.get(v, v))
bgk_locs['d1'].unique()

bgk_locs[bgk_locs['d1'] == '수원시']
bgk_locs.iloc[101] = ['경기도', '수원시']
bgk_locs['d2'].unique()

bgk_locs.isnull().sum()
bgk_locs.fillna({'d1': '미확인', 'd2': '미확인'}, inplace=True)

B = bgk_locs.apply(lambda r: r['d1'] + ' ' + r['d2'], axis=1).value_counts()
B.head()
