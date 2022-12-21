# from turtle import home
import streamlit as st


st.set_page_config(page_title="GDP Analysis | Home",page_icon="💰")

st.header("REPUBLIC OF INDIA ")
st.title("GDP Analysis and Prediction application")

st.image(".\img\gdp.jpg")

st.title("What is GDP")

st.subheader("Gross domestic product (GDP) is the total monetary or market value of all the finished goods and services produced within a country’s borders in a specific time period. As a broad measure of overall domestic production, it functions as a comprehensive scorecard of a given country’s economic health.")


st.sidebar.success("Select the page Above")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
