import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils import Data

data = Data("https://github.com/hhssccab/clasestreamlit/blob/main/iris.csv")
flowers_variety = data.get_data()['variety'].unique()

variety = st.selectbox(
    "Seleccione una variedad de flor", flowers_variety)

sepal_length = st.number_input("filtro para largo del tallo")

st.write(data.get_summary_statistics())

st.write("Media", data.calculate_mean())



