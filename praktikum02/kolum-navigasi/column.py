import streamlit as st

st.title("Column")
st.write("Kelompok: 29")
st.markdown("""
    1. Amirullah - 0110222106
    2. Indah Agustin - 0110222250
    3. Miftahul Jannah - 0110222101
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("../../praktikum01/assets/animal1.jpg")
col1.write("Ini adalah kolum kedua")
col1.image("../../praktikum01/assets/animal3.jpg")