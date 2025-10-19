import sqlite3
from datetime import datetime

class Dados:

    def __init__(self,nome=None,idade=None,data=None):
        self.nome = nome
        self.idade = idade
        self.data = data
    
    def gerar_resultados(self):
        self.nome = input("Nome : ").strip()
        self.idade = int(input("Idade : "))
        self.data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def criar_sql(self):
        con = sqlite3.connect("random_dados.db")#criado banco de dados
        cn = con.cursor() #cn base de criar comandos

        cn.execute("""
        CREATE TABLE IF NOT EXISTS perfil(
            nome TEXT,
            idade INTEGER,
            data DATETIME
        )
        """)

        cn.execute("""
            INSERT INTO perfil VALUES(? , ? ,?)
    """,(self.nome,self.idade,self.data))
        
        con.commit()
        con.close()

        print(f"Dados salvos com sucesso")

pessoa = Dados()

pessoa.gerar_resultados()
pessoa.criar_sql()