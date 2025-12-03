import streamlit as st
import numpy as np

st.title("Container")

with st.container():
    st.write("Element Inside Container")
    # Defining Chart Element
    st.line_chart(np.random.randn(48, 4))

st.write("Element Outside Container")

import streamlit as st
import numpy as np

st.title("Out of Order Container")

# Defining Containers
container_one = st.container()

container_one.write("Element One Inside Container")

st.write("Element Outside Container")

# How to insert few more elements in the container_one
container_one.write("Element Two Inside Container")
container_one.line_chart(np.random.randn(48, 4))