# 1. 라이브러리 import
import pandas as pd
import sqlalchemy

# 2. connector 설정
engine = sqlalchemy.create_engine("postgresql://{user}:{password}@{host}:{port}/{databasename}")

# 3. pandas.read_sql() 사용하여 데이터베이스 조회하기
# 1번째 인자는 쿼리, 2번째 인자는 커넥터
# 참고로, read_sql으로는 commit이나 grant 등을 시도하면 에러가 나므로 알아주시면 좋을 것 같습니다.
to_sql_test = pd.read_sql('select * from skma.table_name', engine)

# 4. pandas.to_sql 사용하여 데이터프레임을 DB 테이블로 만들기
# 1번째 인자는 생성할 테이블명, 2번째는 커넥터, 3번째는 테이블을 생성할 스케마명 (미지정시 디폴트스케마)
# if_exists = 'replace' or 'append'
to_sql_test.to_sql('tb_copied',con = engine, schema='skma', if_exists='replace', index=False)






# sqlalchemy로 postgresql접근
from sqlalchemy import create_engine

# engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")
db = create_engine('postgresql://user:password@localhost:port/database')
for i in range(1,2000):
    conn = db.connect()
    #some simple data operations
    conn.close()
db.dispose()

# sqlalchemy로 postgresql 쓰기/읽기
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://id:password@localhost:port/database')
df.to_sql('table_name', engine)
pd.read_sql("select * from users limit 1", engine)




# _건축물대장 DB생성


# --------------------
# DB에 데이터프레임 업로드 (I)
# --------------------

import pandas as pd
from sqlalchemy import create_engine

# 데이터프레임 생성
df = pd.read_csv("C:/Users/Administrator/Desktop/mart_djy_03.txt",
                 sep="|",
                 header=0,
                 nrows=10
                 )

# xlcol = pd.read_excel("C:/Users/Administrator/Desktop/데이터구조.xlsx",
#                       header=0,
#                       usecols=[0, 1])

# df.columns = xlcol["컬럼한글명"]

print(df.columns)
print(df.shape)
print(df.head(1))

# PostgreSQL 연결
user = 'postgres'
password = 'cyberuser'
host = 'localhost'
port = '5432'
dbname = 'postgres'

engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")

# 데이터프레임을 PostgreSQL 테이블로 저장
table_name = 'building'
df.to_sql(table_name, engine, index=False, if_exists='append')  # 테이블이 존재하면 덮어씌움 'replace', 추가하려면 'append'  

print(f"DataFrame이 PostgreSQL의 '{table_name}' 테이블로 성공적으로 저장되었습니다.")


# --------------------
# dbeaver 에서 직접 업로드(II)
# --------------------

import pandas as pd
import psycopg2 as pg2

# 데이터구조 파일로 부터 columns 추출
xlcolumns = pd.read_excel("C:/Users/Administrator/Desktop/데이터구조.xlsx",
                          header=0,
                          usecols=[0, 1])
print(xlcolumns.values)

str_temp = ""
sub_sql = ""
for a in xlcolumns.values :
    column_name = a[0].replace('(%)', '').replace('(', '_').replace(')', '')
    str_temp = str_temp + column_name + " " + a[1] + ", "
    sub_sql = str_temp[:-2]

# DB에 테이블 컬럼 생성
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

# 데이터가져오기
# 옵션: column delimiter=|, header position=None, encoding=cp949


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
