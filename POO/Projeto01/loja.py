import json
from collections import defaultdict
from random import uniform,choice
class Loja:
    def __init__(self):
        self.produtosalvos = []
        self.sugestoes_nomes = ['Pao','Quero CAFE','SOPAO','Passoca','Sorvete','Pizza','ROBINHOS']
        self.sugestoes_categorias = ['Alimentos','Domesticos','Eletronicos','SEM IDEIAS PORRA']
        self.id = 1

    def adicionar(self):
        while True:
            try:
                y = int(input('Criação de quantos produtos ?'))
                break
            except ValueError:
                print('Erro volte ao começo !')
                continue
        for i in range(y):
            nome = f'{choice(self.sugestoes_nomes)}#{i}'
            valor = round(uniform(8, 10000),2)
            categoria = choice(self.sugestoes_categorias)
            pd = {'id' : self.id , 'nome' : nome , 'valor' : valor , 'categoria' : categoria}
            self.produtosalvos.append(pd)
            self.id +=1

        print('FEITOS COM SUCESSO PORRA !!!!!!')
        self.salvar()

    def salvar(self):
        with open('criadosP.json','w') as arquivo:
            json.dump(self.produtosalvos, arquivo)

    def exibir(self):
        try:
            with open('criadosP.json','r') as arquivo:
                self.produtosalvos = json.load(arquivo)
        except json.decoder.JSONDecodeError:
            self.produtosalvos = []

        print('Produtos Criados !')
        print('-=-'*12)
        for l in self.produtosalvos:
            print('°',l['id'],'-' ,'Produto ', l['nome'] , 'R$', l['valor'] , 'Categoria :', l['categoria'])

def main():
    p1 = Loja()
    while True:
        print('-=-'*10)
        print('PROGRAMA DE LOJA')
        print('-=-'*10)
        print('1.Criação de Produtos')
        print('2.Exibir Produtos criados')
        print('3.Salvar')
        print('0.Sair')
        opcao = input('Escolha :')
        match opcao:
            case '1':
                p1.adicionar()
            case '2':
                p1.exibir()
            case '3':
                p1.salvar()
            case '0':
                print('ACABOU FAMILIA !')
                break

if __name__ == '__main__':
    main()