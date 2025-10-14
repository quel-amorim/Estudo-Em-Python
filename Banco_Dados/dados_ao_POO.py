                                    #Versão 03 => Orientada ao Objeto
# Criação de classes
from random import randint
#Na class Contato apenas crio as variaveis nome,email,telefone
class Contato:

    def __init__(self,nome,email,telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
    #Aqui ele vai me mostra o resultado
    def __str__(self):
        return f'Nome : {self.nome}  | Email : {self.email}  | Telefone : {self.telefone}'

# Aqui faço as criações da lista de contato , das funções de criar , consultar , deletar e mostrar todos os contatos
class Agenda:
    def __init__(self):
        self.contatos = []
    
    def adicionar_contato(self):
        nome = input('Nome para salvar ')
        ddd = randint(11 , 99)
        cell = randint(0 , 99999999)
        telefone = f'+55 ({ddd:02d}) 9{cell:08d}'
        email = input('Email : ')
        novo = Contato(nome , email , telefone)
        self.contatos.append(novo)
        print(f'Contato : {nome} adicionado com sucesso !')
    
    def consultar_contato(self):
        if not self.contatos:
            print('Nada salvo')
            return
        
        tipo = input('Buscar por nome , email ou telefone : ').lower().strip()
        valor = input('Digite o valor da busca : ').strip()
        encontra = False

        for contatos in self.contatos:
            if((tipo == 'nome' and contatos.nome == valor)or
               (tipo =='email' and contatos.email == valor)or
               (tipo =='telefone' and contatos.telefone == valor)):
                print(f'Contato encontrado : {contatos}')
                encontra = True
                break
        
        if not encontra:
            print('Contato não encontrado !')
        
    def deletar_contato(self):
        if not self.contatos:
            print('Nenhum contato salvo!')
            return

        nome = input('Digite o nome do contato que deseja deletar: ')
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print(f'Contato "{nome}" removido com sucesso!')
                break
        else:
            print('Contato não encontrado!')
    
    def listar_contatos(self):
        if not self.contatos:
            print('Nenhum contato salvo!')
        else:
            print('\n--- Lista de Contatos ---')
            for i, contato in enumerate(self.contatos, start=1):
                print(f"{i}. {contato}")
    
#Programa principal

def main():
    agenda = Agenda()

    texto_inicio = ' Bem-vindo ao seu teste de um Banco de Dados (versão POO) '
    print('-' * len(texto_inicio))
    print(texto_inicio)
    print('-' * len(texto_inicio))

    while True:
        print('\nOpções do sistema')
        print('-=-' * 10)
        
        print('[1] Criar Contato')
        print('[2] Consultar Contato')
        print('[3] Deletar Contato')
        print('[4] Mostrar todos os Contatos')
        print('[5] Sair')
        

        try:
            escolha = int(input('Escolha: '))
        except ValueError:
            print('Erro: apenas números são permitidos!')
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
            print('Saindo do sistema... Fim!')
            break
        else:
            print('Opção desconhecida, tente novamente!')


if __name__ == "__main__":
    main()