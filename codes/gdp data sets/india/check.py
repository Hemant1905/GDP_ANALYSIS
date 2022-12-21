# import streamlit as st
import pandas as pd
import plotly.express as px


df_jj = pd.read_csv("D:\codeverse\python\projects\gdp analysis\codes\gdp data sets\china\China.csv")    
fig = px.line(df_jj,x="Year",y="GDP in US$",title="Apple Share Prices over time (2014)")
fig.show()

# st.plotly_chart(fig)

