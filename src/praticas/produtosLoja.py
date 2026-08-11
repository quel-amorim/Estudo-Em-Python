from random import randint
class Produto:
    def __init__(self,nome,categoria,valor,quantidade,fornecedor):
        self.identificacao = randint(0 , 100)
        self.nome = nome
        self.categoria = categoria
        self.valor = valor
        self.quantidade = quantidade
        self.fornecedor = fornecedor

    def __repr__(self):
        print(f'ID#{self.identificacao} | {self.nome} Catégoria : {self.categoria} R${self.valor} Quantidade :{self.quantidade} -> Distribuidora : {self.fornecedor}')


itens01 = Produto('AMD Ryzen 5 4600G','HARDWARE',700,100,'AMD')
itens02 = Produto('NVIDIA GTX 1650 4GB','HARDWARE',1500,20,'NVIDIA')
itens03 = Produto('Ração de Calopsita','ALIMENTO',29.90,1000,'ATACADAO')

class Gerenciamento:
    def __init__(self):
        self.produtosListados = [itens01,itens02,itens03]

    def filtrar(self):
        print('Como gostaria filtrar?\n1.nome\n2.categoria\n3.fornecedor')
        modelo = input('Escolha :')
        match (modelo):
            case '1':
                for filtroN in self.produtosListados['nome']:
                    print(filtroN)

            case '2':
                for filtroC in self.produtosListados['categoria']:
                    print(filtroC)

            case '3':
                for filtroD in self.produtosListados['forcedor']:
                    print(filtroD)

    def exibicao(self):
        for produto in self.produtosListados:
            print(produto)

def main():
    gerente = Gerenciamento()

    print('Todos os Produtos')
    gerente.exibicao()

if __name__ == "__main__":
    main()