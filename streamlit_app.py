
import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt

df=pd.read_csv('dati.csv',index_col=0)


st.title('Azienda 1 Dashboard')

st.bar_chart(data=df['Capitale a disposizione'])
st.bar_chart(data=df[['Materiale disponibile da circolarità','Investimenti in processi circolari']])

import plotly.graph_objects as go
import numpy as np

df["Color"] = np.where(df["Esternalità negative totali prodotte dall'azienda"].cumsum()<0, 'green', 'red')

# Plot
fig = go.Figure()
fig.add_trace(
    go.Bar(name='Esternalità negative',
           y=df["Esternalità negative totali prodotte dall'azienda"].cumsum(),
           marker_color=df['Color']))
fig.add_trace(go.Line(name='Vendite',y=df['Vendite'],marker_color='black'))
fig.update_layout(barmode='stack')
st.plotly_chart(fig, use_container_width=True)


st.title('KPI')
st.bar_chart(data=df['Brand reputation.1'])
st.bar_chart(data=df['Importo finale / Importo iniziale'])
st.bar_chart(data=df['Obiettivi raggiunti'])

