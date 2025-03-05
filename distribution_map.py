import pandas as pd
import folium
from folium.plugins import MarkerCluster

# 엑셀 파일 읽기
df = pd.read_excel('서울시건축물대장표제부.xlsx')

# 지도 생성 (첫 번째 좌표를 중심으로 설정)
map_center = [df['위도'].iloc[0], df['경도'].iloc[0]]
m = folium.Map(location=map_center, zoom_start=10)

# 마커 클러스터 생성
marker_cluster = MarkerCluster().add_to(m)

# 유형별 색상 정의
color_dict = {
    '판매시설': 'red',
    '근생시설': 'blue',
    '업무시설': 'black',
    '의료시설': 'green'
}

# 각 좌표에 마커 추가
for index, row in df.iterrows():
    # 유형에 따라 색상 선택 (기본값은 gray)
    color = color_dict.get(row['주용도'], 'gray')
    
    folium.Marker(
        location=[row['위도'], row['경도']],
        popup=f"{row['주용도'][:2]} - {row['연면적']}",
        icon=folium.Icon(color=color, icon='info-sign'),
    ).add_to(marker_cluster)

# 범례 추가
legend_html = '''
<div style="position: fixed; bottom: 50px; left: 50px; width: 120px; height: 90px; 
    border:2px solid grey; z-index:9999; font-size:14px; background-color:white;
    ">&nbsp;<b>범례:</b><br>
    &nbsp;<i class="fa fa-map-marker fa-2x" style="color:red"></i> 판매시설<br>
    &nbsp;<i class="fa fa-map-marker fa-2x" style="color:blue"></i> 근생시설<br>
    &nbsp;<i class="fa fa-map-marker fa-2x" style="color:black"></i> 업무시설<br>
    &nbsp;<i class="fa fa-map-marker fa-2x" style="color:green"></i> 의료시설
</div>
'''
m.get_root().html.add_child(folium.Element(legend_html))

# 지도를 HTML 파일로 저장
m.save('distribution_map.html')
