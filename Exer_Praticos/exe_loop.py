from time import sleep
#Calculadora
def somar(num1,num2):
    print(f'{num1} + {num2} = {num1+num2}')
def sub(num1,num2):
    print(f'{num1} - {num2} = {num1-num2}')
def ds(num1,num2):
    if num2 == 0:
        print('Divisão por zero ! ')
    else:
        print(f'{num1} / {num2} = {num1/num2}')
def mult(num1,num2):
    print(f'{num1} x {num2} = {num1*num2}')
def calculadora():
    print(' | Iniciando a Calculadora |')
    print('-=-'*10)
    while True:
        num1 = float(input('Digite um valor : '))
        num2 = float(input('Digite outro valor  : '))
        sleep(1)
        print('\n[1] Somar')
        print('[2] Subtrair')
        print('[3] Divisão')
        print('[4] Multiplicar')
        print('[5] Todas as operações')
        print('[0] Sair\n')
        sleep(1)
        opcao = int(input("Escolha :"))
        if opcao == 1:
            somar(num1,num2)
        elif opcao == 2:
            sub(num1,num2)
        elif opcao == 3:
            ds(num1,num2)
        elif opcao == 4:
            mult(num1,num2)
        elif opcao == 5:
            somar(num1,num2)
            sub(num1,num2)
            ds(num1,num2)
            mult(num1,num2)
        elif opcao == 0:
            print(' Fim !')
            break
        else:
            print('Opção inválida!')
            sleep(1)

calculadora()
