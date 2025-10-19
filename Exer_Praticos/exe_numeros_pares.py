texto = 'Esse é um programa para ver se o número digitado é NÚMERO PAR OU IMPAR'
print('-'* len(texto))
print(texto)
print('-'* len (texto))
num = int(input('Digite qualquer valor : '))
if num % 2 ==0:
    print(f'\nNúmero : {num} é NÚMERO PAR')
else:
    print(f'\nNúmero : {num} é NÚMERO IMPAR')
