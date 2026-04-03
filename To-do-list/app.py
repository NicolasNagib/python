import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
    

conn = sqlite3.connect("db_toDoList.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS itemsList(
        title TEXT,
        completed BOOL,
        create_date DATE DEFAULT (date('now'))
    );
               """)
conn.close()


@app.route("/", methods=['POST'])
def insertItems():
    conn = sqlite3.connect("db_toDoList.db")
    cursor = conn.cursor()
    
    data = request.json
    title = data.get("title")
    query = cursor.execute(f"SELECT ROWID FROM itemsList WHERE title = '{title}'").fetchall()
    if query != []:
            return jsonify({"status_code":208}), 208            
    elif query == []:
        query = """
            INSERT INTO itemsList(title, completed)
            VALUES(?,?)
                """
        dataQuery = title, False
        cursor.execute(query, dataQuery)
        conn.commit()
        
        conn.close()
        return jsonify({"status_code":200})
    else: 
        return jsonify({"status_code":400}), 400

@app.route("/addRepeatItem", methods=['POST'])
def addRepeatItem():
    conn = sqlite3.connect("db_toDoList.db")
    cursor = conn.cursor()
    
    data = request.json
    title = data.get("title")
    addItem = data.get("addItem")
    
    if addItem == False:
        conn.close()
        return jsonify({"status_code": 409}), 409
    else:
        query = """
            INSERT INTO itemsList(title, completed)
            VALUES(?,?)
                """
        dataQuery = title, False
        cursor.execute(query, dataQuery)
        conn.commit()
        
        conn.close()
        return jsonify({"status_code":200})

@app.route("/loadItems", methods=['GET'])
def loadItems():
    conn = sqlite3.connect("db_toDoList.db")
    cursor = conn.cursor()
    
    query = cursor.execute("SELECT title, ROWID, completed FROM itemsList").fetchall()
    if query != []:
        return jsonify({"items":query})
    else:
        return jsonify({'items': []}), 404



@app.route("/completeTask/<id>", methods=['PATCH'])
def completeTask(id):
    conn = sqlite3.connect("db_toDoList.db")
    cursor = conn.cursor()
    
    data = request.json
    complete = data.get("complete")
    
    if complete == 1:
        complete = 0
    else:
        complete = 1
    
    query = cursor.execute(f"UPDATE itemsList SET completed = {complete} WHERE ROWID = {id}").fetchall()
    conn.commit()
    conn.close()
    if query != []:
        return jsonify({"items":query})
    else:
        return jsonify({'items': []}), 404
    
@app.route("/deleteTask/<id>", methods=["PUT"])
def deleteTask(id):
    conn = sqlite3.connect("db_toDoList.db")
    cursor = conn.cursor()
    
    query = cursor.execute(f"DELETE FROM itemsList WHERE ROWID = {id}")
    conn.commit()
    conn.close()
    return jsonify({}), 200
    