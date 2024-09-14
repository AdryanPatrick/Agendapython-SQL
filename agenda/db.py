import sqlite3

def conectar():
    """Conecta ao banco de dados e retorna o objeto de conexão."""
    try:
        conn = sqlite3.connect('agenda.db')  # Gera o arquivo agenda.db
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
