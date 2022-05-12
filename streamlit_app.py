
import streamlit as st
import pandas as pd
import altair as alt

df=pd.read_csv('dati.csv',index_col=0)

fig=alt.Chart(df['Capitale a disposizione']).mark_bar().encode()
st.altair_chart(fig, use_container_width=True)
col1, col2 = st.columns([3,2])

with col1:
  st.title('Azienda 1 Dashboard')
  st.bar_chart(data=df['Capitale a disposizione'])
  st.bar_chart(data=df[['Materiale disponibile da circolarità','Investimenti in processi circolari']])

with col2:
  st.title('KPI')
  st.bar_chart(data=df['Brand reputation.1'])
  st.bar_chart(data=df['Importo finale / Importo iniziale'])
  st.bar_chart(data=df['Obiettivi raggiunti'])

    










