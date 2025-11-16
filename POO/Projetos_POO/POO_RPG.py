from random import choice, uniform, randint

# ============== CLASSE BASE PARA ENTIDADES (Jogador / Mob) ================= #

class EntidadeBase:
    def __init__(self):
        self.salvos = []  

    def gerar_id(self):
        """Gera um ID sempre com 4 dígitos."""
        return randint(1000, 9999)

    def exibir_lista(self, titulo):
        if not self.salvos:
            print(f"\nNenhum {titulo} encontrado!")
            return

        print(f"\n--- LISTA DE {titulo.upper()} ---")
        for entidade in self.salvos:
            print(
                f"ID {entidade['id']} | "
                f"{entidade['nome']} LV {entidade['nivel']} | "
                f"HP {entidade['hp']} | DPS {entidade['forca']} | "
                f"EXP {entidade['exp']}"
            )


# ======================== JOGADORES ======================== #

class Jogador(EntidadeBase):
    def criar(self):
        try:
            qts = int(input("Criar quantos jogadores? "))
        except ValueError:
            print("Valor inválido!")
            return

        nomes = ["Lutador", "Mago", "PorraLouca"]

        for _ in range(qts):
            jogador = {
                "id": self.gerar_id(),
                "nome": choice(nomes),
                "nivel": 1,
                "forca": round(uniform(10, 100), 2),
                "hp": randint(1000, 10000),
                "exp": round(uniform(1, 100), 2),
            }

            self.salvos.append(jogador)

        print("Jogadores criados com sucesso!")

    def exibir(self):
        super().exibir_lista("Jogadores")


# ======================== MOBS ======================== #

class Mob(EntidadeBase):
    def criar(self):
        try:
            qts = int(input("Criar quantos mobs? "))
        except ValueError:
            print("Valor inválido!")
            return

        nomes = ["Demônio", "Anjo", "Vampiro", "OLHA O OTAKU"]

        for _ in range(qts):
            mob = {
                "id": self.gerar_id(),
                "nome": choice(nomes),
                "nivel": 1,
                "forca": round(uniform(10, 100), 2),
                "hp": round(uniform(1000, 10000), 2),
                "exp": randint(1, 100),
            }

            self.salvos.append(mob)

        print("Mobs criados com sucesso!")

    def exibir(self):
        super().exibir_lista("Mobs")


# ======================== MENU PRINCIPAL ======================== #

def main():
    jogadores = Jogador()
    mobs = Mob()

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("[1] Criar Jogadores")
        print("[2] Criar Mobs")
        print("[3] Listar Tudo")
        print("[4] Sair")

        try:
            op = int(input("Escolha uma opção: "))
        except ValueError:
            print("Digite apenas números!")
            continue

        if op == 1:
            jogadores.criar()
        elif op == 2:
            mobs.criar()
        elif op == 3:
            jogadores.exibir()
            mobs.exibir()
        elif op == 4:
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
