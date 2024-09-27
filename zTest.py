import pandas as pd
import matplotlib.pyplot as plt

# 데이터 정의
data = {
    '관심고객구분': [
        'WTC', '오창에너지솔루션', 'BIFC', '한국타이어테크노링',
        '카카오판교아지트', 'SK서린빌딩', 'KCC오토타워', '엘지가산디지털센터',
        '강서사옥', '서울역빌딩', '인화원', '건양대학교',
        '마포운영센터', '부산진구청', 'sk가스사옥', '메리츠화재',
        '광화문빌딩', '금융투자협회', '상암CNS', 'JW과천',
        '각화골드클래스', '대신증권(위례)'
    ],
    '보유주차면수': [
        50, 50, 38, 30, 26, 17, 10, 10,
        9, 9, 9, 8, 8, 8, 7, 6,
        4, 4, 4, 3, 3, 2
    ]
}

# 데이터프레임 생성
df = pd.DataFrame(data)

# 구간화 수행
# df['구간_등간격'] = pd.cut(df['보유주차면수'], bins=7)
df['구간_등빈도'] = pd.qcut(df['보유주차면수'], 7)

# 결과 출력
print(df)

# 구간별 집계
grouped = df.groupby('구간_등빈도').agg({'보유주차면수': 'count'}).reset_index()
grouped.columns = ['구간', '고객 수']

# 결과 출력
print("\n구간별 집계:")
print(grouped)

plt.bar(grouped["구간"], grouped["고객 수"])
plt.boxplot(df['보유주차면수'])
