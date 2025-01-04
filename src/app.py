import streamlit as st
from chatbot import Chatbot

if "chatbot" not in st.session_state:
    st.session_state.chatbot = Chatbot()

user_input = st.text_input("Digite sua mensagem:")
if user_input:
    response = st.session_state.chatbot.respond(user_input)
    st.write(response)
