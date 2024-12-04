# =====================
# Basic
# =====================

# 웹 대시보드 개발 라이브러리인 스트림릿은 main 함수가 있어야 한다.

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


# --------------------
# 문구
# --------------------

import streamlit as st

st.title('this is title')
st.header('this is header')
st.subheader('this is subheader')


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

#PIL 패키지에 이미지 모듈을 통해 이미지 열기 
img = Image.open('zarathu.png')
st.image(img)


# =====================
# 사용자 입력
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



# --------------------
# 이미지
# --------------------


