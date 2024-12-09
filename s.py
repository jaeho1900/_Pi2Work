import streamlit as st

message = st.text_area('메세지를 입력하세요.', height = 70)
st.text(message)

st.number_input('숫자 입력', 1, 100)
# 실수 입력
st.number_input('실수 입력', 1.000, 100.000)