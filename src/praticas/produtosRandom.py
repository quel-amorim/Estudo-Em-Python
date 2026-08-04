from random import uniform,choice
class Loja:
    def __init__(self):
        self.minhaLista = []

    def criacaoProdutos(self,x):
        for _ in range(x):
            sugestoes_produtos = ['Café','Doce','Pizza','Pipoca','Processador','Placa de Video','Curso']
            nomeProduto = choice(sugestoes_produtos)
            if nomeProduto == 'Placa de Video':
                tiposPlacas = ['Nvidia GeForce RTX 50','Radeon RX 9000','Intel Arc Alchemist'] # Placas mais novas
                tlp = choice(tiposPlacas)
                valorPlaca = round(uniform(2000, 10000),2)
                meuProduto = {'nomeproduto' : nomeProduto , 'modelo' : tlp, 'valorproduto' : valorPlaca}
                self.minhaLista.append(meuProduto)
            elif nomeProduto == 'Processador':
                tiposProcessadores = ['Ryzen Gen 9','Intel Core Ultra']
                pr = choice(tiposProcessadores)
                valorProcessadores = round(uniform(1000, 3000),2)
                meuProduto = {'nomeproduto' : nomeProduto,'modelo' : pr, 'valorproduto' : valorProcessadores}
                self.minhaLista.append(meuProduto)
            elif nomeProduto == 'Café':
                tiposCafe = ['Passado','Super Doce']
                c = choice(tiposCafe)
                valoCafe = round(uniform(10 , 100),2)
                meuProduto = {'nomeproduto' : nomeProduto, 'tipo' : c, 'valorproduto' : valoCafe}
                self.minhaLista.append(meuProduto)
            elif nomeProduto == 'Curso':
                modelosCurso = ['Desing','IA','Desenvolvimento Pessoal/Espiritual','Programação']
                m= choice(modelosCurso)
                valoresCurso = round(uniform(2500,7000),2)
                parcelado = valoresCurso / 12 #parcelado em 12x
                meuProduto = {'nomeproduto' : nomeProduto,'modelo' : m,'valor' : valoresCurso , 'parcelado' : parcelado}
                self.minhaLista.append(meuProduto)

        print(f'Foram Criados no {x} produtos com sucesso !')

    def exibir(self):
        print(self.minhaLista)

while True:
    log = Loja()
    log.criacaoProdutos(10)

    log.exibir()
    break