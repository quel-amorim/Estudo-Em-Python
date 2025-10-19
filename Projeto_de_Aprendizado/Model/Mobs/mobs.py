from random import randint, choice

# ---------------- CLASSE BASE ---------------- #
class Mob:
    def __init__(self, nome, nivel, hp, dano):
        self.nome = nome
        self.nivel = nivel
        self.hp = hp
        self.dano = dano

    def __str__(self):
        return f"{self.nome} | LV {self.nivel} | HP {self.hp} | Dano {self.dano}"

    def atacar(self):
        return f"{self.nome} atacou com um golpe básico!"


# ---------------- SUBCLASSES ---------------- #
class Demonio(Mob):
    def __init__(self, nivel, hp, dano):
        super().__init__("Demônio", nivel, hp, dano)
        self.elemento = "Fogo"

    def atacar(self):
        return f"{self.nome} lançou uma bola de fogo!"


class Anjo(Mob):
    def __init__(self, nivel, hp, dano):
        super().__init__("Anjo", nivel, hp, dano)
        self.elemento = "Luz"

    def atacar(self):
        return f"{self.nome} lançou uma rajada de luz!"


class MortoVivo(Mob):
    def __init__(self, nivel, hp, dano):
        super().__init__("Morto-Vivo", nivel, hp, dano)
        self.elemento = "Trevas"

    def atacar(self):
        return f"{self.nome} lançou um golpe sombrio!"


# ---------------- SISTEMA DE GERENCIAMENTO ---------------- #
class ExibirMobs:
    def __init__(self):
        self.mobs_list = []

    def gerador_mobs(self):
        try:
            qts = int(input("Criar quantos mobs? "))
        except ValueError:
            print("Erro: digite apenas números!")
            return

        # Lista de classes, não de strings
        tipos = [Demonio, Anjo, MortoVivo]

        for i in range(qts):
            tipo_mob = choice(tipos)  # Escolhe uma classe aleatória
            nivel = randint(1, 80)
            hp = randint(1000, 10000)
            dano = round(hp / 2)

            mob = tipo_mob(nivel, hp, dano)
            self.mobs_list.append(mob)
            print(f"{mob.nome} criado com sucesso! (LV {mob.nivel})")

        print("\n--- Lista de Mobs Criados ---")
        for mob in self.mobs_list:
            print(mob, "→", mob.atacar())


# ---------------- FUNÇÃO PRINCIPAL ---------------- #
def main():
    teste = ExibirMobs()

    print("-" * 45)
    print("Bem-vindo à Interface de Criação de Mobs")
    print("-" * 45)

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
            teste.gerador_mobs()
        elif escolha == 0:
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")


# ---------------- EXECUÇÃO ---------------- #
if __name__ == "__main__":
    main()
