
import streamlit as st
import seaborn as sns

df = sns.load_dataset('iris')
species = df['species'].unique()


video_file = open('시연.mp4', 'rb')
st.video(video_file)

# >>> 비디오 파일의 경로를 그대로 넣어 다이렉트로 불러오기 -----

# .video('경로와 파일이름', format='video/mp4')

# 비디오 파일의 확장자만 잘 맞으면 format은 생략해도 된다.
st.video('시연.mp4')
