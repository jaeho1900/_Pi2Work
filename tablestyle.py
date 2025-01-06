# Formatting values, the index and columns headers, using .format() and .format_index(),
# Renaming the index or column header labels, using .relabel_index()
# Hiding certain columns, the index and/or column headers, or index names, using .hide()
# Concatenating similar DataFrames, using .concat()

import pandas as pd
import numpy as np
import matplotlib as mpl

# Formatting Values 예제 1 -----
df = pd.DataFrame({
    "strings": ["Adam", "Mike"],
    "ints": [1, 3],
    "floats": [1.123, 1000.23]
})
df.style \
  .format(precision=2, thousands=",", decimal=".") \
  .format_index(str.upper, axis=1) \
  .relabel_index(["row 1", "row 2"], axis=0)

# Formatting Values 예제 2 -----
weather_df = pd.DataFrame(np.random.rand(10,2)*5,
                          index=pd.date_range(start="2021-01-01", periods=10),
                          columns=["Tokyo", "Beijing"])

def rain_condition(v):
    if v < 1.75:
        return "Dry"
    elif v < 2.75:
        return "Rain"
    return "Heavy Rain"

def make_pretty(styler):
    styler.set_caption("Weather Conditions")
    styler.format(rain_condition)
    styler.format_index(lambda v: v.strftime("%A"))
    styler.background_gradient(axis=None, vmin=1, vmax=5, cmap="YlGnBu")
    return styler

weather_df
weather_df.loc["2021-01-04":"2021-01-08"].style.pipe(make_pretty)

# Hiding Data 예제 3 -----
df = pd.DataFrame(np.random.randn(5, 5))
df.style \
  .hide(subset=[0, 2, 4], axis=0) \
  .hide(subset=[0, 2, 4], axis=1)

# Concatenating DataFrame Outputs 예제 4 -----
df = pd.DataFrame(np.random.randn(5, 5))
summary_styler = df.agg(["sum", "mean"]).style \
                   .format(precision=3) \
                   .relabel_index(["Sum", "Average"])
df.style.format(precision=1).concat(summary_styler)

# Styler Object and HTML 예제 5 -----
df = pd.DataFrame([[38.0, 2.0, 18.0, 22.0, 21, np.nan],[19, 439, 6, 452, 226,232]],
                  index=pd.Index(['Tumour (Positive)', 'Non-Tumour (Negative)'], name='Actual Label:'),
                  columns=pd.MultiIndex.from_product([['Decision Tree', 'Regression', 'Random'],['Tumour', 'Non-Tumour']], names=['Model:', 'Predicted:']))
df.style

s = df.style.format('{:.0f}').hide([('Random', 'Tumour'), ('Random', 'Non-Tumour')], axis="columns")
s

# Table Styles 예제 6 -----

# <!-- 
# 	table(테이블) 태그 : 데이터 표를 만드는 태그.
# 	- tr 태그 : 테이블의 행을 만드는 태그.
# 	- th 태그 : 테이블의 열(타이틀-제목)을 만드는 태그.
# 	- td 태그 : 테이블의 열을 만드는 태그.
#  -->
# <table border="1" cellspacing="0" width="250">
# 	<tr>
# 		<th>아이디</th>
# 		<th>이   름</th>
# 		<th>나   이</th>
# 	</tr>
# 	<tr>
# 		<td>hong</td>
# 		<td>홍길동</td>
# 		<td>27</td>
# 	</tr>
# 	<tr>
# 		<td>lee</td>
# 		<td>이순신</td>
# 		<td>32</td>
# 	</tr>
# 	<tr>
# 		<td>you</td>
# 		<td>유관순</td>
# 		<td>25</td>
# 	</tr>
# </table>

df = pd.DataFrame([[38.0, 2.0, 18.0, 22.0, 21, np.nan],[19, 439, 6, 452, 226,232]],
                  index=pd.Index(['Tumour (Positive)', 'Non-Tumour (Negative)'], name='Actual Label:'),
                  columns=pd.MultiIndex.from_product([['Decision Tree', 'Regression', 'Random'],['Tumour', 'Non-Tumour']], names=['Model:', 'Predicted:']))
s = df.style.format('{:.0f}').hide([('Random', 'Tumour'), ('Random', 'Non-Tumour')], axis="columns")

cell_hover = {  # for row hover use <tr> instead of <td>
    'selector': 'td:hover',
    'props': [('background-color', '#ffffb3')]
}
index_names = {
    'selector': '.index_name',
    'props': 'font-style: italic; color: darkgrey; font-weight:normal;'
}
headers = {
    'selector': 'th:not(.index_name)',
    'props': 'background-color: #000066; color: white;'
}
s.set_table_styles([cell_hover, index_names, headers])  # styled DF에 적용

# Table Styles 예제 7 -----
s.set_table_styles([
    {'selector': 'th.col_heading', 'props': 'text-align-last: center;'},
    {'selector': 'th.col_heading.level0', 'props': 'font-size: 1.5em;'},
    {'selector': 'td', 'props': 'text-align: right; font-weight: bold;'},
], overwrite=False)

# Table Styles 예제 8 -----
s.set_table_styles({
    ('Regression', 'Tumour'): [{'selector': 'th', 'props': 'border-left: 1px solid white'},
                               {'selector': 'td', 'props': 'border-left: 1px solid #FF0000'}]
}, overwrite=False, axis=0)

# Data Cell CSS Classes 예제 9 -----
s.set_table_styles([  # create internal CSS classes
    {'selector': '.true', 'props': 'background-color: #e6ffe6;'},
    {'selector': '.false', 'props': 'background-color: #ffe6e6;'},
], overwrite=False)
cell_color = pd.DataFrame([['true ', 'false ', 'true ', 'false '],
                           ['false ', 'true ', 'false ', 'true ']],
                          index=df.index,
                          columns=df.columns[:4])
s.set_td_classes(cell_color)

# Finer Control with Slicing 예제 10 -----
df3 = pd.DataFrame(np.random.randn(4,4),
                   pd.MultiIndex.from_product([['A', 'B'], ['r1', 'r2']]),
                   columns=['c1','c2','c3','c4'])
df3

def highlight_max(s, props=''):
    return np.where(s == np.nanmax(s.values), props, '')
slice_ = ['c3', 'c4']
df3.style.apply(highlight_max, props='color:red;', axis=0, subset=slice_)\
         .set_properties(**{'background-color': '#ffffb3'}, subset=slice_)

# Finer Control with Slicing 예제 11 -----
idx = pd.IndexSlice
slice_ = idx[idx[:,'r1'], idx['c2':'c4']]
df3.style.apply(highlight_max, props='color:red;', axis=0, subset=slice_)\
         .set_properties(**{'background-color': '#ffffb3'}, subset=slice_)
