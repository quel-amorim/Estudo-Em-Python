'''Projeto de Listamento de contas'''
#Versão 1 POO - Criação da classe conta e gerenciar
#Fazer : melhor o CRUD(criar,exibir,remover,editar) , fazer uma classe pessoa tendo as informações de nome,email e salario
from random import uniform
class Conta:
    def __init__(self,nomeConta,valor,dataVencimento):
        self.nomeConta = nomeConta
        self.valor = valor
        self.dataVencimento = dataVencimento

#Contas já definidas
luz = Conta('Conta de LUZ',178.99,'14/07/2026')
agua = Conta('Conta de Agua',159.89,'10/06/2026')
#Contas interativas

class Gerenciar:
    def __init__(self):
        self.gerenciamento = [luz,agua]
        self.salarioPadrao = round(uniform(1500,3000),2)

    def exibir(self):
        for x in self.gerenciamento:
            print('-' , x.nomeConta ,'R$ :', x.valor ,'Vencimento',x.dataVencimento)

def main():
    admin = Gerenciar()

    admin.exibir()

if __name__ == '__main__':
    main()