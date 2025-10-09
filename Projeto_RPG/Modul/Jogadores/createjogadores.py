from random import choice

lista_jogadores = ('Lutador' , 'Mago' , 'Feiticeiro' , 'Guerreiro' , 'Arqueiro')
jogadores_criados = []

def criador_ply():
    qts = int(input("Criar quantos jogadores ? "))
    for i in range(qts):
        nome = choice(lista_jogadores)
        nivel = 1
        if nome == 'Lutador' or nome == 'Guerreiro':
            hp = 4000
            dano = 500
            defesa = 2000
            mana = 0
            critico = 0
            dano_fisico = 0
            dano_magico = 0
            print(f'\n{nome} LV {nivel} HP {hp} Mana {mana} | Dano {dano} /  Defesa {defesa}')
        elif nome == 'Arqueiro':
            hp = 2000
            dano = 350
            defesa = 200
            mana = 250
            critico = 40
            dano_fisico = 0
            dano_magico = 0
            print(f'\n{nome} LV {nivel} HP {hp} Mana {mana} | Dano {dano}  / Defesa {defesa} / Critico : {critico} %')
        else:
            hp = 1800
            dano = 0
            dano_fisico = 100
            dano_magico = 600
            mana = 4000
            defesa = 150
            critico = 0
            print(f'\n{nome} LV {nivel} HP {hp} Mana {mana} | Dano_fisico {dano_fisico} / Dano Magico {dano_magico} / Defesa {defesa}')

        jogadores_criados.append({
            "nome" : nome,
            "hp" : hp,
            "mana" : mana,
            "dano" : dano,
            "dano_fisico" : dano_fisico,
            "dano_magico" : dano_magico,
            "defesa" : defesa,
            "critico" : critico
        })
    3
criador_ply()