# --------------------
# 상호작용 버튼
# --------------------

import streamlit as st
import seaborn as sns

df = sns.load_dataset('iris')
species = df['species'].unique()

# >>> 버튼 -----

# 버튼을 누를시 정해진 작업 수행
# .button('버튼이름')

if st.button('대문자') :
    st.write(df['species'].str.upper().head(3))

# >>> 라디오 버튼 -----

# 여러 선택지 중에 하나를 선택하여 선택된 작업 수행
# .radio('보여줄 메시지', '선택지1, 선택지2...')

my_order = ['오름차순', '내림차순']         # 라디오 버튼에 보여줄 텍스트
status = st.radio('정렬방법선택', my_order) # 라디오 버튼의 상태 변수화
 
if status == my_order[0] :   # 첫번째 선택시 오름차순
    st.write(df.sort_values('petal_length'))
elif status == my_order[1] : # 두번째 선택시 내림차순
    st.write(df.sort_values('petal_length', ascending=False))

# >>> 체크 박스 -----

# 예/아니오 상황 체크만으로 작업 수행
# .checkbox('보여줄 메시지')

if st.checkbox('헤드 5개 보기'):
    st.write(df.head())
else:
    st.text('헤드를 숨겼습니다.')

# >>> 셀렉트 박스 -----

# 여러 개의 목록을 보여주고 그 중 하나를 선택하여 작업 수행
# .selectbox('보여줄 메시지', '리스트1, 리스트2...')

language = ['Python', 'C', 'Java', 'Go', 'PHP']
my_choice = st.selectbox('좋아하는 언어 선택', language)

if my_choice == language[0] :
    st.write("파이썬 선택")
    # 이후 생략

# >>> 멀티 셀렉트 -----

# 여러 개의 목록에서 하나 이상을 선택
# .multiselect('보여줄 메시지', '리스트1, 리스트2...')

columns_list = df.columns
choice_list = st.multiselect('컬럼을 선택하세요', columns_list)
st.write( df[choice_list] )

# >>> 슬라이더 -----

# 숫자를 조정하는데 주로 사용, 조정된 숫자로 작업 수행
# .slider('보여줄 메시지', 시작값, 끝값, 기본값, 스텝)

age = st.slider('나이', 1, 120, 30, 10)
st.text('제가 선택한 나이는 {}입니다.'.format(age))

# >>> 사이드 바 -----

# 화면 왼쪽에 프레임을 나누어 따로 표기
# .sidebar ~ : 왼쪽 프레임에서 할 행동 표시

st.sidebar.text('안녕하세요')
st.sidebar.button('버튼')

# >>> 익스팬더 -----

# 활성화시 숨겨져 있던 정해진 작업을 수행 (확장 개념, =펼쳐보기 느낌)
# .expander('보여줄 메시지')

with st.expander('Hello') :
    st.text('변경')
    st.write(df)


# --------------------
# 매체(이미지, 영상, 음악) 사용하기
# --------------------

import streamlit as st

# >>> 내 서버(혹은 컴퓨터)에 있는 이미지 파일 불러오기 -----

# 옵션 > use_column_width=True로 설정하면 현재 창을 기준으로 가로세로 너비가 조절
st.image('pic.png')
st.image('pic.png', use_container_width = True, caption = 'pic')

# >>> 인터넷 URL을 이용하여 이미지 불러오기 -----

# .image('경로와 파일이름')에는 경로가 URL도 포함되어 불러 올 수 있다.
# 보통은 URL이 길기 때문에 가독성을 위해 변수로 저장해서 사용한다.
img_url = 'https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FVF9W6%2FbtrCCFKYs6k%2FxMJQ2AfBtZRiEJlML71Lak%2Fimg.png'
st.image(img_url)

# >>> 비디오 파일의 경로와 모드가 포함 되어 있는 변수를 이용하여 불러오기 -----

# 변수 = open('경로와 파일 이름', '모드')
# .video(변수)
# 여기서 모드란, 읽고 쓰기의 개념으로 무엇을 할지 정하는 것, rb를 사용한다. (read, 읽기)
# rb는 이진 읽기라는 뜻이긴 한데, 쉽게 말해서 텍스트를 제외한 파일은 rb를 사용하면 된다.

video_file = open('시연.mp4', 'rb')
st.video(video_file)

# >>> 비디오 파일의 경로를 그대로 넣어 다이렉트로 불러오기 -----

# .video('경로와 파일이름', format='video/mp4')

# 비디오 파일의 확장자만 잘 맞으면 format은 생략해도 된다.
st.video('시연.mp4')


# --------------------
# 텍스트 필드로 유저와 상호작용하기
# --------------------

# >>> 텍스트 필드에 값 입력 받기 (text_input) -----

# .text_input('보여줄 메시지')
# 입력 받은 데이터를 이용해 상호작용 
# 옵션 > max_chars 를 사용하여 최대 길이 설정
# 옵션 > type=password 을 사용하여 별표 처리

import streamlit as st

name = st.text_input('이름을 입력하세요 !', max_chars=10)
if name != '' : # 입력시 출력
    st.subheader(name + '님 안녕하세요.')

pwd = st.text_input('비밀번호 입력', type='password')
st.write(pwd)

# >>> 텍스트 필드에 여러줄 입력받기 (text_area) -----

# .text_area('보여줄 메시지') 
# 옵션 > height 를 사용하여 칸 높이 설정, at least 68 pixels

message = st.text_area('메세지를 입력하세요.', height = 68)
st.text(message)

# >>> 텍스트 필드에 숫자 데이터 입력받기 (number_input) -----

# .number_input('보여줄 메시지', 시작값, 끝값)
# 숫자 데이터는 정수와 실수로 받아서 처리 할 수 있다.

# 정수 입력
st.number_input('숫자 입력', 1, 100)
# 실수 입력
st.number_input('실수 입력', 1.0, 100.0)

# >>> 텍스트 필드에 날짜/시간을 입력 받아 데이터 입력받기 (date/time_input) -----

# 날짜 : .date_input('보여줄 메시지')
# 입력 받은 날짜로 요일을 구할 수 있음
# 요일 구하기 : 날짜데이터.weekday() / strftime('%A')
# 시간 : .time_input('보여줄 메시지')

my_date = st.date_input('약속 날짜')
st.write(my_date)
st.write(my_date.weekday())
st.write(my_date.strftime('%A'))
 
my_time = st.time_input('시간 입력')
st.write(my_time)

# >>> 사용자에게 색 입력 받기 (color_picker) -----

# .color_picker('보여줄 메시지') : 컬러 팔레트에서 색을 선택

my_color = st.color_picker('색 선택')
st.write(my_color)


# --------------------
# GitHub에 업로드
# --------------------

import streamlit as st
import os
from datetime import datetime

# >>> 파일 업로드 함수 -----

# .file_uploader('보여줄 메시지', type= '업로드파일 확장자')
# 옵션 > accept_multiple_files=True로 하면 여러 파일을 업로드

# 업로드를 할 수 있게 해주는 기능이 사용자에게 나타나지만, 실제로 업로드가 되진 않는다.
# 업로드한 파일의 정보를 담고 있으며 이 정보를 이용해 업로드를 진행해아한다.

upload_file = st.file_uploader('이미지 파일 선택', type=['jpg', 'png', 'jpeg'])

# >>> 파일이름 정의하기 -----

# 업로드된 파일의 정보를 저장하기 위한 파일의 제목을 정해야 한다.

current_time = datetime.now()
upload_file.name = current_time.isoformat().replace(':', '_') + '.jpg'

# >>> 파일 불러오기/저장 함수 -----

# .open(파일이름, 모드)
# .write(경로와 파일이름)
# .close()

# 업로드 파일을 가져오고 서버에 저장을 할 예정이기 때문에 wb(쓰기)를 사용
# with를 사용해 close()를 사용할 필요가 없습니다.
# getbuffer를 활용해 파일의 크기를 확인하고 알아서 저장하게 합니다.
# 주의 사항 : getbuffer에는 반드시 파일의 데이터를 가지고 있는 변수여야 합니다.

# 파일 쓰기(저장), 성공시 안내 문구 출력
with open(upload_file.name, 'wb') as f:
    f.write(upload_file.getbuffer())
    st.success("Saved file : {}".format(upload_file.name))

# >>> 전체 소스 코드 -----

import streamlit as st
import os
from datetime import datetime
 
def main() :
    # 이미지 업로더, 이미지 파일만 업로드하게 설정
    st.title('이미지 파일 업로드')
    upload_file = st.file_uploader('이미지 파일 선택', type=['jpg', 'png', 'jpeg'])
 
    # 지금 시간을 기준으로 업로드 파일 이름 설정
    current_time = datetime.now()
    upload_file.name = current_time.isoformat().replace(':', '_') + '.jpg'
 
    # 파일 생성
    with open(upload_file.name, 'wb') as f :
        f.write(upload_file.getbuffer())
        st.success("Saved file : {}".format(upload_file.name))
 
if __name__ == '__main__' :
    main()


# --------------------
# 라이브러리로 분리하여 작동하기
# --------------------

# >>> 메인 파일 'test.py' -----

import streamlit as st
import test_home
 
def main():
    st.title(' 파일 분리 앱 ')
    menu = ['Home', 'EDA', 'ML', 'About']
    choice = st.sidebar.selectbox('메뉴', menu)
 
    if choice == menu[0] :
        test_home.run_home()

if __name__ == '__main__' :
    main()

# >>> 서브 파일 : 'test_home.py' -----

import streamlit as st 

def run_home():
    st.subheader('홈 화면입니다')
    st.text('파일 분리 앱 테스트')


# =====================
# 웹 대시보드에 그래프 그리기
# =====================

# matplotlib/seaborn 라이브러리도 사용가능


# --------------------
# Streamlit 자체 제공 그래프
# --------------------

import streamlit as st
import pandas as pd
import seaborn as sns

df = sns.load_dataset('iris')

# >>> 선으로 표현된 그래프 그리기 (line_chart) -----

# .line_chart(데이터) : 그래프를 꺾은 선으로 시각화
st.line_chart(df)

# >>> 영역으로 표현된 그래프 그리기 (area_chart) -----

# .area_chart(데이터) : 그래프를 범위형으로 시각화
st.area_chart(df)

# >>> 막대으로 표현된 그래프 그리기 (bar_chart) -----

# .bar_chart(데이터) : 그래프를 막대로 시각화
st.bar_chart(df)

# >>> 지도로 표현된 맵 그래프 그리기 (map) -----

# .map(데이터) : 경도와 위도를 이용하여 지도의 해당 부분을 표시
df2 = pd.DataFrame({'lat': [37.5684, 37.5701],'lon':[126.6762, 126.6820]})
st.map(df2)


# --------------------
# altair 라이브러리를 이용
# --------------------

import streamlit as st
import altair as alt
import seaborn as sns

df = sns.load_dataset('iris')

# >>> 점으로 표현된 그래프 그리기 (mark_circle) -----

# .Chart(데이터) .mark_circle() .encode(x=x축데이터, y=y축데이터, color=그룹별 색상)
# streamlit.altair_chart(데이터) : 스트림릿을 이용하여 altair로 생성된 데이터만 사용 할 수 있다.

alt_chart = alt.Chart(df).mark_circle().encode(x='petal_length',y='petal_width',color='species')
st.altair_chart(alt_chart)


# --------------------
# plotly 라이브러리를 이용
# --------------------

import plotly.express as px

# >>> 비율이 표시된 원형 그래프 그리기 (pie) -----

# .pie(데이터, names='인덱스', values='값', title= '그래프에 표시될 제목')
# streamlit.plotly_chart(데이터) : 스트림릿을 활용하여 plotly로 생성된 데이터만 사용 할 수 있다.

fig = plotly.pie(df, names='lang', values='Sum', title='각 언어별 파이차트')
st.plotly_chart(fig)



