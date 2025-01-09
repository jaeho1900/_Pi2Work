# =====================
# HTML의 <table>태그 Style
# =====================

# --------------------
# CSS 
# --------------------

# CSS 적용 방법: 인라인 방식(태그에 직접 적용), 내부 스타일시트 방식(head 영역에 <style>태그로 적용), 외부 파일 방식(*.css)
# CSS 사용 형식: HTML요소{속성명:속성값; 속성명:속성값;} 또는 상위태그 하위태그{속성명:속성값; 속성명:속성값;}

# 참고. HTML 요소의 style 속성(attribute)을 이용하면 CSS 스타일을 HTML 요소에 직접 설정할 수 있다.
#       <태그이름 style="속성이름:속성값; 속성이름:속성값;">


# --------------------
# <table> 관련 태그
# --------------------

# <table>: Table element
# <thead>: Table Head element
# <tbody>: Table Body element
# <tfoot>: Table Foot element

# <tr>: Table Row element
# <th>: Table Header element
# <td>: Table Data Cell element


# --------------------
# <table> 속성
# --------------------

# colspan : 가로칸을 넓히는 개수를 지정 
# rowspan : 세로칸을 넔히는 개수를 지정
# border : 테이블 경계선 굵기를 지정(예: border="10")
# width : 너비를 지정(픽셀이나, %)
# height : 높이를 지정(픽셀이나, %)
# cellpadding : 셀과 경계선 사이의 여백
# cellspacing : 셀과 셀 사이의 여백
# text-align : 테이블 요소(th, td) 내부에서 텍스트의 수평 방향 정렬(<th>은 가운데 정렬, <td>태그는 왼쪽 정렬이 기본)
# text-align-last : 줄바꿈된 문단의 마지막 줄의 정렬 방식을 설정(auto | start | end | left | right | center | justify)
# vertical-align : 테이블 요소(th, td) 내부에서 텍스트의 수직 방향 정렬(<th>태그 및 <td>태그 모두 가운데 정렬이 기본)
# bgcolor : 배경색 지정, 색상명(green), 색상코드(#ff0000), rgb(0,0,255) 등 사용
# bordercolor: 경계선 색깔 지정


# --------------------
#  사례 구문
# --------------------

#<html>
# <head>
#  <style>
#   table {
#     border-collapse: collapse;                # 테이블의 tr 공백 제거(한개의 선으로 표현)
#     border: 2px solid rgb(140 140 140);
#     font-family: sans-serif;
#     font-size: 0.8rem;
#     letter-spacing: 1px;
#   }
  
#   caption {
#     caption-side: bottom;
#     padding: 10px;
#     font-weight: bold;
#   }
  
#   thead,                                        # head와 foot에 같이 적용
#   tfoot {
#     background-color: rgb(228 240 245);
#   }
  
#   th,                                           # th와 td에 같이 적용
#   td {
#     border: 1px solid rgb(160 160 160);
#     padding: 8px 10px;
#   }
  
#   td {                                          # td에만 적용
#        text-align: right;
#    }
  
#   td:last-of-type {                             # 행의 마지막 요소(td)에만 적용
#     text-align: center;
#   }
  
#   tbody {
#     background-color: #e4f0f5;
#   }
  
#   tbody > tr:nth-of-type(even) {                # 한줄띄면서 적용 
#     background-color: rgb(237 238 242);
#   }
  
#   tfoot th {
#     text-align: right;
#   }
  
#   tfoot td {
#     font-weight: bold;
#   }
#   </style>
#  </head>

#  <body>  
#   <table>
#     <caption>
#       Front-end web developer course 2021
#     </caption>
#     <thead>
#       <tr>
#         <th scope="col">Person</th>
#         <th scope="col">Most interest in</th>
#         <th scope="col">Age</th>
#       </tr>
#     </thead>
#     <tbody>
#       <tr>
#         <th scope="row">Chris</th>
#         <td>HTML tables</td>
#         <td>22</td>
#       </tr>
#       <tr>
#         <th scope="row">Dennis</th>
#         <td>Web accessibility</td>
#         <td>45</td>
#       </tr>
#       <tr>
#         <th scope="row">Sarah</th>
#         <td>JavaScript frameworks</td>
#         <td>29</td>
#       </tr>
#       <tr>
#         <th scope="row">Karen</th>
#         <td>Web performance</td>
#         <td>36</td>
#       </tr>
#     </tbody>
#     <tfoot>
#       <tr>
#         <th scope="row" colspan="2">Average age</th>
#         <td>33</td>
#       </tr>
#     </tfoot>
#   </table>

#  </body>
# </html>


# =====================
# Pandas DataFrame Style
# =====================

import pandas as pd
import numpy as np

# >>> Helps style a DataFrame or Series according to the data with HTML and CSS -----

# pandas.io.formats.style.Styler(
#     data: DataFrame | Series,
#     formatter: ExtFormatter | None = None,
#     na_rep: str | None = None,
#     precision: int | None = None,
#     decimal: str | None = None,
#     thousands: str | None = None,
#     table_styles: CSSStyles | None = None,
#     table_attributes: str | None = None,
#     caption: str | tuple | list | None = None,
#     cell_ids: bool = True,
#     uuid: str | None = None,
#     uuid_len: int = 5,
#     escape: str | None = None,
#     )

df = pd.DataFrame([[1.0, 2.0, 3.0], [4, 5, 6]], index=['a', 'b'],
                  columns=['A', 'B', 'C'])

pd.io.formats.style.Styler(df, precision=2, caption="My table")

# >>> Format the text display value of cells -----

# Styler.format(formatter=None, subset=None, na_rep=None, precision=None, \
#               decimal='.', thousands=None, escape=None, hyperlinks=None)
#        formatter: str, callable, dict or None
#        subset: label, array-like, IndexSlice, optional
#        na_rep: str, optional
#        precision: int, optional
#        decimal: str, default "."
#        thousands: str, optional, default None
#        escape: str, optional
#        hyperlinks: {"html", "latex"}, optional

df = pd.DataFrame([[np.nan, 1988.0, 'A'], [2025.0, np.nan, 3.0]])

df.style.format(na_rep='MISS', precision=2)

df.style.format('{:,.2f}', na_rep='MISS', subset=[0,1])

df.style.format({0: '{:,.1f}', 1: '£ {:.2f}'}, na_rep='MISS', precision=2)

(df.style.format(na_rep='MISS', precision=1, subset=[0])
         .format(na_rep='PASS', precision=2, subset=[1, 2])) 

func = lambda s: 'STRING' if isinstance(s, str) else 'FLOAT'
df.style.format({0: '{:.1f}', 2: func}, precision=4, na_rep='MISS')

def rain_condition(v):
    if v < 1.75:
        return "Dry"
    elif v < 2.75:
        return "Rain"
    return "Heavy Rain"
weather_df = pd.DataFrame(np.random.rand(10,2)*5,
                          index=pd.date_range(start="2021-01-01", periods=10),
                          columns=["Tokyo", "Beijing"])
weather_df.style.format(rain_condition)

# >>> Format the text display value of index labels or column headers -----

# Styler.format_index(formatter=None, axis=0, level=None, na_rep=None, \
#                     precision=None, decimal='.', thousands=None, escape=None, \
#                     hyperlinks=None)

df = pd.DataFrame([[1, 2, 3]], columns=[2.0, np.nan, 4.0])
df.style.format_index(axis=1, na_rep='MISS', precision=3)  

# >>> Apply a CSS-styling function column-wise, row-wise, or table-wise -----

# Styler.apply(func, axis=0, subset=None, **kwargs)
#        func: function
#        axis: {0 or 'index', 1 or 'columns', None}, default 0
#        subset: label, array-like, IndexSlice, optional
#        **kwargs: dict

def highlight_max(x, color):
    return np.where(x == np.nanmax(x.to_numpy()), f"color: {color};", None)
df = pd.DataFrame(np.random.randn(5, 2), columns=["A", "B"])

df.style.apply(highlight_max, color='red', subset=["A", "B"])
df.style.apply(highlight_max, color='red', subset=([0, 1, 2], slice(None)))
df.style.apply(highlight_max, color='red', subset=(slice(0, 5, 2), "B"))

total_style = pd.Series("color:red; font-weight: bold; font-size:20px;", index=[4])
df.style.apply(lambda s: total_style, subset=(slice(None), ["A", "B"]))

df = pd.DataFrame(np.random.randn(5, 2), columns=["A", "B"])
total_style = pd.Series("color:red; font-weight: bold; font-size:20px;", index=[4])
pd.io.formats.style.Styler(df, precision=2, caption="My table").apply(lambda s: total_style, subset=(slice(None), "B"))

# >>> Apply a CSS-styling function to the index or column headers, level-wise -----

# Styler.apply_index(func, axis=0, level=None, **kwargs)
#        func: function
#        axis: {0, 1, “index”, “columns”}
#        level: int, str, list, optional
#        **kwargs: dict

df = pd.DataFrame([[1,2], [3,4]], index=["A", "B"])
def color_b(s):
    return np.where(s == 1, "background-color: yellow;", "")
df.style.apply_index(color_b, axis=1) \
        .relabel_index(["row 1", "row 2"], axis=0) 


midx = pd.MultiIndex.from_product([['ix', 'jy'], [0, 1], ['x3', 'z4']])
df = pd.DataFrame([np.arange(8)], columns=midx)
def highlight_x(s):
    return ["background-color: yellow;" if "x" in v else "" for v in s]
df.style.apply_index(highlight_x, axis='columns', level=[0, 2])

for v in pd.DataFrame([np.arange(8)]):
    if "x" not in str(v):
            print(v)
    else:
        ""

# >>> Hide the entire index / column headers, or specific rows / columns from display -----

# Styler.hide(subset=None, axis=0, level=None, names=False)
#        names: bool

df = pd.DataFrame([[1,2], [3,4], [5,6]], index=["a", "b", "c"])
df.style.hide(["a", "b"]) 

midx = pd.MultiIndex.from_product([["x", "y"], ["a", "b", "c"]])
df = pd.DataFrame(np.random.randn(6,6), index=midx, columns=midx)
df.style.format("{:.1f}").hide()   # Hide the index 

df.style.format("{:.1f}").hide(subset=(slice(None), ["a", "c"]))

df.style.format("{:.1f}").hide(subset=(slice(None), ["a", "c"])).hide()

df.style.format("{:,.1f}").hide(level=1) 

df.index.names = ["lev0", "lev1"]
df.style.format("{:,.1f}").hide(names=True, axis=1) 

# >>> Set the table styles included within the <style> HTML element -----

# Styler.set_table_styles(table_styles=None, axis=0, overwrite=True, css_class_names=None)
#        table_styles: list or dict
#        axis: {0 or ‘index’, 1 or ‘columns’, None}, default 0
#        overwrite: bool, default True
#        css_class_names: dict, optional

df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])

df.style.set_table_styles({
                           'A': [{'selector': '',                  # columnLable에도 영향
                                  'props': [('color', 'red')]}],
                           'B': [{'selector': 'td',                # 데이터에만 영향
                                  'props': 'color: blue;'}]
                          }, overwrite=False)
df.style.set_table_styles([{'selector': 'tr:hover',
                            'props': [('background-color', 'yellow'), ('font-size', '2em')]
                           }])
df.style.set_table_styles([{'selector': 'tr:hover',
                            'props': 'background-color: yellow; font-size: 2em;' # CSS strings
                           }])
df.style.set_table_styles({
                           0: [{'selector': 'td:hover',
                                'props': [('font-size', '25px')]}]
                          }, axis=1, overwrite=False)

# >>> Set defined CSS-properties to each <td> HTML element for the given subset -----

# Styler.set_properties(subset=None, **kwargs)

df = pd.DataFrame([[1.0, 2.0, 3.0, 4.0], [4, 5, 6, 7], ['top', 'soribada', 'copy', 'sound']],
                  columns=['Aa', 'Bbb', 'C', 'Dddd'])

df.style.set_properties(**{'color':'lightblue', 'text-align':'left'}, subset=['Aa','Dddd'])
df.style.set_properties(**{'background-color': 'yellow', 'color': 'black'}, subset=['Aa','Dddd'])

# >>> Append another Styler to combine the output into a single table -----

# Styler.concat(other)

df = pd.DataFrame(np.random.randn(5, 5))
summary_styler = df.agg(["sum", "mean"]).style \
                   .relabel_index(["Sum", "Average"])
df.style.concat(summary_styler)

df = pd.DataFrame([[4, 6], [1, 9], [3, 4], [5, 5], [9, 6]],
                  columns=["Mike", "Jim"],
                  index=["Mon", "Tue", "Wed", "Thurs", "Fri"])

descriptors = df.agg(["sum", "mean"])
descriptors.index = ["Total", "Average"]
other = (descriptors.style
         .highlight_max(axis=1, subset=(["Total", "Average"], slice(None)))
         .format(subset=("Average", slice(None)), precision=2, decimal=",")
         .map(lambda v: "font-weight: bold;"))
styler = (df.style
            .highlight_max(color="salmon")
            .set_table_styles([{"selector": ".foot_row0",
                                "props": "border-top: 1px solid black;"}]))
styler.concat(other)  

# >>> Reset the Styler, removing any previously applied styles -----

# Styler.clear()

df = pd.DataFrame({'A': [1, 2], 'B': [3, np.nan]})
df.style.highlight_null(color='yellow')
df.style.clear()  


# =====================
# List, Set, Dict Comprehension
# =====================

# 1-1. 반복문
[i**2 for i in range(10)]

# 1-2. 2개의 반복문
a = ['a','b','c' ]
b = ['1','2','3' ]
[i+j for i in a for j in b]

# 2-1. if 조건문
[i for i in range(10) if i%2 ==0]

# 2-2. 2개의 if 조건문
[i for i in range(50) if i%2 ==0 if i%3 == 0]  # and 조건

# 2-3. if~else 조건문 : elif 조건은 사용불가, for문이 뒤로 빠짐
['even' if i%2 ==0 else 'odd' for i in range(10)]

# 2-4. 2개의 if~else 조건문 : elif 유사 조건
['zero' if i==0 else 'even' if i%2 ==0 else 'odd' for i in range(10)]

lst = []
for i in range(10):
     if i==0:
        lst.append('zero')
     elif i%2 ==0:
        lst.append('even')
     else:
        lst.append('odd')
print(lst)


# =====================
# Generator Expression
# =====================

# Comprehension 구문을 소괄호로 묶어주면 파이썬이 generator expression으로 인식하여
# generator 객체로 생성한다.
# 이를 사용하기 위해서는 해당 객체를 next()로 감싸서 호출하면 순서대로 하나씩 출력되고
# 모든 값을 한바퀴를 돌게 되면 StopIteration 오류를 출력한다.

a = (i**2 for i in range(10))
print(a)

print(next(a))


# =====================
# slice()함수
# =====================

# index 기준으로 슬라이싱
# slice(stop)
# slice(start, stop[, step])

# String slicing
String = 'GeeksforGeeks'
print(String[slice(None)])
print(String[slice(3)])
print(String[slice(1, 5, 2)])

# List, Array slicing
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(L[slice(None)])
print(L[slice(3)])
print(L[slice(-1)])
print(L[slice(2, 9, 3)])
print(L[2:9:3])
