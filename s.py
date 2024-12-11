import streamlit as st
import altair as alt
import seaborn as sns

df = sns.load_dataset('iris')

# >>> 점으로 표현된 그래프 그리기 (mark_circle) -----

# .Chart(데이터) .mark_circle() .encode(x=x축데이터, y=y축데이터, color=그룹별 색상)
# streamlit.altair_chart(데이터) : 스트림릿을 이용하여 altair로 생성된 데이터만 사용 할 수 있다.

alt_chart = alt.Chart(df).mark_circle().encode(x='petal_length',y='petal_width',color='species')
st.altair_chart(alt_chart)