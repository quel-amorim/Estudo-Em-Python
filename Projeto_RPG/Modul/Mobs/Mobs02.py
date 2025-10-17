from random import choice, randint

class Mob:  # Classe base
    def __init__(self, nome, nivel, hp):
        self.nome = nome
        self.nivel = nivel
        self.hp = hp

    def __str__(self):
        return f'{self.nome} | LV: {self.nivel} | HP: {self.hp}'

    def atacar(self):
        return f"{self.nome} atacou com um golpe básico!"

# ------------------ Subclasses ------------------

class Demonio(Mob):
    def __init__(self, nivel, hp):
        super().__init__("Demônio", nivel, hp)
        self.elemento = "Fogo"

    def atacar(self):
        return f"{self.nome} lançou uma bola de fogo!"

class Anjo(Mob):
    def __init__(self, nivel, hp):
        super().__init__("Anjo", nivel, hp)
        self.elemento = "Luz"

    def atacar(self):
        return f"{self.nome} invocou uma luz divina!"

class MortoVivo(Mob):
    def __init__(self, nivel, hp):
        super().__init__("Morto-Vivo", nivel, hp)
        self.elemento = "Trevas"

    def atacar(self):
        return f"{self.nome} usou um ataque sombrio!"

class TierList:
    def __init__(self):
        self.combo_mobs = []

    def gerador_de_mobs(self):
        try:
            qts = int(input("Quantos mobs deseja criar? "))
        except ValueError:
            print("Erro: apenas números!")
            return

        for i in range(qts):
            tipo = choice([Demonio, Anjo, MortoVivo])
            nivel = randint(1, 80)
            hp = randint(1000, 10000)
            mob = tipo(nivel, hp)
            self.combo_mobs.append(mob)
            print(f"{mob.nome} criado com sucesso! (LV {mob.nivel})")

        print("\n--- Lista de Mobs Criados ---")
        for mob in self.combo_mobs:
            print(mob, "→", mob.atacar())

def main():
    tier = TierList()

    print("-" * 40)
    print("Bem-vindo à Interface de Criação de Mobs")
    print("-" * 40)

    while True:
        print("\nOpções:")
        print("[1] Criar Mobs")
        print("[0] Sair")
        try:
            escolha = int(input("Escolha: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if escolha == 1:
            tier.gerador_de_mobs()
        elif escolha == 0:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()