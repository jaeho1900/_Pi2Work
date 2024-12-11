import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import numpy as np
import pandas as pd
import plotly.express as px
import io

with st.sidebar:
    choose = option_menu("App Gallery", ["About", "Photo Editing", "Project Planning"],
                         menu_icon="bi bi-airplane-engines", # "app-indicator",
                         icons=['house', 'camera fill', 'kanban'],
                         default_index=0,  # default_index = 처음에 보여줄 페이지 인덱스 번호
                         styles={
                                 "container": {"padding": "5!important", "background-color": "#D5D5D5"},
                                 "icon": {"color": "orange", "font-size": "25px"}, 
                                 "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#ABF200"},
                                 "nav-link-selected": {"background-color": "#02ab21"},
                                }
                        )