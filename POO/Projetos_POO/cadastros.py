import sqlite3
from random import uniform, randint


class Usuario:
    def __init__(self, nome, telefone, email, salario):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.salario = salario

    def __str__(self):
        return f"Nome: {self.nome} | Telefone: {self.telefone} | Email: {self.email} | Salário: R$ {self.salario:.2f}"


class Caminhos:
    def __init__(self, banco="usuarios.db"):
        self.banco = banco
        self.con = sqlite3.connect(self.banco)
        self.movimento = self.con.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.movimento.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                telefone TEXT,
                email TEXT,
                salario FLOAT(7,4)
            )
            """
        )
        self.con.commit()

    def adicionar(self):
        nome = input("Nome de Usuário: ")
        ddd = randint(11, 99)
        c = randint(0, 999999999)
        telefone = f"+55 ({ddd}) 9{c:08d}"
        email = input("Email de contato: ")
        salario = round(uniform(10, 10000), 2)

        self.movimento.execute(
            "INSERT INTO usuarios (nome, telefone, email, salario) VALUES (?, ?, ?, ?)",
            (nome, telefone, email, salario)
        )
        self.con.commit()

        print(f"Usuário {nome} registrado com sucesso!")

    def consultar(self):
        tipo = input("Buscar por nome, email ou telefone: ").lower().strip()
        valor = input("Digite o valor da busca: ").strip()

        if tipo not in ["nome", "email", "telefone"]:
            print("Tipo inválido! Use nome, email ou telefone.")
            return

        query = f"SELECT nome, telefone, email, salario FROM usuarios WHERE {tipo} = ?"
        self.movimento.execute(query, (valor,))
        resultado = self.movimento.fetchone()

        if resultado:
            user = Usuario(*resultado)
            print(f"\nUsuário encontrado:\n{user}")
        else:
            print("Usuário não encontrado!")

    def deletar(self):
        nome = input("Digite o nome do usuário que deseja deletar: ").strip()

        self.movimento.execute("SELECT * FROM usuarios WHERE nome = ?", (nome,))
        if not self.movimento.fetchone():
            print("Usuário não encontrado!")
            return

        self.movimento.execute("DELETE FROM usuarios WHERE nome = ?", (nome,))
        self.con.commit()
        print(f"Usuário '{nome}' removido com sucesso!")

    def listar(self):
        self.movimento.execute("SELECT nome, telefone, email, salario FROM usuarios")
        usuarios = self.movimento.fetchall()

        if not usuarios:
            print("Nenhum usuário salvo!")
        else:
            print("\n--- Lista de Usuários ---")
            for i, (nome, telefone, email, salario) in enumerate(usuarios, start=1):
                print(f"{i}. Nome: {nome} | Telefone: {telefone} | Email: {email} | R$ {salario:.2f}")

    def fechar(self):
        self.con.close()


def main():
    codar = Caminhos()

    print("-" * 60)
    print(" Bem-vindo ao Sistema de Usuários com Banco de Dados (SQLite) ")
    print("-" * 60)

    while True:
        print("\nOpções do Sistema")
        print("-=-" * 10)
        print("[1] Criar ")
        print("[2] Consultar ")
        print("[3] Deletar ")
        print("[4] Mostrar todos ")
        print("[5] Sair")

        try:
            escolha = int(input("Escolha: "))
        except ValueError:
            print("Erro: apenas números!")
            continue

        if escolha == 1:
            codar.adicionar()
        elif escolha == 2:
            codar.consultar()
        elif escolha == 3:
            codar.deletar()
        elif escolha == 4:
            codar.listar()
        elif escolha == 5:
            codar.fechar()
            print("Saindo do sistema... Fim!")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
