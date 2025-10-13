                                                                #Versão 02
# Notas Importates => Falta fazer as funções de consultar , deletar contato e fazer uma de mostra todos os contatos que tem no sistema !
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
    print('[4] Sair ')
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
    elif escolha == 3:
        print('Deletando ....')
        sleep(0.5)
    elif escolha == 4:
        print('Entendi saindo do loop')
        print(' Fim ')
        sleep(1)
        break
    else:
        print('Desconhecido volte ao inicio !')



    