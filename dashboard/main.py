import streamlit as st
import pandas as pd
import sqlite3
from datetime import date
from paginas.adicionar_registro import adicionar_registro
from paginas.dashboard import dashboard
from paginas.gerenciar_registros import gerenciar_registros




st.markdown("""
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="Content-Language" content="pt-BR">
    </head>
    </html>
""", unsafe_allow_html=True)


# ---------------- BANCO DE DADOS ----------------
conn = sqlite3.connect("banco.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS registros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tipo TEXT,
    fonte TEXT,
    valor REAL,
    data DATE
)
""")
conn.commit()



# ---------------- INTERFACE ----------------
st.set_page_config("Finanças Familiar", layout="wide")
st.title(" Controle Financeiro Familiar")

menu = st.sidebar.radio("Menu", ["Dashboard", "Adicionar Registro", "Gerenciar Registros"])


# ---------------- ADICIONAR REGISTROS ----------------
if menu == "Adicionar Registro":
    adicionar_registro()

# ---------------- DASHBOARD ----------------
elif menu == "Dashboard":
    dashboard()

elif menu == "Gerenciar Registros":
    gerenciar_registros()