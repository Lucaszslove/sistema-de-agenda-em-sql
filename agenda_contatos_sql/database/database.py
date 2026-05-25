import sqlite3


conexao = sqlite3.connect("database.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS dados_contato(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL UNIQUE
            )""")
conexao.commit()