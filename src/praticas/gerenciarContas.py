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

    def criar(self,x):
        for _ in range(x):
            sugestao = ['Roupas','Eletronico','Alimento','Remedio','Cafe']
            id = 1
            nome = choice(sugestao)
            valor = round(uniform(10 , 500), 2)
            quantidade = randint(0 , 100)
            data = datetime.now()
            vencimentoproduto = data + timedelta(days=60)
            produto = {'id' : id , 'nome': nome,'valor':valor,'quantidade':quantidade,
                       'data':vencimentoproduto.strftime('%d/%m/%Y')}
            self.listaprodutos.append(produto)
            id +=1

        print('Criação de {} na lista de produtos'.format(x))
        self.salvarprodutos()

    def salvarprodutos(self):
        with open('produtos.json','w') as arquivo_json:
            json.dump(self.listaprodutos,arquivo_json)

    def exibir(self):
        for y in self.listaprodutos:
            print(f'{y['id']} ->{y['nome']} R${y['valor']}, QTS {y['quantidade']} VENCIMENTO PRODUTO {y['data']}')

    def exibir02(self):
        with open('produtos.json','r') as arquivo_json:
            self.listaprodutos = json.load(arquivo_json)
            print(self.listaprodutos)

    def remover(self):
        pass