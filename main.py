import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Phil Cooke")
    content = """
    Hello and welcome to my home page. I am a chartered accountant and a developer. I started my ICT career in 2023,
after having worked as an accountant for 16 years. With expertise in both industries enables me to provide 
ICT solutions to financial problems. 
    """
    st.info(content)

introMsg = """
Included below are a list of projects I have worked on in my own time for self development. 
Please feel free to browse the below Python apps.
"""
st.write(introMsg)

