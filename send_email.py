import os
import smtplib
import ssl
import streamlit as st


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    try:
        password = os.getenv("GA_PAUL_PASS")
    except Exception as ex:
        password = st.secrets("GA_PAUL_PASS")

    user_mail = "gunzeuxapp@gmail.com"
    receiver_mail = "pauljoe221102@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_mail, password)
        server.sendmail(user_mail, receiver_mail, message)
    print("completed")