                                                                 #Versão 02
#Notas Importantes => Programa funcionando muito bem !
from time import sleep
# Criar lista
lista_de_contatos = []

#Criar as funções de gerar contato , consultar e deletar contato
def gerador_contato():
    nome = input('Nome para salvar : ')
    sorte = int(input('Número da sorte : '))
    mensagem = input('Mensagem para deixar salva no seu contato : ')
    cliente = {'nome' : nome , 'sorte' : sorte , 'mensagem' : mensagem}
    lista_de_contatos.append(cliente)
    return cliente

def consultar_contato():
    if not lista_de_contatos:
        print('Nenhum contato salvo!')
        return
    
    tipo = input('Buscar por [nome], [sorte] ou [mensagem]: ').lower().strip()

    valor = input('Digite o valor da busca: ')
    
    encontrado = False
    for cliente in lista_de_contatos:
        if (
            (tipo == 'nome' and cliente['nome'] == valor)
            or (tipo == 'sorte' and str(cliente['sorte']) == valor)
            or (tipo == 'mensagem' and cliente['mensagem'] == valor)
        ):
            print(f"\nContato encontrado:\nNome: {cliente['nome']}\nSorte: {cliente['sorte']}\nMensagem: {cliente['mensagem']}")
            encontrado = True
            break
    
    if not encontrado:
        print('Contato não encontrado!')

def deletar_contato():
    if not lista_de_contatos:
        print('Nenhum contato salvo!')
        return

    nome = input('Digite o nome do contato que deseja deletar: ')
    for cliente in lista_de_contatos:
        if cliente['nome'] == nome:
            lista_de_contatos.remove(cliente)
            print(f'Contato {nome} removido com sucesso!')
            break
    else:
        print('Contato não encontrado!')

def mostra_lista():
    if not lista_de_contatos:
        print('Nenhum contato salvo!')
    else:
        print('\n--- Lista de Contatos ---')
        for i, cliente in enumerate(lista_de_contatos, start=1):
            print(f"{i}. Nome: {cliente['nome']} | Sorte: {cliente['sorte']} | Mensagem: {cliente['mensagem']}")

#Criar as opções de criar conta , deletar e consultar

texto_inicio = ' Bem-vindo ao seu teste de um Banco de Dados '
print('-'*len(texto_inicio))
print(texto_inicio)
print('-'*len(texto_inicio))
# Aqui começa o loop
while True:
    print('\nOpções do seu teste') 
    print('-=-'*10)
    sleep(0.5)
    print('[1] Criar Conta ')
    print('[2] Consultar Conta ')
    print('[3] Deletar Conta ')
    print('[4] Mostrar todos os contatos salvos no sistema ')
    print('[5] Sair ')
    sleep(1)
    #verificação para apenas numeros , sem strings
    try:
        escolha = int(input('Escolha : '))
    except ValueError:
        print('Erro : apenas números seu burro !')
        continue

    if escolha == 1:
        print('Criando ...')
        sleep(1)
        gerador_contato()

    elif escolha == 2:
        print('Consultando ...')
        sleep(1)
        consultar_contato()

    elif escolha == 3:
        print('Deletando ....')
        sleep(0.5)
        deletar_contato()

    elif escolha == 4:
        print('Mostrando todos os contatos ! ...')
        mostra_lista()
    
    elif escolha == 5:
        print('Entendi saindo do loop')
        print(' Fim ')
        sleep(1)
        break
    else:
        print('Desconhecido volte ao inicio !')
