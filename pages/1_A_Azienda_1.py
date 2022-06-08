
import streamlit as st
import pandas as pd
import altair as alt


df=pd.read_excel('/app/corso/dati.xlsx',sheet_name='data')

df=df.drop(df[df['Capitale a disposizione']==' '].index)

df.to_csv('/app/corso/dati.csv',index=False)
##########################################
data=pd.read_csv('/app/corso/dati.csv')

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

st.set_page_config(page_title="Plotting Demo", page_icon="📈")

st.title('Master Strategia e Gestione della Sostenibilità Aziendale')
st.header('Cruscotto Business Game')

st.sidebar.success("Select a demo above.")

with st.container():
  st.header('Azienda 1')
  st.subheader('Dashboard KPI Aziendali')
  st.altair_chart(chart1, use_container_width=True)
  st.altair_chart(importo, use_container_width=True)
  st.altair_chart(brand, use_container_width=True)
  st.altair_chart(obiettivi, use_container_width=True)

    
st.button("Re-run")
