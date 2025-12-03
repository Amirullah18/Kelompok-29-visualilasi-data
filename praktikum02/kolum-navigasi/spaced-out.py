import streamlit as st
from PIL import Image

img = Image.open("../../praktikum01/assets/animal3.jpg")

st.title("Spaced-Out Columns")

# Defining two Rows
for _ in range(2):
    # Defining no. of columns with size
    cols = st.columns((3, 1, 2, 1))
    
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)  # Mengubah index dari 1 menjadi 3