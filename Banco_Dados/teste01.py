                                                #versão 01

from random import  randint , uniform

class Banco:

    def __init__(self,nome ,agencia,telefone,email,saldo):
        self.nome = nome
        self.agencia = agencia
        self.telefone = telefone
        self.email = email
        self.saldo = saldo
    
    def __repr__(self):
        return f'Dados : {self.nome} | Ag : {self.agencia} | Contato : {self.telefone} | Email : {self.email} | Saldo na Conta : R$ {self.saldo}'

def criador_dados(n):
    nomes = [input('Coloque um nome : ') for _ in range(n)] #nome
    ag = [randint(0 , 9999) for _ in range(n)] # agencia
    ddd = randint(11 , 99)
    cel = randint(0 , 999999999)
    completo = [f'+55 ({ddd:02d}) 9{cel:08d}' for _ in range(n)] #contato
    conta_email = [input('Register email : ') for _ in range(n)] # email
    saldo_conta = [round(uniform(800 , 10000), 2) for _ in range(n)]#saldo

    return [Banco(nomes[i],ag[i],completo[i],conta_email[i],saldo_conta[i]) for i in range(n)]

teste = criador_dados(1)

print(teste)
