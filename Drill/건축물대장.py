"""
_건축물대장 표제부 DB작업.py
2023.06.26
"""

import pandas as pd
import psycopg2 as pg2

# ----------
# '데이터구조.xls' 로 부터 DB.columns 추출
xlcolumns = pd.read_excel("C:/Users/Thanki/Desktop/데이터구조.xls",
                          engine='xlrd',
                          header=1,
                          usecols=[0, 1])

str_temp = ""
for a in xlcolumns.values:
    column_name = a[0].replace('(%)', '').replace('(', '_').replace(')', '')
    str_temp = str_temp + column_name + " " + a[1] + ", "

sub_sql = str_temp[:-2]

# ----------
# DB 생성
conn = pg2.connect(database="postgres",
                   user="postgres",
                   password="cyberuser",
                   host="localhost",
                   port="5432")
cur = conn.cursor()
sql = "CREATE TABLE building(" + sub_sql + ")"
cur.execute(sql)
conn.commit()
cur.close()
conn.close()

# ----------
# 레코드 생성

# import Data 수행(옵션: encoding=cp949, column delimiter=|, header position=None)

# ----------
# 레코드 조회

query = '''
SELECT *
FROM building
WHERE 대지_위치 like '서울%'
  AND (옥내_자주식_대수_대 + 옥외_자주식_대수_대) >=1;
'''
Temp = pd.read_sql(query, conn)
conn.commit()
conn.close()

# SELECT 주_용도_코드_명, count("연면적_㎡"), sum("연면적_㎡")
# FROM building
# where "주_용도_코드_명" = '숙박시설' or "주_용도_코드_명" = '노유자시설'
# group by 주_용도_코드_명 ;

# SELECT 시군구_코드, count("연면적_㎡"), sum("연면적_㎡")
# FROM building
# where "주_용도_코드_명" = '숙박시설' or "주_용도_코드_명" = '노유자시설'
# group by 시군구_코드 ;

# SELECT distinct 시군구_코드, left(대지_위치,5)
# FROM building
# where "주_용도_코드_명" = '숙박시설' or "주_용도_코드_명" = '노유자시설'
# order by 시군구_코드;

# SELECT
#     COUNT(case when 연면적_㎡ < 33058 then 1 end) as "1만평미만_동수",
#     COUNT(case when 33058 <= 연면적_㎡ and 연면적_㎡ <= 66116 then 1 end) as "1만평이상2만평이하_동수",
#     COUNT(case when 66116 < 연면적_㎡ then 1 end) as "2만평초과_동수",
#     sum(case when 연면적_㎡ < 33058 then 연면적_㎡ end) as "1만평미만_연면적합계",
#     sum(case when 33058 <= 연면적_㎡ and 연면적_㎡ <= 66116 then 연면적_㎡ end) as "1만평이상2만평이하_연면적합계",
#     sum(case when 66116 < 연면적_㎡ then 연면적_㎡ end) as "2만평초과_연면적합계"
# FROM building
# where "주_용도_코드_명" = '업무시설';
