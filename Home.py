import streamlit as st
import pandas as pd

df = pd.read_csv("Paul_Data.csv")
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/img.png")

with col2:
    st.title("Paul Joseph")
    contents = """Hello! I'm an inquisitive and energetic Mechanical Engineering student 
    with a keen interest in programming and technical skills. 
    I am currently focused on honing my development skills through 
    collaborative, communicative, and creative approaches. My goal 
    is to integrate my strong technical foundation with innovative 
    problem-solving skills in a team-oriented environment. I am 
    passionate about leveraging my knowledge and energy to contribute 
    effectively to projects that push the boundaries of engineering 
    and technology.
    """
    st.info(contents)

st.write("The below are some of my projects and skills")

col3, empty_space, col4 = st.columns([1.5, 0.5, 1.5])
length = len(df)
with col3:
    for index, row in df[:7].iterrows():
        st.header(row["skill"])
        st.write(row["description"])

with col4:
    for index, row in df[7:].iterrows():
        st.header(row["skill"])
        st.write(row["description"])