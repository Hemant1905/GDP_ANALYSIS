# from http.client import _DataType
from operator import index
from re import X
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import os

st.set_page_config(page_title="GDP Analysis | Analytics",page_icon="💰")


#starting 
st.header("Dashboard")
st.markdown("In this Analytics section you will get to see exact data of the top 5 countries..")

custom_html = """<br></br>
                   """
st.markdown(custom_html,unsafe_allow_html=True)

option = st.selectbox(
    'Select the country',
    ('USA', 'China', 'Japan','India','United kingdom'))

dashboard = {
        
        "USA":{
            "curr_gdp":"$24.8 Trillion",
            "growth":"-1.6%",
            "population":"332 Million",
            "pop_growth":"+0.38%",
            "gdp_rank":"1st"
        },
        
        "China":{
            "curr_gdp":"$19.91 Trillion",
            "growth":"4%",
            "population":"1.42 Billion",
            "pop_growth":"+0.1%",
            "gdp_rank":"2th"
        },
          
        "Japan":{
            "curr_gdp":"$6.11 Trillion",
            "growth":"1.7%",
            "population":"125.93 million",
            "pop_growth":"-0.53%",
            "gdp_rank":"3rd"
        },
          
         "India":{
            "curr_gdp":"$3.5 Trillion",
            "growth":"8.7%",
            "population":"1.41 Billion",
            "pop_growth":"+0.68%",
            "gdp_rank":"5th"
        },                 
        
          "United kingdom":{
            "curr_gdp":"$3.32 Trillion",
            "growth":"-0.6%",
            "population":"60.8 Million",
            "pop_growth":"+0.34%",
            "gdp_rank":"6th"
          }      
}

st.write('You Have selected:', option)

#accessing select box of different countries 
if option:
    st.title(f"GDP Data Analytics -{option}")
    col1, col2, col3 = st.columns(3)
    col1.metric("Current GDP ",dashboard[option]["curr_gdp"],dashboard[option]["growth"])
    col2.metric("Population", dashboard[option]["population"], dashboard[option]["pop_growth"])
    col3.metric("GDP Rank",dashboard[option]["gdp_rank"])
    
    

custom_html = """<br></br>
                   """
st.markdown(custom_html,unsafe_allow_html=True)

st.header("Graphical Representation")







#representation of graphs 

col_1,col_2 = st.columns(2)

with col_1:
    graph_state = st.radio(
    "Please Select the Graph State ",
    ('Static', 'Dynamic'))
    

with col_2:
    st.write("Select the Graph Type")
    graph_type_1 = st.checkbox('Line Graph')
    graph_type_2 = st.checkbox('Bubble Graph')
    df_jj = pd.read_csv("D:\codeverse\python\projects\gdp analysis\codes\gdp data sets\china\China.csv")
    
#loading the data 
def Load_Data():
    global box,options_country,options_data,box,box_data
   
    numeric_df = df_jj.select_dtypes(['float','int'])
    numeric_cols = numeric_df.columns
    
    text_df = df_jj.select_dtypes(["object"])
    text_cols = text_df.columns
    
    country_column = df_jj['Country']
    unique_country = country_column.unique()
    
    options_country = st.multiselect(
    'Select the countries',
    options=unique_country)
    
    options_data = []
    box_data = []
    
    for col in df_jj.columns:
        options_data.append(col)
    box = st.selectbox("select the data you want to compare ",options_data[2::])
    # if box:
    # box_data.append(box)
  
  


def Show_Data():
    
        
    for count in options_country:
        if box and count:
            box_data.append(count)
            
            if count and graph_state=='Static' and graph_type_1 == True:   
                fig = px.line(df_jj.loc[df_jj["Country"] == f"{count}"],x="Year",y=box,title=f"{box} of {count} over time 1991-2022", 
                              markers = True, height=550,width=800)
                # st.write(box_data)
                st.plotly_chart(fig)
                
            if count and graph_state=='Static' and graph_type_2 == True:
                fig = px.scatter(df_jj.loc[df_jj["Country"] == f"{count}"],x="Year",y=box,title=f"{box} of {count} over time 1991-2022", 
                               height=550,width=800)
                st.plotly_chart(fig)
               
            if graph_state=='Dynamic' and graph_type_1 == True:
                st.write(f"You selected {graph_state} and line graph with {count} and box is {box} ")
                fig = px.scatter(df_jj.loc[df_jj["Country"] == f"{count}"], x="Year", y=box, title=f"{box} of {count} over time 1991-2022",
                 animation_frame="Year",size=box,  log_x=True, range_x=[1991,2021], range_y=[0,100])

                st.plotly_chart(fig)
            #    if graph_state=='Dynamic' and graph_type_2 == True:
            #        st.write(f"You selected {graph_state} and bubble graph with {count} and box is {box}")
                   
                #    fig = px.line(df_jj,x="Year",y=box,title="Apple Share Prices over time (2014)")
                #    st.plotly_chart(fig)
                
# df_jj = pd.read_csv("D:\codeverse\python\projects\gdp analysis\codes\gdp data sets\china\China.csv")    

Load_Data()
Show_Data()


   

         
        
    
    
        

    
    
    
    
  
    










hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)




