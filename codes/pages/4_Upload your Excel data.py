
from unicodedata import name
from datetime import *
import streamlit as st
import pandas as pd 
import plotly.express as px
import base64  # Standard Python Module
from io import StringIO, BytesIO  # Standard Python Module
import plotly.graph_objects as go
from pandas_profiling import ProfileReport 


st.set_option('deprecation.showfileUploaderEncoding', False)

# global dataframe
st.set_page_config(page_title="GDP Analysis | Analyse your data",page_icon="💰")

st.title("Upload your excel data")
st.header("Visualization settings")

global uploaded_file
uploaded_file = st.file_uploader(label="Upload your Excel file", type = ['csv','xlsx'])

if uploaded_file is not None:
  
    try:
        dataframe = pd.read_csv(uploaded_file) 
        
    except:
        dataframe = pd.read_excel(uploaded_file)
    finally:
        # st.warning("hello")
        st.write(dataframe)

#representation of graphs 
        st.header("Graphical Representation")
        
        #extracting the data 
        numeric_dataframe = dataframe.select_dtypes(['float','int'])
        numeric_cols = numeric_dataframe.columns
           
        text_dataframe = dataframe.select_dtypes(["object"])
        text_cols = text_dataframe.columns
        
        
        
        # getting the country column
        count_box = []
        for count in dataframe.columns:
            count_box.append(count)
        country_box = st.selectbox("Select the country column ",count_box)
        
        country = country_box
        country_column = dataframe[country]
        # st.write(country_column)
        unique_country = country_column.unique().tolist()
        # st.write(unique_country)
          
         
        
        #getting the year column
        year_box = []
        for year in dataframe.columns:
            year_box.append(year)
        y_box = st.selectbox("select the year column",year_box)
        
        st.write(y_box)
        
        
        total_year = []
        for year_list in dataframe[y_box].unique():
            total_year.append(year_list)
        st.write(type(total_year))
        
        
        
   
            
                
        
        #defining country selector
        options_country = st.multiselect(
            'Select the countries',
            options=unique_country)
        
        # defining the data selector
        options_data = []
        box_data = []
            
        for col in dataframe.columns:
            options_data.append(col)
        box = st.selectbox("select the data you want to compare ",options_data[2::])
        
        
        # list_data = ["None","Maximum","Minimum"]
        # analysis_type = st.selectbox("Select the analysis type ",list_data)
        st.write("Select the Graph Type")
        graph_type_1 = st.checkbox('Line Graph')
        
        
        fig = go.Figure()
        
        dataframes = {i: dataframe[dataframe[country] == i] for i in options_country} 
        # st.write(datafrs)
        
        if count and graph_type_1 and graph_type_1 == True:
                
            for i, dataframe in dataframes.items():
                figure = fig.add_trace(go.Scatter(x=dataframe[y_box], y=dataframe[box], name=i)) 
                # layout = dict(title = 'Multiple text labels')
                
                figure.update_traces(textposition='top center')
                
                figure.update_layout(
                    height=500,width=800,
                    title_text=f"{box}  over time {dataframe[y_box].iat[0]} to {dataframe[y_box].iat[-1]}",
                    xaxis = dict(title = y_box),yaxis = dict(title = box)
                    )
                
                figure.update_traces(marker=dict(size=12,
                              line=dict(width=2,
                                        color='DarkSlateGrey')),
                  selector=dict(mode='markers'))
            st.plotly_chart(figure)
    
    
    # data_analyse = st.selectbox

    
    # if analysis_type == "Maximum":
    #     st.write("hello maximum ")
         
                




                        
 
    
    def generate_html_download_link(dataframe):
        # Credit Plotly: https://discuss.streamlit.io/t/download-plotly-plot-as-html/4426/2
        profile = ProfileReport(dataframe)
        href = profile.to_file(output_file = "report.html")
        return st.markdown(href, unsafe_allow_html=True)
    
    # -- DOWNLOAD SECTION
    st.subheader('Downloads:')
    
    button = st.button("Download the report")
    if button:
             generate_html_download_link(dataframe)


               
        
























hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)




# st.set_page_config(page_title="GDP Analysis || Predictions")