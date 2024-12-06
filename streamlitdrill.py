# =====================
# 사용법
# =====================

# >>> main 함수 작성 -----

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

# >>> 종료 -----

# 터미널 창에서 Ctrl+C


# --------------------
# 텍스트 출력
# --------------------

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


# --------------------
# 데이터프레임
# --------------------

import streamlit as st
import seaborn as sns

df = sns.load_dataset('iris')
species = df['species'].unique()

# 웹 대시보드에 출력(dataframe 또는 write) 
st.dataframe(df.head())
st.write(df.head())


# --------------------
# 상호작용 버튼
# --------------------

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


# --------------------
# 레이아웃
# --------------------

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


# --------------------
# 이미지
# --------------------

import streamlit as st
from PIL import Image

# PIL 패키지에 이미지 모듈을 통해 이미지 열기 
img = Image.open('zarathu.png')
st.image(img)


# =====================
# 사용자 input
# =====================

import numpy as np
import pandas as pd 
from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt
import streamlit as st

iris_dataset = load_iris()

df= pd.DataFrame(data=iris_dataset.data,columns= iris_dataset.feature_names)
df.columns= [ col_name.split(' (cm)')[0] for col_name in df.columns] # 컬럼명을 뒤에 cm 제거하였습니다
df['species']= iris_dataset.target 


species_dict = {0 :'setosa', 1 :'versicolor', 2 :'virginica'} 

def mapp_species(x):
  return species_dict[x]

df['species'] = df['species'].apply(mapp_species)
print(df)

# >>> DataTable 표출 -----

# streamlit 에서 데이터 프레임을 보여주는 방식은 table과 dataframe 가 있다.

st.subheader('this is table')
st.table(df.head())

st.subheader('this is data frame')
st.dataframe(df.head())

# >>> Select Box -----

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

# >>> Multi select -----

# 여러 값을 선택하기 위해서는 multiselect를 이용, return : list
select_multi_species = st.sidebar.multiselect(
    '확인하고자 하는 종을 선택해 주세요. 복수선택가능',
    ['setosa','versicolor','virginica']

)
tmp_df = df[df['species'].isin(select_multi_species)]
st.table(tmp_df)

# >>> Radio / Slider -----

# 라디오에 선택한 내용을 radio select변수에 담습니다.
radio_select =st.sidebar.radio(
    "what is key column?",
    ['sepal length', 'sepal width', 'petal length','petal width'],
    horizontal=True
    )

# 선택한 컬럼의 값의 범위를 지정할 수 있는 slider를 만듭니다.
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


# =====================
# 시각화
# =====================

# 스트림릿에서는 bokeh, plotly, matplotlib 등의 패키지로 생성한 그림을 웹에 표시하는 기능 제공


# --------------------
# Plotly
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


# --------------------
# 지도 표시
# --------------------

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
# 로딩상태 구현
# --------------------

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


# =====================
# DBMS 연결 및 배포
# =====================

# DB연결 : https://docs.streamlit.io/develop/tutorials/databases
# 링크배포 : https://docs.streamlit.io/deploy/tutorials
