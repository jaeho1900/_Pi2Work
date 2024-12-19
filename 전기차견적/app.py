import streamlit as st
import pandas as pd
from PIL import Image

st.markdown('<h1 style="text-align: center;">견 적 서</h1>', unsafe_allow_html=True)
# st.image('상호.png')

tab1, tab2, tab3= st.sidebar.tabs(['Step 1 ▷▷', 'Step 2 ▷▷', 'Step 3'])

with tab1:
  step1 = st.radio(label = '① 전기차 진화 시스템 약정 기간 선택', options = ["무약정", "36개월(3년) 약정", "60개월(5년) 약정"])

with tab2:
  step2 = st.radio(label = '② 원격 관제 시스템 약정 기간 선택', options = ["미선택", "무(일시납) 약정", "24개월(2년) 약정", "36개월(3년) 약정", "60개월(5년) 약정"])

with tab3:
  st.markdown('<h5 style="text-align: left;">③ 설치장소 및 필요수량(연속공간 기준) 입력</h5>', unsafe_allow_html=True)
  df_order = pd.DataFrame(
                    {"지하 층위치":['B1F'],
                     "연속된 주차면수":['1']
                    }
  )

  st.data_editor(
      df_order, hide_index=True, num_rows="dynamic", use_container_width=True, key="추출", # 키값을 부여하여 세션스테이트와 연결
      column_config={
                    "지하 층위치": st.column_config.SelectboxColumn(
                                        label="지하 층위치",
                                        help="지하 층위치를 선택하세요",
                                        options=["B1F", "B2F", "B3F", "B4F", "B5F", "B6F", "B7F", "B8F", "기타"],
                                        required=True,
                                        default= "B1F"
                                        ),
                    "연속된 주차면수": st.column_config.NumberColumn(
                                          label="연속된 주차면수",
                                          help="주차면수 1~30사이의 숫자를 입력하세요",
                                          min_value=1,
                                          max_value=30,
                                          format="%d 면",
                                          required=True,
                                          default= 1
                                        )
                    }
  )

st.divider()
st.write(step1)
st.write(step2)
st.divider()

st.write(st.session_state["추출"])
