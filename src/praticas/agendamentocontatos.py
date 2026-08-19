from random import randint
from datetime import datetime
class Agenda:
    def __init__(self):
        self.listacontatos = []

class Contato(Agenda):
    def __init__(self):
        super().__init__()
        self.numerocontatos = 0

    def criarcontato(self):
        while True:
            try:
                qts = int(input("Adicionar quantos contatos?"))
                break
            except ValueError:
                print('Volte ao começo')
                continue

        for _ in range(qts):
            nome = input("Informe o nome do contato: ")
            n1 = str(randint(0, 9999))
            n2 = str(randint(0, 9999))
            telefone = f'+55 9 {n1}-{n2}'
            data = datetime.now().strftime('%d/%m/%Y')
            contatos = {
                'id' : self.numerocontatos,
                'nome' : nome,
                'telefone' : telefone,
                'data' : data
            }
            self.listacontatos.append(contatos)

        print(f'Foi adicionado {qts} na agenda')