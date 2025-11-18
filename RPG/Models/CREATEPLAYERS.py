from database.CREATEDATABASE import DataBase
from random import choice , randint
class Player(DataBase):
    def __init__(self):
        super().__init__()
        self.sugestoes = ["Lutador", "Mago", "Porra Louca"]
    
    def addInsert(self):
        """Adicionar dados"""
        while True:
            try:
                y = int(input("Criar quantos jogadores ?"))
                break
            except ValueError:
                print("Erro !NOIAAAAAAAAAAAAAA")
                continue
        
        for _ in range(y):
            nome = choice(self.sugestoes)
            nivel = randint(1 , 40)

            self.cur.execute("INSERT INTO jogadores (nome , nivel) VALUES(? , ?)" , (nome , nivel))
            self.con.commit()
        
        print(f"Jogadores salvos")
    
    def viewerPlayer(self):
        self.cur.execute("SELECT * FROM jogadores")
        dados = self.cur.fetchall()

        if not dados:
            print("Nenhum jogador no banco.")
        else:
            for i, jog in enumerate(dados, start=1):
                print(f"{i} - Nome: {jog[0]} | Nível: {jog[1]}")

    def closeBase(self):
        self.con.close()
    