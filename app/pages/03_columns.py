import streamlit as st
import pandas as pd

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )

st.write(add_selectbox)
st.write(add_radio)


col1, col2, col3 = st.columns(3)

with col1:
    st.text("비둘기")
    st.image('https://image.dongascience.com/Photo/2016/07/14694309465749.png')
with col2:
    st.text("노랑새") 
    st.image('https://i.imgur.com/e0JBf0q.jpg')
with col3: 
    st.text("펭귄")
    st.image('https://i.imgur.com/6qRYLMC.jpg')