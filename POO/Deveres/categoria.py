class Categoria:
    def __init__(self):
        self.categorias = []
    
    def criar_categoria(self):
        while True:
            try:
                qts = int(input("Deseja criar quantas categorias? "))
                break
            except ValueError:
                print("Erro: apenas números! Tente novamente.")
        
        for i in range(qts):
            nome = input(f"Nome da categoria {i+1}: ").strip()
            if nome:
                self.categorias.append(nome)
            else:
                print("Categoria vazia ignorada.")
        
        print("Categorias salvas com sucesso!")
    
    def exibir_categoria(self):
        if not self.categorias:
            print("Nenhuma categoria salva.")
        else:
            print("Lista de categorias:")
            for i, ctg in enumerate(self.categorias, start=1):
                print(f"{i}. {ctg}")
    
    def deletar_categoria(self):
        if not self.categorias:
            print("Não tem nada nessa lista")
        else:
            nome = input("Digite o nome da catégoria que deseja excluir : ").strip().lower()
            
            for categoria in self.categorias:
                if categoria.lower() == nome:
                    self.categorias.remove(categoria)
                    print(f"Catégoria Excluida")
                else:
                    print("Catégoria não encontrada")
