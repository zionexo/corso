
import streamlit as st
import pandas as pd
import altair as alt

df=pd.read_csv('dati.csv')
st.dataframe(df.columns)
fig1=alt.Chart(df).mark_line().encode(x=alt.X('turno:O',label=alt.Lablel(labelAngle=90)),
                                      y=alt.Y('Capitale a disposizione'),
                                     
                                     )

fig2=alt.Chart(df).mark_line().encode(
  alt.Column('Vendite'), alt.X('turno'),
    alt.Y("Esternalità negative totali prodotte dall\'azienda", axis=alt.Axis(grid=False))
)



col1, col2 = st.columns(2)

with col1:
  st.title('Azienda 1 Dashboard')
  st.altair_chart(fig1, use_container_width=True)
  st.altair_chart(fig2, use_container_width=True)
  

with col2:
  st.title('KPI')
  st.bar_chart(data=df['Brand reputation.1'])
  st.bar_chart(data=df['Importo finale / Importo iniziale'])
  st.bar_chart(data=df['Obiettivi raggiunti'])

    










