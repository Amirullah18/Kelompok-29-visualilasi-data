import streamlit as st
import pandas as pd
import numpy as np

st.title("Area Chart")
st.write("Kelompok: 29")
st.markdown("""
    1. Amirullah - 0110222106
    2. Indah Agustin - 0110222250
    3. Miftahul Jannah - 0110222101
""")

df = pd.DataFrame(
    np.random.randn(40, 4),
    columns=["C1", "C2", "C3", "C4"]
)

st.area_chart(df)