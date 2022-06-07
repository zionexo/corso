
import streamlit as st
import pandas as pd
import altair as alt


data=pd.read_csv('dati.csv')

data['capitale totale']=data['Capitale a disposizione']+data['Disponibilità di magazzino']*3

turno=alt.Chart(data).mark_line().encode(x='turno:O')
capitale=turno.encode(y='Capitale a disposizione')
magazzino=turno.encode(y='Disponibilità di magazzino')
tot=turno.encode(y='capitale totale')

chart=alt.layer(
    capitale.mark_line(point=alt.OverlayMarkDef(filled=False)),
    magazzino.mark_line(color='green',point=alt.OverlayMarkDef(color='green',filled=False)),
    tot.mark_line(strokeDash=[1,1],color='red',point=alt.OverlayMarkDef(color='red',filled=False))
)
chart0=chart.encode(y=alt.Y(title='Capitale')).configure(background='transparent')


importo=turno.encode(y='Importo finale / Importo iniziale')
brand=turno.encode(y='Brand reputation')
obiettivi=turno.encode(y='Obiettivi raggiunti')

chart1=alt.hconcat(importo,brand,obiettivi).configure(background='transparent')

#conf=pd.read_excel('dati.xlsx',sheet_name='conf',header=1)
conf=pd.read_csv('conf.csv')
conf['Est_Neg_/_Vendite totali']=conf['Est_Neg_/_Vendite totali']*100
conf['RSI_/_importo finale']=conf['RSI_/_importo finale']*100

conf_turno=alt.Chart(conf).mark_line(point=True).encode(x='turno',color='Indicatori aziendali')
conf_impo=conf_turno.encode(y=alt.Y('Importo finale_/_Importo iniziale',title='Importo finale / Importo iniziale'))
conf_bran=conf_turno.encode(y='Brand reputation')
conf_obiet=conf_turno.encode(y='Obiettivi raggiunti')

conf_est=conf_turno.encode(y='Est_Neg_/_Vendite totali')

conf_rsi=conf_turno.encode(y='RSI_/_importo finale')


col1, col2 = st.columns(2)

with col1:
  st.title('Azienda 1 Dashboard')
  st.altair_chart(chart1, use_container_width=True)
  st.altair_chart(chart0, use_container_width=True)
  

with col2:
  st.title('KPI')
  st.altair_chart(conf_impo, use_container_width=True)
  st.altair_chart(conf_bran, use_container_width=True)

    










