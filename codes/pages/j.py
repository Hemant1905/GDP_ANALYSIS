import pandas as pd
import streamlit as st
from datetime import datetime


data = {
    'Date': ['2017', '2018', '2022', '2023', '2024', '2025'],
    'Sold': [5, 4, 8, 2, 9, 4]
}

df = pd.DataFrame(data)

st.write('### Initial data')
st.dataframe(df)

Date = df["Date"].unique().tolist()

min_value = datetime.strptime(min(Date),"%Y")   # str to datetime
max_value = datetime.strptime(max(Date),"%Y")
value = (min_value, max_value)

st.write(value)

Model = st.slider(
    'Date:',
    min_value=min_value,
    max_value=max_value,
    value=value)

selmin, selmax = Model
selmind = selmin.strftime('y')  # datetime to str
selmaxd = selmax.strftime('y')



dfres = df.loc[(df['Date'] >= selmind) & (df['Date'] <= selmaxd)]

st.write('### Data from selected date')
st.dataframe(dfres)