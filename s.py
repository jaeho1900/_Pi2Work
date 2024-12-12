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