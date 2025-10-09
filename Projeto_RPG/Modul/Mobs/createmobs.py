from random import choice

lista_mob = ('Demonio', 'Anjo', 'Morto-Vivo', 'Esqueleto', 'Vampiro')

mobs_criados = []

def criacao():
    qts = int(input('X vezes: '))
    for i in range(qts):
        nome = choice(lista_mob)
        nivel = 1

        if nome == 'Demonio' or nome == 'Anjo':
            hp = 3000
            dano = 400
            mana = 500
            defesa = hp / 2
        else:
            hp = 1500
            dano = 150
            mana = 80
            defesa = hp / 2

        mobs_criados.append({
            "nome": nome,
            "nivel": nivel,
            "hp": hp,
            "dano": dano,
            "defesa": defesa,
            "mana": mana
        })

        print(f'{nome} LV: {nivel} | HP {hp}/{hp} | Mana {mana}/{mana} | Defesa: {defesa} | Dano: {dano}')

    return mobs_criados

criacao()
