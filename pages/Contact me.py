import streamlit as st
import pandas as pd

df = pd.read_csv("Topic.csv")

st.title("Contact me")

with st.form("Send Message"):
    user_mail = st.text_input("Your E-Mail")
    user_option = st.selectbox("Type on Enquiry :", df)
    raw_msg = st.text_area("Message")
    st.form_submit_button("Submit")
