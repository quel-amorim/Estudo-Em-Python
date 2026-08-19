from random import randint
import json

class Agenda:
    def __init__(self):
        self.lista = []

class Contato(Agenda):
    def __init__(self):
        super().__init__()
        self.id = 1

    def criarcontato(self):
        while True:
            try:
                qts = int(input('Quantos contatos deseja criar: '))
                if qts < 0:
                    print('Quantidade de contatos negativo.')
                    continue

                break
            except ValueError:
                print('Volte ao inicio')
                continue
        for _ in range(qts):
            nome = input('Informe o nome do contato: ')
            n1 = randint(0,9999)
            n2 = randint(0,9999)
            telefone = f'+55 9 {n1}-{n2}'
            contatos = {
                'id' : self.id,
                'nome' : nome,
                'telefone': telefone
            }
            self.id +=1
            self.lista.append(contatos)

        print('Contatos adicionados com sucesso !')

    def salvar(self):
        with open('contatos.json','w') as arquivo_json:
            json.dump(self.lista,arquivo_json,indent=4,ensure_ascii=False)

    def remover(self):
        idremover = int(input('Informe o id do contato: '))
        if idremover in self.lista:
            self.lista.remove(idremover)
            print(f'ID{idremover} removido com sucesso !')

        if idremover not in self.lista:
            print('Desconhecido !')

        self.salvar()