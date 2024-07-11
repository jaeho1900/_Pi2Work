import pandas as pd
import psycopg2 as pg2
import seaborn
import matplotlib

# ----------
# '데이터구조.xls' 로 부터 DB.columns 추출
xlcolumns = pd.read_excel ("C:/Users/Administrator/Desktop/데이터구조.xls",
                            engine='xlrd',
                            header=1,
                            usecols=[0, 1])
str_temp = ""
for a in xlcolumns.values :
    column_name = a[0].replace('(%)', '').replace('(', '_').replace(')', '')
    str_temp = str_temp + column_name + " " + a[1] + ", "
    sub_sql = str_temp[:-2]

# ----------
# DB 생성
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