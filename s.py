
import time
import streamlit as st

latest_iteration = st.empty()
bar = st.progress(0)

# Update the progress bar with each iteration.
for i in range(100):
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  # 0.05 초 마다 1씩증가
  time.sleep(0.05)

with st.spinner('Wait for it...'):
  time.sleep(5)
  st.success('Done!')

# 시간 다 되면 풍선 이펙트 보여주기 
st.balloons()