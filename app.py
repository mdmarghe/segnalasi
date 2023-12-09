import streamlit as st

st.set_page_config(page_title="Segnalasi", 
                page_icon="✊", 
                layout="wide")
st.header("segnalasi")
col1,col2=st.columns(2)
with col1:
    inputName=st.text_input("nome*")
with col2:
    inputSurname=st.text_input("cognome*" )


if inputSurname is None or (inputName is None):
    st.warning("Necessari entrambi i campi")
else:
    st.write("o")



