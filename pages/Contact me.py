import streamlit as st
import pandas as pd
from send_email import send_email


df = pd.read_csv("Topic.csv")

st.title("Contact me")

with st.form("Send Message"):
    user_mail = st.text_input("Your E-Mail")
    user_option = st.selectbox("Type on Enquiry :", df)
    raw_msg = st.text_area("Message")
    button = st.form_submit_button("Submit")

    if button:
        message = f"""
Subject: New Enquiry for {user_option} from Portfolio

From: {user_mail}
{raw_msg}"""
        send_email(message)

        print("completed")

