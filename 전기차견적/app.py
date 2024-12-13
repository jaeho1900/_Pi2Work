import streamlit as st
import pandas as pd
from PIL import Image

# st.set_page_config(layout="wide")

st.markdown('<h1 style="text-align: center;">견 적 서</h1>', unsafe_allow_html=True)
st.image('상호.png')

df = pd.DataFrame(
    { "구분":["1.전기차 진화 시스템 구축비", "2.원격 관제 시스템 구축비", "3.원격관제시스템 월운영서비스료"],
      "약정개월/층위치":['','',''],
      "주차면수":['','',''],
      "단가":['','',''],
      "금액":['','',''],
      "비고":['','',''] 
    }
)

st.dataframe(df, use_container_width=True, hide_index=True)
df2 = st.data_editor(df, use_container_width=True, hide_index=True,num_rows="dynamic")
st.table(df2)

