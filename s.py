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


title_writing = "Test Title"
title_format = f'<p style="text-align: center; font-family: ' \
               f'Arial; color: #808080; font-size: 40px; ' \
               f'font-weight: bold;">{title_writing}</p>'
st.markdown(title_format, unsafe_allow_html=True)

st.markdown('<div style="text-align: center;">Hello World!</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: left;">Hello World!</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: right;">Hello World!</div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: justify;">Hello World!</div>', unsafe_allow_html=True)