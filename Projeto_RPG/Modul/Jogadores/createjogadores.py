from random import choice

lista_jogadores = ('Lutador', 'Mago', 'Feiticeiro', 'Guerreiro', 'Arqueiro')

skill_lutador = ['Golpe Furioso', 'Jogar Escudo']
skill_arq = ['Golpe certeiro', 'Acertei nem olhei haha']
skill_mago = ['Raio', 'Bola de Fogo', 'Fica frio ai']

jogadores_criados = []
proximo_id = 1  

def criador_ply():
    global proximo_id

    qts = int(input("Criar quantos jogadores ? "))

    for i in range(qts):
        nome = choice(lista_jogadores)
        nivel = 1
        id = f'ID#{proximo_id}'
        proximo_id += 1  

        if nome in ['Lutador', 'Guerreiro']:
            skill = choice(skill_lutador)
            hp = 4000
            dano = 500
            defesa = 2000
            mana = 0
            critico = 0
            dano_fisico = 0
            dano_magico = 0

        elif nome == 'Arqueiro':
            skill = choice(skill_arq)
            hp = 2000
            dano = 350
            defesa = 200
            mana = 250
            critico = 40
            dano_fisico = 0
            dano_magico = 0

        else:
            skill = choice(skill_mago)
            hp = 1800
            dano = 0
            dano_fisico = 100
            dano_magico = 600
            mana = 4000
            defesa = 150
            critico = 0

        jogadores_criados.append({
            "id": id,
            "nome": nome,
            "nivel": nivel,
            "hp": hp,
            "mana": mana,
            "dano": dano,
            "dano_fisico": dano_fisico,
            "dano_magico": dano_magico,
            "defesa": defesa,
            "critico": critico,
            "skill": skill
        })

        print(f'{id} {nome} LV {nivel} | HP: {hp} | Mana: {mana} | Dano: {dano} | Dano Físico: {dano_fisico} | Dano Mágico: {dano_magico} | Defesa: {defesa} | Crítico: {critico}%\nGolpe: {skill}\n')

criador_ply()
