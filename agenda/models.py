from .db import conectar

def criar_tabela():
    conn = conectar()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS compromissos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL,
            hora TEXT NOT NULL,
            descricao TEXT
        )
        ''')
        conn.commit()
        conn.close()

def adicionar_compromisso(data, hora, descricao):
    conn = conectar()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO compromissos (data, hora, descricao) VALUES (?, ?, ?)
        ''', (data, hora, descricao))
        conn.commit()
        conn.close()

def listar_compromissos():
    conn = conectar()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM compromissos')
        compromissos = cursor.fetchall()
        conn.close()
        return compromissos

def apagar_compromisso(id_compromisso):
    conn = conectar()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM compromissos WHERE id = ?', (id_compromisso,))
        conn.commit()
        conn.close()
