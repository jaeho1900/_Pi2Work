# import streamlit as st

# # 사이드바에 탭 생성
# selected_tab = st.sidebar.radio("Select Tab", ["Tab 1", "Tab 2", "Tab 3"])

# # 각 탭에 해당하는 내용 표시
# if selected_tab == "Tab 1":
#     st.header("Tab 1")
#     slider_value1 = st.slider("Slider in Tab 1", min_value=0, max_value=100, value=50)
#     st.write(f"Slider Value in Tab 1: {slider_value1}")

# elif selected_tab == "Tab 2":
#     st.header("Tab 2")
#     slider_value2 = st.slider("Slider in Tab 2", min_value=0, max_value=100, value=25)
#     st.write(f"Slider Value in Tab 2: {slider_value2}")

# elif selected_tab == "Tab 3":
#     st.header("Tab 3")
#     slider_value3 = st.slider("Slider in Tab 3", min_value=0, max_value=100, value=75)
#     st.write(f"Slider Value in Tab 3: {slider_value3}")

import streamlit as st

# 제목 설정
st.title('My Dashboard')

# 사이드바에 탭 선택 항목 추가
tab_titles = ['User Inputs', 'Data Display', 'Data Analysis']
selected_tab = st.sidebar.selectbox('Select a tab', tab_titles)

# 선택된 탭에 따라 콘텐츠 표시
if selected_tab == 'User Inputs':
    st.header('User Inputs')
    # 슬라이더 추가
    slider_value = st.slider('Select a value', 0, 100, 50)
    st.write(f'Selected value: {slider_value}')
    # 텍스트 입력
    text_input = st.text_input('Some text 입력')
    st.write(f'Text input: {text_input}')
    # 숫자 입력
    number_input = st.number_input('Number 입력', min_value=0, max_value=100, value=50)
    st.write(f'Number input: {number_input}')

elif selected_tab == 'Data Display':
    st.header('Data Display')
    # 데이터 표 표시
    data = {'column1': [1, 2, 3], 'column2': [4, 5, 6]}
    st.table(data)

elif selected_tab == 'Data Analysis':
    st.header('Data Analysis')
    # 선 그래프 표시
    chart_data = [1, 2, 3, 4, 5]
    st.line_chart(chart_data)



# st.number_input('숫자 입력', min_value=1, max_value=100, value=50)