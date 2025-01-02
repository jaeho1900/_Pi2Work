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

# 세션스테이트에 초기값이 없으면, if문을 통해 초기값을 생성한다.
# 세션스테이트에 사용자가 입력한 인풋에 따라서 dataframe이 재가공 되는데 이 값이 interactive하게 지정되게
# 하기 위해 st.session_state값으로 사용합니다.

# 예시코드 
# import streamlit as st

# if 'final_dataframe' not in st.session_state:
#   st.session_state['final_dataframe']= df

# dataframe이 조작될 때 마다 session_state 객체 안의 final_dataframe이 interactive하게 변경된다.
# st.table(st.session_state.final_dataframe)


# --------------------
# 캐쉬
# --------------------

# 시간이 오래걸리는 결과물을 미리 만들어두고, 필요할때 꺼내는 것이 cache기능이다.

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

# >>> 수평 구분선 -----

st.divider()


# =====================
# 텍스트
# =====================

import streamlit as st

# >>> markdown으로 CSS 적용 -----

# st.markdown 인자
# body (str) : 표시할 마크다운 텍스트를 입력한다
# unsafe_allow_html (bool) : True로 설정하면 HTML 태그를 사용할 수 있다. (기본값은 False)
# help (str) : 텍스트 옆에 표시되는 선택적 툴팁.

# 기본 마크다운 사용
st.markdown("# 대제목")
st.markdown("## 부제목")
st.markdown("*이탤릭체 텍스트*")
st.markdown("**볼드 텍스트**")
st.markdown("`인라인 코드`")

# 맞춤 정렬
st.markdown('<div style="text-align: center;">Hello World!</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: left;">Hello World!</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: right;">Hello World!</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">Hello World!</div>', unsafe_allow_html=True) # 균등맞춤

# 가운데 맞춤(1)
st.markdown("<h1 style='text-align: center; color: grey;'>Big headline</h1>", unsafe_allow_html=True)

# 가운데 맞춤(2)
title_writing = "Test Title"
title_format = f'<p style="text-align: center; font-family: ' \
               f'Arial; color: #808080; font-size: 40px; ' \
               f'font-weight: bold;">{title_writing}</p>'
st.markdown(title_format, unsafe_allow_html=True)

# 리스트와 링크를 포함하는 마크다운
st.markdown("""
- 목록 항목 1
- 목록 항목 2 [Google 링크](https://www.google.com)
""")

# HTML 태그 사용 (unsafe_allow_html=True일 때만 작동)
st.markdown("<span style='color:red'>빨간색 텍스트</span>", unsafe_allow_html=True)

# st.markdown으로 <style> 태그를 직접 입력해주어야합니다.
# unsafe_allow_html 옵션을 True로 설정해줍니다.

# 브라우저의 개발자 도구를 이용해서 스타일을 적용하고 싶은 태그를 확인하고,
# <style> 태그 안 쪽에 CSS 코드를 작성해주어 스타일을 적용할 수 있습니다.
st.markdown("""
<style>
	
</style>
""", unsafe_allow_html=True)

st.title('this is title', help='Title')
st.header('this is header', help=None, divider=False)
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

# >>> 데이터프레임 적용 -----

import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'A':[1,2,3,4],
    'B':[1111,2,33,44444],
    'C':[1,2,3,4]
})

styled_df = df.style.set_properties(**{
    "background-color": "white", 
    "color": "black", 
    "border-color": "black", 
    'text-align': 'center'
})

st.dataframe(styled_df)
st.write(styled_df.to_html(), unsafe_allow_html=True)


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
st.number_input('숫자 입력', min_value=1, max_value=100, value=50)
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

# >>> write -----

# pandas dataframe을 보여주기 위해 st.write를 사용해도 되지만,
st.write(df.head())

# >>> dataframe -----

# 더 많은 옵션들을 사용할 수 있는 pd.dataframe을 더 많이 사용합니다.
# use_container_width : True로 설정 시, 부모 컨테이너의 폭에 맞춤.
st.dataframe(
       data=df.head(),
       width=None,
       height=None,       
       use_container_width=False, 
       hide_index=None, 
       column_order=None, 
       column_config=None
)

df1 = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
st.dataframe(df1)  # Same as st.write(df)

df2 = pd.DataFrame(
    {
        "name": ["Roadmap", "Extras", "Issues"],
        "url": ["https://roadmap.streamlit.app", "https://extras.streamlit.app", "https://issues.streamlit.app"],
        "stars": [random.randint(0, 1000) for _ in range(3)],
        "views_history": [[random.randint(0, 5000) for _ in range(30)] for _ in range(3)],
    }
)
st.dataframe(
    df2,
    column_config={
        "name": "App name",
        "stars": st.column_config.NumberColumn(
            "Github Stars",
            help="Number of stars on GitHub",
            format="%d ⭐",
        ),
        "url": st.column_config.LinkColumn("App URL"),
        "views_history": st.column_config.LineChartColumn(
            "Views (past 30 days)", y_min=0, y_max=5000
        ),
    },
    hide_index=True,
)

# >>> table -----

# st.table()을 사용하기도 합니다. 사용하는 방법은 st.dataframe과 완전히 동일한데,
# 테이블의 디자인이 조금 달라서 table이 더 깔끔해보인다 싶을 때 사용합니다.
st.table(df.head())

# >>> data_editor -----

# 테이블 형태의 UI에서 편집할 수 있게 하는 위젯을 표시
st.data_editor(
       data=None, 
       width=None,
       height=None,
       use_container_width=False,
       hide_index=None,
       column_order=None,
       column_config=None,
       num_rows="fixed",  # 사용자가 행을 추가하거나 삭제할 수 있는지 여부를 지정
       disabled=False,    # 열의 편집 가능 여부를 제어
       key=None,
       on_change=None,
       args=None,
       kwargs=None
)

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)
edited_df = st.data_editor(df)
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]

# >>> metric -----

# 주요 지표를 크고 굵은 글꼴로 표시하는 위젯
# label
# 지표의 헤더 또는 제목.
# Markdown 요소를 포함할 수 있다.

# value
# 지표의 값. int, float, str, None 중 하나를 사용할 수 있다.

# delta
# 지표가 어떻게 변화했는지 나타내는 지표.
# 양수 또는 음수일 수 있으며, None일 경우 표시되지 않는다.

# delta_color
# 변화량의 색상을 지정합니다.
# "normal", "inverse", "off" 중 하나를 선택할 수 있다.

# help
# 지표 레이블 옆에 표시되는 선택적 툴팁.

# label_visibility
# 레이블의 가시성을 지정. "visible", "hidden", "collapsed" 중 하나를 선택할 수 있다.

st.metric(label, value, delta=None, delta_color="normal", help=None, label_visibility="visible")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

# >>> st.column_config.Column -----

# st.column_config.Column은 st.dataframe 또는 st.data_editor의 열을 구성할 때 사용
# label
# 열의 상단에 표시되는 레이블
# width
# 열의 표시 너비 ("small", "medium", "large" 중 하나).
# help
# 열 레이블 위로 마우스를 가져갔을 때 표시되는 도움말 툴팁.
# disabled
# 이 열의 편집을 비활성화할지 여부를 지정.
# required
# 편집된 셀이 None이 아닌 값을 가져야 하는지 여부를 지정.

df = pd.DataFrame(
    {
        "name": ["Park", "Lee", "Kim", "Choi"],
        "age": [24, 31, 40, 19],
    }
)

st.dataframe(
    df,
    column_config={
        "name": st.column_config.Column(
            label="Name Column",
            width="large",
            help="Please enter a name",
            required=True
        )
    }
)

# >>> st.column_config.TextColumn -----

# st.data_editor 사용 시 텍스트 입력 위젯을 통해 편집을 활성화할 수 있다.

# label
# 열의 상단에 표시되는 레이블
# width
# 열의 표시 너비 ("small", "medium", "large" 중 하나).
# help
# 열 레이블 위로 마우스를 가져갔을 때 표시되는 도움말 툴팁.
# disabled
# 이 열의 편집을 비활성화할지 여부.
# required
# 편집된 셀이 None이 아닌 값을 가져야 하는지 여부를 지정.
# max_chart
# 셀이 입력할 수 있는 최대 글자 수
# validate
# 셀의 값이 특정 조건을 충족하는지 확인. 정규식을 통해 작성 가능.

st.header("📌 TextColumn")
st.data_editor(
    df,
    column_config={
        "name": st.column_config.TextColumn(
            label="Name Column",
            width="medium",
            help="You can modify the name (max 5)",
            max_chars=5,
        )
    }
)

# >>> st.column_config.NumberColumn -----

# label
# 열의 상단에 표시되는 레이블.
# width
# 열의 표시 너비 ("small", "medium", "large" 중 하나).
# help
# 열 레이블 위로 마우스를 가져갔을 때 표시되는 도움말 툴팁.
# disabled
# 이 열의 편집을 비활성화할지 여부.
# required
# 편집된 셀이 None이 아닌 값을 가져야 하는지 여부.
# default
# 사용자가 새 행을 추가할 때 이 열의 기본값을 지정.
# format
# 셀 값의 표시 형식을 지정. 예를 들어, 소수점 이하 자릿수나 통화 형식 등을 설정할 수 있다. ("$ %.2f")
# min_value
# 셀이 가질 수 있는 최소값.
# max_value
# 셀이 가질 수 있는 최대값.
# step
# 셀 값이 증가 또는 감소할 수 있는 단계 크기를 지정.

st.data_editor(
    df,
    column_config={
        "age": st.column_config.NumberColumn(
            label="Age Column",
            width="medium",
            help="You can only enter numbers",
            required=True,
            min_value=10,
            max_value=99,
            format="%d세"
        )
    }
)

# >>> st.column_config.CheckboxColumn -----

# label
# 열 상단에 표시되는 레이블.
# width
# 열의 표시 너비. ("small", "medium", "large" 또는 None)
# help
# 열 레이블 위로 마우스를 가져갔을 때 표시되는 도움말 툴팁.
# disabled
# 이 열의 편집을 비활성화할지 여부를 지정
# required
# 편집된 셀이 None이 아닌 값을 가져야 하는지 여부를 지정
# default
# 사용자가 새 행을 추가할 때 이 열의 기본값을 지정.

df = pd.DataFrame(
    {
        "name": ["Park", "Lee", "Kim", "Choi"],
        "age": [24, 31, 40, 19],
        "flag": [True, False, True, False]
    }
)

st.data_editor(
    df,
    column_config={
        "flag": st.column_config.CheckboxColumn(
            label="Attendance status",
            help="Check if you are present",
            default=False
        )
    }
)

# >>> st.column_config.SelectboxColumn -----

# label
# 열 상단에 표시되는 레이블.
# width
# 열의 표시 너비. ("small", "medium", "large" 또는 None)
# help
# 열 레이블 위로 마우스를 가져갔을 때 표시되는 도움말 툴팁.
# disabled
# 이 열의 편집을 비활성화할지 여부를 지정
# required
# 편집된 셀이 None이 아닌 값을 가져야 하는지 여부를 지정
# default
# 사용자가 새 행을 추가할 때 이 열의 기본값을 지정
# options
# 사용자가 선택할 수 있는 옵션 목록

df = pd.DataFrame(
    {
        "name": ["Park", "Lee", "Kim", "Choi"],
        "age": [24, 31, 40, 19],
        "flag": [True, False, True, False],
        "lang": [None, "JavaScript", "Python", "C"]
    }
)

st.data_editor(
    df,
    column_config={
        "lang": st.column_config.SelectboxColumn(
            label="Main Language",
            help="What is your the main language?",
            options=[
                "JavaScript", 
                "Python",
                "C",
                "Rust"
            ]
        )
    }
)

# >>> st.column_config.DatetimeColumn -----

# label
# 열 상단에 표시되는 레이블
# width
# 열의 표시 너비 ("small", "medium", "large" 또는 None)
# help
# 열 레이블 위로 마우스를 가져갔을 때 표시되는 도움말 툴팁
# disabled
# 이 열의 편집을 비활성화할지 여부.
# required
# 편집된 셀이 값을 가져야 하는지 여부.
# default
# 새 행이 추가될 때 이 열의 기본값을 지정.
# format
# 날짜 및 시간이 표시되는 형식을 지정.
# min_value
# 입력할 수 있는 최소 날짜 및 시간을 지정.
# max_value
# 입력할 수 있는 최대 날짜 및 시간을 지정.
# step
# 시간 증가 또는 감소의 단계 크기를 지정 (초단위).
# timezone
# 이 열의 시간대를 지정.

from datetime import datetime

df = pd.DataFrame(
    {
        "name": ["Park", "Lee", "Kim", "Choi"],
        "age": [24, 31, 40, 19],
        "flag": [True, False, True, False],
        "lang": [None, "JavaScript", "Python", "C"],
        "join": [
            datetime(2024, 4, 22, 12, 30),
            datetime(1992, 11, 26, 18, 0),
            datetime(2021, 6, 6, 12, 00),
            datetime(2024, 1, 1, 1, 0),
        ]
    }
)

st.data_editor(
    df,
    column_config={
        "join": st.column_config.DatetimeColumn(
            label="Join Date",
            help="Enter the date and time you signed up",
            min_value=datetime(1992, 1, 1),
            max_value=datetime(2024, 1, 20),
            step=60
        )
    }
)

# >>> st.column_config.DateColumn -----

# label
# 열 상단에 표시되는 레이블
# width
# 열의 표시 너비 ("small", "medium", "large" 또는 None)
# help
# 열 레이블 위로 마우스를 가져갔을 때 표시되는 도움말 툴팁
# disabled
# 이 열의 편집을 비활성화할지 여부.
# required
# 편집된 셀이 값을 가져야 하는지 여부.
# default
# 새 행이 추가될 때 이 열의 기본값.
# format
# 날짜가 표시되는 형식.
# min_value
# 입력할 수 있는 최소 날짜.
# max_value
# 입력할 수 있는 최대 날짜.
# step
# 날짜 증가 또는 감소의 단계 크기.

from datetime import date
df = pd.DataFrame(
    {
        "name": ["Park", "Lee", "Kim", "Choi"],
        "age": [24, 31, 40, 19],
        "flag": [True, False, True, False],
        "lang": [None, "JavaScript", "Python", "C"],
        "birthday": [
            date(2024, 4, 22),
            date(1992, 11, 26),
            date(2021, 6, 6),
            date(2024, 1, 1),
        ]
    }
)

st.data_editor(
    df,
    column_config={
        "birthday": st.column_config.DateColumn(
            label="Birth Day 😍",
            help="Enter your birthday",
            min_value=date(1992, 1, 1),
            max_value=date(2024, 1, 20),
            format="DD.MM.YYYY",
            step=1
        )
    }
)

# >>> st.column_config.TimeColumn -----

# label
# 컬럼에 보여지는 라벨
# width
# 컬럼의 Width
# help
# 호버했을 때의 툴팁
# disabled
# editing이 가능한지 여부
# required
# null 값이 가능한지 여부
# default
# 컬럼의 기본값
# format
# time의 포맷 (HH:mm:ss)
# min_value
# 최소 시간
# max_value
# 최대 시간
# step
# Step의 간격

df = pd.DataFrame(
    {
        "name": ["Park", "Lee", "Kim", "Choi"],
        "access_time": [
            time(12, 4, 0),
            time(6, 11, 0),
            time(21, 6, 0),
            time(16, 1, 0),
        ]
    }
)

st.data_editor(
    df,
    column_config={
        "access_time": st.column_config.TimeColumn(
            label="Access Time is",
            width="medium",
            required=False,
            format="HH:mm",
            step=60
        )
    }
)

# >>> st.column_config.ListColumn -----

# 리스트 유형의 값을 갖는 열을 설정

# label
# 컬럼에 보여지는 라벨
# width
# 컬럼의 Width
# help
# 호버했을 때의 툴팁

import random
df = pd.DataFrame(
    {
        "name": ["Park", "Lee", "Kim", "Choi"],
        "score": [
            random.sample(range(10, 100), 5),
            random.sample(range(10, 100), 5),
            random.sample(range(10, 100), 5),
            random.sample(range(10, 100), 5),
        ]
    }
)

st.dataframe(
    df,
    column_config={
        "score": st.column_config.ListColumn(
            label="Scores",
            width="large",
            help="These are test scores"
        )
    }
)

# >>> st.column_config.LinkColumn -----

# 하이퍼링크가 적용되는 열을 구성
# label
# 컬럼에 보여지는 라벨
# width
# 컬럼의 Width
# help
# 호버했을 때의 툴팁
# disabled
# editing이 가능한지 여부
# required
# null 값이 가능한지 여부
# default
# 컬럼의 기본값
# max_chars
# 컬럼값의 최대 글자수
# validate
# 데이터의 유효성 검사
# e.g. `"^https://.+$"`
# display_text
# - None으로 하면 URL을 출력
# - str으로 입력하면 모두 동일한 str로 출력
# - 정규식으로도 정의 가능
# e.g `"https://(.*?)\.streamlit\.app"`

df = pd.DataFrame(
    {
        "name": ["Data", "Text", "Column"],
        "url": ["Data_elements", "Text_elements", "Column_config"]
    }
)

st.dataframe(
    df,
    column_config={
        "url": st.column_config.LinkColumn(
            label="Go to URL",
            width="large",
            help="If you click the link, go to the URL",
            display_text="Go to this section"
        )
    }
)

# >>> st.column_config.ImageColumn -----

# 열에 이미지를 넣는다.
# label
# 컬럼에 보여지는 라벨
# width
# 컬럼의 Width
# help
# 호버했을 때의 툴팁

df = pd.DataFrame(
    {
        "name": [
            "초인의 시대",
            "킬러 경찰",
            "인생존망2",
            "화산귀환"
        ],
        "preview": [
            "https://search.pstatic.net/common?type=f&size=206x268&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F730694%2Fthumbnail%2Fthumbnail_IMAG21_e6fc219d-e5ea-4d93-b7d6-45b595c2a3cb.jpeg",
            "https://search.pstatic.net/common?type=f&size=206x268&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F808439%2Fthumbnail%2Fthumbnail_IMAG21_19387806-c0b0-4669-8fac-90607bbe12d6.jpg",
            "https://search.pstatic.net/common?type=f&size=206x268&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F820354%2Fthumbnail%2Fthumbnail_IMAG21_1627d92f-77a9-4720-973d-820bc585df89.jpg",
            "https://search.pstatic.net/common?type=f&size=206x268&quality=75&direct=true&src=https%3A%2F%2Fshared-comic.pstatic.net%2Fthumb%2Fwebtoon%2F769209%2Fthumbnail%2Fthumbnail_IMAG21_3511dcdd-6e33-4171-8839-598d6d266215.jpg"
        ]
    }
)

st.dataframe(
    df,
    column_config={
        "preview": st.column_config.ImageColumn(
            label="Thumbnail",
            width="small",
            help="A thumbnail of the webcomic"
        )
    }
)

# >>> st.column_config.LineChartColumn -----

# 라인(선형) 차트 열을 설정
# label
# 컬럼에 보여지는 라벨
# width
# 컬럼의 Width
# help
# 호버했을 때의 툴팁
# y_min
# y-axis의 최소값
# y_max
# y-axis의 최대값

df = pd.DataFrame(
    {
        "name": ["Kakao", "Naver", "Samsung", "LG"],
        "sales": [
            random.sample(range(0, 10000), 4),
            random.sample(range(0, 10000), 4),
            random.sample(range(0, 10000), 4),
            random.sample(range(0, 10000), 4),
        ]
    }
)

df["sales_chart"] = df["sales"]

st.dataframe(
    df,
    column_config={
        "sales_list": st.column_config.ListColumn(
            label="Sales Data",
            width="medium",
            help="It is sales data"
        ),
        "sales_chart": st.column_config.LineChartColumn(
            label="Sales Chart",
            width="medium",
            help="It is a sales chart"
        )
    }
)

# >>> st.column_config.BarChartColumn -----

# label
# 컬럼에 보여지는 라벨
# width
# 컬럼의 Width
# help
# 호버했을 때의 툴팁
# y_min
# y-axis의 최소값
# y_max
# y-axis의 최대값

df = pd.DataFrame(
    {
        "name": ["Kakao", "Naver", "Samsung", "LG"],
        "margin": [
            random.sample(range(4000, 10000), 4),
            random.sample(range(4000, 10000), 4),
            random.sample(range(4000, 10000), 4),
            random.sample(range(4000, 10000), 4),
        ]
    }
)

df["margin_chart"] = df["margin"]

st.dataframe(
    df,
    column_config={
        "margin": st.column_config.ListColumn(
            label="Margin Data",
            width="medium",
            help="This is margins data"
        ),
        "margin_chart" : st.column_config.BarChartColumn(
            label="Margin Bar Chart",
            help="This is margins chart",
            width="medium",
        )
    }
)

# >>> st.column_config.ProgressColumn -----

# label
# 컬럼에 보여지는 라벨
# width
# 컬럼의 Width
# help
# 호버했을 때의 툴팁
# format
# progress에 표시될 텍스트의 format
# (%d %e %f %g %i %u.)
# e.g `"$ %.2f"`
# min_value
# progress bar의 최소값
# max_value
# progress bar의 최대값

df = pd.DataFrame(
    {
        "name": ["Kim", "Park", "Lee", "Choi"],
        "progress": [
            random.choice(range(0, 101)),
            random.choice(range(0, 101)),
            random.choice(range(0, 101)),
            random.choice(range(0, 101)),
        ]
    }
)

st.dataframe(
    df,
    column_config={
        "progress": st.column_config.ProgressColumn(
            label="Currnt progress",
            format="%d%%",
            width="medium",
            help="Displays the current progress status"
        )
    }
)

# >>> 종합 예시 코드 -----

df = pd.DataFrame(
    {
        "name": ["Kakao", "Naver", "Samsung", "LG"],
        "image": [
            "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fwww.kakaocorp.com%2Fpage%2Ffavicon.ico&type=f30_30_png_expire24",
            "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fu%2F2014%2F0328%2Fmma_204243574.png&type=f30_30_png_expire24",
            "https://search.pstatic.net/sunny?src=https%3A%2F%2Fwww.samsung.com%2Fsec%2Fstatic%2F_images%2Ffavicon.ico&type=f30_30_png_expire24",
            "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fwww.lg.co.kr%2Ffavicon.ico&type=f30_30_png_expire24"
        ],
        "revenue": [
            random.sample(range(5000, 10000), 4),
            random.sample(range(5000, 10000), 4),
            random.sample(range(5000, 10000), 4),
            random.sample(range(5000, 10000), 4),
        ]
    }
)

df["margin"] = df["revenue"].apply(lambda x : [x[idx]-each for idx, each in enumerate(random.sample(range(0, 5001), 4))])
df["max_ratio"] = df.apply(lambda x: max([x.margin[idx]/sale for idx, sale in enumerate(x.revenue)])*100, axis=1)

st.dataframe(
    df,
    column_config={
        "image": st.column_config.ImageColumn(
            "Logo",
            width="small",
            help="This is the brand logo"
        ),
        "revenue": st.column_config.BarChartColumn(
            "Bar chart Sales (2023Y)",
            width="medium",
            help="This is the company's revenue in 2023",
            y_min=5000,
            y_max=10000
        ),
        "margin": st.column_config.LineChartColumn(
            "Margins",
            width="small",
            help="This is the company's 2023 margins",
            y_min=0,
            y_max=5001,
        ),
        "max_ratio": st.column_config.ProgressColumn(
            "Maximum value for Ratio",
            width="medium",
            help="The maximum value of the operating margin",
            format="%.1f%%",
            min_value=0,
            max_value=100
        )
    }
)


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

# label
# 버튼에 표시될 짧은 라벨로, 굵은 글씨, 기울임꼴, 인라인 코드, 이모지 지원.
# key
# 위젯의 고유 식별자
# help
# 마우스를 올렸을 때 표시되는 도움말 텍스트
# on_click
# 버튼 클릭 시 호출될 콜백 함수
# args
# 콜백에 전달할 인자
# kwargs
# 콜백에 전달할 키워드 인자
# type
# 버튼 타입으로 "secondary", "primary"이 있으며, 기본값은 "secondary"이다.
# disabled
# True로 설정하면 버튼이 비활성화됨. 기본값은 False.
# use_container_width
# True로 설정하면 버튼 너비가 부모 컨테이너와 동일해짐.

if st.button('대문자') :
    st.write(df['species'].str.upper().head(3))

btn = st.button("Click me", type="primary")
if btn :
    st.write("You clicked me!")

# >>> 다운로드 버튼 -----

# 사용자가 애플리케이션에서 직접 파일을 다운로드할 수 있는 버튼
# label
# 사용자에게 버튼 용도를 설명하는 짧은 라벨.
# data
# 다운로드할 파일의 내용.
# file_name
# 다운로드할 파일의 이름. 지정하지 않으면 자동으로 생성된다.
# mime
# 데이터의 MIME 타입. 지정하지 않으면 데이터 유형에 따라 자동으로 설정.
# key
# 위젯의 고유 키.
# help
# 버튼에 마우스를 올렸을 때 표시되는 도움말 툴팁.
# on_click
# 버튼 클릭 시 호출될 콜백 함수.
# args
# 콜백 함수에 전달할 인수.
# kwargs
# 콜백 함수에 전달할 키워드 인수.
# type
# 버튼 유형. "primary"는 강조 버튼, "secondary"는 일반 버튼이다.
# disabled
# 버튼을 비활성화. 기본값은 False.
# use_container_width
# 버튼의 너비를 부모 컨테이너의 너비에 맞춘다.

download = st.download_button(
    label="Download this file",
    data=b"Hello, world!",
    file_name="hello.txt",
    mime="text/plain",
)

# >>> 링크 버튼 -----

# 지정한 URL로 사용자를 리디렉션하는 기능
# label
# 사용자에게 버튼 용도를 설명하는 라벨. 마크다운을 포함할 수 있으며, 특정 스타일과 이모지 지원.
# url
# 클릭 시 열리는 URL
# help
# 버튼 위에 마우스를 올렸을 때 표시되는 도움말 툴팁
# type
# 버튼 유형 ("primary" 또는 "secondary"), 기본값은 "secondary"
# disabled
# 버튼 비활성화 여부, 기본값은 False
# use_container_width
# 버튼 너비를 부모 컨테이너의 너비에 맞춤

link = st.link_button("Go to Data elemetns Page", url="Data_elements")
google_link = st.link_button("Go to Google", url="https://google.com")

# >>> 페이지 링크 -----

# 사용자가 다른 페이지로 이동할 수 있는 하이퍼링크를 생성
# page
# 멀티페이지 앱 내 다른 페이지나 외부 페이지로 이동하는 링크의 경로 또는 URL.
# label
# 페이지 링크의 라벨. 외부 페이지에는 필수이며 Markdown 지원.
# icon
# 링크 아이콘으로 사용될 이모지. 단일 문자 사용 권장.
# help
# 링크 위에 마우스를 올렸을 때 표시되는 도움말 툴팁.
# disabled
# 페이지 링크 비활성화 여부. 기본값은 False.
# use_container_width
# 링크 너비를 부모 컨테이너의 너비에 맞춤.

st.page_link("https://www.google.com", label="Google", icon="🔗")
st.page_link("pages/Data_elements.py", label="Data Elements", icon="🪪")

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

# 사용자가 선택할 수 있는 체크박스를 생성
# label
# 체크박스가 무엇을 위한 것인지 설명하는 라벨.
# value
# 체크박스가 처음 렌더링될 때 사전 선택 여부.
# key
# 위젯의 고유 키로 사용되는 선택적 문자열 또는 정수.
# help
# 체크박스 옆에 표시되는 선택적 도구 설명.
# on_change
# 체크박스의 값이 변경될 때 호출되는 콜백.
# args
# 콜백에 전달할 선택적 args 튜플.
# kwargs
# 콜백에 전달할 선택적 kwargs 딕셔너리.
# disabled
# True로 설정하면 체크박스를 비활성화.
# label_visibility
# 라벨의 가시성. "visible", "hidden", "collapsed"을 사용할 수 있으며, 기본값은 "visible"이다.

chk = st.checkbox("Check me") #  label_visibility="visible"
if chk :
    st.write("You checked me!")

hidden_chk = st.checkbox("Hidden checkbox", label_visibility="hidden")

# >>> 토글 -----

# label
# 토글의 라벨
# value
# 토글이 처음 렌더링될 때의 사전 선택 여부
# key
# 위젯의 고유 식별자
# help
# 토글 옆에 표시되는 도구 설명
# on_change
# 이 토글의 값이 변경될 때 호출되는 콜백 함수
# args
# 콜백 함수에 전달할 추가적인 args 튜플
# kwargs
# 콜백 함수에 전달할 추가적인 kwargs 딕셔너리
# disabled
# 토글을 비활성화하고자 할 때 사용. True로 설정하면 토글을 비활성화
# label_visibility
# 라벨의 가시성. "visible", "hidden", "collapsed"을 사용할 수 있으며, 기본값은 "visible"이다.

toggle = st.toggle("Toggle me", key="toggle")
if toggle :
    st.write("You toggled me!")

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

# >>> 선으로 표현된 그래프 그리기 (line_chart) -----

# .line_chart(데이터) : 그래프를 꺾은 선으로 시각화
df = pd.DataFrame(
    {
        "quoter": ["1Q", "2Q", "3Q", "4Q"],
        "sales": random.sample(range(0, 100), 4), 
        "margin": random.sample(range(0, 100), 4), 
    }
)

st.line_chart(
    df,
    x="quoter",
    y=["sales", "margin"],
    color=["#1764AB", "#4A98CA"],
)

# >>> 영역으로 표현된 그래프 그리기 (area_chart) -----

# .area_chart(데이터) : 그래프를 범위형으로 시각화
df = pd.DataFrame(
    np.random.randn(20, 4),
    columns=["a", "b", "c", "d"])

st.area_chart(
    df,
    x="a",
    y=["b", "c", "d"],
    color=["#1764AB", "#4A98CA", "#94C5DF"],
    use_container_width=True  # 차트 너비를 컬럼 너비에 맞춥니다. 이 설정은 width 인자보다 우선
)

# >>> 막대으로 표현된 그래프 그리기 (bar_chart) -----

# .bar_chart(데이터) : 그래프를 막대로 시각화
df = pd.DataFrame(
    {
        "a": range(1, 13),
        "b": np.random.randn(12), 
        "c": np.random.randn(12), 
        "d": np.random.randn(12), 
    }
)

st.bar_chart(
    df,
    x="a",
    y=["b", "c", "d"],
    color=["#1764AB", "#4A98CA", "#94C5DF"],
)

# >>> 산점도 그래프 (scatter_chart) -----

df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
df['d'] = np.random.choice(['A','B','C'], 20)

st.scatter_chart(
    df,
    x='a',
    y='b',
    color='d',
    size='c',
)

# >>> 지도로 표현된 맵 그래프 그리기 (map) -----

# .map(데이터) : 경도와 위도를 이용하여 지도의 해당 부분을 표시
# 랜덤 데이터 생성 (한국 기준)
lat = np.random.uniform(35, 38, 20)  # 위도: 33도에서 38도 사이의 랜덤 값
lon = np.random.uniform(126, 129, 20)  # 경도: 126도에서 129도 사이의 랜덤 값
size = np.random.randint(1, 300, 20)*100  # 사이즈: 1에서 50 사이의 랜덤 정수 값

# 랜덤 HEX Code
def generate_hex_color(alpha='80'):
    # RGB 값과 함께 알파(투명도) 값을 포맷 문자열에 추가
    return '#{0:02X}{1:02X}{2:02X}{3}'.format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), alpha)

hex_colors = [generate_hex_color() for _ in range(20)]


df = pd.DataFrame({
    '위도': lat,
    '경도': lon,
    'size': size,
    'color': hex_colors
})

st.map(
    df,
    latitude='위도',
    longitude='경도',
    size='size',
    color='color')

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
