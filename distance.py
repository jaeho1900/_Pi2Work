import pandas as pd
from geopy.distance import geodesic

# 엑셀 파일 읽기
df = pd.read_excel('서울시건축물대장표제부.xlsx')

# 데이터프레임의 구조를 확인합니다.
print(df.head())

# 위도와 경도 열의 이름을 확인하고, 필요에 따라 수정하세요.
latitude_col = '위도'
longitude_col = '경도'

# 4개의 서로 다른 지점의 위도와 경도 및 이름
reference_points = {
    '마포강북': (37.548358618, 126.953655998),
    '광화문': (37.5693, 126.9715),
    '강서인천': (37.482151377, 126.879704646),
    '강남강동': (37.503654600, 127.035923489)
}

# 각 지점에서 가장 가까운 지점까지의 거리와 이름 계산
def find_nearest_distance_and_name(row):
    point = (row[latitude_col], row[longitude_col])
    distances = {name: geodesic(point, coords).kilometers for name, coords in reference_points.items()}
    nearest_name = min(distances, key=distances.get)
    nearest_distance = distances[nearest_name]
    return pd.Series([nearest_name, nearest_distance])

# 거리와 지점명을 새로운 열에 추가
df[['Nearest Point', 'Nearest Distance (Km)']] = df.apply(find_nearest_distance_and_name, axis=1)

# 결과 출력
print(df.head())

# 결과를 새로운 엑셀 파일로 저장
df.to_excel('서울시건축물대장표제부_distance.xlsx', index=False)
