import sqlite3

# Banco de dados !
class Dados:
    """Criação do banco de dados e tabela"""
    def __init__(self,banco='armazenamento.db'):
        self.banco = banco
        self.con = sqlite3.connect(self.banco)
        self.comandos = self.con.cursor()
        #Tabela
        self.comandos.execute("""
CREATE TABLE IF NOT EXISTS informacoes (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              nome TEXT NOT NULL,
                              telefone TEXT
                              )
""")
        self.con.commit()

class Usuario(Dados):
    def __init__(self):
        super().__init__()