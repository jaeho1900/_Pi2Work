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
df = pd.read_excel('C:/Users/Administrator/Desktop/■서비스센터 월간 보고서_5월.xlsx',
                   sheet_name='엣지공수데이터 5월',
                   index_col=0,
                   usecols='A:N')

gdf = df.groupby(['서비스센터', '작업일자', '계약공간']).agg({'작업일자':'count', '작업시간(분)':'sum', '이동시간(분)':'sum'})
