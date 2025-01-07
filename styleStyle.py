import pandas as pd
import numpy as np

# clsass pandas.io.formats.style.Styler(
#     data: DataFrame | Series,
#     precision: int | None = None,
#     table_styles: CSSStyles | None = None,
#     uuid: str | None = None,
#     caption: str | tuple | list | None = None,
#     table_attributes: str | None = None,
#     cell_ids: bool = True,
#     na_rep: str | None = None,
#     uuid_len: int = 5,
#     decimal: str | None = None,
#     thousands: str | None = None,
#     escape: str | None = None,
#     formatter: ExtFormatter | None = None,
#     )

df = pd.DataFrame([[1.0, 2.0, 3.0], [4, 5, 6]], index=['a', 'b'],
                  columns=['A', 'B', 'C'])

pd.io.formats.style.Styler(df, precision=2, caption="My table")


# >>> styler.apply(func, axis=0, subset=None, **kwargs) -----

def highlight_max(x, color):
    return np.where(x == np.nanmax(x.to_numpy()), f"color: {color};", None)
df = pd.DataFrame(np.random.randn(5, 2), columns=["A", "B"])

df.style.apply(highlight_max, color='red', subset=["A", "B"])
df.style.apply(highlight_max, color='red', subset=([1, 2, 3], slice(None)))
df.style.apply(highlight_max, color='red', subset=(slice(0, 4, 2), "A"))

total_style = pd.Series("color:red; font-weight: bold; font-size:20px;", index=[4])
df.style.apply(lambda s: total_style, subset=(slice(None), ["A", "B"]))

df = pd.DataFrame(np.random.randn(5, 2), columns=["A", "B"])
total_style = pd.Series("color:red; font-weight: bold; font-size:20px;", index=[4])
pd.io.formats.style.Styler(df, precision=2, caption="My table").apply(lambda s: total_style, subset=(slice(None), "B"))


# >>> styler.apply_index(func, axis=0, level=None, **kwargs) -----

df = pd.DataFrame([[1,2], [3,4]], index=["A", "B"])
def color_b(s):
    return np.where(s == "B", "background-color: yellow;", "")
df.style.apply_index(color_b)  


# >>> styler.format(formatter=None, subset=None, na_rep=None, precision=None, decimal='.', thousands=None, escape=None, hyperlinks=None) -----