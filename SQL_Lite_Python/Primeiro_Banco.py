import sqlite3

#Criar banco de dados
con = sqlite3.connect("Dados_Banco.db")

#O  nex sera usado para todos os comandos que envolve o sql
nex = con.cursor()

nex.execute("""
    CREATE TABLE IF NOT EXISTS informações(
            descricao TEXT,
            nota INTEGER
            )
""")

nex.executemany(
    "INSERT INTO informações VALUES(? , ?)",
    [
        ("Python é muito bom para iniciantes" , 10),
        ("Java é muito complexo para um iniciante entender" , 7)
    ]
)

con.commit() # Aqui ele confirma as mundaças 

nex.execute("SELECT descricao , nota FROM informações")#Consulta os dados que dessa vez é a descricao da table informações
resultado = nex.fetchall() #Cria uma variavel para ver no terminal

for linhas  in resultado:
    print(linhas)

con.close() # Fecha a conexao 