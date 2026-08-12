'''Projeto de Listamento de contas'''
#Versão 1 POO - Criação da classe conta e gerenciar
#Fazer : melhor o CRUD(criar,exibir,remover,editar) , fazer uma classe pessoa tendo as informações de nome,email e salario
from random import uniform
from datetime import timedelta,datetime
class Conta:
    def __init__(self,nomeconta,valor):
        self.nomeconta = nomeconta
        self.valor = valor
        self.dataatual = datetime.now()
        self.vencimento = timedelta(days=15) + self.dataatual

luz = Conta('Conta de LUZ',178.99)
agua = Conta('Conta de Agua',159.89)

class Gerenciar:
    def __init__(self):
        self.gerenciamento = [luz,agua]
        self.salariopadrao = round(uniform(1500,3000),2)

    def exibir(self):
        for x in self.gerenciamento:
            print('-' , x.nomeconta ,'R$ :', x.valor ,'Fechamento de Fatura',x.dataatual.strftime('%d/%m/%Y'),'Vencimento',x.vencimento.strftime('%d/%m/%Y'))

def main():
    admin = Gerenciar()

    admin.exibir()

if __name__ == '__main__':
    main()