import json  #Projeto Gerenciamento de Contas !
#Versão 1 POO - Criação da classe conta e gerenciar
#Fazer : melhor o CRUD(criar,exibir,remover,editar) , fazer uma classe pessoa tendo as informações de nome,email e salario
from random import uniform , choice , randint
from datetime import timedelta,datetime
#Versão POO - com divisão em partes
#class Conta:
  #  def __init__(self,nomeconta,valor):
      #  self.nomeconta = nomeconta
      #  self.valor = valor
      #  self.dataatual = datetime.now()
       # self.vencimento = timedelta(days=15) + self.dataatual

#luz = Conta('Conta de LUZ',178.99)
#agua = Conta('Conta de Agua',159.89)

#class Gerenciar:
 #   def __init__(self):
  #      self.gerenciamento = [luz,agua]
   #     self.salariopadrao = round(uniform(1500,3000),2)

   # def exibir(self):
      #  for x in self.gerenciamento:
      #      print('-' , x.nomeconta ,'R$ :', x.valor ,'Fechamento de Fatura',x.dataatual.strftime('%d/%m/%Y'),
                                                            #      'Vencimento',x.vencimento.strftime('%d/%m/%Y'))



class Loja:
    def __init__(self):
        self.listaprodutos = []

    def criar(self, x):
        sugestao = ['Roupas', 'Eletronico', 'Alimento', 'Remedio', 'Cafe']

        for _ in range(x):
            id = len(self.listaprodutos) + 1
            nome = choice(sugestao)
            valor = round(uniform(10, 500), 2)
            quantidade = randint(0, 100)
            data = datetime.now()
            vencimentoproduto = data + timedelta(days=60)

            produto = {
                'id': id,
                'nome': nome,
                'valor': valor,
                'quantidade': quantidade,
                'data': vencimentoproduto.strftime('%d/%m/%Y')
            }

            self.listaprodutos.append(produto)

        print(f'Criação de {x} produtos na lista')

    def salvarprodutos(self):
        with open('produtos.json', 'w') as arquivo_json:
            json.dump(self.listaprodutos, arquivo_json, indent=4)

    def exibir(self):
        for y in self.listaprodutos:
            print(
                f"{y['id']} -> {y['nome']} "
                f"R${y['valor']}, "
                f"QTS {y['quantidade']} "
                f"VENCIMENTO PRODUTO {y['data']}"
            )

    def exibir02(self):
        try:
            with open('produtos.json', 'r') as arquivo_json:
                self.listaprodutos = json.load(arquivo_json)

            self.exibir()

        except FileNotFoundError:
            print('Nenhum arquivo de produtos foi encontrado!')

    def remover(self):
        remocaoID = int(input('Quer remover qual produto pelo ID? '))

        for produto in self.listaprodutos:
            if produto['id'] == remocaoID:
                self.listaprodutos.remove(produto)
                print(f'Produto de ID {remocaoID} removido com sucesso!')
                return

        print('Produto não encontrado!')


teste01 = Loja()

while True:
    print('=' * 10)
    print('Menu de Opções')
    print('=' * 10)
    print('1. Criação de Produtos')
    print('2. Salvar Produtos criados')
    print('3. Exibir Produtos')
    print('4. Remoção de Produtos por ID')
    print('0. Sair')

    escolha = input('Escolha agora! : ')

    match escolha:
        case '1':
            teste01.criar(10)

        case '2':
            teste01.salvarprodutos()
            print('Produtos salvos com sucesso!')

        case '3':
            teste01.exibir02()

        case '4':
            teste01.remover()

        case '0':
            print('Fechando Aplicação')
            break

        case _:
            print('Opção inválida!')