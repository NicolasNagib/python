# Parte inicial do Flask
import random as rd
import string
from flask import Flask, redirect, request, jsonify
app = Flask(__name__)
    
def redirectUrl(url):
    return redirect(url, 301)



# Bd com sqlite

import sqlite3 as sql

conn = sql.connect("db_url_shortener.db")

cursor = conn.cursor() # Serve para executar as consultas, sem commitar ainda

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
