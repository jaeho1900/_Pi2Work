# =====================
# 기본 문형 및 작동 방식
# =====================

# --------------------
# main 함수 작성
# --------------------

import streamlit as st
from PIL import Image

def main() :
        img1 = Image.open('pic.png')
        # col1, col2 = st.columns([2,3])
        tab1, tab2 = st.tabs(['Tab A', 'Tab B'])

        # with col1:
        with tab1:
                st.title('This is Title')
                st.header('This is Header')
                st.subheader('This is Subheader')
        # with col2:
        with tab2:
                st.header('this is Tab2')
                st.image(img1)
                st.checkbox('this is checkbox')

        st.sidebar.title('this is sidebar')
        st.sidebar.checkbox('체크박스에 표시될 문구')

if __name__ == '__main__' :
    main()

# >>> 실행 -----

# 터미널에서 streamlit run 파일명.py
# http://localhost:8501/ 브라우저로 접속

# >>> 종료 -----

# 터미널 창에서 Ctrl+C


# --------------------
# 세션 스테이트
# --------------------

# 상태가 자꾸 변하는 것들을 세션스테이트에 관리해두면 바뀌는 값에 따라 내용이 바뀌는 것들을 기록할 수 있다.

# 세션스테이트에 초기값이 없으면, if문을 통해 초기값을 생성합니다.
# 세션스테이트에 사용자가 입력한 인풋에 따라서 dataframe이 재가공 되는데 이 값이 interactive하게 지정되게 하기 위해 st.session_state값으로 사용합니다.

# 예시코드 
# import streamlit as st

# if 'final_dataframe' not in st.session_state:
#   # session state 에 final 이라는 값이 없으면, 초기값 데이터를 집어넣습니다.
#   st.session_state['final_dataframe']= df

# # 아래 코드는 df의 테이블 값이 바뀌더라도 interactive하게 연동되서 바뀌지 않습니다.
# st.table(df)

# #  아래 코드는  dataframe이 조작될 때 마다 session_state객체 안에 final_dataframe값을 변경하면,
# #  수정 될 때  계속 바뀌어서 보여줍니다. 
# st.table(st.session_state.final_dataframe)


# --------------------
# 캐쉬
# --------------------

# 시간이 오래걸리는 결과물을 미리 만들어두고, 보이지 않는 곳에 캐싱하여 필요할때 꺼내는 것을 cache기능이라고 할 수 있다.
# 큰 데이터를 로드하거나, 실행이 오래걸리는 복잡한 연산을 해야할 때 cache기능을 이용

import streamlit as st
import pandas as pd 

file_path = '~~~filepath'
@st.cache
def load_data():
  data = pd.read_csv(file_path)
  return data


# --------------------
# DBMS 연결 및 배포
# --------------------

# DB연결 : https://docs.streamlit.io/develop/tutorials/databases
# 링크배포 : https://docs.streamlit.io/deploy/tutorials


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
# 레이아웃
# =====================

# >>> 구성 -----

# 여백 |        이미지           | 여백
# 여백 | 셀렉트박스| 데이터프레임 | 여백
# 여백 |     긴셀렉트박스        | 여백
# 여백 | 동영상   | 동영상설명    | 여백

from tkinter.tix import COLUMN
from pyparsing import empty
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

# 꽉찬화면 : 라이브러리 불러오는 부분 밑에 추가해 주면 가운데 정렬 영역을 좌정렬 꽉찬 화면으로 바꾼다.
st.set_page_config(layout="wide")

empty1,con1,empty2 = st.columns([0.3, 1.0, 0.3])
empyt1,con2,con3,empty2 = st.columns([0.3, 0.5, 0.5, 0.3])
empyt1,con4,empty2 = st.columns([0.3, 1.0, 0.3])
empyt1,con5,con6,empty2 = st.columns([0.3, 0.5, 0.5, 0.3])

with empty1 :
    empty() # 여백부분1    
with con1 :
    st.subheader('이미지')
with con2 :
    st.subheader('셀렉트박스')
with con3 :
    st.subheader('데이터프레임')
with con4 :
    st.subheader('긴셀렉트박스')
with con5 :
    st.subheader('동영상')
with con6 :
    st.subheader('동영상설명')
with empty2 :
    empty() # 여백부분2

# >>> column -----

import streamlit as st

# 공간을 2:3 으로 분할하여 col1과 col2라는 이름을 가진 컬럼을 생성합니다.  
col1,col2 = st.columns([2,3])

# with 구문 사용
with col1 :
  st.title('here is column1')
with col2 :
  st.title('here is column2')
  st.checkbox('this is checkbox1 in col2 ')

# with 구문 이외 사용 
col1.subheader(' i am column1  subheader !! ')
col2.checkbox('this is checkbox2 in col2 ') 

# >>> Tab -----

import streamlit as st

# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
tab1, tab2= st.tabs(['Tab A' , 'Tab B'])

with tab1:
  st.write('hello')
with tab2:
  st.write('hi')

# >>> sidebar -----

import streamlit as st

st.sidebar.title('this is sidebar')
st.sidebar.checkbox('체크박스에 표시될 문구')


# =====================
# 텍스트
# =====================

import streamlit as st

st.title('this is title')
st.header('this is header')
st.subheader('this is subheader')

# 일반 텍스트
st.title('타이틀 웹 대시보드')
st.header('헤더 이 영역은 헤더')
st.subheader('서브 헤더 이 영역은 서브헤더')
st.text('텍스트 웹 대시보드 개발하기')

# 안내 텍스트 박스
st.success('작업이 성공 했을 때 사용하기')
st.warning('경고 문구를 보여주고 싶을 때 사용하기')
st.info('정보를 보여주고 싶을 때 사용하기')
st.error('문제가 발생했을 때 사용하기')

# 포맷팅 출력
name = ['홍길동', '마징가']
st.text('제 이름은 {}입니다.'.format(name))

# 파이썬의 함수 사용법을 보여주고 싶을 때
st.help(sum)
st.help(len)

# >>> 긴 문자열 출력할때 텍스트 영역 -----

content = '''요즘 스트림릿(Streamlit)로 
프로젝트 진행중인데~
화면구성이 내맘처럼 쉽게 안되네요^^
오늘도 여러가지 찾아보느라
삽질에 삽질을ㅠ'''

st.text(content)
st.markdown(content)


# --------------------
# 텍스트 필드로 유저에게 입력받기
# --------------------

# >>> 텍스트 필드에 값 입력 받기 (text_input) -----

# .text_input('보여줄 메시지')
# 입력 받은 데이터를 이용해 상호작용 
# 옵션 > max_chars 를 사용하여 최대 길이 설정
# 옵션 > type='password' 을 사용하여 별표 처리

import streamlit as st

name = st.text_input('이름을 입력하세요 !', max_chars=10)
if name != '' : # 입력시 출력
    st.subheader(name + '님 안녕하세요.')

pwd = st.text_input('비밀번호 입력', type='password')
st.write(pwd)

# >>> 텍스트 필드에 여러줄 입력받기 (text_area) -----

# .text_area('보여줄 메시지') 
# 옵션 > height 를 사용하여 글상자높이 설정, at least 68 pixels

message = st.text_area('메세지를 입력하세요.', height = 68)
st.text(message)

# >>> 텍스트 필드에 숫자 데이터 입력받기 (number_input) -----

# .number_input('보여줄 메시지', 시작값, 끝값)
# 숫자 데이터는 정수와 실수로 받아서 처리 할 수 있다.

# 정수 입력
st.number_input('숫자 입력', 1, 100)
# 실수 입력
st.number_input('실수 입력', 1.0, 100.0)

# >>> 텍스트 필드에 날짜 또는 시간을 입력 받아 데이터 입력받기 (date/time_input) -----

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


# =====================
# 데이터프레임
# =====================

import streamlit as st
import seaborn as sns

df = sns.load_dataset('iris')
species = df['species'].unique()

# pandas dataframe을 보여주기 위해 st.write를 사용해도 되지만,
st.write(df.head())

# 더 많은 옵션들을 사용할 수 있는 pd.dataframe을 더 많이 사용합니다.
# hide_index입니다. (인덱스 행을 없애주면 테이블이 더 깔끔해 보여서요)
# st.dataframe(df, hide_index = True)
st.dataframe(df.head(), hide_index = True)

# st.table()을 사용하기도 합니다. 사용하는 방법은 st.dataframe과 완전히 동일한데,
# 테이블의 디자인이 조금 달라서 table이 더 깔끔해보인다 싶을 때 사용합니다.
st.table(df.head())


# =====================
# 상호작용 도구
# =====================

import numpy as np
import pandas as pd 
from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt
import streamlit as st

# import seaborn as sns
# df = sns.load_dataset('iris')
# species = df['species'].unique()

iris_dataset = load_iris()

df= pd.DataFrame(data=iris_dataset.data,columns= iris_dataset.feature_names)
df.columns= [ col_name.split(' (cm)')[0] for col_name in df.columns] # 컬럼명을 뒤에 cm 제거하였습니다
df['species']= iris_dataset.target 

species_dict = {0 :'setosa', 1 :'versicolor', 2 :'virginica'} 

def mapp_species(x):
  return species_dict[x]

df['species'] = df['species'].apply(mapp_species)
print(df)

# >>> 사이드 바 -----

# 화면 왼쪽에 프레임을 나누어 따로 표기
# .sidebar ~ : 왼쪽 프레임에서 할 행동 표시

st.sidebar.text('안녕하세요')
st.sidebar.button('버튼')

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

# 라디오에 선택한 내용을 radio select변수에 담습니다.
radio_select =st.sidebar.radio(
    "what is key column?",
    ['sepal length', 'sepal width', 'petal length','petal width'],
    horizontal=True
    )

# 라디오버튼을 수평으로 놓는 방법
st.radio(label = 'Radio buttons', options = ['5점', '4점', '2점', '1점'])
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

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

# 사이드바에 select box를 활용
st.sidebar.title('Iris Species🌸')

# select_species 변수에 사용자가 선택한 값을 지정
select_species = st.sidebar.selectbox(
    '확인하고 싶은 종을 선택하세요',
    ['setosa','versicolor','virginica']
)

# 필터링된 임시 dataframe을 생성
tmp_df = df[df['species']== select_species]

# 선택한 종의 맨 처음 5행을 보여줍니다.
st.table(tmp_df.head())

# >>> 멀티 셀렉트 -----

# 여러 개의 목록에서 하나 이상을 선택
# .multiselect('보여줄 메시지', '리스트1, 리스트2...')

columns_list = df.columns
choice_list = st.multiselect('컬럼을 선택하세요', columns_list)
st.write( df[choice_list] )

# 여러 값을 선택하기 위해서는 multiselect를 이용, return : list
select_multi_species = st.sidebar.multiselect(
    '확인하고자 하는 종을 선택해 주세요. 복수선택가능',
    ['setosa','versicolor','virginica']

)
tmp_df = df[df['species'].isin(select_multi_species)]
st.table(tmp_df)

# >>> 슬라이더 -----

# 숫자를 조정하는데 주로 사용, 조정된 숫자로 작업 수행
# .slider('보여줄 메시지', 시작값, 끝값, 기본값, 스텝)

age = st.slider('나이', 1, 120, 30, 10)
st.text('제가 선택한 나이는 {}입니다.'.format(age))

# 사이드바에 slider를 만듭니다.
slider_range = st.sidebar.slider(
    "choose range of key column",
     0.0,      # 시작 값 
     10.0,     # 끝 값  
    (2.5, 7.5) # 기본값, 앞 뒤로 2개 설정 /  하나만 하는 경우 value=2.5 이런 식으로 설정 가능
)

# 필터 적용버튼 생성
start_button = st.sidebar.button(
    "filter apply 📊" #"버튼에 표시될 내용"
)

# button 이 눌리는 경우 start_button의 값이 true로 바뀌게 된다.
# 이를 이용해서 if문으로 버튼이 눌렸을 때를 구현 
# slider_range : list 형식으로 2개의 값이 저장됩니다. 양쪽 앞뒤로 두개의 값을 저장합니다.
# slider_range[0] : 최솟값 
# slider_range[1] : 최댓값  
if start_button:
    tmp_df = df[df['species'].isin(select_multi_species)]
    # slider input으로 받은 값에 해당하는 값을 기준으로 데이터를 필터링합니다.
    tmp_df= tmp_df[ (tmp_df[radio_select] >= slider_range[0]) & (tmp_df[radio_select] <= slider_range[1])]
    st.table(tmp_df)
    # 성공문구 + 풍선이 날리는 특수효과 
    st.sidebar.success("Filter Applied!")
    st.balloons()

# >>> 익스팬더 -----

# 활성화시 숨겨져 있던 정해진 작업을 수행 (확장 개념, =펼쳐보기 느낌)
# .expander('보여줄 메시지')

with st.expander('Hello') :
    st.text('변경')
    st.write(df)


# =====================
# 매체(이미지, 영상, 음악)
# =====================

import streamlit as st
from PIL import Image

# >>> PIL 패키지에 이미지 모듈을 통해 이미지 열기 -----

img = Image.open('zarathu.png')
st.image(img)

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

# >>> 오디오 -----

import streamlit as st
audio_file = open('data2/song.mp3', 'rb')
st.audio( audio_file.read() , format='audio/mp3')


# =====================
# 그래프
# =====================

# plotly, matplotlib, seaborn 등 사용 가능


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
k = df.groupby('species')['sepal_length'].sum()

# >>> 점으로 표현된 그래프 그리기 (mark_circle) -----

# .Chart(데이터) .mark_circle() .encode(x=x축데이터, y=y축데이터, color=그룹별 색상)
# streamlit.altair_chart(데이터) : 스트림릿을 이용하여 altair로 생성된 데이터만 사용 할 수 있다.

alt_chart = alt.Chart(df).mark_circle().encode(x='petal_length',y='petal_width',color='species')
st.altair_chart(alt_chart)


# --------------------
# plotly
# --------------------

# st.plotly_chart(figure_or_data, use_container_width=False, theme="streamlit", **kwargs)
# figure_or_data : 그림의 이름이 들어가는 위치
# use_container_width : 해상도를 조절 여부(True, False)
# theme : 테마 설정(streamlit, None)

import plotly.express as px
import streamlit as st

df = px.data.gapminder()

fig = px.scatter(
    df.query("year==2007"),
    x="gdpPercap",
    y="lifeExp",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=60,
)
fig.show()

tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
with tab1:
    # Use the Streamlit theme.(default, So you can also omit the theme argument)
    st.plotly_chart(fig, theme="streamlit", use_container_width=True)
with tab2:
    # Use the native Plotly theme.
    st.plotly_chart(fig, theme=None, use_container_width=True)


# >>> 비율이 표시된 원형 그래프 그리기 (pie) -----

# .pie(데이터, names='인덱스', values='값', title= '그래프에 표시될 제목')
# streamlit.plotly_chart(데이터) : 스트림릿을 활용하여 plotly로 생성된 데이터만 사용 할 수 있다.

import streamlit as st
import plotly.express as px
import seaborn as sns

df = sns.load_dataset('iris')
df_k = df.groupby('species')['sepal_length'].sum()

fig = px.pie(df_k, names='sepal_length', title='파이차트')
st.plotly_chart(fig)

# >>> 막대로 표현된 그래프 그리기 (bar) -----

# .bar(데이터, x=x축데이터, y=y축데이터)
# streamlit.plotly_chart(데이터)

df_sorted = df_k.sort_values(ascending=False) # 합이 높은순 정렬
fig = px.bar(df_sorted)
st.plotly_chart(fig)


# --------------------
# 멀티 페이지 사이드바 메뉴 시각화하기(streamlit_option_menu)
# --------------------

# 스트림릿 옵션 메뉴 설치
# pip install streamlit-option-menu

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io

with st.sidebar:
    choose = option_menu("App Gallery", ["About", "Photo Editing", "Project Planning"],
                         menu_icon="bi bi-airplane-engines", # "app-indicator",
                         icons=['house', 'camera fill', 'kanban'],
                         default_index=0,  # default_index = 처음에 보여줄 페이지 인덱스 번호
                         styles={
                                 "container": {"padding": "5!important", "background-color": "#D5D5D5"},
                                 "icon": {"color": "orange", "font-size": "25px"}, 
                                 "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#ABF200"},
                                 "nav-link-selected": {"background-color": "#02ab21"},
                                }
                        )

# >>> 메뉴 아이콘 바꾸기 -----

# 메뉴 아이콘은 아래의 사이트에서 원하는 아이콘을 클릭하여 선택한 후,
# 아이콘 페이지의 'Icon font' 속 <i class ="이름"> 에서 이름을 복사하여 입력한다.
# https://icons.getbootstrap.com/


# =====================
# 맵
# =====================

import numpy as np
import pandas as pd 
import streamlit as st

#지도 위에 표시될 점 좌표 값을 위도경도에 담습니다 .
#중심점의 위도, 경도 좌표를 리스트에 담습니다.
base_position =  [37.5073423, 127.0572734]

# base_position에, 랜덤으로 생성한 값을 더하여 5개의 좌표를 데이터 프레임으로 생성하였고,
# 컬럼명은 위도 :lat  경도 lon으로 지정하였습니다. 
map_data = pd.DataFrame(
    np.random.randn(5, 1) / [20, 20] + base_position , 
    columns=['lat', 'lon'])

# map data 생성 : 위치와 경도 
print(map_data)

# 웹사이트에 어떤 코드인지 표시해주기 
st.code('st.map(map_data)')
# 제목 생성 
st.subheader('Map of Data ')
# 지도 생성 
st.map(map_data)


# =====================
# 진행상태바
# =====================

# >>> st.progress -----

import time
import streamlit as st

latest_iteration = st.empty()
bar = st.progress(0)

# Update the progress bar with each iteration.
for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  # 0.05 초 마다 1씩증가
  time.sleep(0.05)

# 시간 다 되면 풍선 이펙트 보여주기 
st.balloons()

# >>> st.spinner -----

import time 
import streamlit as st

with st.spinner('Wait for it...'):
  time.sleep(5)
  st.success('Done!') 
