import json
from time import sleep
class Lista:
    def __init__(self):
        self.lista_tarefas = []
        self.pontuacao = []

class Tarefas(Lista):
    def __init__(self):
        super().__init__()
        self.numerao_tarefas = 1
        self.feitos = 0
        self.nao_feitos = 0

    def criar_tarefas(self):
        while True:
            try:
                x = int(input("Criar quantas tarefas ? "))
                break
            except ValueError:
                print('Erro volte')
                continue
        for _ in range(x):
            nome_tarefa = input('Nome da tarefa : ')
            descricao = input('Descrição da tarefa : ')
            op = input('Tarefa foi feita ? [S | N] || Resposta :')
            self.pontuacoes(op)
            pr = {"NUMERO TAREFAS" : self.numerao_tarefas, "TAREFA" : nome_tarefa, "DESCRICAO" : descricao , "RESULTADO" : op}
            self.lista_tarefas.append(pr)
            self.numerao_tarefas +=1

        print('-=-'*10)
        print(f'No total foi criado {x} Tarefas ')
        print('Pontos Registrados !')
        print('-=-' * 10)
        sleep(1)

        self.exibir_pontuacao()

    def pontuacoes(self, op):
        if op == "S":
            self.feitos += 1
            self.pontuacao.append(self.feitos)
        elif op == "N":
            self.nao_feitos += 1
            self.pontuacao.append(self.nao_feitos)
        else:
            print('Erro de Resposta !')

    def exibir_pontuacao(self):
        print('\n---- / Pontuação / ----')
        resultados = {"TAREFAS FEITAS " : self.feitos, "TAREFAS NAO FEITOS " : self.nao_feitos}
        print(resultados)
        self.pontuacao.append(resultados)
        self.salvar_pontuacao()

    def salvar_lista_tarefas(self):
        if not self.lista_tarefas:
            pass
        else:
            with open('tarefas.json','w',encoding='utf-8') as jsonfile:
                json.dump(self.lista_tarefas, jsonfile,indent=4)

    def salvar_pontuacao(self):
        if not self.pontuacao:
            pass
        else:
            with open('pontuacao.json','w',encoding='utf-8') as jsonfile:
                json.dump(self.pontuacao, jsonfile,indent=4)


Tarefas().criar_tarefas()