

import streamlit as st
import pandas as pd
import altair as alt


conf=pd.read_excel('dati.xlsx',sheet_name='conf',header=1)
##########################################

conf=pd.read_csv('conf.csv')
conf['Est_Neg_/_Vendite totali']=conf['Est_Neg_/_Vendite totali']*100
conf['RSI_/_importo finale']=conf['RSI_/_importo finale']*100

conf_turno=alt.Chart(conf).mark_line(point=True).encode(x='turno',color='Indicatori aziendali')
conf_impo=conf_turno.encode(y=alt.Y('Importo finale_/_Importo iniziale',title='Importo finale / Importo iniziale'))
conf_bran=conf_turno.encode(y='Brand reputation')
conf_obiet=conf_turno.encode(y='Obiettivi raggiunti')

conf_est=conf_turno.encode(y=alt.Y('Est_Neg_/_Vendite totali', title='Est.Neg./Vendite totali'))

conf_rsi=conf_turno.encode(y='RSI_/_importo finale')


st.set_page_config(page_title="Competitors", page_icon="🌍")

st.title('Master Strategia e Gestione della Sostenibilità Aziendale')
st.header('Cruscotto Business Game')


with st.container():
  st.subheader('KPI Confronto con altre aziende')
  st.altair_chart(conf_impo, use_container_width=True)
  st.altair_chart(conf_bran, use_container_width=True)
  st.altair_chart(conf_est, use_container_width=True)