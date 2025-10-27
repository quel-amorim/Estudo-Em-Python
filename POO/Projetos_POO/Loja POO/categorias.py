class Categoria:
    def __init__(self):
        self.categorias = []
    
    def criar(self):
        while True:
            try:
                qts = int(input("Quantas categorias deseja adicionar ? "))
                break
            except ValueError:
                print("Erro volte ao inicio ! ")
                continue
        
        for i in range(qts):
            nome = input(f"Informe o nome da categoria {i + 1}: ").strip()
            if nome:
                self.categorias.append(nome)
            else:
                print("Nome de categoria vazio ignorado.")
        
        print("Categoria(s) salva(s) com sucesso!")

    def exibir(self):
        if not self.categorias:
            print("Nenhuma categoria salva!")
        else:
            print("Categorias salvas:")
            for i, nome in enumerate(self.categorias, start=1):
                print(f"{i}. {nome}")