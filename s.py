
import streamlit as st
import seaborn as sns

df = sns.load_dataset('iris')
species = df['species'].unique()


columns_list = df.columns

choice_list = st.multiselect('컬럼을 선택하세요', columns_list)
st.write( df[choice_list] )


age = st.slider('나이', 1, 120, 30, 10)
st.text('제가 선택한 나이는 {}입니다.'.format(age))


st.sidebar.text('안녕하세요')
st.sidebar.button('버튼')


with st.expander('Hello') :
    st.text('변경')
    st.write(df)