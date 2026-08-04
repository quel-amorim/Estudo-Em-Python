
class Personagem:
    def __init__(self,nome,nivel,hp,mana,forca,intl,agli,resister):
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

    def exibirAtributos(self):
        print(f'Atributos da classe {self.nome}')
        print(f'{self.atributos}')

class Lutador(Personagem):
    def __init__(self):
        super().__init__('Lutador',1,200,100,16,7,10,15)

class Mago(Personagem):
    def __init__(self):
        super().__init__('Mago',1,200,200,8,18,15,15)

class Arqueiro(Personagem):
    def __init__(self):
        super().__init__('Arqueiro',1,200,150,20,16,20,10)

l1 = Lutador()

l1.exibirAtributos()