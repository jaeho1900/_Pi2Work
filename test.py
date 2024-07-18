import pandas as pd

data = {
    'A': [1, 2, 3, 0, 5],
    'B': [0, 0, 2, -3, 4],
    'C': [-1, 7, 0, 0, 0]
}
df = pd.DataFrame(data)

# 데이터프레임의 열별 0이 아닌 값들의 합계와 갯수 구하기
print(df[df != 0].sum(), df[df != 0].count(), sep='\n\n')
print(df[df != 0].sum(), (df != 0).sum(), sep='\n\n')
df.apply(lambda x: pd.Series([x[x != 0].sum(), len(x[x != 0])], index=['sum', 'count']))
df.apply(lambda x: [x[x != 0].sum(), len(x[x != 0])])