from categoria import Categoria

def main():
    primeiro_teste = Categoria()

    print("=== / Bem-Vindo a Interface do Programa / ===")
    while True:
        print("Opções de Comandos Feitos")
        print('[1] Criar catégoria ')
        print('[2] Exibir catégoria ')
        print('[3] Excluir catégoria ')
        print('[0] Fecha o programa ')

        try:
            opcao = int(input("Escolha qual comando executar : "))
        except ValueError:
            print("Erro : apenas números , volte ao inicio")
            continue

        if opcao == 1:
            primeiro_teste.criar_categoria()
        elif opcao == 2:
            primeiro_teste.exibir_categoria()
        elif opcao  == 3:
            primeiro_teste.deletar_categoria()
        elif opcao == 0:
            print("Fechando o programa !")
            print("=== / Fim / ===")
            break
        else:
            print("Desconhecido")

if __name__ == "__main__":
    main()