            # Programação Orientada ao Objeto
from random import choice , randint

class Jogador: #Criamos a classe jogador para colocar as variaveis : nome , nivel , hp e dano

    def __init__(self,nome,nivel,hp,dano):
        self.nome = nome
        self.nivel = nivel
        self.hp = hp
        self.dano = dano
    
    def __str__(self):
        return f"{self.nome} LV {self.nivel}\nHP : {self.hp} | Dano {self.dano}"


class TierListPLAY:

    def __init__(self): # Criamos nossa lista para salvar os resultados que serão feitas aqui
        self.lista_jogadores = []

    def criar_jogador(self):
        qts = int(input("Deseja criar quantos personagens ? "))
        for i in range(qts):
            sugestao_nomes = ['Lutador','Mago','Arqueiro','Assassino']
            nome = choice(sugestao_nomes)
            nivel = randint(0 , 100)
            hp = 1000 * nivel
            dano = hp/2
            novo = Jogador(nome,nivel,hp,dano)
            self.lista_jogadores.append(novo) # Colocar o resultado da variavel novo para a lista de jogadores
            print("Personagens feitos com sucesso ! ")
        

#Interface
def main():
    lista = TierListPLAY()

    while True: # Loop começa
        print("Bem-Vindo a tela de Personalidade")
        print("Opções de comandos")
        print("[1] Criar Personagem ")
        print("[0] Sair ")
        try:
            escolha = int(input("Escolha alguma opção : "))
        except ValueError:
            print("Erro : Você tentou colocar uma string ,apenas números seu burro !!!!")
            continue
        if escolha == 1:
            print("Ótimo vamos criar seu personagem ! ")
            lista.criar_jogador()
        else:
            print("Fechando o programa ")
            break
    

if __name__ == "__main__": #Executar tudo

    main()
