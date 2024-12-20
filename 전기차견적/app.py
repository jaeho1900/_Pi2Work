# import streamlit as st
# import pandas as pd
# # from PIL import Image

# st.markdown('<h1 style="text-align: center;">견 적 서</h1>', unsafe_allow_html=True)

# # st.image('상호.png')

# tab1, tab2, tab3= st.sidebar.tabs(['Step 1 ▷▷', 'Step 2 ▷▷', 'Step 3'])

# with tab1:
#   step1 = st.radio(label = '① 전기차 진화 시스템 약정 기간 선택', options = ["무약정", "36개월(3년) 약정", "60개월(5년) 약정"])

# with tab2:
#   step2 = st.radio(label = '② 원격 관제 시스템 약정 기간 선택', options = ["미선택", "무(일시납) 약정", "24개월(2년) 약정", "36개월(3년) 약정", "60개월(5년) 약정"])

# with tab3:
#   st.markdown('<h5 style="text-align: left;">③ 설치장소 및 필요수량(연속공간 기준) 입력</h5>', unsafe_allow_html=True)
#   df_order = pd.DataFrame({"지하 층위치": [], "연속된 주차면수": []})
#   st.data_editor(
#       df_order, hide_index=True, num_rows="dynamic", use_container_width=True, key="추출", # 키값을 부여하여 세션스테이트와 연결
#       column_config={
#                     "지하 층위치": st.column_config.SelectboxColumn(
#                                         label="지하 층위치",
#                                         help="지하 층위치를 선택하세요",
#                                         options=["B1F", "B2F", "B3F", "B4F", "B5F", "B6F", "B7F", "B8F", "기타"],
#                                         required=True,
#                                         default= "B1F"
#                                         ),
#                     "연속된 주차면수": st.column_config.NumberColumn(
#                                           label="연속된 주차면수",
#                                           help="주차면수 1~30사이의 숫자를 입력하세요",
#                                           min_value=1,
#                                           max_value=30,
#                                           format="%d 면",
#                                           required=True,
#                                           default= 1
#                                         )
#                     }
#   )

# st.divider()
# st.write("step1 choice is --> ", step1)
# st.write("step2 choice is --> ", step2)
# st.divider()

# # df2 = st.session_state["추출"]

# for i in range(0, len(st.session_state["추출"])):
#   row_col = st.session_state["추출"]
#   st.write(row_col)



# # click event 대체



# ==========================================

# import streamlit as st
# import pandas as pd

# # 데이터프레임 초기화
# df_order = pd.DataFrame({"지하 층위치": [], "연속된 주차면수": []})

# # 데이터 에디터로 사용자 입력 받기
# df_order = st.data_editor(df_order, height=200, num_rows="dynamic")

# # 입력된 데이터 확인 및 주차 가능 여부 표시
# if not df_order.empty:
#     for index, row in df_order.iterrows():
#         if 1 < row["연속된 주차면수"] < 10:
#             status = "주차 가능"
#         else:
#             status = "주차 불가"
        
#         # 지하 층위치와 주차 가능 여부를 새로운 행으로 추가
#         new_row = pd.Series({"지하 층위치": row["지하 층위치"], "주차 가능 여부": status}, name=index)
#         st.write(new_row)
# ==========================================

import streamlit as st
import pandas as pd

# 데이터프레임 생성
df_order = pd.DataFrame({"지하 층위치": [], "연속된 주차면수": []})

# st.data_editor를 사용하여 데이터 입력 받기
df_order = st.data_editor(df_order, num_rows="dynamic")

# 입력된 데이터에 대해 '주차 가능' 또는 '주차 불가'를 표시하는 함수 정의
def check_parking_availability(parking_count):
    if 1 < parking_count <= 10:
        return '주차 가능'
    elif parking_count > 10:
        return '주차 불가'
    else:
        return ''

# 입력된 데이터에서 '연속된 주차면수'에 대해 주차 가능 여부 표시
if not df_order.empty:
    # '연속된 주차면수'에 대해 계산
    df_order['주차 가능 여부'] = df_order['연속된 주차면수'].apply(check_parking_availability)

    # 결과 표시
    st.write("주차 가능 여부:", df_order)

# 조건에 맞지 않는 입력이 있을 경우 경고 메시지
else:
    st.warning("주차 정보를 입력해주세요.")

if not df_order.empty:
    for index, row in df_order.iterrows():        
        new_row = pd.Series({"지하 층위치": row["지하 층위치"], "주차 가능 여부": row["주차 가능 여부"]}, name=index)
st.write(new_row)
