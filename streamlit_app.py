

import streamlit as st
import pandas as pd
import altair as alt


df=pd.read_excel('dati.xlsx',sheet_name='data')

df=df.drop(df[df['Capitale a disposizione']==' '].index)

df.to_csv('dati.csv',index=False)

conf=pd.read_excel('dati.xlsx',sheet_name='conf',header=1)
##########################################
data=pd.read_csv('dati.csv')

data['capitale totale']=data['Capitale a disposizione']+data['Disponibilità di magazzino']*3

turno=alt.Chart(data).mark_line().encode(x='turno')
capitale=turno.encode(y=alt.Y('Capitale a disposizione', axis=alt.Axis(title='Capitale',titleColor='blue')))
magazzino=turno.encode(y=alt.Y('Disponibilità di magazzino', axis=alt.Axis(title='Capitale Magazzino',titleColor='green')))
tot=turno.encode(y='capitale totale')

chart=alt.layer(
    capitale.mark_line(point=alt.OverlayMarkDef(filled=False)),
    magazzino.mark_line(color='green',point=alt.OverlayMarkDef(color='green',filled=False)
                       ),
    #tot.mark_line(strokeDash=[1,1],color='red',point=alt.OverlayMarkDef(color='red',filled=False))
).resolve_scale(
    y = 'independent'
)

chart0=chart.configure(background='transparent')


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

conf_est=conf_turno.encode(y=alt.Y('Est_Neg_/_Vendite totali', title='Est.Neg./Vendite totali'))

conf_rsi=conf_turno.encode(y='RSI_/_importo finale')

st.title('Master Strategia e Gestione della Sostenibilità Aziendale')
st.header('Cruscotto Business Game')

st.sidebar.success("Select a demo above.")

with st.container():
  st.header('Azienda 1')
  st.subheader('Dashboard KPI Aziendali')
  st.altair_chart(chart1, use_container_width=True)
  st.altair_chart(chart0, use_container_width=True)
  

with st.container():
  st.subheader('KPI Confronto con altre aziende')
  st.altair_chart(conf_impo, use_container_width=True)
  st.altair_chart(conf_bran, use_container_width=True)
  st.altair_chart(conf_est, use_container_width=True)
