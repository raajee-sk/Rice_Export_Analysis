#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
# ============================================       /     STREAMLIT DASHBOARD      /       ================================================= #
# Comfiguring Streamlit GUI 
st.set_page_config(layout='wide')

# Title
st.header(':violet[Rice Exports Data Analysis ]')
st.write(':green[**(Note)**:-This data between 2019 to 2022 ]')

# Selection option
option = st.radio(':violet[**Select your option**]',('Analysis', 'Explore'),horizontal=True)
df=pd.read_csv(r"C:\Users\SKAN\Desktop\Raajee\rice_export\rice_export_analysis.csv")
if option == 'Analysis':
    tab1,tab2,tab3,tab4,tab5=st.tabs(["Importer/Exporter Overview","Geographical Analysis","Product Analysis",'Financial Analysis','Time-Series Analysis'])
    with tab1:
        col1,col2=st.columns(2)
        with col1:
          st.markdown(
    f"<h1 style='color:#ff6666; font-size: 20px;'>Top  Exporters based on the quantity of rice exported</h1>",
    unsafe_allow_html=True,)
          exporters=df.groupby("EXPORTER NAME")["QUANTITY"].sum().reset_index().sort_values(by="QUANTITY",ascending=False).head(10)
          st.dataframe(exporters )
        with col2:  
          fig = px.bar(data_frame=exporters,
                      x='EXPORTER NAME',
                     y='QUANTITY',
                     color='EXPORTER NAME',
                     title='Top 10 Exporters of Rice'
                    )
          st.plotly_chart(fig,use_container_width=True)

        col1,col2=st.columns(2)
        with col1:
          st.markdown(
    f"<h1 style='color:#ff6666; font-size: 20px;'>Top  Importers based on the quantity of rice imported</h1>",
    unsafe_allow_html=True,)
          exporters=df.groupby("IMPORTER NAME")["QUANTITY"].sum().reset_index().sort_values(by="QUANTITY",ascending=False).head(10)
          st.dataframe(exporters )
        with col2:  
          fig = px.bar(data_frame=exporters,
                      x='IMPORTER NAME',
                     y='QUANTITY',
                     color='IMPORTER NAME',
                     title='Top 10 Importers of Rice'
                    )
          st.plotly_chart(fig,use_container_width=True)
        col1,col2=st.columns(2)
        with col1:
          st.markdown(
    f"<h1 style='color:#ff6666; font-size: 20px;'>Top  Exporters based on the IMPORT VALUE FOB of rice exported</h1>",
    unsafe_allow_html=True,)
          exporters=df.groupby("EXPORTER NAME")["IMPORT VALUE FOB"].sum().reset_index().sort_values(by="IMPORT VALUE FOB",ascending=False).head(10)
          st.dataframe(exporters )
        with col2:  
          fig = px.bar(data_frame=exporters,
                      x='EXPORTER NAME',
                     y='IMPORT VALUE FOB',
                     color='EXPORTER NAME',
                     title='Top 10 Exporters of Rice'
                    )
          st.plotly_chart(fig,use_container_width=True)
        col1,col2=st.columns(2)
        with col1:
          st.markdown(
    f"<h1 style='color:#ff6666; font-size: 20px;'>Top  Importers based on the IMPORT VALUE FOB of rice imported</h1>",
    unsafe_allow_html=True,)
          exporters=df.groupby("IMPORTER NAME")["IMPORT VALUE FOB"].sum().reset_index().sort_values(by="IMPORT VALUE FOB",ascending=False).head(10)
          st.dataframe(exporters )
        with col2:  
          fig = px.bar(data_frame=exporters,
                      x='IMPORTER NAME',
                     y='IMPORT VALUE FOB',
                     color='IMPORTER NAME',
                     title='Top 10 Importers of Rice'
                    )
          st.plotly_chart(fig,use_container_width=True) 
        with tab2:
           fig = px.choropleth(df, locations="IMPORTER NAME", locationmode="country names",
                    color="IMPORT VALUE FOB", color_continuous_scale="RdYlGn",
                    labels={"Net Export": "Net Export Value (in million USD)"},
                    title="Rice Trade Map(IMPORT VALUE FOB)")
           st.plotly_chart(fig,use_container_width=True) 
           fig1 = px.choropleth(df, locations="IMPORTER NAME", locationmode="country names",
                    color="QUANTITY", color_continuous_scale="RdYlGn",
                    labels={"Net Export": "Net Export Value (in million USD)"},
                    title="Rice Trade Map(QUANTITY)")
           st.plotly_chart(fig1,use_container_width=True)
        with tab3:
          
            st.markdown(f"<h1 style='color:#ff6666; font-size: 20px;'>Top 5 rice varieties by Quantity</h1>",
                unsafe_allow_html=True,)
            df5=df.groupby("HS CODE DESCRIPTION")["QUANTITY"].sum().reset_index().sort_values(by="QUANTITY",ascending=False).head(5)
            df5
          
            fig2 = px.bar(data_frame=df5,
                     x='HS CODE DESCRIPTION',
                     y='QUANTITY',
                     color='HS CODE DESCRIPTION',
                     title='Top 5 rice varieties by Quantity'
                    )
            st.plotly_chart(fig2,use_container_width=True) 
           
                      
            st.markdown(f"<h1 style='color:#ff6666; font-size: 20px;'>Top 5 rice varieties by Import Value of FOB</h1>",
                unsafe_allow_html=True,)
            df6=df.groupby("HS CODE DESCRIPTION")["IMPORT VALUE FOB"].sum().reset_index().sort_values(by="IMPORT VALUE FOB",ascending=False).head(5)
            df6
          
            fig3 = px.bar(data_frame=df6,
                     x='HS CODE DESCRIPTION',
                     y='IMPORT VALUE FOB',
                     color='HS CODE DESCRIPTION',
                     title='Top 5 rice varieties by Import Value of FOB'
                    )
            st.plotly_chart(fig3,use_container_width=True) 
        with tab4:
         col1,col2=st.columns(2)
         with col1:
            total_trade_volume = df["QUANTITY"].sum()
            st.markdown(f"<h1 style='color:#ff6666; font-size: 24px;'>Total Trade Volume</h1>",
                unsafe_allow_html=True,)
            st.write(total_trade_volume)
         with col2: 
           st.markdown(f"<h1 style='color:#ff6666; font-size: 24px;'>The summary of IMPORT VALUE FOB</h1>",
                unsafe_allow_html=True,)
           des=df["IMPORT VALUE FOB"].describe()
           st.write(des)
         st.markdown(f"<h1 style='color:#ff6666; font-size: 24px;'>The Import Value of Currency</h1>",
                unsafe_allow_html=True,)  
         df1 =df[["CURRENCY","IMPORT VALUE FOB"]]
         st.line_chart(df1,x="CURRENCY",y="IMPORT VALUE FOB")

        with tab5:
          
          st.markdown(f"<h1 style='color:#ff6666; font-size: 24px;'>Import Values by Year</h1>",
                unsafe_allow_html=True,) 
          df=pd.read_csv(r"C:\Users\SKAN\Desktop\Raajee\rice_export\rice_export_analysis.csv")
          df["ARRIVAL DATE"] = pd.to_datetime(df["ARRIVAL DATE"])
          df.set_index('ARRIVAL DATE',inplace=True)
          df_year = df.resample("Y")["IMPORT VALUE FOB"].sum().reset_index() 
          st.line_chart(df_year,x="ARRIVAL DATE",y="IMPORT VALUE FOB")

          st.markdown(f"<h1 style='color:#ff6666; font-size: 24px;'>Import Values by Quarter</h1>",
                unsafe_allow_html=True,) 
          df_Quarter = df.resample("Q")["IMPORT VALUE FOB"].sum().reset_index() 
          st.line_chart(df_Quarter,x="ARRIVAL DATE",y="IMPORT VALUE FOB")

          st.markdown(f"<h1 style='color:#ff6666; font-size: 24px;'>Import Values by Month</h1>",
                unsafe_allow_html=True,) 
          df_month = df.resample("m")["IMPORT VALUE FOB"].sum().reset_index() 
          st.line_chart(df_month,x="ARRIVAL DATE",y="IMPORT VALUE FOB")

if option=='Explore':
  tab1,tab2,tab3=st.tabs(["Importer_Name","Exporter_Name","Year"])    
  with tab1:
    importer_name = st.selectbox('Select a Importer Name:',df["IMPORTER NAME"].astype(str).unique())
    button=st.button("Search")
    if button:
        st.markdown(f"<h1 style='color:#ff6666; font-size: 24px;'>Importer Name Vs Import value FOB Vs Year</h1>",
                unsafe_allow_html=True,)  
        df=pd.read_csv(r"C:\Users\SKAN\Desktop\Raajee\rice_export\rice_export_analysis.csv")
            
        filtered_data = df[df["IMPORTER NAME"] == importer_name]
        grouped_data = filtered_data.groupby(["IMPORTER NAME", "YEAR"])["IMPORT VALUE FOB"].sum().reset_index()
        st.dataframe(grouped_data)
        st.line_chart(grouped_data,x="YEAR",y="IMPORT VALUE FOB")

        st.markdown(f"<h1 style='color:#ff6666; font-size: 24px;'>Importer Name Vs Product Vs Year</h1>",
                unsafe_allow_html=True,)  
        grouped_data1 = filtered_data.groupby(["IMPORTER NAME", "HS CODE DESCRIPTION",'YEAR'])["QUANTITY"].sum().reset_index()
        st.dataframe(grouped_data1)
        fig = px.bar(data_frame= grouped_data1 ,
                      x='YEAR',
                     y='QUANTITY',
                     color='HS CODE DESCRIPTION',
                     title='Importer Name Vs Product Vs Year'
                    )
        st.plotly_chart(fig,use_container_width=True)
       

        
  with tab2:
    exporter_name = st.selectbox('Select a Exporter Name:',df["EXPORTER NAME"].astype(str).unique())
    button1=st.button("search")
    if button1:
        st.markdown(f"<h1 style='color:#ff6666; font-size: 24px;'>Exporter Name Vs Import value FOB Vs Year</h1>",
                unsafe_allow_html=True,)  
        df=pd.read_csv(r"C:\Users\SKAN\Desktop\Raajee\rice_export\rice_export_analysis.csv")            
        filtered_data = df[df["EXPORTER NAME"] == exporter_name]
        grouped_data = filtered_data.groupby(["EXPORTER NAME", "YEAR"])["IMPORT VALUE FOB"].sum().reset_index()
        st.dataframe(grouped_data)
        st.line_chart(grouped_data,x="YEAR",y="IMPORT VALUE FOB")

        st.markdown(f"<h1 style='color:#ff6666; font-size: 24px;'>Exporter Name Vs Product Vs Year</h1>",
                unsafe_allow_html=True,)  
        grouped_data1 = filtered_data.groupby(["EXPORTER NAME", "HS CODE DESCRIPTION",'YEAR'])["QUANTITY"].sum().reset_index()
        st.dataframe(grouped_data1)
        fig = px.bar(data_frame= grouped_data1 ,
                      x='YEAR',
                     y='QUANTITY',
                     color='HS CODE DESCRIPTION',
                     title='Exporter Name Vs Product Vs Year'
                    )
        st.plotly_chart(fig,use_container_width=True)
           


  with tab3:
    year = st.selectbox('Select Year:',df["YEAR"].astype(str).unique())
    
    button2=st.button("Enter")
    if button2:
        df=pd.read_csv(r"C:\Users\SKAN\Desktop\Raajee\rice_export\rice_export_analysis.csv")  
        filtered_data = df[df["ARRIVAL DATE"].str.contains(str(year))]

        st.markdown(f"<h1 style='color:#ff6666; font-size: 24px;'>Top 10 Importers</h1>",
                unsafe_allow_html=True,) 
        grouped_data = filtered_data.groupby(["IMPORTER NAME","YEAR","HS CODE DESCRIPTION"])["IMPORT VALUE FOB"].sum().reset_index().sort_values(by="IMPORT VALUE FOB",ascending=False).head(10)
        st.dataframe(grouped_data)
        fig = px.bar(data_frame= grouped_data ,
                      x='IMPORTER NAME',
                     y='IMPORT VALUE FOB',
                     color='HS CODE DESCRIPTION',
                     title='Top 10 Importers'
                    )
        st.plotly_chart(fig,use_container_width=True)
        st.markdown(f"<h1 style='color:#ff6666; font-size: 24px;'>Top 10 Exporters</h1>",
                unsafe_allow_html=True,) 
        grouped_data = filtered_data.groupby(["EXPORTER NAME","YEAR","HS CODE DESCRIPTION"])["IMPORT VALUE FOB"].sum().reset_index().sort_values(by="IMPORT VALUE FOB",ascending=False).head(10)
        st.dataframe(grouped_data)
        fig = px.bar(data_frame= grouped_data ,
                      x='EXPORTER NAME',
                     y='IMPORT VALUE FOB',
                     color='HS CODE DESCRIPTION',
                     title='Top 10 Exporters'
                    )
        st.plotly_chart(fig,use_container_width=True)


               

        

