from .db import conectar

def criar_tabela():
    conn = conectar()
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
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO compromissos (data, hora, descricao)
    VALUES (?, ?, ?)
    ''', (data, hora, descricao))
    conn.commit()
    conn.close()


def listar_compromissos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM compromissos')
    compromissos = cursor.fetchall()
    conn.close()
    return compromissos


def atualizar_compromisso(id, nova_data, nova_hora, nova_descricao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE compromissos
    SET data = ?, hora = ?, descricao = ?
    WHERE id = ?
    ''', (nova_data, nova_hora, nova_descricao, id))
    conn.commit()
    conn.close()


def excluir_compromisso(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM compromissos WHERE id = ?', (id,))
    conn.commit()
    conn.close()
