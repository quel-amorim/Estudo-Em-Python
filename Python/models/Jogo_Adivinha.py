from random import randint
import json
class Adivinha:
    def __init__(self):
        self.pontos_j = 1
        self.pontos_s = 1
        self.acertosJogador = []
        self.acertosSistema = []
        self.rodadas = []

    def gameplay(self):
        while True:
            try:
                x = int(input('Quantas Rodadas quer jogar ?'))
                break
            except ValueError:
                print('Erro volte')
                continue
        
        for i in range(x):
            sistema = randint(1 , 5)
            jogador = randint(1 , 5)
            partida = {"Partida N#" : i , "J" : jogador , "S" : sistema}
            if jogador == sistema:
                self.pontos_j +=1
                self.acertosJogador.append(self.pontos_j)
            else:
                self.pontos_s +=1
                self.acertosSistema.append(self.pontos_s)

            self.rodadas.append(partida)
    
    def salvar_historico(self):
        if not self.rodadas:
            print('Não tem nada !')
        else:
            with open('historico_adivinho.json' , 'w') as arquivo:
                json.dump(self.rodadas , arquivo , indent=4)
    
    def pontuacao_partidas(self):
        print('Rank de pontuação das partidas feitas !')
        print('-=-'*20)
        print(f'Pontos Jogador : {max(self.acertosJogador)} | Pontos Sistema : {max(self.acertosSistema)}')
        print('-=-'*20)
    
    def mostrar_resultados(self):
        if not self.rodadas:
            print('Não tem nada !')
        else:
            print('Partidas Encontradas !')
            for _ ,partidas in enumerate(self.rodadas):
                print(partidas)

    def atalhos(self):
        print('[1] Iniciar o Jogo de Adivinhar')
        print('[2] Salvar os resultados')
        print('[3] Exibir a Pontuação')
        print('[4] Ver o historico')

    def MenuPrograma(self):
        while True:
            self.atalhos()
            escolha = input('\nEscolha :')
            match escolha :
                case "1":
                    self.gameplay()
                case "2":
                    self.salvar_historico()
                case "3":
                    self.pontuacao_partidas()
                case "4":
                    self.mostrar_resultados()
                case _:
                    break

