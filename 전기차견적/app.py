import streamlit as st
import pandas as pd
import numpy as np
# from PIL import Image

# 전기차 진화 시스템 구축비
def putout_fire_system_sales(step1, num_parking):
    if step1 == "무약정":
        if 7 <= num_parking <= 30:
            return 9000000
        elif 4 <= num_parking < 7:
            return 10000000    
        elif 2 <= num_parking < 4:
            return 13500000
        else:
            return "주차면수가 2~30면이 아닌 경우는 별도 문의 주세요"
    elif step1 == "36개월(3년) 약정":
        if 7 <= num_parking <= 30:
            return 11000000
        elif 4 <= num_parking < 7:
            return 11500000    
        elif 2 <= num_parking < 4:
            return 16000000
        else:
            return "주차면수가 2~30면이 아닌 경우는 별도 문의 주세요"   
    elif step1 == "60개월(5년) 약정":
        if 7 <= num_parking <= 30:
            return 12000000
        elif 4 <= num_parking < 7:
            return 13500000    
        elif 2 <= num_parking < 4:
            return 19500000
        else:
            return "주차면수가 2~30면이 아닌 경우는 별도 문의 주세요"
    else:
        return "입력 오류 입니다."

# RMS 시스템 구축비
def rms_system_sales(step2, num_parking):
    if step2 == "무(일시납) 약정":
        if 7 <= num_parking <= 30:
            return 1100000
        elif 4 <= num_parking < 7:
            return 1400000    
        elif 2 <= num_parking < 4:
            return 2000000
        else:
            return "주차면수가 2~30면이 아닌 경우는 별도 문의 주세요"
    elif step2 == "24개월(2년) 약정":
        if 7 <= num_parking <= 30:
            return 1180000
        elif 4 <= num_parking < 7:
            return 1500000    
        elif 2 <= num_parking < 4:
            return 2140000
        else:
            return "주차면수가 2~30면이 아닌 경우는 별도 문의 주세요"   
    elif step2 == "36개월(3년) 약정":
        if 7 <= num_parking <= 30:
            return 1220000
        elif 4 <= num_parking < 7:
            return 1550000    
        elif 2 <= num_parking < 4:
            return 2220000
        else:
            return "주차면수가 2~30면이 아닌 경우는 별도 문의 주세요"   
    elif step2 == "60개월(5년) 약정":
        if 7 <= num_parking <= 30:
            return 1400000
        elif 4 <= num_parking < 7:
            return 1780000    
        elif 2 <= num_parking < 4:
            return 2540000
        else:
            return "주차면수가 2~30면이 아닌 경우는 별도 문의 주세요"
    else:
        return 0

# RMS 월 운영비
def rms_operation_monthly_sales(step2, num_parking):
    basic_k = 0
    if 7 <= num_parking <= 30:
        basic_k = 25000
    elif 4 <= num_parking < 7:
        basic_k = 50000    
    elif 2 <= num_parking < 4:
        basic_k = 100000
    else:
        basic_k = 0

    if step2 == "24개월(2년) 약정":
        return basic_k * num_parking * 24
    elif step2 == "36개월(3년) 약정":
        return basic_k * num_parking * 36
    elif step2 == "60개월(5년) 약정":
        return basic_k * num_parking * 60
    else:
        return 0


# form ----------------

st.markdown('<h1 style="text-align: center;">견 적 서</h1>', unsafe_allow_html=True)

# st.image('상호.png')

step1 = st.sidebar.radio(label = '① 전기차 진화 시스템 약정 기간 선택', options = ["무약정", "36개월(3년) 약정", "60개월(5년) 약정"])
st.sidebar.divider()

step2 = st.sidebar.radio(label = '② 원격 관제 시스템 약정 기간 선택', options = ["미선택", "무(일시납) 약정", "24개월(2년) 약정", "36개월(3년) 약정", "60개월(5년) 약정"])
st.sidebar.divider()

st.sidebar.markdown('<h5 style="text-align: left;">③ 설치대수(연속공간 기준)</h5>', unsafe_allow_html=True)
df = pd.DataFrame({"지하층위치": ["B1F"], "연속된주차면수": [2]})
edited_df = st.sidebar.data_editor(
                        df, num_rows="dynamic",
                        column_config={
                                       "지하층위치": st.column_config.SelectboxColumn(
                                                        help="지하 층위치를 선택하세요",
                                                        options=["B1F", "B2F", "B3F", "B4F", "B5F", "B6F", "B7F", "B8F", "기타"],
                                                        default="B1F"
                                                        ),
                                       "연속된주차면수": st.column_config.NumberColumn(
                                                            help="주차면수 2~30사이의 숫자를 입력하세요",
                                                            min_value=2,
                                                            max_value=30,
                                                            format="%d 면",
                                                            default=2
                                                            )
                       })

i = edited_df.shape[0]
j = edited_df.shape[1]

st.write(edited_df.shape)
st.divider()

df_new = pd.DataFrame(np.random.rand(i+1, 5), columns=['구분','약정개월/층위치','주차면수','단가','금액'])
# st.write(df_new)

total = 0
for m, n in edited_df.iterrows():   
   df_new.iloc[m+1, 0] = ''
   df_new.iloc[m+1, 1] = edited_df.iloc[m,0]
   df_new.iloc[m+1, 2] = edited_df.iloc[m,1]
   df_new.iloc[m+1, 3] = '{:,}'.format(putout_fire_system_sales(step1, edited_df.iloc[m,1]))
   df_new.iloc[m+1, 4] = edited_df.iloc[m,1] * putout_fire_system_sales(step1, edited_df.iloc[m,1])
   total += edited_df.iloc[m,1] * putout_fire_system_sales(step1, edited_df.iloc[m,1])

df_new.iloc[0, 0] = '1.전기차 진화 시스템 구축비'
df_new.iloc[0, 1] = step1
df_new.iloc[0, 2] = edited_df.loc[:,"연속된주차면수"].sum()
df_new.iloc[0, 3] = ''
df_new.iloc[0, 4] = total

st.write(df_new)
