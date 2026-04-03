# Parte inicial do Flask
import random as rd
import sqlite3 as sql
import string
from flask import Flask, redirect, request, jsonify
app = Flask(__name__)
    
def redirectUrl(url):
    return redirect(url, 301)

conn = sql.connect("db_url_shortener.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS urls(
        url       TEXT,
        alias TEXT UNIQUE
    )               
''')

conn.close()

# Rotas
@app.route("/<alias>")
def dinamicRoutes(alias):
    conn = sql.connect("db_url_shortener.db")
    cursor = conn.cursor()
    
    url = cursor.execute(f"SELECT url FROM urls WHERE alias = '{alias}'").fetchone()
    print(url, alias)
    
    conn.close()
    if url != None:
        return redirect(url[0], 301)
    else:
        return "404"

@app.route("/forms", methods=['POST'])
def formsValues():
    
    conn = sql.connect("db_url_shortener.db")
    cursor = conn.cursor()
        
    data = request.json
    url = data.get('url')
    alias = data.get('alias')
    
    verifyAlias = cursor.execute(f"SELECT alias FROM urls WHERE url = '{url}'").fetchone()
    if url[:8] != "https://" and url[:7] != "http://":
        url = "https://" + url
    
    if verifyAlias == None:
        randomValue = string.ascii_letters + string.digits
        if alias == '':
            alias = ''.join(rd.choice(randomValue) for i in range(1,8))
        
        query = '''
                    INSERT INTO urls (url, alias) 
                    VALUES (?,?);
                    '''
        data = url, alias
        cursor.execute(query, data)
        conn.commit()
        conn.close()
        
        return jsonify({"status_code": "200", "url":url, "alias":alias})
    else:
        alias = verifyAlias[0]
        return jsonify({"status_code": "208", "url":url, "alias":alias}), 208
    
    
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