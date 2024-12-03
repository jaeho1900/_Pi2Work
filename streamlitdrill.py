import streamlit as st
from PIL import Image

# 웹 대시보드 개발 라이브러리인 스트림릿은 main 함수가 있어야 한다.
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
