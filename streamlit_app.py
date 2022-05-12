
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('dati.csv',index_col=0)


st.title('Azienda 1 Dashboard')

st.bar_chart(data=df['Capitale a disposizione'])
st.bar_chart(data=df[['Materiale disponibile da circolarità','Investimenti in processi circolari']])


x=df["Esternalità negative totali prodotte dall'azienda"].index
y=df["Esternalità negative totali prodotte dall'azienda"].cumsum().values
y2=df["Vendite"].cumsum().values
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax2.plot(x, y2, color='k')
ax2.set_ylabel('Vendite', color='k')
color = ['g' if i<0 else 'r' for i in y]
ax1.bar(x, y, color=color)
ax1.set_ylabel('Esternalità negative', color='k')

st.pyplot(fig)


st.title('KPI')
st.bar_chart(data=df['Brand reputation.1'])
st.bar_chart(data=df['Importo finale / Importo iniziale'])
st.bar_chart(data=df['Obiettivi raggiunti'])

