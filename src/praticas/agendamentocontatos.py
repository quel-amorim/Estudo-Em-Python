import json
from random import randint , choice

class Agenda:
    def __init__(self):
        self.lista = []
        self.numeroid = 1
        self.variantes_email = ['@gmail.com','@hotmail.com','@yahoo.com']

    def criarcontato(self):
        while True:
            try:
                x = int(input('Vamos adicionar quantos contatos?'))
                if x < 0:
                    print('Não é permitido deixar valor zero')
                    continue

                break
            except ValueError:
                print('Volte ao começo')
                continue

        for _ in range(x):
            nome = input('Informe o nome do contato:')
            n1 = str(randint(0,9999))
            n2 = str(randint(0,9999))
            telefone = f'+55 9{n1}-{n2}'
            email = f'teste{x}',choice(self.variantes_email)
            contato = {
                'id' : self.numeroid,
                'nome' : nome,
                'email': email,
                'telefone': telefone
            }
            self.numeroid +=1
            self.lista.append(contato)

        print('Contatos adcionados com sucesso !')

    def salvar(self):
        with open('contatos.json','w') as arquivo:
            json.dump(self.lista,arquivo,indent=4,ensure_ascii=False)

    def exibir(self):
        for contato in self.lista:
            print(f'{contato['nome']} -> {contato["telefone"]} | {contato["email"]}')

    def buscar(self):
        buscando = input('Informe o nome do contato:')
        for buscar in self.lista:
            if buscar['nome'] == buscando:
                print(f'{buscando} -> {buscar}')

            if buscar['nome'] not in self.lista:
                print('Esse nome não está listado' , buscando)

    def remover(self):
        IDremover = int(input('Informe o ID do contato:'))
        for remover in self.lista:
            if remover['id'] == IDremover:
                self.lista.remove(remover)
                print('ID#', IDremover ,'removido com sucesso !')
                self.salvar()

def main():
    telefone = Agenda()

    while True:
        print('-' * 10)
        print('Menu do Programa')
        print('-'*10)
        print('1.Criar')
        print('2.Salvar')
        print('3.Exibir')
        print('4.Buscar')
        print('5.Remover')
        print('0.Sair')
        escolha = input('\nEscolha:')
        match escolha:
            case '1':
                telefone.criarcontato()
            case '2':
                telefone.salvar()
            case '3':
                telefone.exibir()
            case '4':
                telefone.buscar()
            case '5':
                telefone.remover()
            case '0':
                print('Saindo do programa')
                break
            case _:
                print('volte ao começo do menu')
                continue
if __name__ == '__main__':
    main()