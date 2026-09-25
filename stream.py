import streamlit as st
# import pandas as pd

st.title("CampusX")

col1,col2 = st.columns(2)

with col1:
    st.image("unnamed.png")

with col2:
    st.write("""
    this is here for no relevency 
    i just i did for just learning and fun purpose only.
    so dont get to happy about it.
    """)
st.header("Courses Offered")
st.subheader("Data Science")
st.subheader("Data Analysis")
st.subheader("Machine Learning")

