class Usuario:
    def __init__(self,user,senha,email):
        self.user = user
        self.senha = senha
        self.email = email
    

class Endereco:

    def __init__(self):
        self.endereco_rota = []
    
    def adicionar(self):
        while True:
            try:
                qts = int(input("Quer cadastra quantos usuarios ? "))
                break
            except ValueError:
                print("Erro volte ao inicio ! ")
                continue
        
        for i in range(qts):
            user = input("Register um nickname : ").strip()
            senha = input("Registro de senha : ").strip().lower()
            email = input("Email de registro : ").strip()

            dados_usuario = Usuario(user,senha,email)
            self.endereco_rota.append(dados_usuario)

        print("Usuário(s) registrado(s) no sistema com sucesso(s) ! ")
        return dados_usuario
    
    def exibir(self):
        if not self.endereco_rota:
            print("Nenhum usuario salvo na lista ! ")
        else:
            print("Usuários encontrados ! ")
            for i , d in enumerate(self.endereco_rota, start=1):
                print (f"ID#{i +1} User : {d.user} | Passoword {d.senha}\nEmail de contato {d.email}")
    
    def remover(self): # Arrumar
        if not self.endereco_rota:
            print("Não existe lista ! ")
        else:
            user = input("Digite o usuario que deseja excluir : ")
            self.endereco_rota.remove(user)

def main():
    cliente = Endereco()

    while True:
        print("\nMenu de Opções ! ")
        print("[1] Criar usuário")
        print("[2] Exibir ")
        print("[3] Remover usuário\n")

        escolha = int(input("Escolha  : "))
        if escolha == 1:
            cliente.adicionar()
        elif escolha == 2:
            cliente.exibir()
        elif escolha == 3:
            cliente.remover()
        else:
            print("Fim")
            break

if __name__ == "__main__":
    main()