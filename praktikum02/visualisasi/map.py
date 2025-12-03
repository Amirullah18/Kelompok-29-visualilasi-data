import streamlit as st
import pandas as pd
import numpy as np

st.title("Map")
st.write("Kelompok: 29")
st.markdown("""
    1. Amirullah - 0110222106
    2. Indah Agustin - 0110222250
    3. Miftahul Jannah - 0110222101
""")

df = pd.DataFrame(
    np.random.randn(50, 2)/[10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)