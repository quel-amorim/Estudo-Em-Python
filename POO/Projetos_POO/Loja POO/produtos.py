from random import uniform, randint, choice
from datetime import datetime, timedelta


class Produto:
    def __init__(self, nome, valor, data_adicao):
        self.nome = nome
        self.valor = valor
        self.data_adicao = data_adicao

    def __repr__(self):
        return f"{self.nome} - R$ {self.valor:.2f} | Data de Adição: {self.data_adicao.strftime('%Y-%m-%d')}"

    @staticmethod
    def gerar_produto():
        """Gera uma quantidade de produtos com valores e datas aleatórias."""
        while True:
            try:
                qts = int(input("Criar quantos produtos? "))
                break
            except ValueError:
                print("Erro! Digite um número inteiro.")
                continue

        tipos = ["Livro", "Roupa", "Alimento", "Eletrônico", "Doméstico", "Hardware"]
        produtos = []

        for _ in range(qts):
            nome = choice(tipos)
            valor = round(uniform(10, 10000), 2)
            data = datetime.now() - timedelta(days=randint(0, 365))
            produtos.append(Produto(nome, valor, data))

        print("\nProdutos criados com sucesso!\n")
        for p in produtos:
            print(p)

        return produtos


def main():
    print("=== CRIAR PRODUTOS ===")
    produtos = Produto.gerar_produto()
    print(f"\nTotal de produtos criados: {len(produtos)}")


if __name__ == "__main__":
    main()
