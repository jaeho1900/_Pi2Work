import streamlit as st
from PIL import Image

tab1, tab2 = st.tabs(['Tab A', 'Tab B'])
col1, col2 = st.columns([2,3])
img1 = Image.open('pic.png')

st.sidebar.title('this is sidebar')
st.sidebar.checkbox('체크박스에 표시될 문구')

with tab1:
        st.title('Hello Seoul')
        st.image(img1)
with tab2:
        st.header('this is header')
        st.subheader('this is subheader')
        st.checkbox('this is checkbox')

