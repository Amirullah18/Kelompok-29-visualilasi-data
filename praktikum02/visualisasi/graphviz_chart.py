import streamlit as st
import graphviz as graphviz

st.title("graphviz_chart")
st.write("Kelompok: 29")
st.markdown("""
    1. Amirullah - 0110222106
    2. Indah Agustin - 0110222250
    3. Miftahul Jannah - 0110222101
""")

st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"
    }
""") 