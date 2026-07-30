"""Projeto padrão para quem deixar práticar os fundamentos básicos"""
n1 = float(input('Primeiro valor :'))
n2 = float(input('Segundo valor :'))
tipoOperacao = input('Opereções do Sistema\n[+]Soma\n[-]Subtração\n[/]Divisão\n[*]Multiplicação\nEscolha o tipo de operação :')
def somar():
    print(f'{n1} + {n2} = {n1 + n2}')
def subtrair():
    print(f'{n1} - {n2} = {n1 - n2}')
def divisao():
    if n2 !=0:
        print(f'{n1} / {n2}')
    else:
        print('Divisão por zero !')
def multiplicar():
    print(f'{n1} x {n2} = {n1 * n2}')

match tipoOperacao:
    case '+':
        somar()
    case '-':
        subtrair()
    case'/':
        divisao()
    case '*':
        multiplicar()
