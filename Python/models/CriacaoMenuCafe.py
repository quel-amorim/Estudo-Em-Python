import json
from random import uniform

class Categoria:
    def __init__(self):
        self.categorias = []
        self.id_atual = 1

    def adicionar(self):
        while True:
            try:
                x = int(input('Quantos produtos ? '))
                break
            except ValueError:
                print('Erro de digitação !')
        
        for _ in range(x):
            nome = input('Produto : ')
            valor = round(uniform(2, 100), 2)  # gerar novo valor
            preco = f"R$ {valor}"

            produto = {
                "ID": self.id_atual,
                "Produto": nome,
                "Valor": preco
            }

            self.categorias.append(produto)
            self.id_atual += 1   # atualizar ID

        print(f'{x} produtos foram criados !')
    
    def salvar(self):
        if not self.categorias:
            print('Nada para salvar !')
        else:
            with open('categorias.json', 'w', encoding='utf-8') as arquivo:
                json.dump(self.categorias, arquivo, indent=4, ensure_ascii=False)
            print("Arquivo salvo com sucesso!")
    
    def mostrar(self):
        if not self.categorias:
            print('Nada para mostrar !')
        else:
            for p in self.categorias:
                print(f'{p["ID"]} - {p["Produto"]} - {p["Valor"]}')
    
    def opcoes(self):
        print('[1] Adicionar')
        print('[2] Salvar Json')
        print('[3] Mostrar')
        print('[0] Sair')
    
    def menu(self):
        print('-'*20)
        print('Bem-vindo ao menu de Categorias')
        print('-'*20)

        while True:
            print('-=-'*10)
            self.opcoes()
            print('-=-'*10)

            escolha = input('\nEscolha: ')

            match escolha:
                case "1":
                    self.adicionar()
                case "2":
                    self.salvar()
                case "3":
                    self.mostrar()
                case "0":
                    print('--- Fim ---')
                    break
                case _:
                    print("Opção inválida!")
