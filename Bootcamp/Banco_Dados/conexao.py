import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent

conexao = sqlite3.connect(ROOT_PATH / 'Banco_Dados' / 'banco_dados.db')
cursor = conexao.cursor()

cursor.execute('CRIATE ')
