import pandas as pd
from geopy.distance import geodesic

# 엑셀 파일에서 데이터 읽기
file_path = 'data.xlsx'  # 엑셀 파일 경로
data = pd.read_excel(file_path)

# 데이터프레임의 구조를 확인합니다.
# print(data.head())

# 위도와 경도 열의 이름을 확인하고, 필요에 따라 수정하세요.
# 예를 들어, 'Latitude'와 'Longitude'라는 열이 있다고 가정합니다.
latitude_col = 'Latitude'
longitude_col = 'Longitude'

# 4개의 서로 다른 지점의 위도와 경도 및 이름 (예시)
reference_points = {
    '서울': (37.5665, 126.978),
    '부산': (35.1796, 129.0756),
    '대전': (35.9078, 127.7669),
    '인천': (37.4563, 126.7052)
}

# 각 지점에서 가장 가까운 지점까지의 거리와 이름 계산
def find_nearest_distance_and_name(row):
    point = (row[latitude_col], row[longitude_col])
    distances = {name: geodesic(point, coords).kilometers for name, coords in reference_points.items()}
    nearest_name = min(distances, key=distances.get)
    nearest_distance = distances[nearest_name]
    return pd.Series([nearest_name, nearest_distance])

# 거리와 지점명을 새로운 열에 추가
data[['Nearest Point', 'Nearest Distance (Km)']] = data.apply(find_nearest_distance_and_name, axis=1)

# 결과 출력
print(data)

# 결과를 새로운 엑셀 파일로 저장
output_file_path = 'output_data.xlsx'
data.to_excel(output_file_path, index=False)
