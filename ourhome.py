import pandas as pd
import re

df = pd.read_csv('c:/users/administrator/desktop/ourhomestore.txt')
df
df.shape

df.columns
df.columns.str.count('option')

a = df.columns.str.replace("amp;", "")
type(a[0])

result = re.findall(r'(?="\>)(.+?)(?<=\<\/option)', a[0])

pack = []
for i in result:
    k = re.match(r'("\>)(.+?)(\<\/option)', i)
    pack.append(k.group(2))

pd.DataFrame(pack, index=range(1, len(pack) + 1), columns=['store_name']) \
    .to_excel('c:/users/administrator/desktop/ourhome.xlsx')
