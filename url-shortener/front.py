import streamlit as st
import requests

st.header("Encurtador de URL")
with st.form("Encurtador de URL"):
    url = st.text_input("Insira sua URL")
    alias = st.text_input("alias(opcional)")
    submit_button = st.form_submit_button("Encurtar URL")
if submit_button:
    jsonForms = {'url':url, 'alias':alias}
    response = requests.post('http://127.0.0.1:5000/forms', json=jsonForms)
    aliasResponse = response.json()['alias']
    
    if response.status_code == 200:
        st.write(f"Seu URL encurtado:")
        st.code(f"127.0.0.1:5000/{aliasResponse}")
    elif response.status_code == 208:
        with st.container(border=True):
            st.write("URL encurtada já existente! Sem modificações no link")
            st.code(f"127.0.0.1:5000/{aliasResponse}")
    else:
        print("Erro no servidor:", response.status_code)