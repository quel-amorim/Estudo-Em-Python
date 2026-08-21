import json
from random import randint , choice

class Agenda:
    def __init__(self):
        self.lista = []
        self.numeroid = 1
        self.variantes_email = ['@gmail.com','@hotmail.com','@yahoo.com']
        self.carregarjson()

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

        for i in range(x):
            nome = input('Informe o nome do contato:')
            numero = randint(900000000, 999999999)
            numero_str = str(numero)
            telefone = f'+55 9 {numero_str[:5]}-{numero_str[5:]}'
            email = f'teste#{i}{choice(self.variantes_email)}'
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
            print(f'{contato['id']}°{contato['nome']} -> {contato["telefone"]} | {contato["email"]}')

    def buscar(self):
        buscando = input('Informe o nome do contato: ')
        encontrado = False
        for contato in self.lista:
            if contato['nome'].lower() == buscando.lower():
                print(f"{contato['nome']} -> {contato['telefone']} ")
                encontrado = True

        if not encontrado:
            print('Contato não encontrado.')

    def remover(self):
        try:
            IDremover = int(input('Informe o ID do contato: '))
        except ValueError:
            print('Informe um ID válido.')
            return
        for contato in self.lista:
            if contato['id'] == IDremover:
                self.lista.remove(contato)
                self.salvar()
                print(f'ID #{IDremover} removido com sucesso!')
                return

        print('ID não encontrado.')

        for indice, contato in enumerate(self.lista, start=1):
            contato["id"] = indice

        self.numeroid = len(self.lista) +1

    def carregarjson(self):
        try:
            with open('contatos.json', 'r', encoding='utf-8') as arquivo:
                self.lista = json.load(arquivo)

        except FileNotFoundError:
            print('Arquivo contatos.json não encontrado.')
            self.lista = []
            self.numeroid = 1

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