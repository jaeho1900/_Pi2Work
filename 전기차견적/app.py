import streamlit as st
import pandas as pd
# from PIL import Image

# 전기차 진화 시스템 구축비
def putout_fire_system_sales(step1, num_parking):
    if step1 == "무약정":
        if 7 <= num_parking <= 30:
            return num_parking * 9000000
        elif 4 <= num_parking < 7:
            return num_parking * 10000000    
        elif 2 <= num_parking < 4:
            return num_parking * 13500000
        else:
            return "주차면수가 2~30면이 아닌 경우는 별도 문의 주세요"
    elif step1 == "36개월(3년) 약정":
        if 7 <= num_parking <= 30:
            return num_parking * 11000000
        elif 4 <= num_parking < 7:
            return num_parking * 11500000    
        elif 2 <= num_parking < 4:
            return num_parking * 16000000
        else:
            return "주차면수가 2~30면이 아닌 경우는 별도 문의 주세요"   
    elif step1 == "60개월(5년) 약정":
        if 7 <= num_parking <= 30:
            return num_parking * 12000000
        elif 4 <= num_parking < 7:
            return num_parking * 13500000    
        elif 2 <= num_parking < 4:
            return num_parking * 19500000
        else:
            return "주차면수가 2~30면이 아닌 경우는 별도 문의 주세요"
    else:
        return "입력 오류 입니다."

# RMS 시스템 구축비
def rms_system_sales(step2, num_parking):
    if step2 == "무(일시납) 약정":
        if 7 <= num_parking <= 30:
            return num_parking * 1100000
        elif 4 <= num_parking < 7:
            return num_parking * 1400000    
        elif 2 <= num_parking < 4:
            return num_parking * 2000000
        else:
            return "주차면수가 2~30면이 아닌 경우는 별도 문의 주세요"
    elif step2 == "24개월(2년) 약정":
        if 7 <= num_parking <= 30:
            return num_parking * 1180000
        elif 4 <= num_parking < 7:
            return num_parking * 1500000    
        elif 2 <= num_parking < 4:
            return num_parking * 2140000
        else:
            return "주차면수가 2~30면이 아닌 경우는 별도 문의 주세요"   
    elif step2 == "36개월(3년) 약정":
        if 7 <= num_parking <= 30:
            return num_parking * 1220000
        elif 4 <= num_parking < 7:
            return num_parking * 1550000    
        elif 2 <= num_parking < 4:
            return num_parking * 2220000
        else:
            return "주차면수가 2~30면이 아닌 경우는 별도 문의 주세요"   
    elif step2 == "60개월(5년) 약정":
        if 7 <= num_parking <= 30:
            return num_parking * 1400000
        elif 4 <= num_parking < 7:
            return num_parking * 1780000    
        elif 2 <= num_parking < 4:
            return num_parking * 2540000
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

# st.markdown('<h1 style="text-align: center;">견 적 서</h1>', unsafe_allow_html=True)

# st.image('상호.png')

step1 = st.sidebar.radio(label = '① 전기차 진화 시스템 약정 기간 선택', options = ["무약정", "36개월(3년) 약정", "60개월(5년) 약정"])
st.sidebar.divider()

step2 = st.sidebar.radio(label = '② 원격 관제 시스템 약정 기간 선택', options = ["미선택", "무(일시납) 약정", "24개월(2년) 약정", "36개월(3년) 약정", "60개월(5년) 약정"])
st.sidebar.divider()

st.sidebar.markdown('<h5 style="text-align: left;">③ 설치대수(연속공간 기준)</h5>', unsafe_allow_html=True)
df = pd.DataFrame({"지하층위치": ["B1F"], "연속된주차면수": [2]})
df_new = st.sidebar.data_editor(
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

st.write("shape: ", df_new.shape)
st.write(df_new)
st.write(df_new.loc[:,"지하층위치"])
st.write(df_new.loc[:,"연속된주차면수"])
st.write(df_new.loc[:,"연속된주차면수"].sum())  # 총 주차면수
st.write(df_new.iloc[0,0])

# num_parking = df_new.iloc[0,1]

# if not df_new.empty:
#     for index, row in df_new.iterrows():
#         for column, value in row.items():            
#             st.divider()
#             st.write(f"인덱스: {index}, 열: {column}, 값: {value}")

# selected_options = df_new["연속된 주차면수"].tolist()
# st.write(selected_options)

# st.divider()
# st.write("step1 choice is --> {}".format(step1))
# st.write("step1 choice is amount? --> {:,}".format(int(putout_fire_system_sales(step1, num_parking))))

# st.divider()
# st.write("step2 choice is --> {}".format(step2))
# st.write("step2 choice is amount? --> {:,}".format(int(rms_system_sales(step2, num_parking))))
# st.write("step3 choice is amount? --> {:,}".format(int(rms_operation_monthly_sales(step2, num_parking))))

