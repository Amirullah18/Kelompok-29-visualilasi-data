import streamlit as st
st.write("Displaying an Images")
# Displaying Image by specifying path
st.image("D:/Praktikum Visualisasi Data/praktikum01/assets/GreenSeaTurtle-2.jpg")
# Image Courtesy by unsplash
st.write("Image Courtesy: unsplash.com")

import streamlit as st
# Image Courtesy
st.write("Diplaying Multiple Images")
# Listing out animal images
animal_images = [
'C:/Praktikum Visualisasi Data/praktikum01/assets/animal1.jpg',
'C:/Praktikum Visualisasi Data/praktikum01/assets/animal2.jpg',
'C:/Praktikum Visualisasi Data/praktikum01/assets/animal3.jpg',
'C:/Praktikum Visualisasi Data/praktikum01/assets/animal2.jpg',
]

# Displaying Multiple images with width 150
st.image(animal_images, width=150)
# Image Courtesy
st.write("Image Courtesy: Unplash")

import streamlit as st
import base64

# Function to set Image as Background
def add_local_background_image(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Image Courtesy: unsplash")
    st.markdown(
    f"""
    <style>
    .stApp {{
    background-image: url(data:files/{"jpg"};base64,{encoded_string.decode()});
    background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )

st.write("Background Image")
# Calling Image in function
add_local_background_image('C:/Praktikum Visualisasi Data/praktikum01/assets/animal1.jpg')

import streamlit as st
from PIL import Image

original_image = Image.open("C:/Praktikum Visualisasi Data/praktikum01/assets/animal2.jpg")
# Display Original Image
st.title("Original Image")
st.image(original_image)

# Resizing Image to 600*400
resized_image = original_image.resize((600, 400))
# Displaying Resized Image
st.title("Resized Image")
st.image(resized_image)