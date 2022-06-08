import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Benvenuto nel sito del CDA della Azienda 1 👋")

st.sidebar.success("Select a page above.")

st.markdown(
    """
    Questo sito raccoglie i dati dei vari cruscotti del business game per il 
    #Master Strategia e Gestione della Sostenibilità Aziendale della 24Ore Business School
    
    (Usa la barra a sinistra per navigare nel contenuto)
    (se la barra non è visibile attivala cliccando su ">" in alto a sinistra)
"""
)
