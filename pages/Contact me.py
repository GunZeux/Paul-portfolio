import streamlit as st
import pandas as pd

df = pd.read_csv("Topic.csv")

st.title("Contact me")

with st.form("Send Message"):
    st.text_input("Your E-Mail")
    st.selectbox("Type on Enquiry :", df)
    st.text_area("Message")
    st.form_submit_button("Submit")
