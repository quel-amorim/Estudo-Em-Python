import json
from random import uniform
class Loja:
    def __init__(self):
        self.menu = []
        self.quantidade = 0

    def adicionar(self):
        while True:
            nome = input('Nome do cafe :')
            valor = round(uniform(10 , 100),2)
            if nome not in self.menu:
                produto = {'nome': nome, 'valor': valor}
                self.menu.append(produto)
                self.quantidade += 1
                break
            else:
                print(f'{nome} já está no sistema !')
                continue

    def exibir(self):
        print(f'Itens da lista : {self.quantidade}')
        for cafe in self.menu:
            print(f' {cafe['nome']} - R$ {cafe['valor']}')

    def salvar(self):
        with open('menuCafe.json','w') as arquivo:
            json.dump(self.menu,arquivo)

    def verificar(self):
        try:
            with open('menuCafe.json','r') as arquivo:
                self.menu = json.load(arquivo)
        except json.decoder.JSONDecodeError:
            self.menu = []

def main():
    sistema = Loja()
    while True:
        print('-'*30)
        print('Menu do sistema da cafeteria')
        print('-'*30)
        print('1.adicionar')
        print('2.salvar')
        print('3.exibir')
        print('0.sair')
        escolha = input('\nEscolha :')
        match escolha:
            case '1':
                sistema.adicionar()
            case '2':
                sistema.salvar()
            case '3':
                sistema.exibir()
            case '':
                print('Desconhecido !')
                continue
            case '0':
                print('--- Fim ---')
                break

if __name__ == '__main__':
    main()