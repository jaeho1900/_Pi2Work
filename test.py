# _건축물대장 DB생성


# --------------------
# 데이터프레임 생성
# --------------------

import pandas as pd

df = pd.read_csv("C:/Users/Administrator/Desktop/mart_djy_03.txt",
                 sep="|",
                 header=0)

xlcol = pd.read_excel("C:/Users/Administrator/Desktop/데이터구조.xlsx",
                      header=0,
                      usecols=[0, 1])

print(df.shape)

df.columns = xlcol["컬럼한글명"]
df.head(1)


# --------------------
# 데이터구조 파일로 부터 columns 추출
# --------------------

import pandas as pd
import psycopg2 as pg2

xlcolumns = pd.read_excel("C:/Users/Administrator/Desktop/데이터구조.xlsx",
                          header=0,
                          usecols=[0, 1])

str_temp = ""
sub_sql = ""
for a in xlcolumns.values :
    column_name = a[0].replace('(%)', '').replace('(', '_').replace(')', '')
    str_temp = str_temp + column_name + " " + a[1] + ", "
    sub_sql = str_temp[:-2]


# --------------------
# DB에 테이블 생성
# --------------------

conn = pg2.connect (database="postgres",
                    user="postgres",
                    password="cyberuser",
                    host="localhost",
                    port="5432")
cur = conn.cursor ()
sql = "CREATE TABLE building(" + sub_sql + ")"
cur.execute (sql)
conn.commit ()
cur.close ()
conn.close ()


# --------------------
# DB에 데이터프레임 업로드 (I)
# --------------------

import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL 연결 설정
user = 'postgres'
password = 'cyberuser'
host = 'localhost'
port = '5432'
dbname = 'postgres'

# SQLAlchemy를 사용해 PostgreSQL 연결 엔진 생성
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")

# 데이터프레임을 PostgreSQL 테이블로 저장
table_name = 'building'
df.to_sql(table_name, engine, index=False, if_exists='replace')  # 테이블이 존재하면 덮어씌움, 추가하려면 'append'  

print(f"DataFrame이 PostgreSQL의 '{table_name}' 테이블로 성공적으로 저장되었습니다.")


# --------------------
# dbeaver 에서 직접 업로드(II)
# --------------------

# 데이터가져오기 > 옵션: column delimiter=|, header position=None, encoding=cp949


# --------------------
# SQL문으로 레코드 조회
# --------------------

query = '''
SELECT *
FROM building
WHERE 대지_위치 like '서울%'
AND (옥내_자주식_대수_대 + 옥외_자주식_대수_대) >=1;
'''
Temp = pd.read_sql (query, conn)
conn.commit ()
conn.close ()

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
# COUNT(case when 연면적_㎡ < 33058 then 1 end) as "1만평미만_동수",
# COUNT(case when 33058 <= 연면적_㎡ and 연면적_㎡ <= 66116 then 1 end) as "1만평이상2만평이하_동수",
# COUNT(case when 66116 < 연면적_㎡ then 1 end) as "2만평초과_동수",
# sum(case when 연면적_㎡ < 33058 then 연면적_㎡ end) as "1만평미만_연면적합계",
# sum(case when 33058 <= 연면적_㎡ and 연면적_㎡ <= 66116 then 연면적_㎡ end) as "1만평이상2만평이하_연면적합계",
# sum(case when 66116 < 연면적_㎡ then 연면적_㎡ end) as "2만평초과_연면적합계"
# FROM building
# where "주_용도_코드_명" = '업무시설';

# SELECT building.*, codetable."short_지명"
# FROM building
# LEFT JOIN codetable
# ON building."시군구_코드" = codetable."시군구_코드"
