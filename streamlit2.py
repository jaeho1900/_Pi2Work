# --------------------
# 상호작용 버튼
# --------------------

import streamlit as st
import seaborn as sns

df = sns.load_dataset('iris')
species = df['species'].unique()

# >>> 버튼 -----

# 버튼을 누를시 정해진 작업 수행
# .button('버튼이름')

if st.button('대문자') :
    st.write(df['species'].str.upper().head(3))

# >>> 라디오 버튼 -----

# 여러 선택지 중에 하나를 선택하여 선택된 작업 수행
# .radio('보여줄 메시지', '선택지1, 선택지2...')

my_order = ['오름차순', '내림차순']         # 라디오 버튼에 보여줄 텍스트
status = st.radio('정렬방법선택', my_order) # 라디오 버튼의 상태 변수화
 
if status == my_order[0] :   # 첫번째 선택시 오름차순
    st.write(df.sort_values('petal_length'))
elif status == my_order[1] : # 두번째 선택시 내림차순
    st.write(df.sort_values('petal_length', ascending=False))

# >>> 체크 박스 -----

# 예/아니오 상황 체크만으로 작업 수행
# .checkbox('보여줄 메시지')

if st.checkbox('헤드 5개 보기'):
    st.write(df.head())
else:
    st.text('헤드를 숨겼습니다.')

# >>> 셀렉트 박스 -----

# 여러 개의 목록을 보여주고 그 중 하나를 선택하여 작업 수행
# .selectbox('보여줄 메시지', '리스트1, 리스트2...')

language = ['Python', 'C', 'Java', 'Go', 'PHP']
my_choice = st.selectbox('좋아하는 언어 선택', language)

if my_choice == language[0] :
    st.write("파이썬 선택")
    # 이후 생략

# >>> 멀티 셀렉트 -----

# 여러 개의 목록에서 하나 이상을 선택
# .multiselect('보여줄 메시지', '리스트1, 리스트2...')

columns_list = df.columns
choice_list = st.multiselect('컬럼을 선택하세요', columns_list)
st.write( df[choice_list] )

# >>> 슬라이더 -----

# 숫자를 조정하는데 주로 사용, 조정된 숫자로 작업 수행
# .slider('보여줄 메시지', 시작값, 끝값, 기본값, 스텝)

age = st.slider('나이', 1, 120, 30, 10)
st.text('제가 선택한 나이는 {}입니다.'.format(age))

# >>> 사이드 바 -----

# 화면 왼쪽에 프레임을 나누어 따로 표기
# .sidebar ~ : 왼쪽 프레임에서 할 행동 표시

st.sidebar.text('안녕하세요')
st.sidebar.button('버튼')

# >>> 익스팬더 -----

# 활성화시 숨겨져 있던 정해진 작업을 수행 (확장 개념, =펼쳐보기 느낌)
# .expander('보여줄 메시지')

with st.expander('Hello') :
    st.text('변경')
    st.write(df)


# --------------------
# 매체(이미지, 영상, 음악) 사용하기
# --------------------
