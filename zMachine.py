# =========================
# 머신러닝
# =========================

# # 머신러닝 프로세스
# 데이터 정리 - 데이터 분리(훈련,검증) - 알고리즘 준비 - 모형학습(훈련) - 예측(검증) - 모형평가 - 모형활용
# 소득이 증가(독립변수x)하면 소비가 증가(종속변수y)한다: x가 주어지면 y를 예측할 수 있다
# 모형이 예측을 위해 사용하는 변수(x): 독립변수, 설명변수
# 모형이 예측하고자하는 변수(y): 종속변수, 예측변수


# ========================
# 예측(지도학습, 회귀분석)
# ========================

# ----------------
# 단순 회귀분석
# ----------------

# y = ax + b 에서 a와 b를 찾기 위한 여정

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# >>> Seaborn 데이터 준비 -----

sns.get_dataset_names()
df = sns.load_dataset('mpg')
print(df.head())
print(df.info())
print(df.describe())

# 전처리 -----
print(df['horsepower'].unique())                        # horsepower 열의 고유값 확인
df.dropna(subset=['horsepower'], axis=0, inplace=True)  # 누락데이터 행을 삭제
print(df.describe())                                    # 데이터 통계 요약정보 확인

# 종속변수(mpg)와 독립변수후보군(cylinders, horsepower, weight) 선정 -----
ndf = df[['mpg', 'cylinders', 'horsepower', 'weight']]
print(ndf.head())

# 종속변수 mpg 와 다른 변수간 선형 관계 확인 -----
ndf.plot(kind='scatter', x='cylinders', y='mpg', c='coral', s=10, figsize=(10, 5))
ndf.plot(kind='scatter', x='horsepower', y='mpg', c='coral', s=10, figsize=(10, 5))
ndf.plot(kind='scatter', x='weight', y='mpg', c='coral', s=10, figsize=(10, 5))
# seaborn으로 그리기
sns.regplot(x='weight', y='mpg', data=ndf) # 분포된 형태가 선형보다는 비선형에 가까움
sns.jointplot(x='weight', y='mpg', data=ndf)
sns.pairplot(ndf)

# 판단 : 후보군확정: 선형관계와 무관한 cylinders 제외 필요

# >>> 훈련 및 검증 데이터셋 분리 -----

X = ndf[['weight']] # 독립 변수 X
y = ndf['mpg']      # 종속 변수 Y
# train data 와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,               # 독립 변수
                                                    y,               # 종속 변수
                                                    test_size=0.3,   # 검증 30%
                                                    random_state=10) # 랜덤 추출 값
print('훈련 데이터: ', X_train.shape)
print('검증 데이터: ', X_test.shape)

# >>> 단순회귀분석 모형 적용 -----

from sklearn.linear_model import LinearRegression

# 모형 객체 생성
lr = LinearRegression()

# 훈련데이터셋으로 모형 학습
lr.fit(X_train, y_train)

# 검증데이터셋으로 결정계수(R-제곱) 산출: 결정계수값이 클수록 모형예측능력 우수
r_square = lr.score(X_test, y_test)
print(r_square)

# 기울기 산출
print('기울기 a: ', lr.coef_)

# y절편 산출
print('y절편 b', lr.intercept_)

# >>> 모형 평가(예측값 y_hat, 실제값 y 비교) -----

y_hat = lr.predict(X)

# 비교 그래프 출력
plt.figure(figsize=(10, 5))
ax1 = sns.kdeplot(y, label="y")
ax2 = sns.kdeplot(y_hat, label="y_hat", ax=ax1)
plt.legend()
plt.show()


# ----------------
# 다항 회귀분석
# ----------------

# 2차 이상의 함수를 이용(2차 함수는 y= ax2 + bx + c 에서 a, b, c를 찾는 과정)

# >>> 다항회귀분석 모형 적용 -----

from sklearn.linear_model import LinearRegression    # 선형회귀분석
from sklearn.preprocessing import PolynomialFeatures # 다항식 변환

# 모형 객체 생성 -----
poly = PolynomialFeatures(degree=2)         # 2차항 적용
X_train_poly = poly.fit_transform(X_train)  # X_train 데이터를 2차항으로 변형
print('원 데이터: ', X_train.shape)
print('2차항 변환 데이터: ', X_train_poly.shape)

# >>> 모형 학습 -----

pr = LinearRegression()
pr.fit(X_train_poly, y_train)

# 결정계수(R-제곱) 산출 -----
X_test_poly = poly.fit_transform(X_test) # X_test 데이터를 2차항으로 변형
r_square = pr.score(X_test_poly, y_test)
print(r_square)

# >>> 모형 평가 -----

# train data의 산점도와 test data로 예측한 회귀선을 그래프로 출력
y_hat_test = pr.predict(X_test_poly)

# 비교 그래프 출력
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1)
ax.plot(X_train, y_train, 'o', label='Train Data')          # 데이터 분포
ax.plot(X_test, y_hat_test, 'r+', label='Predicted Value')  # 모형이 학습한 회귀선
ax.legend(loc='best')
plt.xlabel('weight')
plt.ylabel('mpg')
plt.show()
plt.close()

# 모형에 전체 X 데이터를 입력하여 예측한 값 y_hat을 실제 값 y와 비교 그래프 출력
X_ploy = poly.fit_transform(X)
y_hat = pr.predict(X_ploy)
plt.figure(figsize=(10, 5))
ax1 = sns.kdeplot(y, label="y")
ax2 = sns.kdeplot(y_hat, label="y_hat", ax=ax1)
plt.legend()
plt.show()

# 판단 : 그래프로 판단할 때 단순회귀분석보단 더 적합한 모형으로 볼 수 있음


# ----------------
# 다중 회귀분석
# ----------------

# 소득의 증가 뿐만아니라 거주지, 자녀수 등 소비에 영향을 주는 다양한 독립변수를 고려하여
# y = b + a1x1 + a2x2 + ... + anxn 에서 a1, a2, ... an, b 를 찾는 과정

# >>> 변수 선정 -----

X = ndf[['cylinders', 'horsepower', 'weight']] # 독립 변수 X1, X2, X3
y = ndf['mpg']                                 # 종속 변수 Y

# >>> 데이터셋 분리(7:3 비율) -----

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
print('훈련 데이터: ', X_train.shape)
print('검증 데이터: ', X_test.shape)

# >>> 다중회귀분석 모형 적용 -----

from sklearn.linear_model import LinearRegression

# 모형 객체 생성
lr = LinearRegression()

# 모형 학습
lr.fit(X_train, y_train)

# 결정계수(R-제곱) 산출
r_square = lr.score(X_test, y_test)
print(r_square)

# 회귀식의 기울기
print('X 변수의 계수 a: ', lr.coef_)

# 회귀식의 y절편
print('상수항 b', lr.intercept_)

# >>> 모형 평가 -----

# 예측회귀선 그래프로출력
y_hat = lr.predict(X_test)

# 비교 그래프 출력
plt.figure(figsize=(10, 5))
ax1 = sns.kdeplot(y_test, label="y_test")
ax2 = sns.kdeplot(y_hat, label="y_hat", ax=ax1)
plt.legend()
plt.show()


# ========================
# 분류(지도학습)
# ========================

# 범주형 y 값을 예측하는 모형

# ----------------
# KNN
# ----------------

# 적절한 k 값을 찾고, 이웃하는 원소들 중 다수를 차지하는 분류값을 따름

# >>> 전처리: 탑승객의 생존여부를 예측하는 모형 만들기 -----

import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')
print(df.head())
print(df.info())

# NaN값이 많은 deck 열을 삭제, embarked와 내용이 겹치는 embark_town 열을 삭제
rdf = df.drop(['deck', 'embark_town'], axis=1)
print(rdf.columns.values)

# age 열에 나이 데이터가 없는 모든 행을 삭제(891개 중 177개의 NaN 값)
rdf = rdf.dropna(subset=['age'], how='any', axis=0)
print(len(rdf))

# embarked 열의 NaN값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기
most_freq = rdf['embarked'].value_counts(dropna=True).idxmax()
print(rdf.describe(include='all')) # embarked 열의 최빈값(top) 재확인
rdf['embarked'].fillna(most_freq, inplace=True)
print(rdf.info())

# >>> 변수 선정 -----

# 예측변수(survived)와 설명변수 후보6개(pclass, sex, age, sibsp, parch, embarked) 로 데이터를 구성
ndf = rdf[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
print(ndf.head())

# 범주형 데이터를 모형이 인식할 수 있도록 불린형으로 변환
onehot_sex = pd.get_dummies(ndf['sex'])
ndf = pd.concat([ndf, onehot_sex], axis=1)

onehot_embarked = pd.get_dummies(ndf['embarked'], prefix='town')
ndf = pd.concat([ndf, onehot_embarked], axis=1)

ndf.drop(['sex', 'embarked'], axis=1, inplace=True)
print(ndf.head())

X = ndf[['pclass', 'age', 'sibsp', 'parch', 'female', 'male', 'town_C', 'town_Q', 'town_S']] # 독립 변수 X
y = ndf['survived'] # 종속 변수 Y

# >>> 설명변수 데이터를 정규화(normalization) -----

from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)

# >>> 데이터셋 분리(7:3 비율) -----

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
print('훈련데이터: ', X_train.shape)
print('검증데이터: ', X_test.shape)

# >>> KNN 분류 모형 적용 -----

from sklearn.neighbors import KNeighborsClassifier

# 모형 객체 생성 (k=5로 설정)
knn = KNeighborsClassifier(n_neighbors=5)

# 모형 학습
knn.fit(X_train, y_train)

# test data를 가지고 y_hat을 예측(분류)
y_hat = knn.predict(X_test)

# 10개 데이터 중 일치갯수 확인
print(y_hat[0:10])
print(y_test.values[0:10])

# >>> 모형 평가 -----

from sklearn import metrics

# Confusion Matrix 출력 -----
# [[TN, FP], [FN, TP]] 형태로 결과 반환
# 미생존바른예측 110(True Negative), 미생존을생존오류 15(False Positive), 생존을미생존오류 26, 생존정확예측 64
knn_matrix = metrics.confusion_matrix(y_test, y_hat)
print(knn_matrix)

# 모형성능 평가지표 출력 -----
# precision(정확도): True로 예측하여 실제 True인 비율, 높을수록 오류가 적음
# recall(재현율): 실제 True를 True로 예측한 비율, 높을수록 오류가 적음
# f1-score(예측정확도): 정확도와 재현율의 조화평균을 계산한 값, 높을수록 예측력이 좋음
# support(개체수)
knn_report = metrics.classification_report(y_test, y_hat)
print(knn_report)

# 판단 : KNN모형평가
# 미생존자(0) 예측정확도가 0.84 , 생존자(1) 예측정확도가 0.76 으로 예측 능력의 차이가 있음


# ----------------
# SVM 분류 모형
# ----------------

# 데이터프레임의 속성(열)별로 벡터를 구성하여 2개열은 2차원, 3개열은 3차원...의 공간좌표를 구성하고
# 같은 분류값을 가지는 데이터끼리 같은 공간에 배치하여, 새로운 데이터의 공간위치로 분류 영역을 예측

# >>> 모형 적용 -----

from sklearn import svm

# 모형 객체 생성 (kernel='rbf' 적용)
svm_model = svm.SVC(kernel='rbf') # 커넬옵션: linearm polynimial, sigmoid 등

# >>> 모형 학습 -----

svm_model.fit(X_train, y_train)

# test data를 가지고 y_hat을 예측(분류)
y_hat = svm_model.predict(X_test)

# 10개 데이터 중 일치갯수 확인
print(y_hat[0:10])
print(y_test.values[0:10])

# >>> 모형 평가 -----

from sklearn import metrics

# Confusion Matrix 출력 -----
# 미생존정확예측 120(True Negative), 미생존을생존오류 5(False Positive), 생존을미생존오류 35, 생존정확예측 55
svm_matrix = metrics.confusion_matrix(y_test, y_hat)
print(svm_matrix)

# 모형성능 평가지표 출력 -----
svm_report = metrics.classification_report(y_test, y_hat)
print(svm_report)

# 판단 : SVM모형평가
# 미생존자(0) 예측정확도가 0.86 , 생존자(1) 예측정확도가 0.73 으로 KMM모형과 유사함


# ----------------
# Decisin Tree 분류 모형
# ----------------

# 속성별 분기점마다 최적의 선택이 이루어지도록 구성

from sklearn import metrics
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd
import numpy as np

# >>> 전처리: Breast Cancer 데이터셋 -----

df = pd.read_csv('./trainingdata/machine/ breast-cancer-wisconsin.csv ', header=None)
df.columns = ['id', 'clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
              'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses', 'class']
print(df.head())
print(df.describe())
print(df.info())

# 유일한 문자형이며 결손값이 있는 bare_nuclei 열 전처리
print(df['bare_nuclei'].unique())
df['bare_nuclei'].replace('?', np.nan , inplace=True)   # '?'을 np.nan 으로 변경
df.dropna(subset=['bare_nuclei'], axis=0, inplace=True) # 누락데이터 행을 삭제
df['bare_nuclei'] = df['bare_nuclei'].astype('int')     # 문자열을 정수형으로 변환
print(df.describe())

# >>> 변수 선정 -----

X = df[['clump', 'cell_size', 'cell_shape', 'adhesion', 'epithlial',
        'bare_nuclei', 'chromatin', 'normal_nucleoli', 'mitoses']] # 설명 변수 X
y = df['class'] # 예측 변수 Y

# 설명 변수 데이터를 정규화
X = preprocessing.StandardScaler().fit(X).transform(X)

# >>> 데이터셋 분리(7:3 비율) -----

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=10)
print('훈련데이터: ', X_train.shape)
print('검증데이터: ', X_test.shape)

# >>> Decision Tree 분류 모형 적용 -----

from sklearn import tree

# 모형 객체 생성 (criterion='entropy', 트리레벨은 '5'로 지정)
tree_model = tree.DecisionTreeClassifier(criterion='entropy', max_depth=5)

# 모형 학습
tree_model.fit(X_train, y_train)

# test data를 가지고 y_hat을 예측(분류)
y_hat = tree_model.predict(X_test) # 2: benign(양성), 4: malignant(악성)

# 10개 데이터 중 일치갯수 확인
print(y_hat[0:10])
print(y_test.values[0:10])

# >>> 모형 평가 -----

# Confusion Matrix 출력
tree_matrix = metrics.confusion_matrix(y_test, y_hat)
print(tree_matrix)

# 모형성능 평가지표 출력
tree_report = metrics.classification_report(y_test, y_hat)
print(tree_report)

# 판단 : 양성예측정확도는 0.98 , 악성예측정확도는 0.96 으로 평균 0.97 의 정확도를 가짐


# ========================
# 군집(비지도학습)
# ========================

# 비지도학습으로 예측변수도 학습과정도 없으며, 필요한 변수를 모두 설명변수로 활용


# ----------------
# K-Means 모형
# ----------------

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./trainingdata/machine/ customer.csv ')
print(df.head())
print(df.info())
print(df.describe())

# >>> 변수 선정 -----

X = df.iloc[:, :]
print(X[:5])

# 설명 변수 데이터를 정규화
from sklearn import preprocessing
X = preprocessing.StandardScaler().fit(X).transform(X)
print(X[:5])

# >>> k-means 군집 모형 적용 -----

from sklearn import cluster

# 모형 객체 생성: 8개의 속성을 이용하여 5개의 클러스터로 관측값을 분류
kmeans = cluster.KMeans(init='k-means++', n_clusters=5, n_init=10)

# 모형 학습
kmeans.fit(X)

# 예측(군집): 모형의 예측값은 매번 달라짐
cluster_label = kmeans.labels_
print(cluster_label)

# 예측 결과를 데이터프레임에 추가
df['Cluster'] = cluster_label
print(df.head())

# 그래프로 표현: 시각화(8개의 변수를 하나씩 그려보아야 함)
df.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1',
colorbar=False, figsize=(10, 10))
df.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1',
colorbar=True, figsize=(10, 10))
plt.show()
plt.close()

# 지나치게 큰 값으로 구성된 클러스터(0, 4)를 제외: 값이 몰려 있는 구간을 자세하게 분석
mask = (df['Cluster'] == 0) | (df['Cluster'] == 4)
ndf = df[~mask]

ndf.plot(kind='scatter', x='Grocery', y='Frozen', c='Cluster', cmap='Set1',
colorbar=False, figsize=(10, 10))
ndf.plot(kind='scatter', x='Milk', y='Delicassen', c='Cluster', cmap='Set1',
colorbar=True, figsize=(10, 10))
plt.show()
plt.close()


# ----------------
# DBSCAN
# ----------------

# 데이터가 위치한 공간 밀집도를 기준으로 클러스터를 구분

import pandas as pd
import folium

# >>> 전처리: 서울시내 중학교 진학률 데이터셋 -----

df = pd.read_excel('./trainingdata/machine/ middle_shcool_report.xlsx ', engine='openpyxl', header=0, index_col=0)
print(df.columns.values)
print(df.head())
print(df.info())
print(df.describe())

# 지도에 위치 표시
mschool_map = folium.Map(location=[ 37.55 , 126.98], tiles='Stamen Terrain', zoom_start=12)

# 중학교 위치정보를 CircleMarker로 표시
for name, lat, lng in zip(df.학교명, df.위도, df.경도):
folium.CircleMarker([lat, lng],
                    radius=5,           # 원의 반지름
                    color='brown',      # 원의 둘레 색상
                    fill=True,
                    fill_color='coral', # 원을 채우는 색
                    fill_opacity=0.7,   # 투명도
                    popup=name
                   ).add_to(mschool_map)

# 지도를 html 파일로 저장
mschool_map.save('./ seoul_mschool_location.html ')

# 문자열데이터를 더미변수로 전환(원핫인코딩)
from sklearn import preprocessing

label_encoder = preprocessing.LabelEncoder()   # label encoder 생성
onehot_encoder = preprocessing.OneHotEncoder() # one hot encoder 생성

onehot_location = label_encoder.fit_transform(df['지역'])
onehot_code = label_encoder.fit_transform(df['코드'])
onehot_type = label_encoder.fit_transform(df['유형'])
onehot_day = label_encoder.fit_transform(df['주야'])

df['location'] = onehot_location
df['code'] = onehot_code
df['type'] = onehot_type
df['day'] = onehot_day
print(df.head())

# >>> 변수 선정 -----

from sklearn import cluster

# 분석에 사용할 속성을 선택 (과학고, 외고국제고, 자사고 진학률)
columns_list = [9, 10, 13]
X = df.iloc[:, columns_list]
print(X[:5])

# 설명 변수 데이터를 정규화
X = preprocessing.StandardScaler().fit(X).transform(X)

# >>> DBSCAN 군집 모형 적용 -----

# 모형 객체 생성
dbm = cluster.DBSCAN(eps=0.2, min_samples=5)

# 모형 학습
dbm.fit(X)

# 예측(군집): -1은 Noise를 나타내고 클러스터는 0,1,2,3으로 모두 4개가 됨
cluster_label = dbm.labels_
print(cluster_label)

# 예측 결과를 데이터프레임에 추가
df['Cluster'] = cluster_label
print(df.head())

# 클러스터 값으로 그룹화하고, 그룹별로 내용 출력 (첫 5행만 출력)
grouped_cols = [0, 1, 3] + columns_list
grouped = df.groupby('Cluster')
for key, group in grouped:
    print('* key :', key)
    print('* number :', len(group))
    print(group.iloc[:, grouped_cols].head())
    print('\n')
# 클러스터(key) -1은 Noise로 255개
# 클러스터(key) 0은 102개로 외고와 자사고 합격률은 높지만 과학고 합격자는 없음
# 클러스터(key) 1은 45개로 자사고 합격자만 존재
# 클러스터(key) 2는 8개로 자사고 합격률 매우 높으며, 외고와 과학고 합격자도 존재
# 클러스터(key) 3은 5개로 자사고 합격자가 있으며, 과학고 합격자는 없고 외고합격률이 매우 낮음

# 그래프로 표현 - 시각화
colors = {-1: 'gray', 0: 'coral', 1: 'blue', 2: 'green', 3: 'red', 4: 'purple',
          5: 'orange', 6: 'brown', 7: 'brick', 8: 'yellow', 9: 'magenta', 10: 'cyan', 11: 'tan'}
cluster_map = folium.Map(location=[ 37.55 , 126.98], tiles='Stamen Terrain',
                         zoom_start=12)
for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster):
    folium.CircleMarker([lat, lng],
                        radius=5, # 원의 반지름
                        color=colors[clus], # 원의 둘레 색상
                        fill=True,
                        fill_color=colors[clus], # 원을 채우는 색
                        fill_opacity=0.7, # 투명도
                        popup=name
                       ).add_to(cluster_map)

# 지도를 html 파일로 저장하기
cluster_map.save('./ seoul_mschool_cluster.html ')

# 변수 추가: X2 데이터셋에 대하여 위의 과정을 반복(과학고, 외고국제고, 자사고 진학률 + 재단유형(국,공,사립))
columns_list2 = [9, 10, 13, 22]
X2 = df.iloc[:, columns_list2]
print(X2[:5])

X2 = preprocessing.StandardScaler().fit(X2).transform(X2)
dbm2 = cluster.DBSCAN(eps=0.2, min_samples=5)
dbm2.fit(X2)
df['Cluster2'] = dbm2.labels_

grouped2_cols = [0, 1, 3] + columns_list2
grouped2 = df.groupby('Cluster2')
for key, group in grouped2:
    print('* key :', key)
    print('* number :', len(group))
    print(group.iloc[:, grouped2_cols].head())
    print('\n')

cluster2_map = folium.Map(location=[ 37.55 , 126.98], tiles='Stamen Terrain',
                          zoom_start=12)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster2):
                                folium.CircleMarker([lat, lng],
                                radius=5,                # 원의 반지름
                                color=colors[clus],      # 원의 둘레 색상
                                fill=True,
                                fill_color=colors[clus], # 원을 채우는 색
                                fill_opacity=0.7,        # 투명도
                                popup=name
                               ).add_to(cluster2_map)

# 지도를 html 파일로 저장하기(11개의 클러스터 생성)
cluster2_map.save('./ seoul_mschool_cluster2.html ')

# 변수 추가: X3 데이터셋에 대하여 위의 과정을 반복(과학고, 외고_국제고)
columns_list3 = [9, 10]
X3 = df.iloc[:, columns_list3]
print(X3[:5])

X3 = preprocessing.StandardScaler().fit(X3).transform(X3)
dbm3 = cluster.DBSCAN(eps=0.2, min_samples=5)
dbm3.fit(X3)
df['Cluster3'] = dbm3.labels_

grouped3_cols = [0, 1, 3] + columns_list3
grouped3 = df.groupby('Cluster3')
for key, group in grouped3:
    print('* key :', key)
    print('* number :', len(group))
    print(group.iloc[:, grouped3_cols].head())
    print('\n')

cluster3_map = folium.Map(location=[ 37.55 , 126.98], tiles='Stamen Terrain',
                          zoom_start=12)

for name, lat, lng, clus in zip(df.학교명, df.위도, df.경도, df.Cluster3):
    folium.CircleMarker([lat, lng],
                        radius=5,                # 원의 반지름
                        color=colors[clus],      # 원의 둘레 색상
                        fill=True,
                        fill_color=colors[clus], # 원을 채우는 색
                        fill_opacity=0.7,        # 투명도
                        popup=name
                       ).add_to(cluster3_map)

# 지도를 html 파일로 저장하기(클러스터 7개 생성)
cluster3_map.save('./ seoul_mschool_cluster3.html ')
