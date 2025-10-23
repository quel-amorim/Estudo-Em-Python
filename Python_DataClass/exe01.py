from dataclasses import dataclass
from random import uniform, choice, randint
from datetime import datetime, timedelta

@dataclass
class Produto:
    nome: str
    valor: float
    data_adicao: str
    categoria: str

    @staticmethod
    def gerador_P(n: int):
        produtos = []
        for i in range(n):
            nome = f"Produto N#{i+1}"
            valor = round(uniform(10, 10000), 2)
            data_adicao = (datetime.now() - timedelta(days=randint(0, 365))).strftime("%d/%m/%Y")
            categoria = choice(["Alimentos", "Roupas", "Eletrônicos"])
            produtos.append(Produto(nome, valor, data_adicao, categoria))
        return produtos


# Teste
teste = Produto.gerador_P(10)

for i, t in enumerate(teste, start=1):
    print(f"ID#{i} | {t.nome} | R$ {t.valor:.2f} | Data: {t.data_adicao} | Categoria: {t.categoria}")
