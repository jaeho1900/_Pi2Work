# =====================
# 맨해튼 거리
# =====================

import pandas as pd
from geopy.distance import geodesic

df = pd.read_excel('서울시건축물대장표제부.xlsx')

# 베이스캠프 위치 정의
base_camps = {
    '마포강북': (37.5483390, 126.953640),
    '광화문': (37.5692569, 126.971556),
    '강서인천': (37.4821346, 126.879683),
    '강남강동': (37.5036451, 127.035888)
}

def calculate_distances(row):
    location = (row['위도'], row['경도'])
    distances = {name: geodesic(location, coords).km for name, coords in base_camps.items()}
    
    # 직선거리 계산
    nearest_direct = min(distances, key=distances.get)
    direct_distance = distances[nearest_direct]
    
    # 맨해튼 거리 계산
    manhattan_distances = {name: abs(location[0]-coords[0]) + abs(location[1]-coords[1]) for name, coords in base_camps.items()}
    nearest_manhattan = min(manhattan_distances, key=manhattan_distances.get)
    manhattan_distance = manhattan_distances[nearest_manhattan] * 111  # 대략적인 km 변환 (1도 ≈ 111km)
    
    return pd.Series({
        '가장 가까운 베이스캠프(직선)': nearest_direct,
        '직선거리(km)': direct_distance,
        '가장 가까운 베이스캠프(맨해튼)': nearest_manhattan,
        '맨해튼거리(km)': manhattan_distance
    })

# 새로운 열 추가
df[['베이스캠프(직선)', '직선거리(km)', '베이스캠프(맨해튼)', '맨해튼거리(km)']] = df.apply(calculate_distances, axis=1)

# 결과를 엑셀 파일로 저장
df.to_excel('서울시건축물대장표제부_distance.xlsx', index=False)
