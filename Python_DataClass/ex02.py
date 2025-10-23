from dataclasses import dataclass

@dataclass
class Categoria:
    nome : str
    valor : float

    @staticmethod
    def criar_categoria():
        categorias = []
        while True:
            try:
                qts = int(input(" X vezes ? "))
                break
            except ValueError:
                print("Erro volte ao inicio ! ")
                continue
        
        for i in range(qts):
            nome = input("Catégoria : ").strip()
            valor = float(input("R$ : "))
            nova = Categoria(nome,valor)
            categorias.append(nova)

        print("Catégoria(s) salvo(s) com sucesso !")

        return categorias

c = Categoria.criar_categoria()

print("\n=== / Catégorias / ===")
for tcg in c:
    print(f"{tcg.nome} => R$ {tcg.valor:.2f}")