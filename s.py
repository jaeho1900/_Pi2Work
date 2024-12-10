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