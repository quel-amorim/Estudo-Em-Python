from random import randint , choice , uniform
import json
class Produto:
    def __init__(self):
        self.sugestoes_produtos = ["Livro" , "Roupa" , "Alimentos"]
        self.dados = []

    def criar_produto(self):
        while True:
            try:
                x = int(input("Quantos produtos deseja criar ?"))
                break
            except ValueError:
                print('Erro !')
                continue
        
        for _ in range(x):
            nome = choice(self.sugestoes_produtos)
            valor = f'R$ {round(uniform(100 , 10000), 2)}'
            quantidade = randint(0 , 100)

            produtos = {
                "ID" : len(self.dados) + 1,
                "nome" : nome,
                "valor" : f"R$ {valor}",
                "quantidade" : quantidade
            }
            self.dados.append(produtos)
        
        print(f"Foram criados {x} de Produtos")
        
    
    def salvar(self):
        if not self.dados:
            print('Não tem nada no dicionario')
        else:
            with open('produtos.json', 'w') as arquivo:
                json.dump(self.dados , arquivo , indent=4)
    
    def exibir(self):
        if not self.dados:
            print('Nenhum produto criado')
        else:
            print('Produtos cadastrados')
            u = int(input('Quer ver até qual produto ?'))
            for p in self.dados[:u]:
                print(p)
    
    def menu_produtos(self):
        print('-'*10)
        print('Menu Loja')
        print('-'*10)
        while True:
            print('[1] Criar')
            print('[2] Exibir')
            print('[3] Salvar')
            print('[0] Sair')

            op = input('\nEscolha :')

            match  op:
                case "1":
                    self.criar_produto()
                case "2":
                    self.exibir()
                case "3":
                    self.salvar()
                case "0":
                    print('Fechar !')
                    break
                case _:
                    print('Desconhecido !')