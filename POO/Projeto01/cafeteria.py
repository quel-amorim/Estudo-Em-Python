from random import uniform
import json
class Cafe:
    def __init__(self):
        self.cardapio = []
    
    def adicionar(self,nome):
        if nome == "":
            print('Não deixe o nome em branco !')
        
        valor = round(uniform(2, 100),2)
        
        produto = {"Cafe" : nome , "R$" : valor}
        self.cardapio.append(produto)
    
    def exibir(self):
        for cafe in self.cardapio:
            print(f'- {cafe['Cafe']} R$ {cafe['R$']}')

c1 = Cafe()

c1.adicionar("Café ao Leite")
c1.adicionar("Café Extremo Forte")

