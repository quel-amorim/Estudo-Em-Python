from random import choice

lista_mob = ('Demonio', 'Anjo', 'Morto-Vivo', 'Esqueleto', 'Vampiro')

skill_d = ['Golpe da alma' , 'Devorador de almas' , 'Golpe sombrio']
skill_a = ['Luz da graça','Golpe do Senhor','Vontade de Deus']
skill_m = ['Golpe de ossos']
skill_v = ['Só uma mordida,não vai dor nada confia']

prox_id = 1

mobs_criados = []

def criacao():
    global prox_id

    qts = int(input('X vezes: '))
    for i in range(qts):
        nome = choice(lista_mob)
        nivel = 1
        id = f'ID#{prox_id}'
        prox_id +=1

        if nome == ['Demonio']:
            skill = choice(skill_d)
            hp = 3000
            dano = 400
            mana = 500
            defesa = hp / 2

        elif nome == ['Anjo']:
            skill = choice(skill_a)
            hp = 3000
            dano = 400
            mana = 500
            defesa = hp / 2

        elif nome == ['Morto-Vivo']:
            skill = choice(skill_m)
            hp = 1500
            dano = 150
            mana = 80
            defesa = hp / 2

        elif nome == ['Vampiro']:
            skill = choice(skill_v)
            hp = 2500
            dano = 350
            mana = 300
            defesa = hp / 2

        else:
            skill = choice(skill_m)
            hp = 1500
            dano = 150
            mana = 80
            defesa = hp / 2

        mobs_criados.append({
            "id" : id,
            "nome": nome,
            "nivel": nivel,
            "hp": hp,
            "dano": dano,
            "defesa": defesa,
            "mana": mana,
            "skill" : skill
        })

        print(f'{id} {nome} LV: {nivel} | HP {hp}/{hp} | Mana {mana}/{mana} | Defesa: {defesa} | Dano: {dano} | Golpe : {skill} |\n')

    return mobs_criados

criacao()
