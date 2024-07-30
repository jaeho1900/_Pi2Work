import pandas as pd
import re

code_df = pd.read_csv("D:/_Pi2Work/ADP_ver01/지도_지명_코드집.csv")

def second_space(text):
    match = re.match(r'(.+?\s.+?\s)', text)
    if match:
        return match.group(0).strip()
    else:
        return ''

df['숏도로명'] = df.대지_위치.map(second_space)

df2 = df.drop_duplicates(subset=['시군구_코드'], keep='last')
df2_blk = df2[df2['숏도로명'] == ""]  # 0, 38022

df2.to_csv("C:/Users/Administrator/Desktop/shortname_org.csv",encoding='CP949')
