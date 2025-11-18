import sqlite3

class DataBase:
    def __init__(self, banco='rpg.db'):
        self.banco = banco
        self.con = sqlite3.connect(self.banco)
        self.cur = self.con.cursor()
        self.create_ply()
        self.create_mob()
    
    def create_ply(self):
        """Aqui vai ser a tabela de jogadores"""
        self.cur.execute("CREATE TABLE IF NOT EXISTS jogadores (nome TEXT NOT NULL, nivel INTEGER)")
        self.con.commit()
    
    def create_mob(self):
        """Tabela de mobs"""
        self.cur.execute("CREATE TABLE IF NOT EXISTS mobs (nome TEXT NOT NULL , nivel INTEGER)")
        self.con.commit()
