import streamlit as st


st.set_page_config(page_title="GDP Analysis | Terminology",page_icon="💰")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)