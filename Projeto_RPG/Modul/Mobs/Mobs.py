from random import choice , randint

class Mob: # Aqui apenas crio class mob ja com as variaveis que eu deseja

    def __init__(self,nome,nivel,hp):
        self.nome = nome
        self.nivel = nivel
        self.hp = hp
    
    def __str__(self):
        return f'Monstro : {self.nome} LV {self.nivel}\nHP : {self.hp}'


class TierList:
    
    def __init__(self): #criar a lista de mobs
        self.combo_mobs = []
    
    def gerador_de_mobs(self): # gerador dos mobs
        try:
            qts = int(input("Quantos mobs deseja criar ? "))
        except ValueError:
            print('Erro apenas números !')

        for i in range(qts):
            sugestao_nomes = ['Demonio','Anjo','Morto-Vivo']
            nomes = choice(sugestao_nomes)
            nivel = randint(0 , 80)
            hp = randint(1000 , 10000)
            novo = Mob(nomes,nivel,hp)
            self.combo_mobs.append(novo)
            print('Mobs salvados com sucesso')


def main(): # Aqui é onde fica as interações do programa
    tier = TierList()

    texto_princial = 'Bem-vindo a Interface de Criação de Mobs'
    print('-'*len(texto_princial))
    print(texto_princial)
    print('-'*len(texto_princial))

    while True:
        print('Essas são as opções do programa')
        print('[1] Criar Mob')
        escolha = int(input('Escolha : '))
        if escolha == 1:
            print('A caminho da criação de personagem !')
            tier.gerador_de_mobs()
            break
        else:
            print('Erro volta ao inicio')
            continue

if __name__ == "__main__": # Executa a função main do programa
    main()