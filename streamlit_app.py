
import streamlit as st
import pandas as pd
import altair as alt

df=pd.read_csv('dati.csv')
st.dataframe(df)
fig1=alt.Chart(df).mark_line().encode(x='turno',y='Capitale a disposizione')

fig2=alt.Chart(df).mark_line().encode(
  x='turno',
  y=['Materiale disponibile da circolarità','Investimenti in processi circolari']
)



col1, col2 = st.columns(2)

with col1:
  st.title('Azienda 1 Dashboard')
  st.altair_chart(fig1, use_container_width=True)
  st.bar_chart(data=df[['Materiale disponibile da circolarità','Investimenti in processi circolari']])

with col2:
  st.title('KPI')
  st.bar_chart(data=df['Brand reputation.1'])
  st.bar_chart(data=df['Importo finale / Importo iniziale'])
  st.bar_chart(data=df['Obiettivi raggiunti'])

    










