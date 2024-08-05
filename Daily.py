import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import platform


from matplotlib import font_manager, rc
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
else:
    print('Unknown system... sorry~~~~')    

plt.rcParams['axes.unicode_minus'] = False

# 데이터 프레임 
df = pd.read_excel("C:/Users/Administrator/Desktop/240802_사업장현황.xlsx")

# '규모' 열의 값이 '대', '중', '소'인 데이터만 추출
df_filtered = df[df['규모'].isin(['대형', '중형', '소형'])]

# 그룹별로 정상 범위를 출력하고 박스플롯을 그리기
plt.figure(figsize=(10, 6))

for size in ['대형', '중형', '소형']:
    group = df_filtered[df_filtered['규모'] == size]
    
    # 사분위수 및 IQR 계산
    q1 = group['연면적(㎡)'].quantile(0.25)
    q3 = group['연면적(㎡)'].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 # - 1.5 * iqr
    upper_bound = q3 # + 1.5 * iqr
    
    # 정상 범위 출력
    print(f"규모 '{size}'의 정상 범위:")
    print(f"하한: {lower_bound:.2f}")
    print(f"상한: {upper_bound:.2f}")
    print()

# 박스플롯 그리기
sns.boxplot(x='규모', y='연면적(㎡)', data=df_filtered)
plt.title('규모별 연면적(㎡) 박스플롯')
plt.show()

