import json
class Tarefa:
    def __init__(self):
        self.tarefas = []
        self.numero = 1
    
    def criacao(self):
        while True:
            try:
                x = int(input('Quantas tarefas ?'))
                break
            except ValueError:
                print('erro !')
                continue
        
        for _ in range(x):
            descricao = input("TAREFA :")
            motiv = int(input('[1] Concluido | [2] Pedente\nEscolha :'))
            if motiv == 1:
                feitos = {"Número" : self.numero ,"Tarefa" : descricao , "Concluido" : "Sim"}
                self.numero +=1
                self.tarefas.append(feitos)
            elif motiv == 2:
                pedente = {"Número" : self.numero ,"Tarefa" : descricao , "Concluido" : "Pedente"}
                self.numero +=1
                self.tarefas.append(pedente)
        
    def salvar(self):
        if not self.tarefas:
            print('Nada')
        else:
            with open('tarefas_registradas.json', 'w') as arquivo:
                json.dump(self.tarefas , arquivo , indent=4)
    
    def exibir(self):
        if not self.tarefas:
            print('nada')
        else:
            print(self.tarefas)
    
    def menu(self):
        print('MENU DO PROGRAMA')

        while True:
            print('[1] CRIAR')
            print('[2] SALVAR')
            print('[3] EXIBIR')
            escolha = input('\nEscolha :')

            match escolha:
                case "1":
                    self.criacao()
                case "2":
                    self.salvar()
                case "3":
                    self.exibir()
