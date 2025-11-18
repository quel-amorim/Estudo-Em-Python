from database.CREATEDATABASE import DataBase
from random import choice, randint
class Mob(DataBase):
    def __init__(self):
        super().__init__()
        self.sugestoes = ["Demonio","Anjo","Zumbi"]
    
    def addInsert(self):
        """Adicionar dados paras as tabelas !"""
        while True:
            try:
                x = int(input("Criar quantos mobs ?"))
                break
            except ValueError:
                print("erro !")
                continue
        
        for _ in range(x):
            nome = choice(self.sugestoes)
            nivel = randint(1 , 30)

            self.cur.execute("INSERT INTO mobs (nome , nivel) VALUES(? , ?)" , (nome , nivel))
            self.con.commit()
        
        print(f"Mobs criados salvos")
    
    def viewerMob(self):
        self.cur.execute("SELECT * FROM mobs")
        dados = self.cur.fetchall()

        if not dados:
            print("Nenhum mob no banco.")
        else:
            for i, mob in enumerate(dados, start=1):
                print(f"{i} - Nome: {mob[0]} | Nível: {mob[1]}")

    def closeBase(self):
        self.con.close()