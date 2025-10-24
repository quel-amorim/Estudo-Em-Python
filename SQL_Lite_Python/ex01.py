import sqlite3
from dataclasses import dataclass

@dataclass
class Dados:
    nome : str
    idade : int
    profissao : str

    @classmethod
    def dados(cls):
        nome = input("Nome : ")
        idade = int(input("Idade : "))
        profissao = input("Trabalha com o que ? ")

        return cls(nome , idade , profissao)
    
    def banco_dados(self):
        conexao = sqlite3.connect("dados.db")
        movimento = conexao.cursor()

        movimento.execute("CREATE TABLE IF NOT EXISTS usuarios (nome TEXT , idade INTEGER , profissao  TEXT)")

        conexao.commit()

        movimento.execute("INSERT INTO usuarios VALUES (? , ? , ?)" , (self.nome , self.idade , self.profissao))

        conexao.commit()
        movimento.close()
        conexao.close()
        print("✅ Dados salvos com sucesso no banco de dados!")

    @staticmethod
    def mostrar_dados():
        """Exibe todos os dados salvos no banco de dados."""
        conexao = sqlite3.connect("dados.db")
        movimento = conexao.cursor()

        movimento.execute("SELECT * FROM usuarios")
        dados = movimento.fetchall()

        if not dados:
            print("⚠️ Nenhum dado encontrado no banco de dados.")
        else:
            print("\n📋 DADOS SALVOS NO BANCO:")
            print("-" * 35)
            for i, (nome, idade, profissao) in enumerate(dados, start=1):
                print(f"{i}. Nome: {nome} | Idade: {idade} | Profissão: {profissao}")
            print("-" * 35)

        movimento.close()
        conexao.close()



def main():
    print("Teste de Interface!")
    print("PASSO 1: REGISTRAR OS DADOS")
    usuario = Dados.dados()

    print("PASSO 2: SALVAR NO BANCO DE DADOS")
    usuario.banco_dados()

    print("PASSO 3 MOSTRAR OS DADOS ! ")
    usuario.mostrar_dados()
if __name__ == "__main__":
    main()