import re
import pandas as pd
import sqlite3

conn = sqlite3.connect("banco.db", check_same_thread=False)
cursor = conn.cursor()

def converter_valor(valor):
    if not valor:
        return 0.0
    valor = re.sub(r"[^\d,]", "", valor)
    valor = valor.replace(".", "").replace(",", ".")
    return float(valor)

def inserir_registro(tipo, fonte, valor, data):
    cursor.execute("""
        INSERT INTO registros (tipo, fonte, valor, data)
        VALUES (?, ?, ?, ?)
    """, (tipo, fonte, valor, data))
    conn.commit()

def carregar_dados():
    return pd.read_sql("SELECT * FROM registros", conn, parse_dates=["data"])

def calcular_saldo():
    df = carregar_dados()

    receitas = df[df["tipo"] == "Receita"]["valor"].sum()
    despesas = df[df["tipo"] == "Despesa"]["valor"].sum()
    investimentos = df[df["tipo"] == "Investimento"]["valor"].sum()

    return receitas - despesas - investimentos
