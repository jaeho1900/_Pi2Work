import streamlit as st
import pandas as pd
import random

df = pd.DataFrame(
    {
        "name": ["Kakao", "Naver", "Samsung", "LG"],
        "image": [
            "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fwww.kakaocorp.com%2Fpage%2Ffavicon.ico&type=f30_30_png_expire24",
            "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fs.pstatic.net%2Fstatic%2Fwww%2Fu%2F2014%2F0328%2Fmma_204243574.png&type=f30_30_png_expire24",
            "https://search.pstatic.net/sunny?src=https%3A%2F%2Fwww.samsung.com%2Fsec%2Fstatic%2F_images%2Ffavicon.ico&type=f30_30_png_expire24",
            "https://search.pstatic.net/sunny/?src=https%3A%2F%2Fwww.lg.co.kr%2Ffavicon.ico&type=f30_30_png_expire24"
        ],
        "revenue": [
            random.sample(range(5000, 10000), 4),
            random.sample(range(5000, 10000), 4),
            random.sample(range(5000, 10000), 4),
            random.sample(range(5000, 10000), 4),
        ]
    }
)

df["margin"] = df["revenue"].apply(lambda x : [x[idx]-each for idx, each in enumerate(random.sample(range(0, 5001), 4))])
df["max_ratio"] = df.apply(lambda x: max([x.margin[idx]/sale for idx, sale in enumerate(x.revenue)])*100, axis=1)

st.dataframe(
    df,
    column_config={
        "image": st.column_config.ImageColumn(
            "Logo",
            width="small",
            help="This is the brand logo"
        ),
        "revenue": st.column_config.BarChartColumn(
            "Bar chart Sales (2023Y)",
            width="medium",
            help="This is the company's revenue in 2023",
            y_min=5000,
            y_max=10000
        ),
        "margin": st.column_config.LineChartColumn(
            "Margins",
            width="small",
            help="This is the company's 2023 margins",
            y_min=0,
            y_max=5001,
        ),
        "max_ratio": st.column_config.ProgressColumn(
            "Maximum value for Ratio",
            width="medium",
            help="The maximum value of the operating margin",
            format="%.1f%%",
            min_value=0,
            max_value=100
        )
    }
)