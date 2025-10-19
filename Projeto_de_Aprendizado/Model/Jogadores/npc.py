from random import choice, randint

class Jogador:
    def __init__(self, nome, nivel, hp, dano):
        self.nome = nome
        self.nivel = nivel
        self.hp = hp
        self.dano = dano
    
    def __str__(self):
        return f"{self.nome} LV {self.nivel} | HP {self.hp}  Dano {self.dano}"
    
    def atacar(self):
        return f"{self.nome} atacou com golpe básico "

class Lutador(Jogador):
    def __init__(self, nivel, hp, dano):
        super().__init__("Lutador", nivel, hp, dano)
        self.tipo = "Físico"
    def atacar(self):
        return f"{self.nome} atacou com golpe pesado "

class Mago(Jogador):
    def __init__(self, nivel, hp, dano):
        super().__init__("Mago", nivel, hp, dano)
        self.tipo = "Mágico"
    def atacar(self):
        return f"{self.nome} lançou rajadas de magia "

class Arqueiro(Jogador):
    def __init__(self, nivel, hp, dano):
        super().__init__("Arqueiro", nivel, hp, dano)
        self.tipo = "Vento"
    def atacar(self):
        return f"{self.nome} lançou flechas com vento "

class Assassino(Jogador):
    def __init__(self, nivel, hp, dano):
        super().__init__("Assassino", nivel, hp, dano)
        self.tipo = "Veneno"
    def atacar(self):
        return f"{self.nome} lançou adagas com veneno "

class Montagem_Jogador:
    def __init__(self):
        self.npcs = []

    def criador_npc(self):
        while True:
            try:
                qts = int(input("Criar quantas classes ? "))
                break
            except ValueError:
                print("Apenas números !")
                continue

        tipo_npc = [Lutador, Mago, Arqueiro, Assassino]

        for i in range(qts):
            tipo_classe = choice(tipo_npc)
            nivel = 1
            hp = randint(1000, 10000)
            dano = round(hp/2)

            npc = tipo_classe(nivel, hp, dano)
            self.npcs.append(npc)
            print(f"Jogador {npc.nome} criado com sucesso LV({npc.nivel})")
        
        print("\n=== / Lista de Jogadores / ===")
        for npc in self.npcs:
            print(npc, "->", npc.atacar())

def main():
    rodar = Montagem_Jogador()

    print("-"*45)
    print("Bem-vindo à Interface de Criação de Jogadores")
    print("-"*45)

    while True:
        print("\nOpções: ")
        print("[1] Criar Jogador ")
        print("[0] Sair ")
        try:
            opcao = int(input("Escolha : "))
        except ValueError:
            print("Apenas números ! volte ao inicio ")
            continue

        if opcao == 1:
            print("Criando Jogador ! ")
            rodar.criador_npc()
        elif opcao == 0:
            print("Encerrando o programa ... ")
            break
        else:
            print("Opção desconhecida !")

if __name__ == "__main__":
    main()
