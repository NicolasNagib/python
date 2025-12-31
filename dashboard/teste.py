import sqlite3

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS registros")

conn.commit()
conn.close()
print("Tabela 'registros' excluída com sucesso!")