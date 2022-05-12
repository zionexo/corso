
import streamlit as st
import pandas as pd
import altair as alt

df=pd.read_csv('dati.csv',index_col=0)

st.title('Azienda 1 Dashboard')

col1, col2, col3 = st.columns(3)

with col1:
  st.bar_chart(data=df['Capitale a disposizione'])
  st.bar_chart(data=df[['Materiale disponibile da circolarità','Investimenti in processi circolari']])

with col2:
  st.title('KPI')
  st.bar_chart(data=df['Brand reputation.1'])
  st.bar_chart(data=df['Importo finale / Importo iniziale'])
  st.bar_chart(data=df['Obiettivi raggiunti'])

with col3:
  st.header("An owl")
  st.image("https://static.streamlit.io/examples/owl.jpg")
    










