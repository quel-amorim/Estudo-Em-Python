                    # Versão com SQLite(Banco de dados)
import sqlite3
from random import randint

# === Classe Contato ===
class Contato:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return f'Nome : {self.nome} | Email : {self.email} | Telefone : {self.telefone}'


# === Classe Agenda ===
class Agenda:
    def __init__(self, banco="agenda.db"):
        self.banco = banco
        self.conexao = sqlite3.connect(self.banco)
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    # Cria a tabela se não existir
    def criar_tabela(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS contatos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT,
                telefone TEXT
            )
        """)
        self.conexao.commit()

    # Adiciona um novo contato
    def adicionar_contato(self):
        nome = input("Nome: ").strip()
        ddd = randint(11, 99)
        cell = randint(0, 99999999)
        telefone = f"+55 ({ddd:02d}) 9{cell:08d}"
        email = input("Email: ").strip()

        self.cursor.execute(
            "INSERT INTO contatos (nome, email, telefone) VALUES (?, ?, ?)",
            (nome, email, telefone)
        )
        self.conexao.commit()
        print(f"Contato '{nome}' adicionado com sucesso!")

    # Consulta contato
    def consultar_contato(self):
        tipo = input("Buscar por nome, email ou telefone: ").lower().strip()
        valor = input("Digite o valor da busca: ").strip()

        if tipo not in ["nome", "email", "telefone"]:
            print("Tipo inválido! Use nome, email ou telefone.")
            return

        query = f"SELECT nome, email, telefone FROM contatos WHERE {tipo} = ?"
        self.cursor.execute(query, (valor,))
        resultado = self.cursor.fetchone()

        if resultado:
            contato = Contato(*resultado)
            print(f"Contato encontrado:\n{contato}")
        else:
            print("Contato não encontrado!")

    # Deletar contato
    def deletar_contato(self):
        nome = input("Digite o nome do contato que deseja deletar: ").strip()

        self.cursor.execute("SELECT * FROM contatos WHERE nome = ?", (nome,))
        if not self.cursor.fetchone():
            print("Contato não encontrado!")
            return

        self.cursor.execute("DELETE FROM contatos WHERE nome = ?", (nome,))
        self.conexao.commit()
        print(f"Contato '{nome}' removido com sucesso!")

    # Listar todos os contatos
    def listar_contatos(self):
        self.cursor.execute("SELECT nome, email, telefone FROM contatos")
        contatos = self.cursor.fetchall()

        if not contatos:
            print("Nenhum contato salvo!")
        else:
            print("\n--- Lista de Contatos ---")
            for i, (nome, email, telefone) in enumerate(contatos, start=1):
                print(f"{i}. Nome: {nome} | Email: {email} | Telefone: {telefone}")

    # Fecha a conexão com o banco (boa prática)
    def fechar(self):
        self.conexao.close()


# === Função Principal ===
def main():
    agenda = Agenda()

    print("-" * 60)
    print(" Bem-vindo ao Sistema de Agenda com Banco de Dados (SQLite) ")
    print("-" * 60)

    while True:
        print("\nOpções do Sistema")
        print("-=-" * 10)
        print("[1] Criar Contato")
        print("[2] Consultar Contato")
        print("[3] Deletar Contato")
        print("[4] Mostrar todos os Contatos")
        print("[5] Sair")

        try:
            escolha = int(input("Escolha: "))
        except ValueError:
            print("Erro: apenas números!")
            continue

        if escolha == 1:
            agenda.adicionar_contato()
        elif escolha == 2:
            agenda.consultar_contato()
        elif escolha == 3:
            agenda.deletar_contato()
        elif escolha == 4:
            agenda.listar_contatos()
        elif escolha == 5:
            agenda.fechar()
            print("Saindo do sistema... Fim!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
