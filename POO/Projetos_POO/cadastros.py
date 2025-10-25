import re
class Usuario:
    def __init__(self,username , email):
        self.username = username
        self.email = email
    

class Endereco:

    def __init__(self):
        self.rota = []
    
    def adicionar(self):
        while True:
            try:
                qts = int(input("Adicionar quantos usuários ? "))
                break
            except ValueError:
                print("Erro volte ao inicio")
                continue
        
        for i in range(qts):
            while True:
                username = input("Nick de usuário : ").strip()
                email = input("Email de contato : ").strip()
                if username == "" or email == "":
                    print("Nome e email não podem está vazios ! ")
                    continue

                if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
                    print(" E-mail inválido! Tente novamente.")
                    continue
                usuarios = Usuario(username ,email)
                self.rota.append(usuarios)
                break
        
        print("\nUsuários adicionados com sucesso ! ")


def main():
    codar = Endereco()

    print("Menu de Opções ")
    print("[1] Adicionar")
    
    opcao = int(input("Escolha : "))
    if opcao == 1:
        print("Adicionando usuário ! ")
        codar.adicionar()

if __name__ == "__main__":
    main()
