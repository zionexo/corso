
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
