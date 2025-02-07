import pandas as pd
from sklearn.datasets import load_iris

iris_raw = load_iris()

iris_raw.keys()

iris = pd.DataFrame(iris_raw.data, columns=iris_raw.feature_names)
iris['Class'] = iris_raw.target
iris['Class'] = iris['Class'].map({0:'Setosa', 1:'Versicolour', 2:'Virginica'})
