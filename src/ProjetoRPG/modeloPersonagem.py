class Personagem:
    def __init__(self,nome,nivel,hp,mana,forca,intl,agli,resister,elemento):
        self.nome = nome
        self.nivel = nivel
        self.hp = hp
        self.mana = mana
        #Atributos
        self.forca = forca
        self.intl = intl
        self.agli = agli
        self.resister = resister
        self.atributos = {'STR' : self.forca,'INT' : self.intl,'AGLI' : self.agli,'RESIST' : self.resister}
        self.elemento = elemento
        # Status
        self.vida = (100 * self.hp) / 2
        self.Mana = (100* self.mana) /2
        self.ataque = 100 *self.forca
        self.defesas = 100 * self.resister
        self.inteligencia = 5 * self.intl
        self.agilidade = 5 * self.agli

    def exibir_atributos(self):
        print(f"--- Atributos de {self.nome} ---")
        print(f"Nível: {self.nivel} | HP: {self.hp} | Mana: {self.mana}")
        if self.elemento:
            print(f"Elemento: {self.elemento}")
        for attr, valor in self.atributos.items():
            print(f"  {attr}: {valor}")
        print("-" * 30)

    def status(self):

        print(f''' CLASSE {self.nome}   
        HP : {self.vida}  MANA : {self.Mana}
        Dano : {self.ataque}
        Defesa : {self.defesas}
        CRT : {self.inteligencia} %
        ENV : {self.agilidade} %
        ''')

    def __repr__(self):
        return f'{self.nome} / {self.nivel}'
class Lutador(Personagem):
    def __init__(self):
        super().__init__('Lutador',1,200,100,16,7,10,15,elemento=None)

class Mago(Personagem):
    def __init__(self):
        super().__init__('Mago',1,200,200,8,18,15,15,elemento=None)

class Arqueiro(Personagem):
    def __init__(self):
        super().__init__('Arqueiro',1,200,150,20,16,20,10,elemento=None)

#Mobs

class Zumbi(Personagem):
    def __init__(self):
        super().__init__('Zumbi',1,200,0,10,0,2,3,'Terra')


class Demonio(Personagem):
    def __init__(self):
        super().__init__('Demonio',1,300,300,17,10,7,10,'Trevaz')


class Anjo(Personagem):
    def __init__(self):
        super().__init__('Anjo',1,300,400,20,19,14,16,'Luz')


# Listar
class Listar:
    def __init__(self):
        self.lista_classes = [Lutador(),Mago(),Arqueiro()]
        self.lista_mobs = [Zumbi(),Demonio(),Anjo()]

    def filtrar(self):
        while True:
            print("\nO que você deseja filtrar?")
            print("1. Classes / Jogadores")
            print("2. Mobs / Monstros")

            opcao = input("Escolha uma opção (1 ou 2): ").strip()

            if opcao == '1':
                print("\n=== Classes de Jogadores ===")
                for classe in self.lista_classes:
                    print(f"- {classe}")
                break
            elif opcao == '2':
                print("\n=== Mobs e Monstros ===")
                for mob in self.lista_mobs:
                    print(f"- {mob}")
                break
            else:
                print("\nOpção inválida! Tente novamente.")

def main():
    listagem = Listar()
    l1 = Lutador()

    l1.status()

if __name__ == '__main__':
    main()