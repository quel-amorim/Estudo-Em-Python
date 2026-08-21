import json
from random import randint, choice


class Agenda:
    def __init__(self):
        self.lista = []
        self.variantes_email = ["@gmail.com","@hotmail.com","@yahoo.com"]
        self.carregar_json()

    def carregar_json(self):
        try:
            with open("agendacontatos.json", "r", encoding="utf-8") as arquivo:
                self.lista = json.load(arquivo)

        except FileNotFoundError:
            self.lista = []

    def salvar_json(self):
        with open("agendacontatos.json", "w", encoding="utf-8") as arquivo:
            json.dump(self.lista,arquivo,indent=4,ensure_ascii=False)

    def gerar_id(self):
        if not self.lista:
            return 1

        return max(contato["id"] for contato in self.lista) + 1

    def gerar_telefone(self):
        telefone = "".join(str(randint(0, 9))for _ in range(9))

        return telefone

    def criar_contato(self):
        nome = input("Nome: ")
        email = choice(self.variantes_email)
        telefone = self.gerar_telefone()
        contato = {
            "id": self.gerar_id(),
            "nome": nome,
            "email": email,
            "telefone": telefone
        }

        self.lista.append(contato)
        self.salvar_json()

        print("\nContato criado com sucesso!")

    def exibir_contatos(self):
        if not self.lista:
            print("\nNenhum contato cadastrado.")
            return

        print("\n--- CONTATOS ---")

        for contato in self.lista:
            print(f'\nID: {contato['id']} Nome: {contato['nome']} -> Telefone: {contato['telefone']}\nEmail:{contato['email']}')

    def buscar_contato(self, id_contato):
        for contato in self.lista:
            if contato["id"] == id_contato:
                return contato

        return None

    def remover_contato(self):
        try:
            id_contato = int(input("Digite o ID que deseja remover: "))

        except ValueError:
            print("Digite um ID válido.")
            return

        contato = self.buscar_contato(id_contato)

        if contato is None:
            print("Contato não encontrado.")
            return

        self.lista.remove(contato)
        self.salvar_json()

        print("Contato removido com sucesso!")

    def editar_contato(self):
        try:
            id_contato = int(input("Digite o ID que deseja editar: "))

        except ValueError:
            print("Digite um ID válido.")
            return

        contato = self.buscar_contato(id_contato)

        if contato is None:
            print("Contato não encontrado.")
            return

        print("\nDeixe vazio para não alterar.")

        novo_nome = input(f"Nome [{contato['nome']}]: ")
        novo_email = input(f"Email [{contato['email']}]: ")
        novo_telefone = input(f"Telefone [{contato['telefone']}]: ")
        if novo_nome:
            contato["nome"] = novo_nome

        if novo_email:
            contato["email"] = novo_email

        if novo_telefone:
            contato["telefone"] = novo_telefone

        self.salvar_json()

        print("Contato atualizado com sucesso!")


    def iniciar(self):
        while True:
            print("""
=========================
     AGENDA DE CONTATOS
=========================

1 - Criar contato
2 - Exibir contatos
3 - Editar contato
4 - Remover contato
0 - Sair
""")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.criar_contato()

            elif opcao == "2":
                self.exibir_contatos()

            elif opcao == "3":
                self.editar_contato()

            elif opcao == "4":
                self.remover_contato()

            elif opcao == "0":
                print("Programa encerrado.")
                break

            else:
                print("Opção inválida.")
                continue

def main():
    ag = Agenda()

    ag.iniciar()

if __name__ == "__main__":
    main()